import boto3
from datetime import date,datetime
import csv
dynamoDB=boto3.resource("dynamodb",region_name='eu-west-1')
table=dynamoDB.Table('WS-Z038_Metadata')

def lambda_handler(event,context):
    csv_name = 'MetaData'+str(date.today())+'-'+datetime.now().strftime("%H-%M")+'.csv'
    tableData=[]
    tabledict=table.scan(
        ProjectionExpression="#AN,account,#S",
        ExpressionAttributeNames={
            '#AN':'account-name',
            '#S':'status',
},
)
    tableList=list(tabledict.items())
    tableResponse=tableList[0][1]
    for index in range(len(tableResponse)):
        tableData.append([tableResponse[index].get('account-name'),
        tableResponse[index].get('account'),
        tableResponse[index].get('status')])


    S3_Client = boto3.client("s3", region_name='eu-west-1')
    allBuckets = S3_Client.list_buckets().get('Buckets')
    foundBucket = False

    j = 0
    while foundBucket == False and j < len(allBuckets) :
        if allBuckets[j].get('Name') == 'ws-z038-metadata-bucket':
            foundBucket = True
        j+=1
    if foundBucket == False:
        S3_Client.create_bucket(
            Bucket='ws-z038-metadata-bucket',
            CreateBucketConfiguration= {
                'LocationConstraint': 'eu-west-1'
            }        
        )
    S3_Client.upload_file('/tmp/'+csv_name,'ws-z038-metadata-bucket',csv_name)