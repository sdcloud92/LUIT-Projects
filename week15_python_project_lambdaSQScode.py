import json
import boto3
from datetime import datetime

def lambda_handler(event, context):  #required
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S %p")
   
   sqs = boto3.client('sqs')  #client is required to interact with 
   sqs.send_message(
       QueueUrl="https://sqs.us-east-1.amazonaws.com/357200527695/my-project-queue",
       MessageBody=current_time
   )
   
   return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }