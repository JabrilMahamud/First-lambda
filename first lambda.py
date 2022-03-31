# from ast import Expression
from asyncore import write
from time import time
from unicodedata import name
import boto3
import csv
import datetime as dt

# from __future__ import print_function
# def lambda_handle(event,context):
#     for record in event['records']:
#         print(record['account_name'])
#         print(record['account'])
#         print(record['status'])
#         # print(datetime.datetime.now)
def write2csv(tableList):
    data = [['Account-name'], ['Account-number'], ['status'],] 
    file = open('test.csv', 'w+', newline ='') 
    with file:     
        write = csv.writer(file) 
        write.writerows(tableData) 
    # tableList=str(tableData)
    # print(tableList)
    # # f.write(tableList)
    # csv.writer=csv.writer(f)
    # writer.writerow(tableData)
    # f.close(tableList)

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

# def lambda_handler(event, context):
#     for record in event['Records']:
# get the changes here and save it

write2csv(tableData)