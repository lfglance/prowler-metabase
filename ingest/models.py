from datetime import datetime
from uuid import uuid4

from peewee import *

from ingest import config


db = PostgresqlDatabase(
    config.DB_NAME, 
    user=config.DB_USER, 
    password=config.DB_PASS,
    host=config.DB_HOST, 
    port=config.DB_PORT
)


def rand_id():
    return uuid4().hex


class BaseTable(Model):
    class Meta:
        database = db

class Customer(BaseTable):
    name = CharField()
    date = DateTimeField(default=datetime.utcnow)


class Report(BaseTable):
    customer = ForeignKeyField(Customer, backref='reports')
    date = DateTimeField(default=datetime.utcnow)


class ReportItem(BaseTable):
    report = ForeignKeyField(Report, backref='items')
    # csv data
    profile = CharField()
    account_id = CharField()
    region = CharField()
    title_id = CharField()
    check_result = CharField()
    item_scored = CharField()
    item_level = CharField()
    title_text = TextField()
    check_result_extended = TextField()
    check_asff_compliance_type = TextField()
    check_severity = TextField()
    check_servicename = CharField()
    check_asff_resource_type = TextField()
    check_asff_type = TextField()
    check_risk = TextField()
    check_remediation = TextField()
    check_doc = CharField()
    check_caf_epic = CharField()

    @property
    def passed(self):
        return True if self.check_result == 'PASS' else False


db.create_tables([Customer, Report, ReportItem])
