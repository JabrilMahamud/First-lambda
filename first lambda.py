# from ast import Expression
from time import time
import boto3
import csv
import datetime
# def csvWriter(tabledata):
#     field_names=tabledata[0].keys()
#     with open(tabledata, 'w', newline='', encoding='utf-8') as csv_file_object:
#         writer = csv.DictWriter(csv_file_object, fieldnames=field_names)
#         writer.writeheader()
#         for row_dict in tabledata:
#             writer.writerow(row_dict)

# from __future__ import print_function
# def lambda_handle(event,context):
#     for record in event['records']:
#         print(record['account_name'])
#         print(record['account'])
#         print(record['status'])
#         # print(datetime.datetime.now)
def write2csv(tableList):
    f=open("test_file.csv","w",newline="")
    tableList=str(tableData)
    print(tableList)
    # f.write(tableList)
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