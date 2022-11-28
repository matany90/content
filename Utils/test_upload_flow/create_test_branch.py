import argparse
import json
import os
import shutil
import subprocess
import time
from pathlib import Path
from typing import Union
from git import GitCommandError, Head, Repo

from Tests.scripts.utils import logging_wrapper as logging
from Tests.scripts.utils.log_util import install_logging

versions_dict = {}
pack_items_dict = {}
changed_packs = set()


def json_write(file_path: str, data: Union[list, dict]):
    """ Writes given data to a json file

    Args:
        file_path: The file path
        data: The data to write

    """
    with open(file_path, "w") as f:
        f.write(json.dumps(data, indent=4))


def add_changed_pack(func):
    def wrapper(*args, **kwargs):
        global changed_packs
        global versions_dict
        global pack_items_dict
        logging.info(f'Running {func.__name__}')
        pack, version, pack_items = func(*args, **kwargs)
        changed_packs.add(pack)
        versions_dict[str(pack.name)] = version
        if pack_items:
            pack_items_dict[str(pack.name)] = pack_items
        logging.info(f"Done running {func.__name__} on pack {pack}")

        return pack, version, pack_items
    return wrapper


@add_changed_pack
def create_new_pack():
    """
        Creates new pack with given pack name
        returns a dict with the created content items in the form of {item_type: item_path}
    """
    content_path = Path(__file__).parent.parent.parent
    source_path = Path(__file__).parent / 'TestUploadFlow'
    dest_path = content_path / 'Packs' / 'TestUploadFlow'
    if dest_path.exists():
        shutil.rmtree(dest_path)
    shutil.copytree(source_path, dest_path)

    return dest_path, '1.0.0', get_pack_content_dict_v2(dest_path)


def get_pack_content_dict_v2(pack_path: Path, marketplace='xsoar'):
    """
    Gets a dict of all the paths of the pack content items as it is in the bucket.

    Args:
        pack_path (Path): The pack path.

    Returns:
        dict: The content paths dict.
    """
    create_artifacts_command = ['demisto-sdk', 'create-content-artifacts', '-a',
                                '.', "-p", f'{pack_path.name}', '--no-zip', '--packs']

    if marketplace == 'marketplacev2':
        create_artifacts_command.extend(['-mp', f'{marketplace}'])

    subprocess.call(create_artifacts_command, stdout=subprocess.DEVNULL)

    content_dict = {}
    new_pack_path = os.path.join('content_packs', pack_path.name)
    sub_dirs = os.listdir(new_pack_path)
    sub_dirs = [str(sub_dir) for sub_dir in sub_dirs if '.' not in str(sub_dir)]

    for content_item_type in sub_dirs:
        if content_item_type not in ['ReleaseNotes', 'TestPlaybooks']:
            content_dict[content_item_type] = ['/'.join(p.parts[1:]) for p in Path(os.path.join(str(new_pack_path), 
                                                                                                content_item_type)).glob('*')]

    shutil.rmtree('./content_packs')
    return content_dict


@add_changed_pack
def add_dependency(base_pack: Path, new_depndency_pack: Path):
    metadata_json = base_pack / 'pack_metadata.json'
    with metadata_json.open('r') as fr:
        base_metadata = json.load(fr)
    new_pack_name = new_depndency_pack.name
    base_metadata['dependencies'][new_pack_name] = {
        "mandatory": True,
        "display_name": new_pack_name
    }
    json_write(str(metadata_json), base_metadata)
    return base_pack, base_metadata['currentVersion'], None


@add_changed_pack
def enhance_release_notes(pack: Path):
    subprocess.call(['demisto-sdk', 'update-release-notes', '-i',
                    f'{pack}', "--force", '--text', 'testing adding new RN'], stdout=subprocess.DEVNULL)
    return pack, get_current_version(pack), None


