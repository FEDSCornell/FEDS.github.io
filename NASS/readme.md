
# NASS QuickStats 

## Caveat
1. census2002, census2007, census2012, and census2017 tables are stacked into the census02_17 in our sql server. Then  [NASSQUICKSTATS].[QSData].[NASS_QuickStats_Census02_07] is renamed as  [NASSQUICKSTATS].[QSData].[NASS_QuickStats_Census] to make the previous queries run smoothly. 

2. In the updated version, we do not keep a table for the suffix zipcode.txt.gz data file because the corresponding census data file already contains the zipcode information.  <span style="color:red">In the census data, if the [AGG_LEVEL_DESC] = 'ZIP CODE', a same record is stored in the zipcode data file, and the [LOCATION_DESCRIPTION] is the same as the column [ZIP_5], which are zip codes.</span>

3. Views split the dynamic data files to census and survey tables (see next section for static and dynamic data files).
4. [NASSQUICKSTATS_SourceData].[NASSQSFTP].[NASS_QuickStats_Demographics] only has [SOURCE_DESC]=CENSUS.
5. 


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

## To Do:
[COUNTRY_CODE] is still 9000 instead of 99000.