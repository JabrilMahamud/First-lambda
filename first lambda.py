from ast import Expression
import boto3

from __future__ import print_function
def lambda_handle(event,context):
    for record in event['records']:
        print(record['account_name'])
        print(record['account'])
        print(record['status'])
    print('successfully processed % records'%str(len(event['Records'])))




dynamodb =boto3.resource("dynamodb",region_name="eu-west-1")
table=dynamodb.Table("WH-0001-DYN_METADATA")


tabledict=table.scan(
    ProjectionExpression="#AN,account,#S",
    ExpressionAttributeNames={
        '#AN':'account-names',
        '#S':'status',
},

)

tableList=list(tabledict.items())
tableResponse=tableList[0][1]
tableData=[]
for i in range(len(tableResponse)):
    tableData.append([tableResponse[i].get('account-name'),
    tableResponse[i].get('account'),
    tableResponse[i].get('status')])

print (tableData)