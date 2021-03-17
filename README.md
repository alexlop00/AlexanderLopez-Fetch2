# boto3 Challenge

# Introduction
## Scope
The purpose of the provided Python script is to deploy a Linux AWS EC2 instance with two volumes and two users.

As per the scope of this script, you will deploy:
* a Virutal Private Cloud (VPC) with CIDR block 192.168.2.0/24
* a Subnet with CIDR block 192.168.2.0/26
* an Internet Gateway, and allocate the resource to the VPC
* a Route Table and Routes, and associate the resource to the Subnet
* a Security Group
* an EC2 instance with the following properties:
  * Instance Type: t2.micro
  * Image Properties:
    * ami_type: amzn2
    * architecture: x86_64
    * root_device_type: ebs
    * virtualization_type: hvm 
  * two volumes: 10 GiB, 100 GiB (mounted in / & /data)
  * two users: user1, user2 (with configured public keys)
  * an Elastic IP address

## Warning

The script defaults to the "us-east-2a" availability zone. Adjust the value according to your configuration.

Location of All Availability Zone Configurations:
* Subnet ... AvailabilityZone: us-east-2a
* EC2 Instance ... AvailabilityZone: us-east-2a

## Security Considerations

This script is intended for demonstration purposes. Open access (i.g. 0.0.0.0/0) is enabled by default. 
Adjust this value as necessary to your configuration. 

Location of All Security Warnings:
* Route ... DestinationCidrBlock: "0.0.0.0/0" 
* Security Group ... CidrIp='0.0.0.0/0'

Additionally, a key pair has not been assigned to the created EC2 instance. Access is via the EC2 Instance Connect console.

Notes: Volumes are not encrypted. Image is not hardened. 

# Prerequisites

Software: 
* Python 3 
* Boto 3
* Amazon Web Services (AWS) Command Line (CLI)
  * Configure AWS with User Access Key

# Deploy

Configure the necessary prerequisites (i.g. software, AWS CLI configuration).

Adjust the Availability Zone values. 

Optional: Restrict access (i.g. Routes, Security Group).

Run the script: python3 Fetch2.py

# Proof of Concept

NOTE: Code has been tested on Ubuntu 20.04 image (AMI Name: ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20210223)

Run the script.

![Script](https://github.com/alexlop00/AlexanderLopez-Fetch2/blob/20662885528e2fb08195a23b92fd26c768306ebf/ProofofConcept/runScript.PNG)

Access EC2 Instance via EC2 Connect.

![EC2 Connect](https://github.com/alexlop00/AlexanderLopez-Fetch2/blob/20662885528e2fb08195a23b92fd26c768306ebf/ProofofConcept/EC2Connect.png)

View created users.

![Created Users](https://github.com/alexlop00/AlexanderLopez-Fetch2/blob/20662885528e2fb08195a23b92fd26c768306ebf/ProofofConcept/users.PNG)

Access user accounts via SSH private key.

![SSH](https://github.com/alexlop00/AlexanderLopez-Fetch2/blob/20662885528e2fb08195a23b92fd26c768306ebf/ProofofConcept/userAccess.png)

View volume mounts.

![Mounts](https://github.com/alexlop00/AlexanderLopez-Fetch2/blob/20662885528e2fb08195a23b92fd26c768306ebf/ProofofConcept/mounts.PNG)



