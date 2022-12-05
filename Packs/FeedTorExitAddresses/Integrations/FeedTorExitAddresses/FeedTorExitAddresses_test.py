import json
import demistomock as demisto
import pytest
from FeedTorExitAddresses import *

INDICATORS = 'ExitNode Node1\n' \
             'Published 2022-11-24 10:34:10\n' \
             'LastStatus 2022-11-24 22:00:00\n' \
             'ExitAddress 1.1.1.1 2022-11-24 22:56:37\n' \
             'ExitNode Node2\n' \
             'Published 2022-11-24 19:31:20\n' \
             'LastStatus 2022-11-24 22:00:00\n' \
             'ExitAddress 2.2.2.2 2022-11-24 22:53:27\n' \
             'ExitNode Node3\n' \
             'Published 2022-11-24 11:10:45\n' \
             'LastStatus 2022-11-24 22:00:00\n' \
             'ExitAddress Node3 2022-11-24 22:45:28\n'


def test_build_iterator(mocker):
    mocker.patch.object(Client, 'http_request_indicators', return_value=INDICATORS)
    client = Client()
    indicators = client.build_iterator(feedTags=None, limit=None)
    assert len(indicators) == 2
    assert indicators[0].get('value') == '1.1.1.1'
    assert indicators[1].get('value') == '2.2.2.2'