@add_changed_pack
def change_image(pack: Path):
    new_image = pack.parent / 'TestUploadFlow' / 'Integrations' / 'TestUploadFlow' / 'TestUploadFlow_image.png'
    for p in Path(pack).glob('**/*.png'):
        shutil.copy(new_image, p)
    return pack, get_current_version(pack), None


@add_changed_pack
def update_existing_release_notes(pack: Path, version: str):
    version_rn = version.replace('.', '_')
    path = pack / 'ReleaseNotes' / f'{version_rn}.md'
    if not path.exists():
        raise Exception("path is not valid release note")

    with path.open('a') as f:
        f.write('testing modifying existing RN')
    return pack, version, None


@add_changed_pack
def set_pack_hidden(pack: Path):
    metadata_json = pack / 'pack_metadata.json'
    with metadata_json.open('r') as f:
        base_metadata = json.load(f)
    base_metadata['hidden'] = True
    with metadata_json.open('w') as f:
        json.dump(base_metadata, f)
    return pack, base_metadata['currentVersion'], None


@add_changed_pack
def update_readme(pack: Path):
    for path in pack.glob('**/*README.md'):
        with path.open('a') as f:
            f.write("readme test upload flow")
    return pack, get_current_version(pack), None


@add_changed_pack
def update_pack_ignore(pack: Path):
    pack_ignore = pack / ".pack-ignore"
    with pack_ignore.open('a') as f:
        f.write("\n[file:1_0_1.md]\nignore=RM104\n")
    return pack, get_current_version(pack), None


@add_changed_pack
def create_failing_pack(pack: Path):
    """
    Modify a pack such that the upload fails on it - modifying a pack
    without adding release notes and without bumping the version.
    """
    metadata_json = pack / 'pack_metadata.json'
    with metadata_json.open('r') as f:
        base_metadata = json.load(f)
    splited_pack_version = base_metadata['currentVersion'].rsplit('.', 1)
    base_metadata['currentVersion'] = '.'.join([splited_pack_version[0], str(int(splited_pack_version[1]) + 1)])
    json_write(str(metadata_json), base_metadata)
    return pack, base_metadata['currentVersion'], None


@add_changed_pack
def modify_pack(pack: Path, integration: str):
    """
    Modify a pack regularly, in order to check if all packs items are uploaded correctly
    """
    integration = pack / integration
    with integration.open('a') as f:
        f.write('\n#  CHANGE IN PACK')

    enhance_release_notes(pack)
    return pack, get_current_version(pack), get_pack_content_dict_v2(pack)


@add_changed_pack
def modify_modeling_rules(modeling_rule: Path, old_name: str, new_name: str):
    """
    Modify modeling rules path, in order to verify that the pack was uploaded again
    """
    
    modify_item_path(modeling_rule / f'{old_name}.xif', f'{new_name}.xif', modeling_rule.parent.parent)
    modify_item_path(modeling_rule / f'{old_name}.yml', f'{new_name}.yml', modeling_rule.parent.parent)
    modify_item_path(modeling_rule / f'{old_name}_schema.json', f'{new_name}_schema.json', modeling_rule.parent.parent)
    parent = modeling_rule.parent
    pack_path = modeling_rule.parent.parent
    modeling_rule.rename(parent.joinpath(new_name))
    return pack_path, get_current_version(pack_path), get_pack_content_dict_v2(pack_path, marketplace='marketplacev2')
    

def modify_item_path(item: Path, new_name: str, pack_path: Path):
    """
    Modify item's path, in order to verify that the pack was uploaded again
    """
    parent = item.parent
    item.rename(parent.joinpath(new_name))


@add_changed_pack
def add_1_0_0_release_notes(pack: Path):
    release_note = pack / 'ReleaseNotes' / '1_0_0.md'
    release_note.write_text(f"""
#### Integrations
##### {pack.name}
first release note
""")
    return pack, get_current_version(pack), None


def get_current_version(pack: Path):
    metadata_json = pack / 'pack_metadata.json'
    with metadata_json.open('r') as f:
        base_metadata = json.load(f)
    return base_metadata['currentVersion']


