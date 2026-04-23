import os
import pandas as pd
import numpy as np
from pandas.core.dtypes.common import is_unsigned_integer_dtype
from pandas.io.sql import to_sql
import mysql.connector
from sqlalchemy import create_engine

password = os.environ["My_SQL"]


def connect_aws():
    engine = create_engine(
        f"mysql+mysqlconnector://admin:{password}@database-1.c5symesi6dhr.eu-north-1.rds.amazonaws.com:3306/test"
    )

    return engine


def connect_mysql():
    engine = create_engine(
        f"mysql+mysqlconnector://root:{password}%40@0.tcp.in.ngrok.io:11099/supermarket "
    )
    return engine


def fetch_table(table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, mysql_engine)
    return df


def insert_table_to_aws(df, table_name):
    df.to_sql(name=table_name, con=aws_engine, if_exists="append", index=False)


aws_engine = connect_aws()
mysql_engine = connect_mysql()
invoices = fetch_table("invoices")
orderleads = fetch_table("orderleads")
salesteam = fetch_table("salesteam")
insert_table_to_aws(invoices, "invoices")

print(invoices.shape, orderleads.shape, salesteam.shape, sep=" ")
