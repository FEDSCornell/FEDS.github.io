# This script is developed for the FEDS project
# copyright: Jing Yi 2019  jy348@cornell.edu

import re
import pandas as pd
import pyodbc

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
        sqlct = "Create Table [" + dbname + "].[" + schema + "].[" + sqltablename + "]  " + query
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

def LoadData(dbname,schema,sqltablename, cursor,csvName):

    sqlInsert = " bulk insert " + "[" + dbname + "].[" + schema + "].[" + sqltablename + "] from " + "'"  + csvName+ "'" + """ WITH(FIELDTERMINATOR='|', firstrow=2)"""
    cursor.execute(sqlInsert)
    cursor.commit()
    print("Loaded data into the SQL table. ")
    return

pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_row', 1000)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)



sqlServerInstance = ".\JINGSQL"
dbname = 'ACS'
schema = 'SourceData'
sqltablename = 'AgeSex'
connectionStr = "DRIVER={SQL Server};SERVER=" + sqlServerInstance + ";DATABASE=" + dbname + ";Trusted Connection = Yes" + ",  autocommit=True"
conn = pyodbc.connect(connectionStr)
cursor = conn.cursor()


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
workingDir = r"C:\Users\jing\Dropbox\Box\FEDSshare\Data\FEDS.github.io\ACS\AgeSex\PEP_2017_PEPAGESEX"
df = pd.read_csv(workingDir+"\\PEP_2017_PEPAGESEX_with_ann.csv",sep='|', encoding="cp1252")
# df = pd.read_csv(workingDir+"\\PEP_2017_PEPAGESEX_with_ann.csv",sep='|', encoding = "ISO-8859-1", engine='python')
df.head(2)
df.shape
df.columns = df.columns.astype(str)
df_cols = [col for col in df.columns if '2017' in col]
# compare columns in each year to make sure there are no changes.
dfNames = []
for yr in range(2010, 2018):
    print(str(yr))
    dfName = "df"+str(yr)
    dfNames.append(dfName)

IDCols = df[['GEO.id','GEO.id2', 'GEO.display-label']]
IDCols[['County','State']] = IDCols['GEO.display-label'].str.split(',', expand=True)
# IDCols['ST'] = IDCols['State'].replace(us_state_abbrev, regex=True).astype(str)

abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))
# read in fips from [LUT].[fips].[co]
df_fips = pd.read_csv(workingDir+"\\FIPS.txt", sep='\t', dtype={'fips_st':str, 'fips_co':str, 'fips':str})
df_fips['State'] = df_fips.ST.replace(abbrev_us_state, regex=True)
IDCols_fips = pd.concat([IDCols,df_fips], axis=1, sort=False)
IDCols_fips.dtypes
IDCols_fips.columns
IDCols_fips.head()
IDCols_out = IDCols_fips[['GEO.id', 'GEO.id2','GEO.display-label', 'ST','county', 'fips_st', 'fips_co' ]]
IDCols_out.head()
year = 2010
for i in range(1,8):
    yr = year

    dfNames[i] = df.filter(regex=str(yr))
    dfNames[i].columns = dfNames[i].columns.astype(str).str.replace(str(yr), "_year_")
    dfNames[i]['Year'] = str(yr)
    year=year+1
dfAll = pd.DataFrame()
for i in range(1,8):
    dfAll=pd.concat([dfAll,dfNames[i]], axis=0, ignore_index=True)

dfAll_id = pd.concat([IDCols_out, dfAll], axis=1)
IDCols_out.shape
dfAll.shape
dfAll_id.shape
dfAll_id.head()
dfAll_id.to_csv(workingDir+'\\AllYears.csv', sep='|', index=None, )

# get data type
dfAll_id.dtypes

create_schema(sqlServerInstance,dbname, schema)
Dir_create_tabletxt = workingDir + '\\SQLTable.txt'
create_tables(Dir_create_tabletxt,sqlServerInstance,dbname,schema,sqltablename, cursor)
csvName = workingDir+'\\AllYears.csv'
LoadData(dbname,schema,sqltablename,  cursor,csvName)
# df2010 =  df.filter(regex='2010')
# df2010.columns = df2010.columns.astype(str).str.replace('2010', "Year_")
# df2010.rename(df2010.columns.astype(str).str.replace('2010', "Year_"))
# df2 =  df.filter(regex='2017')
# df.columns[df.columns.astype(str).str.contains(r'[0-9][0-9][0-9][0-9]')=='2017']
# df.filter(regex=r'[0-9][0-9][0-9][0-9]').columns.values