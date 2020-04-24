# 2015 Water Update

This readme file is created to document the technical steps of updating data of 2015 water use by the U.S. food system. The Food Environment Data System (FEDS) team follows Sarah Rehkamp's[ documentation](https://cornell.box.com/s/s3cr4pnjvkuux7dfv01veogdojqxt8o0 "documentation") to update the water data with technical changes. 

# <span style="color:blue">Step 1 & 2</span>


## Data Source:



### 1. EXCEl file

[https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8](https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8 "https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8")

### 2. NWIS Web Interface: 

**county level:**

[https://waterdata.usgs.gov/al/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=2015&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties--](https://waterdata.usgs.gov/al/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=2015&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties-- "https://waterdata.usgs.gov/al/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=2015&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties--")

## Python script:

[https://cornell.box.com/s/nihol1fmsz0cdtyfbzaebc6dz3g8erxq](https://cornell.box.com/s/nihol1fmsz0cdtyfbzaebc6dz3g8erxq)


The python script is developed by the FEDS team to 

1. download the excel file to have the dictionary file
2. compare the variable names and definitions with previous years 
3. update the concordance sql table based on the 2015 variables names and definitions
4. scrape data from the USGS Web interface for each county
5. call the [R script](https://cornell.box.com/s/rt90klz106zvf0v5bkrks6lphajy9374 "R script") to combine all the downloaded data
6. create the "nwis20_load" SQL table and load raw data into this SQL table
7. create the "nwis20_TSV" sql table based on the "nwis20_load" SQL table. 

create the **[USGS].[nwuip2015].[USCO2015_DD]** and **[USGS].[nwuip2015].[USCO2015]** tables from the source data **usco2015v2.0.xlsx**. 

The python script is also developed to update the [nwuip].[usco_VariableConcordance_2015].

## SQL Tables:

Tables are saved in the "unreviewed" DB before review. 

	1. **[USGS].[nwuip2015].[USCO2015_DD]**: 
		
dictionary table for 2015 USGS water data
	
	2. **[nwuip].[usco_VariableConcordance_2015]**:
updated concordance table with 2015 informaiton

	3. **[nwis].[nwis20_load]**:
raw data of 2015 water use of each county

	4. **[nwis].[nwis20_TSV]**: 
cleaned data

	5. **[nwuip2015].[USCO2015_excel]**: 
2015 water data based on the excel file 

## Variable Update:

### 1. New variables:
2015 USGS water data contains new variables

### 2. Changed variable names:


	2015: DO-WDelv, the definition is the same as the variable "DO-TOTAL" in 2010. So in the Python script, I changed this variable to "DO-TOTAL" to facilitate scripts development. 

	2010: DO-TOTAL
	
	Right now, in the python code, I changed "DO-WDelv" to "DO-TOTAL" in order to reuse the existing code. 




## Data Validation:

1. use the web interface 
2. use the SQL table created based on the excel file
3. compare with downloaded txt files


**Differences between the excel file and the web interface:**

![](https://i.imgur.com/aauZmI3.png)



# <span style="color:blue">Step 3 </span>

## Code:

All scripts in this step are integrated into the [Python script: USGSWater2015_Step3](https://cornell.box.com/s/k0v5x9xbt26n5c6naas4r1ep8y76n7e0).

## Technical steps:

### <span style="color:orange">I. Irrigated acres from COA </span>

#### 1. Created [COA17].[IrrigationData] SQL table

<span style="color:red">Need to re-run the python script to update</span>


	
[**Dependence**: QSData.NASS_QuickStats_Census that the FEDS team created based on NASS data](https://fedscornell.github.io/Food-Environment-Data-System/NASS/). 

	FROM QSData.NASS_QuickStats_Census
	where [PRODN_PRACTICE_DESC] LIKE '%IRRIGATED%'
	and [YEAR]='2017'

Updated the census 2017 data on Apr 21, 2020 to reflect the most recent NASS records. 

	a. the sql query is incorporated into the Python script. 
	
	b. the sql query is developed based on "COA95_10_IrrigationData_NASSQuickStats_sqlprod01_Query_20171127.sql" 
	
	c. changed "year" in the original sql query to 2017.
	
	Note: This table only includes 2017 records



#### 2. Created \[COA17].[AcresHarvestedData] SQL table 

[**Dependence**: QSData.NASS_QuickStats_Census that the FEDS team created based on NASS data](https://fedscornell.github.io/Food-Environment-Data-System/NASS/). 

	  FROM  QSData.NASS_QuickStats_Census
	  WHERE [STATISTICCAT_DESC] = 'AREA HARVESTED'
	  AND [YEAR] IN ('2017')
	  AND [AGG_LEVEL_DESC] IN ('COUNTY','NATIONAL','STATE')
  
Note:

	a. the SQL query in the Python script is developed based on "COA95_10_AreaHarvestedData_NASSQuickStats_sqlprod01_Query_20171127.sql"
	
	b. changed "year" in the original sql query to 2017, so this SQL table only includes 2017 records

#### 3. Created \[COA17].[IrrigationData_Integrated]  SQL view 
	
<span style="color:blue">**Dependence**: </span> <span style="color:purple">**[COA17].[IrrigationData]** and 
**[COA95_10].[NAICS8]** </span> 

This **[COA17].[IrrigationData_Integrated]** SQL view:

[##### Data changes in 2017 census:](https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_1_US/usappxb.pdf)

**Added items include:**

• Aronia berries

• Cherimoyas

• Chickpeas

• Coffee – first time collected in States other than
Hawaii

• Elderberries

• Indian or traditional corn

• Raspberries, other

**Deleted items include:**

• Pineapples not harvested

• Sugarcane not harvested

• Berry acres harvested and not harvested

• Grain storage capacity

**Other changes include:**

• Ginger root added to the vegetable section;
removed from the field crop section

• Pineapple added to fruit, nuts, and berries section;
removed from the field crop section

• Taro root added to the vegetable section; removed
from the field crop section

• Berry acreage for 2017 was collected as bearing
age and nonbearing age, similar to all other fruit; 

**Items combined with another item(s) on the 2017
report form that were reported individually on the
2012 report form include:**


• Small grain dry hay

• Wild dry hay

• Other tame dry hay excluding small grain hay and
wild hay

**You can also find livestock and poultry data changes from** [https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_1_US/usappxb.pdf](https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_1_US/usappxb.pdf "https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_1_US/usappxb.pdf")


<span style="color:purple">**[COA95_10].[NAICS8]**:</span>

ERS developed the special NACIS8 based on MACIS6. Description of the NACIS8 can be found from FEDS server: <span style="color:purple"> [LUT].[MITERS].[NAICS8_v2]</span>


To update 2015 water use data, I need to create new NAICS8 to incorporate the changes. The python script also reflects the changes in the [LUT].[MITERS].[NAICS8_v3] which is developed based on [LUT].[MITERS].[NAICS8_v2]. 

**Created <span style="color:purple">[USGS].[MITERS].[NAICS8_v2017]</span>**


**Validation:**

		SELECT   [NAICS8]
		    ,[NAICS8_DESC]
		    ,[2017Census]
		FROM [USGS].[MITERS].[NAICS8_v2017]
		where [2017Census]='1'



1. filters out the irrigated acreage records 
2. integrate with NAICS8 information 
3. Flagging supressed data:

		[ACRES_F] = CASE WHEN [VALUE] = '(D)' THEN 1
		ELSE 0





<span style="color:red">Questions: </span>

<span style="color:red">Berries: Before union with berry records from [IrrigationData], there are berry records already. 

Data before union with berries and NACIS8 : [IrrigationData_integrated data before including NAICS8:](https://cornell.box.com/s/95fuzkqsre0ehi2xhoodgbbtibd3bc6e)

Created using [This SQL script](https://cornell.box.com/s/r2c74fmre7smuws83cb1kaog6tqofujp)
</span>


No records returned using
		
		select *
		FROM [COA17].[IrrigationData]
		where year = '2017'
		and COMMODITY_DESC = 'berry totals'
		and PRODN_PRACTICE_DESC IN ('IRRIGATED', 'IN THE OPEN IRRIGATED')
		and AGG_LEVEL_DESC = 'national'
		and unit_desc = 'ACRES'
		and   try_convert(float,[VALUE]) is not null




	Note: the sql query of developing the [COA17].[IrrigationData_Integrated] SQL view in the Python script is developed based on the [COA95_10].[IrrigationData_Integrated] SQL view
	
	Note: 
	
	1). made changes in the queries as SQL Server 2012 is more restrictive about data types. It's harder to convert varchar to decimals. In the [IrrigationData] SQL table, [value] is varchar with a lot of nulls. I apply "try_convert" to deal with nulls. 
	
	2). This SQL query only uses 2017 records as the dependent table [COA17].[IrrigationData] only has 2017 records. 

#### 4. Created \[COA17].[Census_IrrigationData_Enhanced]  SQL table 
		
	a. this is created based on the [COA17].[IrrigationData_Integrated] SQL view  
		
	b. the sql query in the Python script is created based on the original "CreateTable_COA95_10_Census_IrrigationData_Enhanced.sql" with changes. 
	
	Changes: 
	
		The original CreateTable_COA95_10_Census_IrrigationData_Enhanced.sql is broken into two pieces in the Python script: 
		<1>. create the SQL table; and 
		<2> insert data into the enhanced sql table. 
		
		Changed view names in the original queries. 
	
	
## <span style="color:orange">II. Irrigated farms from COA </span>

#### 1. Create view [COA17].[IrrFarmsData]
	
	a. this view depends on [COA17].[IrrigationData] and [COA95_10].[NAICS8].
	
	b. developed the sql query based on the [AgCensus].[COA95_10].[IrrigationData] SQL view
	
	c. only includes 2017 records in the query
	
	d. added the "try_convert(float,[VALUE])" clause 
	
#### 2. Create [COA95_10].[Census_IrrFarmsData_Enhanced] SQL table <span style="color:orange"></span>

	a. depends on [COA17].[IrrFarmsData] 
	b. based on the original "CreateTable_COA95_10_Census_IrrFarmsData_Enhanced.sql"
	c. changed table and view names in the original sql query.
	d. the enhanced table removes duplicates from the [IrrigationData_Integrated] view.

## <span style="color:orange">III. Combining COA farms and acreage </span>

<span style="color:blue">**Dependence**: </span> <span style="color:purple">**[COA17].[Census_IrrigationData_Enhanced]**,**[COA95_10].[Irr_UBLB_Edited]**,  **[COA95_10].[2002_Berries]**, and **[COA95_10].[NAICS8]** </span> 

#### 
1. Created [COA17].[IrrDataGAMS] 

	
	Where is the [COA95_10].[2002_Berries] ? 
	

#### 2. Create view [COA95_10].[Irr_UBLB_Edited] in my local. In the FEDS server, there is no need to recreate this SQL view. But on my local, i need to replicate this view to create the [IrrDataGAMS] sql table. 



In [AgCensus].[COA95_10].[IrrigationData]:

change [LOCATION_DESC] \[varchar](50) NULL to 
[LOCATION_DESC] \[varchar](500) NULL,


[value] is varchar in  [COA17].[IrrigationData]. This causes problems in sql queries such as:

select ...[ACRES]= SUM(CAST([VALUE] AS decimal(20,10) )) 
	  --,[ACRES_F] = 0
FROM [COA17].[IrrigationData]

## <span style="color:orange">IV. GAMS scripts </span>

	irrCOA12model.gms
	
	irrCOA12modeldata.gms
	
	irrCOA12source.gms
	
	irrCOA12setsnparms.inc


## <span style="color:orange"> FRIS </span>

Name is changed to: **2018 Irrigation and Water Management Survey**

[https://www.nass.usda.gov/Publications/AgCensus/2017/Online_Resources/Farm_and_Ranch_Irrigation_Survey/index.php](https://www.nass.usda.gov/Publications/AgCensus/2017/Online_Resources/Farm_and_Ranch_Irrigation_Survey/index.php "All tables")


Table 6 changed to Table 7. Irrigation by Estimated Quantity of Water Applied: 2018 and 2013

Table 36.csv is created using the R script: **FRIS_PDF_Scraping_Table_36_2020.R**

### Data Source

[file:///C:/Users/jing/Dropbox/BoxOld/FEDSshare/Data/FEDS.github.io/WaterUseUpdate/Step3/Data/fris_csv/fris_index.htm](file:///C:/Users/jing/Dropbox/BoxOld/FEDSshare/Data/FEDS.github.io/WaterUseUpdate/Step3/Data/fris_csv/fris_index.htm "File Index")


----------

----------

# Questions:



<span style="color:red">NAICS8 </span>

**"NAICS-based codes"**

2012 is the most recent **"NAICS-based codes"** --> no need to update the nacis8 table, right?


https://www.census.gov/eos/www/naics/faqs/faqs.html

https://www.census.gov/eos/www/naics/downloadables/downloadables.html

https://www.census.gov/manufacturing/numerical_list/

no 2017 nacis8 available 

**2017 to 2012 NAICS Concordance:**
https://www.census.gov/eos/www/naics/concordances/concordances.html


<span style="color:red">CREATE VIEW [COA17].[IrrDataGAMS] </span>




<span style="color:red">haven't conducted this change in the concordance table:</span>

	2015: DO-WDelv, the definition is the same as the variable "DO-TOTAL" in 2010. So in the Python script, I changed this variable to "DO-TOTAL" to facilitate scripts development. 

	2010: DO-TOTAL


<span style="color:red">why there are suffix "_2" in "[IrrFarmsData_2]" and "[Census_IrrFarmsData_Enhanced_2]" </span>


<span style="color:red">Berries</span>
https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_1_US/usappxb.pdf

previous: 
Berries - Harvested for Sale and Irrigated: 2002 and 1997
[http://usda.mannlib.cornell.edu/usda/AgCensusImages/2002/01/40/1704/Table-32.pdf](http://usda.mannlib.cornell.edu/usda/AgCensusImages/2002/01/40/1704/Table-32.pdf "http://usda.mannlib.cornell.edu/usda/AgCensusImages/2002/01/40/1704/Table-32.pdf")

2017 and 2012 irrigated berries:

[https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0032_0032.pdf](https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0032_0032.pdf "https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0032_0032.pdf")


link for AL:
[https://www.nass.usda.gov/Quick_Stats/CDQT/chapter/2/table/32/state/AL/year/2017](https://www.nass.usda.gov/Quick_Stats/CDQT/chapter/2/table/32/state/AL/year/2017 "https://www.nass.usda.gov/Quick_Stats/CDQT/chapter/2/table/32/state/AL/year/2017")




Aronia berries and Elderberries are new
items for 2017. In 2012 and previous censuses, data
were included in Other berries. A new summarization
of Blueberries, all for 2017, which combines
Blueberries, tame and Blueberries, wild data was
added. Raspberries, other was added as an additional
breakout for the Raspberries, all summarization in
2017. Berry acreage for 2017 was collected as bearing
age and nonbearing age, similar to all other fruit
crops; however, in 2012, data were collected as
harvested and not harvested acres. 


berries by acres: 2017

[https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_1_US/st99_1_0038_0038.pdf](https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_1_US/st99_1_0038_0038.pdf "https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_1_US/st99_1_0038_0038.pdf")

CA:

[https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0032_0032.pdf](https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0032_0032.pdf "https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0032_0032.pdf")

**state level:**

table 35:  2018 and 2013 berries at the state level

[https://www.nass.usda.gov/Publications/AgCensus/2017/Online_Resources/Farm_and_Ranch_Irrigation_Survey/fris_2_0035_0035.pdf](https://www.nass.usda.gov/Publications/AgCensus/2017/Online_Resources/Farm_and_Ranch_Irrigation_Survey/fris_2_0035_0035.pdf "https://www.nass.usda.gov/Publications/AgCensus/2017/Online_Resources/Farm_and_Ranch_Irrigation_Survey/fris_2_0035_0035.pdf")

**state and county level :**

2017

[Table 32. Land in Berries: 2017 and 2012](Table 32. Land in Berries: 2017 and 2012 "https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0032_0032.pdf")

it is created by:

[https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/](https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/ "https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/")



[https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0033_0033.pdf](https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0033_0033.pdf "https://www.nass.usda.gov/Publications/AgCensus/2017/Full_Report/Volume_1,_Chapter_2_County_Level/California/st06_2_0033_0033.pdf")

download whole dataset

https://www.nass.usda.gov/Quick_Stats/CDQT/chapter/2/table/32/state/AL/county/003/year/2017

# Other resources

[FEDS SQL Server Catalog](https://fedscornell.github.io/Food-Environment-Data-System/SQLServer/)
