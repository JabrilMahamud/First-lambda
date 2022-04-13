<<<<<<< HEAD
from asyncore import write
=======
>>>>>>> fceaa2a9133c16f42a93b3caa39375ac195cfd4d
from time import time
import boto3
import csv
from datetime import datetime

def write2csv(tableList):
    data = [['Account-name'], ['Account-number'], ['status'],] 
    file = open('test.csv', 'w+', newline ='') 
    with file:     
        write = csv.writer(file) 
        write.writerows(tableData) 

    def write2csv(tableList):
        data = [['Account-name'], ['Account-number'], ['status'],] 
        file = open(date_time+'.csv', 'w+', newline ='') 
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

<<<<<<< HEAD
write2csv(tableData)
=======

    write2csv(tableData)

main()
>>>>>>> fceaa2a9133c16f42a93b3caa39375ac195cfd4d
