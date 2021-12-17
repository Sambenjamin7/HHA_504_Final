#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:16:17 2021

@author: samanthabenjamin
"""


##Packages for the sql connection 
from sqlalchemy import create_engine
import sqlalchemy

#Packages for DataFrame
import pandas as pd

MYSQL_HOSTNAME = '52.188.151.163' # change this to your IP address which is found on your AZURE dashboard
MYSQL_USER = 'dba'
MYSQL_PASSWORD = 'ahi2021'
MYSQL_DATABASE = 'tempdata'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

print (engine.table_names())

csvfile = pd.read_csv('/Users/samanthabenjamin/Downloads/H1N1_Flu_Vaccines.csv')
csvfile.to_sql('h1n1_data', con=engine, if_exists='append')
