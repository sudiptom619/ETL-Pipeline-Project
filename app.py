import os

import mysql.connector

conn = mysql.connector.connect(
    host="database-1.c5symesi6dhr.eu-north-1.rds.amazonaws.com",
    user="admin",
    password=os.environ["My_SQL"],
    database="test",
)
