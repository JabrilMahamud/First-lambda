import boto3
from datetime import date,datetime
import csv

def lambda_handler(event,context):
    csv_name = 'MetaData'+str(date.today())+'-'+datetime.now().strftime("%H-%M")+'.csv'
    i=0    
    dynamoDB=boto3.resource("dynamodb",region_name='eu-west-2')
    table=dynamoDB.Table('Metadatajson')
    tabledict=table.scan(
        ProjectionExpression="#AN,account,#S",
        ExpressionAttributeNames={
            '#AN':'account-name',
            '#S':'status',
        },
    )
    tableList=list(tabledict.items())
    tableResponse=tableList[0][1]
    tableData=[]
    for index in range(len(tableResponse)):
        tableData.append([tableResponse[index].get('account-name'),
        tableResponse[index].get('account'),
        tableResponse[index].get('status')])
    csv_name = 'Metadata-'+str(date.today())+'-'+datetime.now().strftime("%H-%M")+'.csv'
    with open('/tmp/'+csv_name, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter= ',', quoting= csv.QUOTE_NONE)
        filewriter.writerow(('account name', 'account ID', 'status'))
        filewriter.writerows(tableData)
    S3_Client = boto3.client("s3", region_name='eu-west-2')
    allBuckets = S3_Client.list_buckets().get('Buckets')
    foundBucket = False

    j = 0
    while foundBucket == False and j < len(allBuckets) :
        if allBuckets[j].get('Name') == 'MetadataJson':
            foundBucket = True
        j+=1
    if foundBucket == False:
        S3_Client.create_bucket(
            Bucket='MetadataJson',
            CreateBucketConfiguration= {
                'LocationConstraint': 'eu-west-2'
            }        
            
        )
    S3_Client.upload_file('/tmp/'+csv_name,'MetadataJson',csv_name)