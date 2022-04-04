from asyncore import write
from time import time
from unicodedata import name
import boto3
import csv
import datetime as dt
class tabledata:

    def __init__(self,account_name,account_no,stature) -> None:
        self.account_name=None
        self.account_no=None
        self.stature=None

    def tableScanner(self,account_name,account_no,stature):
        tabledict=table.scan(
        ProjectionExpression="#AN,account,#S",
        ExpressionAttributeNames={
            '#AN':'account-name',
            '#S':'status',
    },
    );   return tabledict
    def tableFormatter(self,tabledict):
        tableList=list(tabledict.items())
        tableResponse=tableList[0][1]
        tableData=[]
        for i in range(len(tableResponse)):
            tableData.append([tableResponse[i].get('account-name'),
            tableResponse[i].get('account'),
            tableResponse[i].get('status')])
        return tableData