def create_new_branch(repo: Repo, new_branch_name: str) -> Head:
    branch = repo.create_head(new_branch_name)
    branch.checkout()
    logging.info(f"Created new branch {repo.active_branch}")
    return branch


def do_changes_on_branch(packs_path: Path):
    """
    Makes the test changes on the created branch

    Args:
        packs_path (Path): Path to the packs.
    """
    # Case 1: Verify new pack - TestUploadFlow
    new_pack_path, _, _ = create_new_pack()

    # Case 2: Verify modified pack - Armorblox
    modify_pack(packs_path / 'Armorblox', 'Integrations/Armorblox/Armorblox.py')

    # Case 3: Verify dependencies handling - Armis
    add_dependency(packs_path / 'Armis', new_pack_path)

    # Case 4: Verify new version - ZeroFox
    enhance_release_notes(packs_path / 'ZeroFox')

    # Case 5: Verify modified existing release notes - Box
    update_existing_release_notes(packs_path / 'Box', "2.1.2")

    # Case 6: Verify pack is set to hidden - Microsoft365Defender
    # set_pack_hidden(packs_path / 'Microsoft365Defender') 
    # TODO: fix after hidden pack mechanism is fixed - CIAC-3848

    # Case 7: Verify changed readme - Maltiverse
    update_readme(packs_path / 'Maltiverse')

    # TODO: didn't verified
    update_pack_ignore(packs_path / 'MISP')

    # Case 8: Verify failing pack - Absolute
    create_failing_pack(packs_path / 'Absolute')

    # Case 9: Verify changed image - Armis
    change_image(packs_path / 'Armis')

    # Case 10: Verify modified modeling rule path - AlibabaActionTrail
    modify_modeling_rules(packs_path / 'AlibabaActionTrail/ModelingRules/AlibabaModelingRules',
                          'AlibabaModelingRules', 'Alibaba')  # TODO: add script

    logging.info("Finished making test changes on the branch")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", nargs="?", help="Content directory path, default is current directory.", default='.')
    parser.add_argument("-cb", "--content-branch", nargs="?",
                        help="The content branch name, if empty will run on current branch.")
    parser.add_argument("-a", "--artifacts_path", help="Path to store the script's output", default=".")
    parser.add_argument("-g", "--gitlab-mirror-token", help="Gitlab mirror token for pushing commits "
                                                            "directly to gitlab repo")
    return parser.parse_args()


def main():
    install_logging('create_test_branch.log', logger=logging)

    args = parse_arguments()
    repo = Repo(args.path)
    if args.content_branch:
        original_branch = args.content_branch
        repo.git.checkout(original_branch)
    else:
        original_branch = repo.active_branch

    try:
        new_branch_name = f"{original_branch}_upload_test_branch_{time.time()}"
        content_path = Path(__file__).parent.parent.parent
        packs_path = content_path / 'Packs'
        branch = create_new_branch(repo, new_branch_name)

        do_changes_on_branch(packs_path)

        for p in changed_packs:
            repo.git.add(f"{p}/*")

        repo.git.commit(m="Added Test file", no_verify=True)
        repo.git.push('--set-upstream',
                      f'https://GITLAB_PUSH_TOKEN:{args.gitlab_mirror_token}@'  # disable-secrets-detection
                      f'code.pan.run/xsoar/content.git', branch)  # disable-secrets-detection
        logging.info("Successfuly pushing the branch to Gitlab content repo")

    except GitCommandError as e:
        logging.error(e)

    finally:
        repo.git.checkout(original_branch)
        json_write(os.path.join(args.artifacts_path, 'packs_items.json'), pack_items_dict)
        json_write(os.path.join(args.artifacts_path, 'versions_dict.json'), versions_dict)

        os.environ['branch'] = new_branch_name
        return new_branch_name
        # print(new_branch_name)  # prints out to the bash variable


if __name__ == "__main__":
    main()
