from asyncore import write
from time import time
import boto3
import csv
import datetime as dt

def write2csv(tableList):
    data = [['Account-name'], ['Account-number'], ['status'],] 
    file = open('test.csv', 'w+', newline ='') 
    with file:     
        write = csv.writer(file) 
        write.writerows(tableData) 

dynamodb =boto3.resource("dynamodb",region_name="eu-west-1")
table=dynamodb.Table("WH-0001-DYN_METADATA")

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