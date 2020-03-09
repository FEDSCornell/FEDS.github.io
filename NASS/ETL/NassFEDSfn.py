from ftplib import FTP
import pandas as pd
import sys
import os
import re
import importlib
import pyodbc
import sys
import ftplib
import datetime
import subprocess
import os
import pyodbc
import re
from operator import itemgetter
import gzip
import shutil
from time import strptime
import calendar
from pandas import DataFrame


def create_schema(sqlServerInstance,dbname, schema):
    connectionStr = "DRIVER={SQL Server};SERVER=" + sqlServerInstance + ";DATABASE=" + dbname + ";Trusted Connection = Yes" + ",  autocommit=True"
    conn = pyodbc.connect(connectionStr)
    cursor = conn.cursor()
    Schema_qry = """ IF NOT EXISTS ( SELECT  * FROM    sys.schemas     WHERE   name = N'""" + schema + """' )   EXEC('CREATE SCHEMA [""" + schema + """]'); """
    cursor.execute(Schema_qry)
    cursor.commit()
    print("Schema " + schema +" is ready")

def create_tables(Dir_create_tabletxt,sqlServerInstance,dbname,schema,sqltablename, cursor):


    try:
        f = open(Dir_create_tabletxt , 'r')
        query = " ".join(f.readlines())
        sqlct = "Create Table [" + dbname + "].[" + schema + "].[" + sqltablename + "]" + query
        cursor.execute(sqlct)
        cursor.commit()
        print(sqltablename + " is created.")

    except Exception as e:
        # print(sqltablename)
        # print ("alread exists")
        # print (e)
        sqlct = "truncate Table [" + dbname + "].[" + schema + "].[" + sqltablename + "]"
        cursor.execute(sqlct)
        cursor.commit()
        print(sqltablename + " is truncated.")
    return

