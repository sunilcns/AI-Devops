#!/bin/sh

# create VPC and a subnet in us-east region 
# VPC CIDR block :  default to
# Subnet CIDR block : default to


echo "Creating VPC and Subnet in us-east-1 region..."
aws ec2 create-vpc --cidr-block 10.0.0.0/16
aws ec2 create-subnet --vpc-id <VPC_ID> --cidr-block 10.0.1.0/24


