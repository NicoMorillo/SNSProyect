import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    tf = event['temperature']*(9/5.0)+32
    response = client.put_item(
        TableName='myLambdaTable',
        Item={
            'timeStamp':{'S':event['timeStamp']},
            'temperature(C)':{'N':str(event['temperature'])},
            'temperature(F)':{'N':str(tf)}
        }
    )
    return 0