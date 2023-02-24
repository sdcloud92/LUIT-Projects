import boto3

# Get the service resource
sqs = boto3.client('sqs')

# Create the queue. 
sqs_client = boto3.client("sqs", region_name="us-east-1")
response = sqs_client.create_queue(
    QueueName="my-project-queue",
    Attributes={
        "DelaySeconds": "0",
        "VisibilityTimeout": "60",  # 60 seconds
    }
)
print(response) #Printing queue url
