#!/usr/bin/env python3

# hack to invoke script from external folders
import sys
sys.path.append('.')

import csv
import glob
from argparse import ArgumentParser

from ingest import config
from ingest.models import *


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='Prowler scan manager',
        description='What the program does',
        epilog='Created by Lance Allen @ Mission Cloud'
    )
    parser.add_argument('scan_csv_path')
    parser.add_argument('-c', '--customer')
    args = parser.parse_args()

    # Create customer if does not exist
    customer = Customer.select().where(
        Customer.name == args.customer
    ).first()
    if not customer:
        print(f'Customer does not exist. Creating...')
        customer = Customer.create(
            name=args.customer
        )
        customer.save()
    else:
        print('found customer...proceeding')
    
    # Create new report
    report = Report.create(
        customer=customer.id
    )
    report.save()

    # Ingest CSV details
    files = glob.glob(config.CSV_DIR + '/*.csv')

    # iterate and parse CSV contents (prowler scans)
    for file in files:
        # read
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            contents = list(reader)
            for row in contents:
                # print(row)
                item = ReportItem.create(
                    report=report.id,
                    profile=row['PROFILE'],
                    account_id=row['ACCOUNT_NUM'],
                    region=row['REGION'],
                    title_id=row['TITLE_ID'],
                    check_result=row['CHECK_RESULT'],
                    item_scored=row['ITEM_SCORED'],
                    item_level=row['ITEM_LEVEL'],
                    title_text=row['TITLE_TEXT'],
                    check_result_extended=row['CHECK_RESULT_EXTENDED'],
                    check_asff_compliance_type=row['CHECK_ASFF_COMPLIANCE_TYPE'],
                    check_severity=row['CHECK_SEVERITY'],
                    check_servicename=row['CHECK_SERVICENAME'],
                    check_asff_resource_type=row['CHECK_ASFF_RESOURCE_TYPE'],
                    check_asff_type=row['CHECK_ASFF_TYPE'],
                    check_risk=row['CHECK_RISK'],
                    check_remediation=row['CHECK_REMEDIATION'],
                    check_doc=row['CHECK_DOC'],
                    check_caf_epic=row['CHECK_CAF_EPIC'],
                )
                item.save()
                print(f'stored item {item.id}')
