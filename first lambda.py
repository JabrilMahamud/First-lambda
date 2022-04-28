import boto3
from datetime import datetime
import csv

def lambda_handler(event, context):
    from time import time
    dynamoDB=boto3.resource("dynamodb",region_name='eu-west-1')
    table=dynamoDB.Table('WS-Z038_Metadata')

    def write2csv(tableList):
        data = [['Account-name'], ['Account-number'], ['status'],] 
        file = open(datetime+'.csv', 'w+', newline ='') 
        with file:     
            write = csv.writer(file) 
            write.writerows(tableData) 
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
    for i in range(len(tableResponse)):
        tableData.append([tableResponse[i].get('account-name'),
        tableResponse[i].get('account'),
        tableResponse[i].get('status')])

    write2csv(tableData)