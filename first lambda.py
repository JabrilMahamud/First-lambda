import boto3
from datetime import date, datetime
import csv

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')
    table = dynamodb.Table('WS-Z038_Metadata')
    
    
    tableDict = table.scan(
        ProjectionExpression='#AN, account, #S',
        ExpressionAttributeNames={
            '#AN': 'account-name',
            '#S': 'status',
        },
    )
    
    
    tableList = list(tableDict.items())
    tableResponse = tableList[0][1]
    tableData = []
    for i in range(len(tableResponse)):
            tableData.append([tableResponse[i].get('account-name'), 
            tableResponse[i].get('account'), 
            tableResponse[i].get('status')])
            
            
    csv_name = 'WS-Z038-'+str(date.today())+'-'+datetime.now().strftime("%H-%M")+'.csv'
    with open('/tmp/'+csv_name, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter= ',', quoting= csv.QUOTE_NONE)
        filewriter.writerow(('account name', 'account ID', 'status'))
    #for j in range(len(tableData)):
        filewriter.writerows(tableData)
    
    
    S3_Client = boto3.client("s3", region_name='eu-west-1')
    allBuckets = S3_Client.list_buckets().get('Buckets')
    foundBucket = False
    i = 0
    while foundBucket == False and i < len(allBuckets) :
        if allBuckets[i].get('Name') == 'ws-z038-metadata-bucket':
            foundBucket = True
        i+=1
    if foundBucket == False:
        S3_Client.create_bucket(
            Bucket='ws-z038-metadata-bucket',
            CreateBucketConfiguration= {
                'LocationConstraint': 'eu-west-1'
            }
            
        )
    
    S3_Client.upload_file('/tmp/'+csv_name,'ws-z038-metadata-bucket',csv_name)
