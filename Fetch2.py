import boto3

#Declare EC2
ec2 = boto3.resource('ec2')

#Virtual Private Cloud (VPC)
vpc = ec2.create_vpc(
        CidrBlock='192.168.2.0/24',
        TagSpecifications=[
            {
                'ResourceType': 'vpc',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Fetch VPC'
                        }
                    ]
                }
            ]
        )

#Subnet
subnet = ec2.create_subnet(
        TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Fetch Subnet'
                        }
                    ]
                }
            ],
        AvailabilityZone='us-east-2a',
        CidrBlock='192.168.2.0/26',
        VpcId=vpc.id
        )

#Internet Gateway
internet_gateway = ec2.create_internet_gateway(
        TagSpecifications=[
            {
                'ResourceType': 'internet-gateway',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Fetch IG'
                        }
                    ]
                }
            ]
        )

attach_IG = vpc.attach_internet_gateway(
        InternetGatewayId=internet_gateway.id
        )

#Route Table
route_table = ec2.create_route_table(
        VpcId=vpc.id,
        TagSpecifications=[
            {
                'ResourceType': 'route-table',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Fetch Route Table'
                        }
                    ]
                }
            ]
        )
#Associate Route Table
attach_route_table = route_table.associate_with_subnet(
        SubnetId=subnet.id
        )

#Route
#Warning
route = route_table.create_route(
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=internet_gateway.id
        )

#Security Group
security_group = ec2.create_security_group(
        Description='Fetch Open SSH',
        GroupName='Fetch Open SSH',
        VpcId=vpc.id,
        TagSpecifications=[
            {
                'ResourceType': 'security-group',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Fetch SG'
                        }
                    ]
                }
            ]
        )
#Allow Inbound SSH - WARNING
inbound_traffic = security_group.authorize_ingress(
        CidrIp='0.0.0.0/0',
        IpProtocol='tcp',
        FromPort=22,
        ToPort=22
        )

#EC2 Instance
instance = ec2.create_instances(
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/xvda',
                'Ebs': {
                    'VolumeSize': 10
                    }
                },
            {
                'DeviceName': '/dev/xvdf',
                'Ebs': {
                    'VolumeSize': 100
                    }
                }
            ],
        ImageId='ami-07a0844029df33d7d',
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': True,
                'DeviceIndex': 0,
                'Groups': [
                    security_group.id
                    ],
                'SubnetId': subnet.id
                }
            ],
        Placement={
            'AvailabilityZone': 'us-east-2a' #Adjust
            },
        UserData='''
            #!/bin/bash
            cd ~/.ssh/
            ssh-keygen -f users-key
            cd /etc/skel
            mkdir .ssh
            cd .ssh
            cp ~/.ssh/users-key.pub authorized_keys
            adduser user1
            adduser user2
            sudo mkfs /dev/xvdf -t xfs
            sudo mkdir /data
            sudo mount /dev/xvdf /data
            sudo mkfs /dev/xvda -t ext4
            sudo mount /dev/xvda /
        ''',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Fetch EC2'
                        }
                    ]
                }
            ]
        )











