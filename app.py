import os
import pandas as pd
import numpy as np
import mysql.connector
from sqlalchemy import create_engine

password = os.environ["My_SQL"]


def connect_aws():
    conn = mysql.connector.connect(
        host="database-1.c5symesi6dhr.eu-north-1.rds.amazonaws.com",
        user="admin",
        password=password,
        database="test",
    )

    return conn


def connect_mysql():
    engine = create_engine(
        f"mysql+mysqlconnector://root:{password}%40@0.tcp.in.ngrok.io:13999/supermarket "
    )
    return engine


def fetch_table(table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, mysql_engine)
    return df


mysql_engine = connect_mysql()
invoices = fetch_table("invoices")
orderleads = fetch_table("orderleads")
salesteam = fetch_table("salesteam")


print(invoices.shape, orderleads.shape, salesteam.shape, sep=" ")
