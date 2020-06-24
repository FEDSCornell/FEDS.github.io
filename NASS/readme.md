
# NASS QuickStats 

## Updates in June 2020
1. created the schema PM for produce models
2. created an index view "[PM].[NASS_QuickStats_Survey_CropsSubset]" which is a subset of the crop view in order to remove some duplicates. These duplicates are not exactly duplicated with each other. The duplicates are mainly caused by Null fields. 
	1. The [PM].[NASS_QuickStats_Survey_CropsSubset] view does not include [GROUP_DESC] = 'CROP TOTALS' , 'FIELD CROPS' or 'COMMODITIES'. 
	2. It does not include almonds, apples and onions data. 
	3. This view is mainly created for the fresh fruits and vegetables study.   
3. Depending on the indexed view, we created views: PM.NassProduction, NassPrice and NassYield for the produce models.

4. The [NASSQUICKSTATS_SourceData].[LUT].[NassNaics8] SQL table is created by the python script: ProductionUpdate2012_2019.py to show the link between NASS data and NAICS8 data. 
5. The NassNaics8 and the production, price and yield views are used to create annual production, price and yield views.

## Updates in April and May 2020
1. Updated the source data of NASS survey crops on April 30, 2020
2. The [NASSQUICKSTATS_SourceData].[NASSQSFTP].[NASS_QuickStats_Crops] table is the original one, and [NASSQUICKSTATS_SourceData].[NASSQSFTP].[NASS_QuickStats_Crops_20200430] is the updated table. 
3. I did not remove or change the [NASSQUICKSTATS_SourceData].[NASSQSFTP].[NASS_QuickStats_Crops] table in case some programs are using it. 
4. Created indexed view [QSData].[NASS_QuickStats_Survey_Crops] 

## Caveat
1. census2002, census2007, census2012, and census2017 tables are stacked into the census02_17 in our sql server. Then  [NASSQUICKSTATS].[QSData].[NASS_QuickStats_Census02_07] is renamed as  [NASSQUICKSTATS].[QSData].[NASS_QuickStats_Census] to make the previous queries run smoothly. 

2. In the updated version, we do not keep a table for the suffix zipcode.txt.gz data file because the corresponding census data file already contains the zipcode information.  <span style="color:red">In the census data, if the [AGG_LEVEL_DESC] = 'ZIP CODE', a same record is stored in the zipcode data file, and the [LOCATION_DESCRIPTION] is the same as the column [ZIP_5], which are zip codes.</span>

3. Views split the dynamic data files to census and survey tables (see next section for static and dynamic data files).
4. [NASSQUICKSTATS_SourceData].[NASSQSFTP].[NASS_QuickStats_Demographics] only has [SOURCE_DESC]=CENSUS.



## Description
  - Download source data from NASS ftp:
  
	[ftp://ftp.nass.usda.gov/quickstats/](ftp://ftp.nass.usda.gov/quickstats/ "ftp://ftp.nass.usda.gov/quickstats/")

![](https://blogs.cornell.edu/jingyi/files/2020/02/nass.png)


**The NASS ftp contains static data files:**

![](https://blogs.cornell.edu/jingyi/files/2020/02/static.png)

**While the following files are updated daily:**
![](https://blogs.cornell.edu/jingyi/files/2020/02/dynamic.png)

## ETL Logic:


1. Python scripts download, transform, and load the data files to [NASSQUICKSTATS_SourceData]. Each data file on the NASS ftp has a corresponding SQL table in [NASSQUICKSTATS_SourceData], except the zipcode files. 

2. Views are created in [NASSQUICKSTATS_SourceData] to clean the raw data. The views were originally developed by USDA-ERS. Minor changes are made to fit into the FEDS SQL server.
3. SQL tables are created in **[NASSQUICKSTATS]** based on views in [NASSQUICKSTATS_SourceData] to improve the speed. 
4. Indices are created to further improve the performance. 


## Scripts
Python code is developed for the ETL job:
	 - NassFEDS.py:
		 - [https://www.dropbox.com/s/v8ufdvbx8q1s2sp/NassFEDS.py?dl=0](https://www.dropbox.com/s/v8ufdvbx8q1s2sp/NassFEDS.py?dl=0 "https://www.dropbox.com/s/v8ufdvbx8q1s2sp/NassFEDS.py?dl=0")
	 - NassFEDSfn.py:
		 - [https://www.dropbox.com/s/8r027131ra6fyim/NassFEDSfn.py?dl=0](https://www.dropbox.com/s/8r027131ra6fyim/NassFEDSfn.py?dl=0 "https://www.dropbox.com/s/8r027131ra6fyim/NassFEDSfn.py?dl=0")
	 
## Restrictions faced by the ETL job:
1. we expect to reuse the code and queries developed for the water use project. So we try to keep the table names in SQL the same as they are in the ERS servers. 
2. NASS updates some files on a daily basis. But the FEDS project does not require daily basis. 



## Updates
1. fixed the digits
2. added time stamps (python does the web scraping, parses out NASS update date, and saved the date in the field  [DownloadDate]. Our loading date is saved in the field of [LoadDate] in the [NASSQUICKSTATS_SourceData] DB. 
3. create indexes for views
	Problems: cannot create index if the view is not schema bound
	Solutions: add schema binding

## To Do:
[COUNTRY_CODE] is still 9000 instead of 99000.