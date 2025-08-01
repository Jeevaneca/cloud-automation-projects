import boto3

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()

    print("=== EC2 Instances ===")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance.get('InstanceId')
            instance_type = instance.get('InstanceType')
            state = instance['State']['Name']
            launch_time = instance.get('LaunchTime')
            print(f"ID: {instance_id} | Type: {instance_type} | State: {state} | Launched: {launch_time}")

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    print("\n=== S3 Buckets ===")
    for bucket in response['Buckets']:
        name = bucket['Name']
        creation_date = bucket['CreationDate']
        print(f"Name: {name} | Created: {creation_date}")

if __name__ == "__main__":
    list_ec2_instances()
    list_s3_buckets()
