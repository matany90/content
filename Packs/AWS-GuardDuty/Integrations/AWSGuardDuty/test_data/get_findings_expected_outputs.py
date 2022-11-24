EXPECTED_FINDING_OUTPUTS = [{'AccountId': 'string',
                             'Arn': 'string',
                             'Confidence': 123.0,
                             'CreatedAt': '2022-11-08T14:24:52.908Z',
                             'Description': 'desc',
                             'Id': 'string',
                             'Partition': 'string',
                             'Region': 'string',
                             'Resource': {'AccessKeyDetails': '{"AccessKeyId": "string", "PrincipalId": '
                                                              '"string", "UserName": "string", '
                                                              '"UserType": "string"}',
                                          'ContainerDetails': '{"ContainerRuntime": "string", "Id": '
                                                              '"string", "Name": "string", "Image": '
                                                              '"string", "ImagePrefix": "string", '
                                                              '"VolumeMounts": [{"Name": "string", '
                                                              '"MountPath": "string"}], '
                                                              '"SecurityContext": {"Privileged": true}}',
                                          'EbsVolumeDetails': '{"ScannedVolumeDetails": [{"VolumeArn": '
                                                              '"string", "VolumeType": "string", '
                                                              '"DeviceName": "string", "VolumeSizeInGB": '
                                                              '123, "EncryptionType": "string", '
                                                              '"SnapshotArn": "string", "KmsKeyArn": '
                                                              '"string"}], "SkippedVolumeDetails": '
                                                              '[{"VolumeArn": "string", "VolumeType": '
                                                              '"string", "DeviceName": "string", '
                                                              '"VolumeSizeInGB": 123, "EncryptionType": '
                                                              '"string", "SnapshotArn": "string", '
                                                              '"KmsKeyArn": "string"}]}',
                                          'EcsClusterDetails': '{"Name": "string", "Arn": "string", '
                                                               '"Status": "string", '
                                                               '"ActiveServicesCount": 123, '
                                                               '"RegisteredContainerInstancesCount": 123, '
                                                               '"RunningTasksCount": 123, "Tags": '
                                                               '[{"Key": "string", "Value": "string"}], '
                                                               '"TaskDetails": {"Arn": "string", '
                                                               '"DefinitionArn": "string", "Version": '
                                                               '"string", "TaskCreatedAt": '
                                                               '"2015-01-01T00:00:00", "StartedAt": '
                                                               '"2015-01-01T00:00:00", "StartedBy": '
                                                               '"string", "Tags": [{"Key": "string", '
                                                               '"Value": "string"}], "Volumes": [{"Name": '
                                                               '"string", "HostPath": {"Path": '
                                                               '"string"}}], "Containers": '
                                                               '[{"ContainerRuntime": "string", "Id": '
                                                               '"string", "Name": "string", "Image": '
                                                               '"string", "ImagePrefix": "string", '
                                                               '"VolumeMounts": [{"Name": "string", '
                                                               '"MountPath": "string"}], '
                                                               '"SecurityContext": {"Privileged": '
                                                               'true}}], "Group": "string"}}',
                                          'EksClusterDetails': '{"Name": "string", "Arn": "string", '
                                                               '"VpcId": "string", "Status": "string", '
                                                               '"Tags": [{"Key": "string", "Value": '
                                                               '"string"}], "CreatedAt": '
                                                               '"2015-01-01T00:00:00"}',
                                          'InstanceDetails': '{"AvailabilityZone": "string", '
                                                             '"IamInstanceProfile": {"Arn": "string", '
                                                             '"Id": "string"}, "ImageDescription": '
                                                             '"string", "ImageId": "string", '
                                                             '"InstanceId": "string", "InstanceState": '
                                                             '"string", "InstanceType": "string", '
                                                             '"OutpostArn": "string", "LaunchTime": '
                                                             '"string", "NetworkInterfaces": '
                                                             '[{"Ipv6Addresses": ["string"], '
                                                             '"NetworkInterfaceId": "string", '
                                                             '"PrivateDnsName": "string", '
                                                             '"PrivateIpAddress": "string", '
                                                             '"PrivateIpAddresses": [{"PrivateDnsName": '
                                                             '"string", "PrivateIpAddress": "string"}], '
                                                             '"PublicDnsName": "string", "PublicIp": '
                                                             '"string", "SecurityGroups": [{"GroupId": '
                                                             '"string", "GroupName": "string"}], '
                                                             '"SubnetId": "string", "VpcId": "string"}], '
                                                             '"Platform": "string", "ProductCodes": '
                                                             '[{"Code": "string", "ProductType": '
                                                             '"string"}], "Tags": [{"Key": "string", '
                                                             '"Value": "string"}]}',
                                          'KubernetesDetails': '{"KubernetesUserDetails": {"Username": '
                                                               '"string", "Uid": "string", "Groups": '
                                                               '["string"]}, "KubernetesWorkloadDetails": '
                                                               '{"Name": "string", "Type": "string", '
                                                               '"Uid": "string", "Namespace": "string", '
                                                               '"HostNetwork": true, "Containers": '
                                                               '[{"ContainerRuntime": "string", "Id": '
                                                               '"string", "Name": "string", "Image": '
                                                               '"string", "ImagePrefix": "string", '
                                                               '"VolumeMounts": [{"Name": "string", '
                                                               '"MountPath": "string"}], '
                                                               '"SecurityContext": {"Privileged": '
                                                               'true}}], "Volumes": [{"Name": "string", '
                                                               '"HostPath": {"Path": "string"}}]}}',
                                          'S3BucketDetails': '[{"Arn": "string", "Name": "string", '
                                                             '"Type": "string", "CreatedAt": '
                                                             '"2015-01-01T00:00:00", "Owner": {"Id": '
                                                             '"string"}, "Tags": [{"Key": "string", '
                                                             '"Value": "string"}], '
                                                             '"DefaultServerSideEncryption": '
                                                             '{"EncryptionType": "string", '
                                                             '"KmsMasterKeyArn": "string"}, '
                                                             '"PublicAccess": {"PermissionConfiguration": '
                                                             '{"BucketLevelPermissions": '
                                                             '{"AccessControlList": '
                                                             '{"AllowsPublicReadAccess": true, '
                                                             '"AllowsPublicWriteAccess": true}, '
                                                             '"BucketPolicy": {"AllowsPublicReadAccess": '
                                                             'true, "AllowsPublicWriteAccess": true}, '
                                                             '"BlockPublicAccess": {"IgnorePublicAcls": '
                                                             'true, "RestrictPublicBuckets": true, '
                                                             '"BlockPublicAcls": true, '
                                                             '"BlockPublicPolicy": true}}, '
                                                             '"AccountLevelPermissions": '
                                                             '{"BlockPublicAccess": {"IgnorePublicAcls": '
                                                             'true, "RestrictPublicBuckets": true, '
                                                             '"BlockPublicAcls": true, '
                                                             '"BlockPublicPolicy": true}}}, '
                                                             '"EffectivePermission": "string"}}]'},
                             'ResourceType': 'string',
                             'SchemaVersion': 'string',
                             'Service': '{"Action": {"ActionType": "string", "AwsApiCallAction": {"Api": '
                                        '"string", "CallerType": "string", "DomainDetails": {"Domain": '
                                        '"string"}, "ErrorCode": "string", "UserAgent": "string", '
                                        '"RemoteIpDetails": {"City": {"CityName": "string"}, "Country": '
                                        '{"CountryCode": "string", "CountryName": "string"}, '
                                        '"GeoLocation": {"Lat": 123.0, "Lon": 123.0}, "IpAddressV4": '
                                        '"string", "Organization": {"Asn": "string", "AsnOrg": "string", '
                                        '"Isp": "string", "Org": "string"}}, "ServiceName": "string", '
                                        '"RemoteAccountDetails": {"AccountId": "string", "Affiliated": '
                                        'true}, "AffectedResources": {"string": "string"}}, '
                                        '"DnsRequestAction": {"Domain": "string", "Protocol": "string", '
                                        '"Blocked": true}, "NetworkConnectionAction": {"Blocked": true, '
                                        '"ConnectionDirection": "string", "LocalPortDetails": {"Port": '
                                        '123, "PortName": "string"}, "Protocol": "string", '
                                        '"LocalIpDetails": {"IpAddressV4": "string"}, "RemoteIpDetails": '
                                        '{"City": {"CityName": "string"}, "Country": {"CountryCode": '
                                        '"string", "CountryName": "string"}, "GeoLocation": {"Lat": '
                                        '123.0, "Lon": 123.0}, "IpAddressV4": "string", "Organization": '
                                        '{"Asn": "string", "AsnOrg": "string", "Isp": "string", "Org": '
                                        '"string"}}, "RemotePortDetails": {"Port": 123, "PortName": '
                                        '"string"}}, "PortProbeAction": {"Blocked": true, '
                                        '"PortProbeDetails": [{"LocalPortDetails": {"Port": 123, '
                                        '"PortName": "string"}, "LocalIpDetails": {"IpAddressV4": '
                                        '"string"}, "RemoteIpDetails": {"City": {"CityName": "string"}, '
                                        '"Country": {"CountryCode": "string", "CountryName": "string"}, '
                                        '"GeoLocation": {"Lat": 123.0, "Lon": 123.0}, "IpAddressV4": '
                                        '"string", "Organization": {"Asn": "string", "AsnOrg": "string", '
                                        '"Isp": "string", "Org": "string"}}}]}, '
                                        '"KubernetesApiCallAction": {"RequestUri": "string", "Verb": '
                                        '"string", "SourceIps": ["string"], "UserAgent": "string", '
                                        '"RemoteIpDetails": {"City": {"CityName": "string"}, "Country": '
                                        '{"CountryCode": "string", "CountryName": "string"}, '
                                        '"GeoLocation": {"Lat": 123.0, "Lon": 123.0}, "IpAddressV4": '
                                        '"string", "Organization": {"Asn": "string", "AsnOrg": "string", '
                                        '"Isp": "string", "Org": "string"}}, "StatusCode": 123, '
                                        '"Parameters": "string"}}, "Evidence": '
                                        '{"ThreatIntelligenceDetails": [{"ThreatListName": "string", '
                                        '"ThreatNames": ["string"]}]}, "Archived": true, "Count": 123, '
                                        '"DetectorId": "string", "EventFirstSeen": "string", '
                                        '"EventLastSeen": "string", "ResourceRole": "string", '
                                        '"ServiceName": "string", "UserFeedback": "string", '
                                        '"AdditionalInfo": {"Value": "string", "Type": "string"}, '
                                        '"FeatureName": "string", "EbsVolumeScanDetails": {"ScanId": '
                                        '"string", "ScanStartedAt": "2015-01-01T00:00:00", '
                                        '"ScanCompletedAt": "2015-01-01T00:00:00", "TriggerFindingId": '
                                        '"string", "Sources": ["string"], "ScanDetections": '
                                        '{"ScannedItemCount": {"TotalGb": 123, "Files": 123, "Volumes": '
                                        '123}, "ThreatsDetectedItemCount": {"Files": 123}, '
                                        '"HighestSeverityThreatDetails": {"Severity": "string", '
                                        '"ThreatName": "string", "Count": 123}, "ThreatDetectedByName": '
                                        '{"ItemCount": 123, "UniqueThreatNameCount": 123, "Shortened": '
                                        'true, "ThreatNames": [{"Name": "string", "Severity": "string", '
                                        '"ItemCount": 123, "FilePaths": [{"FilePath": "string", '
                                        '"VolumeArn": "string", "Hash": "string", "FileName": '
                                        '"string"}]}]}}}}',
                             'Severity': 0,
                             'Title': 'title',
                             'Type': 'string',
                             'UpdatedAt': '2022-11-08T14:24:52.908Z'},
                            {'AccountId': 'string',
                             'Arn': 'string',
                             'Confidence': 123.0,
                             'CreatedAt': '2022-11-08T14:24:52.908Z',
                             'Description': 'desc',
                             'Id': 'finding2',
                             'Partition': 'string',
                             'Region': 'string',
                             'Resource': {'AccessKeyDetails': '{"AccessKeyId": "string", "PrincipalId": '
                                                              '"string", "UserName": "string", '
                                                              '"UserType": "string"}',
                                          'ContainerDetails': '{"ContainerRuntime": "string", "Id": '
                                                              '"string", "Name": "string", "Image": '
                                                              '"string", "ImagePrefix": "string", '
                                                              '"VolumeMounts": [{"Name": "string", '
                                                              '"MountPath": "string"}], '
                                                              '"SecurityContext": {"Privileged": true}}',
                                          'EbsVolumeDetails': '{"ScannedVolumeDetails": [{"VolumeArn": '
                                                              '"string", "VolumeType": "string", '
                                                              '"DeviceName": "string", "VolumeSizeInGB": '
                                                              '123, "EncryptionType": "string", '
                                                              '"SnapshotArn": "string", "KmsKeyArn": '
                                                              '"string"}], "SkippedVolumeDetails": '
                                                              '[{"VolumeArn": "string", "VolumeType": '
                                                              '"string", "DeviceName": "string", '
                                                              '"VolumeSizeInGB": 123, "EncryptionType": '
                                                              '"string", "SnapshotArn": "string", '
                                                              '"KmsKeyArn": "string"}]}',
                                          'EcsClusterDetails': '{"Name": "string", "Arn": "string", '
                                                               '"Status": "string", '
                                                               '"ActiveServicesCount": 123, '
                                                               '"RegisteredContainerInstancesCount": 123, '
                                                               '"RunningTasksCount": 123, "Tags": '
                                                               '[{"Key": "string", "Value": "string"}], '
                                                               '"TaskDetails": {"Arn": "string", '
                                                               '"DefinitionArn": "string", "Version": '
                                                               '"string", "TaskCreatedAt": '
                                                               '"2015-01-01T00:00:00", "StartedAt": '
                                                               '"2015-01-01T00:00:00", "StartedBy": '
                                                               '"string", "Tags": [{"Key": "string", '
                                                               '"Value": "string"}], "Volumes": [{"Name": '
                                                               '"string", "HostPath": {"Path": '
                                                               '"string"}}], "Containers": '
                                                               '[{"ContainerRuntime": "string", "Id": '
                                                               '"string", "Name": "string", "Image": '
                                                               '"string", "ImagePrefix": "string", '
                                                               '"VolumeMounts": [{"Name": "string", '
                                                               '"MountPath": "string"}], '
                                                               '"SecurityContext": {"Privileged": '
                                                               'true}}], "Group": "string"}}',
                                          'EksClusterDetails': '{"Name": "string", "Arn": "string", '
                                                               '"VpcId": "string", "Status": "string", '
                                                               '"Tags": [{"Key": "string", "Value": '
                                                               '"string"}], "CreatedAt": '
                                                               '"2015-01-01T00:00:00"}',
                                          'InstanceDetails': '{"AvailabilityZone": "string", '
                                                             '"IamInstanceProfile": {"Arn": "string", '
                                                             '"Id": "string"}, "ImageDescription": '
                                                             '"string", "ImageId": "string", '
                                                             '"InstanceId": "string", "InstanceState": '
                                                             '"string", "InstanceType": "string", '
                                                             '"OutpostArn": "string", "LaunchTime": '
                                                             '"string", "NetworkInterfaces": '
                                                             '[{"Ipv6Addresses": ["string"], '
                                                             '"NetworkInterfaceId": "string", '
                                                             '"PrivateDnsName": "string", '
                                                             '"PrivateIpAddress": "string", '
                                                             '"PrivateIpAddresses": [{"PrivateDnsName": '
                                                             '"string", "PrivateIpAddress": "string"}], '
                                                             '"PublicDnsName": "string", "PublicIp": '
                                                             '"string", "SecurityGroups": [{"GroupId": '
                                                             '"string", "GroupName": "string"}], '
                                                             '"SubnetId": "string", "VpcId": "string"}], '
                                                             '"Platform": "string", "ProductCodes": '
                                                             '[{"Code": "string", "ProductType": '
                                                             '"string"}], "Tags": [{"Key": "string", '
                                                             '"Value": "string"}]}',
                                          'KubernetesDetails': '{"KubernetesUserDetails": {"Username": '
                                                               '"string", "Uid": "string", "Groups": '
                                                               '["string"]}, "KubernetesWorkloadDetails": '
                                                               '{"Name": "string", "Type": "string", '
                                                               '"Uid": "string", "Namespace": "string", '
                                                               '"HostNetwork": true, "Containers": '
                                                               '[{"ContainerRuntime": "string", "Id": '
                                                               '"string", "Name": "string", "Image": '
                                                               '"string", "ImagePrefix": "string", '
                                                               '"VolumeMounts": [{"Name": "string", '
                                                               '"MountPath": "string"}], '
                                                               '"SecurityContext": {"Privileged": '
                                                               'true}}], "Volumes": [{"Name": "string", '
                                                               '"HostPath": {"Path": "string"}}]}}',
                                          'S3BucketDetails': '[{"Arn": "string", "Name": "string", '
                                                             '"Type": "string", "CreatedAt": '
                                                             '"2015-01-01T00:00:00", "Owner": {"Id": '
                                                             '"string"}, "Tags": [{"Key": "string", '
                                                             '"Value": "string"}], '
                                                             '"DefaultServerSideEncryption": '
                                                             '{"EncryptionType": "string", '
                                                             '"KmsMasterKeyArn": "string"}, '
                                                             '"PublicAccess": {"PermissionConfiguration": '
                                                             '{"BucketLevelPermissions": '
                                                             '{"AccessControlList": '
                                                             '{"AllowsPublicReadAccess": true, '
                                                             '"AllowsPublicWriteAccess": true}, '
                                                             '"BucketPolicy": {"AllowsPublicReadAccess": '
                                                             'true, "AllowsPublicWriteAccess": true}, '
                                                             '"BlockPublicAccess": {"IgnorePublicAcls": '
                                                             'true, "RestrictPublicBuckets": true, '
                                                             '"BlockPublicAcls": true, '
                                                             '"BlockPublicPolicy": true}}, '
                                                             '"AccountLevelPermissions": '
                                                             '{"BlockPublicAccess": {"IgnorePublicAcls": '
                                                             'true, "RestrictPublicBuckets": true, '
                                                             '"BlockPublicAcls": true, '
                                                             '"BlockPublicPolicy": true}}}, '
                                                             '"EffectivePermission": "string"}}]'},
                             'ResourceType': 'string',
                             'SchemaVersion': 'string',
                             'Service': '{"Action": {"ActionType": "string", "AwsApiCallAction": {"Api": '
                                        '"string", "CallerType": "string", "DomainDetails": {"Domain": '
                                        '"string"}, "ErrorCode": "string", "UserAgent": "string", '
                                        '"RemoteIpDetails": {"City": {"CityName": "string"}, "Country": '
                                        '{"CountryCode": "string", "CountryName": "string"}, '
                                        '"GeoLocation": {"Lat": 123.0, "Lon": 123.0}, "IpAddressV4": '
                                        '"string", "Organization": {"Asn": "string", "AsnOrg": "string", '
                                        '"Isp": "string", "Org": "string"}}, "ServiceName": "string", '
                                        '"RemoteAccountDetails": {"AccountId": "string", "Affiliated": '
                                        'true}, "AffectedResources": {"string": "string"}}, '
                                        '"DnsRequestAction": {"Domain": "string", "Protocol": "string", '
                                        '"Blocked": true}, "NetworkConnectionAction": {"Blocked": true, '
                                        '"ConnectionDirection": "string", "LocalPortDetails": {"Port": '
                                        '123, "PortName": "string"}, "Protocol": "string", '
                                        '"LocalIpDetails": {"IpAddressV4": "string"}, "RemoteIpDetails": '
                                        '{"City": {"CityName": "string"}, "Country": {"CountryCode": '
                                        '"string", "CountryName": "string"}, "GeoLocation": {"Lat": '
                                        '123.0, "Lon": 123.0}, "IpAddressV4": "string", "Organization": '
                                        '{"Asn": "string", "AsnOrg": "string", "Isp": "string", "Org": '
                                        '"string"}}, "RemotePortDetails": {"Port": 123, "PortName": '
                                        '"string"}}, "PortProbeAction": {"Blocked": true, '
                                        '"PortProbeDetails": [{"LocalPortDetails": {"Port": 123, '
                                        '"PortName": "string"}, "LocalIpDetails": {"IpAddressV4": '
                                        '"string"}, "RemoteIpDetails": {"City": {"CityName": "string"}, '
                                        '"Country": {"CountryCode": "string", "CountryName": "string"}, '
                                        '"GeoLocation": {"Lat": 123.0, "Lon": 123.0}, "IpAddressV4": '
                                        '"string", "Organization": {"Asn": "string", "AsnOrg": "string", '
                                        '"Isp": "string", "Org": "string"}}}]}, '
                                        '"KubernetesApiCallAction": {"RequestUri": "string", "Verb": '
                                        '"string", "SourceIps": ["string"], "UserAgent": "string", '
                                        '"RemoteIpDetails": {"City": {"CityName": "string"}, "Country": '
                                        '{"CountryCode": "string", "CountryName": "string"}, '
                                        '"GeoLocation": {"Lat": 123.0, "Lon": 123.0}, "IpAddressV4": '
                                        '"string", "Organization": {"Asn": "string", "AsnOrg": "string", '
                                        '"Isp": "string", "Org": "string"}}, "StatusCode": 123, '
                                        '"Parameters": "string"}}, "Evidence": '
                                        '{"ThreatIntelligenceDetails": [{"ThreatListName": "string", '
                                        '"ThreatNames": ["string"]}]}, "Archived": true, "Count": 123, '
                                        '"DetectorId": "string", "EventFirstSeen": "string", '
                                        '"EventLastSeen": "string", "ResourceRole": "string", '
                                        '"ServiceName": "string", "UserFeedback": "string", '
                                        '"AdditionalInfo": {"Value": "string", "Type": "string"}, '
                                        '"FeatureName": "string", "EbsVolumeScanDetails": {"ScanId": '
                                        '"string", "ScanStartedAt": "2015-01-01T00:00:00", '
                                        '"ScanCompletedAt": "2015-01-01T00:00:00", "TriggerFindingId": '
                                        '"string", "Sources": ["string"], "ScanDetections": '
                                        '{"ScannedItemCount": {"TotalGb": 123, "Files": 123, "Volumes": '
                                        '123}, "ThreatsDetectedItemCount": {"Files": 123}, '
                                        '"HighestSeverityThreatDetails": {"Severity": "string", '
                                        '"ThreatName": "string", "Count": 123}, "ThreatDetectedByName": '
                                        '{"ItemCount": 123, "UniqueThreatNameCount": 123, "Shortened": '
                                        'true, "ThreatNames": [{"Name": "string", "Severity": "string", '
                                        '"ItemCount": 123, "FilePaths": [{"FilePath": "string", '
                                        '"VolumeArn": "string", "Hash": "string", "FileName": '
                                        '"string"}]}]}}}}',
                             'Severity': 0,
                             'Title': 'title',
                             'Type': 'string',
                             'UpdatedAt': '2022-09-07T13:48:00.814Z'}]
