# from ast import Expression
from time import time
import boto3
import csv
import datetime as dt
def main():
    dynamodb =boto3.resource("dynamodb",region_name="eu-west-1")
    table=dynamodb.Table("WH-0001-DYN_METADATA")

    def write2csv(tableList):
        data = [['Account-name'], ['Account-number'], ['status'],] 
        file = open('test.csv', 'w+', newline ='') 
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

    # def lambda_handler(event, context):
    #     for record in event['Records']:
    # get the changes here and save it

    write2csv(tableData)

main()