def NASSprocess(workingDir,NassNames):
    foundAFile = False
    downloadedFile = False

    if (os.path.exists(str(workingDir + "qs." + NassNames + ".txt"))):

        os.remove(str(workingDir + "qs." + NassNames + ".txt"))

    for (thisDir, subsHere, filesHere) in os.walk(workingDir):
        for filename in filesHere:
            if filename.endswith('.gz'):
                os.remove(os.path.join(thisDir, filename))

    # # open a log file and write the current date to it
    fdLog = open(workingDir + 'NASSUpdate.log', 'a')
    fdLog.write(str(datetime.datetime.today()) + '\n')
    fdLog.flush()

    # connect to the NASS FTP server and go to the Quick Stats directory
    print ('logging into NASS ftp...')
    ftp = ftplib.FTP('ftp.nass.usda.gov')
    ftp.login()
    ftp.cwd('quickstats')
    print ('logged into ftp')
    # Get a list of files in the Quick Stats directory
    directoryList = []
    ftp.retrlines('LIST', directoryList.append)

    # Check to see if there is an 'all' files
    for fileEntry in directoryList:
        if fileEntry.find("qs." + str(NassNames) ) > -1:
            foundAFile = True
            break
    fdLog.write(str(foundAFile))
    fdLog.flush()
    # If a file was found, process it
    # foundAFile = True
    if foundAFile:
        print("found " + str(NassNames))
        # Get the date that the file was created on
        parts = fileEntry.split()

        ftp.retrbinary('RETR ' + parts[8], open(workingDir + parts[8], 'wb').write)
        downloadedFile = True
        fdLog.write('downloaded ' + parts[8] + '\n')
        fdLog.close()
        ftp.close()
        print(workingDir + 'qs.' + str(NassNames) + '.txt' + " is stored on the disk")
        # uncompress the file
        with gzip.open(workingDir + parts[8], 'rb') as f_in:
            with open(str(workingDir + 'qs.' + str(NassNames) + '.txt'), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    else:
        raise Exception('force to fail')
        print("Donwload Failed!!! Please Check! ")

def NASSFileFlat(workingDir, NassNames, DownloadDate,LoadDate):
    NASSFile = [x for x in os.listdir(workingDir) if re.match('qs.' + str(NassNames) + '.txt$', x)]
    if NASSFile:
        fdIn = open(workingDir + NASSFile[0], 'r')
        # if (os.path.exists(str(workingDir + "qs." + str(NassNames) + "_ref.txt"))):
        #     os.remove(str(workingDir + "qs." + str(NassNames) + "_ref.txt"))
        mylist = []
        if NassNames =='environmental':
            for chunk in pd.read_csv(workingDir + "qs." + str(NassNames) + ".txt", sep='\t',  dtype=object, header=0, low_memory=False, chunksize=20000, encoding = "ISO-8859-1"):
                mylist.append(chunk)
        else:
            for chunk in pd.read_csv(workingDir + "qs." + str(NassNames) + ".txt", sep='\t', dtype=object, header=0,low_memory=False,chunksize=20000):
                mylist.append(chunk)
        data = pd.concat(mylist,axis=0)
        del mylist
        if NassNames=="census2007zipcode":
            print(NassNames)
            data['CV_PCT']=float("NaN")
        else:
            print("no need to edit CV")
        data['NASSUpdateDate'] = DownloadDate
        data['LoadDate'] = LoadDate

        # data = pd.read_csv(workingDir + "qs." + str(NassNames) + ".txt", sep='\t', header=None,low_memory=False,error_bad_lines = False)
        data.to_csv(workingDir + NassNames + '.txt', sep='|', index=None, header=False)
        fdIn.close()
        # fdOut = open(workingDir + "qs." + str(NassNames) + "_ref.txt", 'w')
        #         # l = fdIn.readline()
        #         # l = fdIn.readline()
        #         # while len(l) > 0:
        #         #     # line = l.replace('\n', '\t\n')
        #         #     # line = '\t' + l
        #         #     line =  l
        #         #     # write the record to the output file
        #         #     fdOut.write(line)
        #         #     l = fdIn.readline()
        #         # fdIn.close()
        # fdOut.close()
    print("Data are exported to the txt file："+workingDir + NassNames + '.txt')
# def NASScsv(workingDir, NassNames):
#     data = pd.read_csv(workingDir + "qs." + str(NassNames) + "_ref.txt", sep='\t', header=None,low_memory=False, nrows=200)
#     data.to_csv(workingDir + NassNames+'.txt', sep='|',index=None, header=None)

def LoadData(dbname,schema,sqltablename, workingDir,NassNames, cursor):
    try:
        if NassNames=='census2007zipcode' or NassNames=='environmental':
            sqlInsert = " bulk insert " + "[" + dbname + "].[" + schema + "].[" + sqltablename + "] from " + "'" + workingDir + NassNames + '.txt' "'" + """ WITH(FIELDTERMINATOR='|')"""
            cursor.execute(sqlInsert)
            cursor.commit()
            print("Loaded data into the SQL table. ")
        else:
            sqlInsert = " bulk insert " + "[" + dbname + "].[" + schema + "].[" + sqltablename + "] from " + "'" + workingDir + NassNames + '.txt' "'" + """ WITH(FIELDTERMINATOR='|',ROWTERMINATOR='\r\n')"""
            # print sqlInsert
            cursor.execute(sqlInsert)
            cursor.commit()
            print("Loaded data into the SQL table. ")
    except Exception as e:
        sqlInsert = " bulk insert " + "[" + dbname + "].[" + schema + "].[" + sqltablename + "] from " + "'" + workingDir + NassNames + '.txt' "'" + """ WITH(FIELDTERMINATOR='|',ROWTERMINATOR='\r\n')"""
        print("problems in loading data to sql")
        print(sqlInsert)
    return

def FindDate(NassNames, url2, url3):
    now = datetime.datetime.now()
    ftp = FTP(url2)
    ftp.login()
    ftp.cwd(url3)
    ls = []
    ftp.retrlines('LIST', ls.append)
    # for entry in ls:
    #     print(entry)
    str1 = ''.join(ls)
    words = re.sub(r'([0-9][0-9]):([0-9][0-9])', ' ' + str(now.year), str1)
    df = words.split('-rw-r--r--')
    df = pd.DataFrame(df, columns=['A'])
    df_1 = pd.DataFrame(df.A.str.split(' ').tolist())
    df_1 = df_1.dropna(thresh=3)
    df_2 = pd.DataFrame(df_1, columns=[17, 18, 20, 21])
    df_2.columns = ['Month', 'Day', 'Year', 'File']

    d = dict((v, k) for k, v in enumerate(calendar.month_abbr))
    df_2.Month = df_2.Month.map(d)
    df_2['Month'] =df_2['Month'].astype(str).str.zfill(2)
    df_2['Date'] = df_2.Month.astype(str) + '_' + df_2['Day'].astype(str) + '_' + df_2['Year'].astype(str)
    df_3 = df_2[df_2['File'].str.contains(str(NassNames)) == True]
    Date = df_3.Date.values[0]

    return(Date)

def PrintOption(url2, url3):
    ftp = FTP(url2)
    ftp.login()
    ftp.cwd(url3)
    ls = []
    ftp.retrlines('LIST', ls.append)
    str1 = ''.join(ls)
    now = datetime.datetime.now()
    words = re.sub(r'([0-9][0-9]):([0-9][0-9])', ' ' + str(now.year), str1)
    df = words.split('-rw-r--r--')
    df = pd.DataFrame(df, columns=['A'])
    df_1 = pd.DataFrame(df.A.str.split(' ').tolist())
    df_1 = df_1.dropna(thresh=3)
    df_2=pd.DataFrame(df_1[21].str.split('.').tolist())
    print(df_2[1])
    return df_2[1]