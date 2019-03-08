import boto3
import time

def lambda_handler(event, context):

    client = boto3.client('ec2')

    response = client.stop_instances(
        InstanceIds=[
            'i-077753e015574a473'
        ],
        # DryRun=True
    )

    time.sleep(120)

    response = client.start_instances(
        InstanceIds=[
            'i-077753e015574a473'
        ],
        # DryRun=True
    )
