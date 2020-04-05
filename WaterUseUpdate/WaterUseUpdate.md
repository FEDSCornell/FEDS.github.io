# USGS

**Data Source:**

[https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8](https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8 "https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8")

**Python script:**

[https://www.dropbox.com/s/3cyo60yw6zq350v/USGSWater.py?dl=0](https://www.dropbox.com/s/3cyo60yw6zq350v/USGSWater.py?dl=0 "https://www.dropbox.com/s/3cyo60yw6zq350v/USGSWater.py?dl=0")


The python script is developed by the FEDS team to create the **[USGS].[nwuip2015].[USCO2015_DD]** and **[USGS].[nwuip2015].[USCO2015]** tables from the source data **usco2015v2.0.xlsx**. 

The python script is also developed to update the [nwuip].[usco_VariableConcordance_2015].

**SQL Tables:**

Tables are saved in the "unreviewed" DB for now. 


**Data Validation:**


Use Delaware data to validate 

[https://waterdata.usgs.gov/de/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=2015&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties--&wu_category_nms=--ALL%2BCategories--](https://waterdata.usgs.gov/de/nwis/water_use?format=html_table&rdb_compression=file&wu_area=County&wu_year=2015&wu_county=ALL&wu_category=ALL&wu_county_nms=--ALL%2BCounties--&wu_category_nms=--ALL%2BCategories-- "Delaware county data from USGS")

Also checked the **[USGS].[nwuip2015].[USCO2015_DD]** table based USGS online data. 

    
    SELECT TOP (1000) [Column Tag]
      ,[Data Element]
      FROM [unreviewed].[nwuip2015].[USCO2015_DD]
      where [Column Tag] IN ( 'TP-TotPop', 'PS-GWPop')
