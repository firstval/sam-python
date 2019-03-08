import boto3

client = boto3.client('lambda')

response = client.invoke(
    FunctionName='arn:aws:lambda:us-east-1:417012313549:function:EC2Restart',
    InvocationType='Event',
    LogType='Tail',
)
print('Invoke successful')