# This Python ETL script is developed for the USDA-ERS & Cornell Food Environment Data Project.
# copyright: Jing Yi, jy348@cornell.edu

# The python script login to NASS FTP, download specific datasets, process and load data to corresponding SQL tables.
# Raw data are stored in the SQL "NASSQUICKSTATS_SourceData" tables.
# Data are further processed and cleaned data can be viewed in SQL views in this DB.
# Using create view functions in SQL, you can see how views are created based on SQL tables
# indexes are created for the views to improve their performance

# Detailed information regarding the NASS database can be found from:
# https://fedscornell.github.io/Food-Environment-Data-System/NASS/


# ***************************************user inputs:******************************************

# when you run this python script, it will print out all available datasets to the screen, and ask for "Enter Nass Download File Name: "
# users need to type in the name of the dataset, and this script will automatically finish the ETL.

# or set up SQL Server agent to execute this Python script,
# Type: CmdExec
# Run as: SQL Server Agent Service Account
# Command:
# py C:\Users\.\NassQuickStats\NassFEDS.py

# ***************************************user inputs (ends here) ******************************

# ***************************************Other:******************************************

# Note: indexes are created in sql queries which are not included in this script. Next update could accommodate this.

# dependency: NassFEDSfn.py

import NassFEDSfn as FEDS
import pandas as pd
import importlib
import pyodbc
import sys
from datetime import date

sqlServerInstance = ".\JINGSQL"
dbname = 'NASSQUICKSTATS'
schema = 'NASSQSFTP'
connectionStr = "DRIVER={SQL Server};SERVER=" + sqlServerInstance + ";DATABASE=" + dbname + ";Trusted Connection = Yes" + ",  autocommit=True"
conn = pyodbc.connect(connectionStr)
cursor = conn.cursor()

# VM connection:
# sqlServerInstance = "****.eastus2.cloudapp.azure.com"
# dbname = '.'
# schema = '.'
# username = '****'
# password = '..@'
# connectionStr = "DRIVER={SQL Server};SERVER=" + sqlServerInstance + ";DATABASE=" + dbname + ";autocommit=True;"+"UID="+username+";PWD="+ password


url1 = 'ftp://ftp.nass.usda.gov/quickstats/'
url2 = 'ftp.nass.usda.gov'
url3 = '/quickstats/'

pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_row', 1000)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

workingDir = "C:\\Users\\jing\\Dropbox\\BoxOld\\FEDSshare\\Data\\\FEDS.github.io\\NASS\\ETL\\"
sys.path.append(workingDir)
# in case the dependency is edited:
importlib.reload(FEDS)
# help(FEDS)

# print out available datasets:
NassOpt = FEDS.PrintOption(url2, url3)
NassNames = input("Enter Nass Download File Name: ")
# NassNames = sys.argv[1]
print(sys.argv)
sqltablename = "NASS_QuickStats_"+str(NassNames.capitalize())
#
# download data
FEDS.NASSprocess(workingDir,NassNames)

# fetch download date and loading date
DownloadDate=FEDS.FindDate(NassNames, url2, url3)
today = date.today()
LoadDate = today.strftime("%m_%d_%Y")


# process the raw data
FEDS.NASSFileFlat(workingDir, NassNames, DownloadDate,LoadDate)
# FEDS.NASScsv(workingDir, NassNames)
# create schema
FEDS.create_schema(sqlServerInstance,dbname, schema)


# create a table or recreate the table
Dir_create_tabletxt = workingDir + 'CreateTable.txt'
FEDS.create_tables(Dir_create_tabletxt,sqlServerInstance, dbname, schema, sqltablename, cursor)

FEDS.LoadData(dbname,schema,sqltablename, workingDir,NassNames, cursor)

cursor.close()
conn.close()

#
# # -----------------------check data --------------------------------------------------------------------
# NASSFile = [x for x in os.listdir(workingDir) if re.match('qs.' + str(NassNames) + '.txt$', x)]
# fdIn = open(workingDir + NASSFile[0], 'r')
# l = fdIn.readline()
# print(l)
#
#
# data = pd.read_csv( workingDir + "qs."+ str(NassNames) + "_ref.txt", sep='\t',  header=None,nrows=20)
# data.head(2)
#     .to_csv(workingDir+'test.txt',sep='|')
#
#
# # fix nass flat function
#
# NASSFile = [x for x in os.listdir(workingDir) if re.match('qs.' + str(NassNames) + '.txt$', x)]
# if NASSFile:
#     fdIn = open(workingDir + NASSFile[0], 'r')
#     if (os.path.exists(str(workingDir + "qs." + str(NassNames) + "_ref.txt"))):
#         os.remove(str(workingDir + "qs." + str(NassNames) + "_ref.txt"))
#
# data = pd.read_csv(workingDir + "qs." + str(NassNames) + ".txt", sep='\t', header=None,low_memory=False, nrows=200)
# data.to_csv(workingDir + NassNames+'.txt', sep='|',index=None, header=False)
# # -----------------------check data (end)--------------------------------------------------------------------
# check census2007zipcode; failed loading to sql
# NassNames="census2007zipcode"
# import glob, os
# os.chdir(workingDir)
# for file in glob.glob("*.txt"):
#     print(file)
# test=pd.read_csv(workingDir + NassNames + '.txt', sep='|', header=None,  nrows=100)
# test.head(3)
#
# data.head(2)testeconomics=pd.read_csv(workingDir + "economics" + '.txt', sep='|', header=None,  nrows=100)
# testeconomics.head(3)
#
#
# fdInCensus = open(workingDir + NASSFile[0], 'r')
# lC = fdInCensus.readline()
# lC = fdInCensus.readline()
#
# NASSFileEcon = [x for x in os.listdir(workingDir) if re.match('qs.' + "economics" + '.txt$', x)]
# fdInEcon = open(workingDir + NASSFileEcon[0], 'r')
# l = fdInEcon.readline()
#
# NassNames="environmental"