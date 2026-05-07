import boto3

# 1. Connecting to the EC2 resource
ec2 = boto3.resource('ec2', region_name='us-east-1')

def create_centos_server():
    try:
        print("Starting creation of CentOS 8 server without keypair...")
        
        # Note: To use a specific VPC, you usually provide a SubnetId 
        # from that VPC. If you don't provide one, it uses the default subnet.
        
        instances = ec2.create_instances(
            ImageId='ami-0b4f379183e5706b9',
            MinCount=1,
            MaxCount=1,
            InstanceType='t3.small',
            # KeyName is removed to proceed without a keypair
            SecurityGroupIds=['sg-0436d2d64293a78c1'],
            # If you want to specify the VPC, you must provide a Subnet ID within that VPC
            SubnetId='subnet-0cded6dba9b7f4394', 
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {'Key': 'Name', 'Value': 'CentOS8-NoKey-Server'},
                        {'Key': 'VPC-ID', 'Value': 'vpc-04853c8f6bc063d04'}
                    ]
                }
            ]
        )
        
        new_instance = instances[0]
        print(f"Success! Instance ID: {new_instance.id}")
        
        print("Waiting for instance to start...")
        new_instance.wait_until_running()
        
        new_instance.reload() 
        print(f"Server is running! Public IP: {new_instance.public_ip_address}")
        print("NOTE: Since no keypair was used, you cannot access this via SSH PEM file.")

    except Exception as e:
        print(f"Error: {e}")

create_centos_server()