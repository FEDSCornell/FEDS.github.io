# USGS 2015 Water Update:



## Data Source:



### 1. EXCEl file

[https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8](https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8 "https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8")

### 2. NWIS Web Interface: 

**county level:**

[https://waterdata.usgs.gov/al/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=2015&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties--](https://waterdata.usgs.gov/al/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=2015&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties-- "https://waterdata.usgs.gov/al/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=2015&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties--")

## Python script:

[https://www.dropbox.com/s/yuv79udqhbqu71q/USGSWater_Jing.py?dl=0](https://www.dropbox.com/s/yuv79udqhbqu71q/USGSWater_Jing.py?dl=0 "https://www.dropbox.com/s/yuv79udqhbqu71q/USGSWater_Jing.py?dl=0")


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


	2015: DO-WDelv

	2010: DO-TOTAL

right now, in the python code, I changed "DO-WDelv" to "DO-TOTAL" in order to reuse the existing code. 


## Data Validation:

1. use the web interface 
2. use the SQL table created based on the excel file
3. compare with downloaded txt files


**Differences between the excel file and the web interface:**

![](https://i.imgur.com/aauZmI3.png)

