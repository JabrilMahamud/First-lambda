import boto3
import csv

dynamodb=boto3.resource("dynamodb",region_name="eu-west-2")
table=dynamodb.Table("MetadataJson")

with open("results.csv", "r", newline="") as file:
    csv_file=csv.reader(file)
    for row in csv_file:
        if row[0] != "account-name":
            table.put_item(
                Item={
                    "account-name": str(row[0]),
                    "account":  str(row[1]),
                    "account-description":  str(row[2]),
                    "account-owner":  str(row[3]),
                    "account-type":  str(row[4]),
                    "buyer-contact":  str(row[5]),
                    "cidr-block-size":  str(row[6]),
                    "cloudability_id":  str(row[7]),
                    "connectivity-type":  str(row[8]),
                    "cons-unit":  str(row[9]),
                    "costcode":  str(row[10]),
                    "date_first_user_added_to_operations_ad_group":  str(row[11]),
                    "dbaas_automation_validation_account":  str(row[12]),
                    "dbaas_automation_version":  str(row[13]),
                    "deletion-date":  str(row[14]),
                    "division":  str(row[15]),
                    "dns_validation_account":  str(row[16]),
                    "dns_version":  str(row[17]),
                    "ds_automation_version":  str(row[18]),
                    "ds_essentials_version":  str(row[19]),
                    "environment-type":  str(row[20]),
                    "expiry-date":  str(row[21]),
                    "internet-facing":  str(row[22]),
                    "ip-range":  str(row[23]),
                    "it-service":  str(row[24]),
                    "monthly-budget":  str(row[25]),
                    "network_access":  str(row[26]),
                    "network_local_subnet":  str(row[27]),
                    "network-type":  str(row[28]),
                    "network-validation-account":  str(row[29]),
                    "network-version":  str(row[30]),
                    "rbac-version":  str(row[31]),
                    "region":  str(row[32]),
                    "requested-by":  str(row[33]),
                    "requested-for":  str(row[34]),
                    "root-account":  str(row[35]),
                    "sc-distributor":  str(row[36]),
                    "status":  str(row[37]),
                    "terms-and-conditions":  str(row[38]),
                    "tgw-attachments":  str(row[39]),
                    "trust-level":  str(row[40]),
                    "user-list":  str(row[41])
                }
            )