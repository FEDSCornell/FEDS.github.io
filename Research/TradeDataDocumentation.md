## Products:

1. [Maps](https://public.tableau.com/profile/feds5440#!/):
2. [Box folder](https://cornell.app.box.com/folder/112384450594):




## Production data:
Production data are pulled from FEDS NASS Quick stats tables. The table was updated on Apr 30, 2020 based on NASS FTP. 

The SQL queries of creating 2012 and 2019 production data:

1. can be found in the [python script](https://cornell.box.com/s/mci0pri4v6a50yk98fz7xilm4b7ximzh) (I didn't save the sql queries separately because i use the python script to create/update data. It's hard to maintain/update same code in different files.)
2. i made changes in the query based on the NASS data. For example, we prefer to use fresh market production records, but it fresh market information is not available in NASS data (no records, suppressed records, etc), we use "ALL UTILIZATION PRACTICES". The SQL code in the python script reflects the strategies. **If you update the production data, probably, you want to pull fresh market data of all selected commodities first, check the data, and then make changes for specific commodities.** 

	**Some special cases:**

	- no fresh market production record of bell pepers in 2012. But it is available in 2019
	- no eggplant production data in NASS. Acres harvested and prices are available, but not production records.
	- squash: fresh market production records in $, not weight. So use "ALL UTILIZATION PRACTICES" for both 2012 & 2019. 
	- Loganberries: the most recent year is 2009
	- Avocados: no production data in 2012. 
	- Guavas: no production data in 2012 & 2019
	- Mangoes: no production data
	- Pineapples: No production data after year 2012, and 2012 production data is suppressed. 
	- Prunes: in last meeting, we agreed to use "ALL UTILIZATION PRACTICES	TONS, FRESH BASIS", but this measurement is not available for 2012 data. I have to switch to all produciton practices, dry basis
	- Other edits made to match NASS commodities with NAICS V2 view:
		
		| NASS Name         | NAICS_V2               |
		|-------------------|------------------------|
		| blueberries wild  | blueberries            |
		| plums & prunes    | plums and prunes       |
		| prunes            | plums and prunes       |
		| lettuce head      | lettuce and romaine    |
		| lettuce romaine   | lettuce and romaine    |
		| lettuce leaf      | lettuce and romaine    |
		| melons honeydew   | honeydews              |
		| melons watermelon | watermelons            |
		| melons cantaloup  | cantaloups             |
		| blueberries tame  | blueberries            |
		| cherries sweet    | cherries  sweet        |
		| plums             | plums and prunes       |
		| strawberries      | strawberry farming     |
		| cherries tart     | cherries  tart         |
		| tangerines        | tangerines & mandarins |
		| peppers bell      | bell peppers           |
		
		 **Note: "NASS  Names" are created by concatenating COMMODITY_DESC and CLASS_DESC, if CLASS_DESC is not "ALL CLASSES"**


	Some commodities are in the 9 category lists, but not in our 2012 production data. Checked each of them. 	

	![](https://blogs.cornell.edu/jingyi/files/2020/05/rightOnly.png)

The byproduct of this step is a mapping table between NASS and NAICS_V2 (not all commodities. only for this study)

| COMMODITY_DESC | CLASS_DESC  | PRODN_PRACTICE_DESC      | UTIL_PRACTICE_DESC        | COM_CLASS         | FIX_COMM               | NAICS8_DESC                                                    | NAICS8   | category |
|----------------|-------------|--------------------------|---------------------------|-------------------|------------------------|----------------------------------------------------------------|----------|----------|
| APRICOTS       | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | apricots          | apricots               | Apricots                                                       | 11133901 | 8        |
| BANANAS        | ALL CLASSES | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | bananas           | bananas                | Bananas                                                        | 11133903 | 7        |
| BOYSENBERRIES  | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | boysenberries     | boysenberries          | Boysenberries                                                  | 11133402 | 6        |
| CHERRIES       | TART        | ALL PRODUCTION PRACTICES | FRESH MARKET              | cherries tart     | cherries  tart         | Cherries  tart                                                 | 11133923 | 8        |
| OLIVES         | ALL CLASSES | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | olives            | olives                 | Olives                                                         | 11133912 | 8        |
| RASPBERRIES    | ALL CLASSES | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | raspberries       | raspberries            | Raspberries                                                    | 11133407 | 6        |
| TANGERINES     | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | tangerines        | tangerines & mandarins | Tangerines & Mandarins                                         | 11132002 | 9        |
| ARTICHOKES     | ALL CLASSES | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | artichokes        | artichokes             | Artichokes                                                     | 11121901 | 4        |
| PEPPERS        | BELL        | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | peppers bell      | bell peppers           | Bell Peppers                                                   | 11121904 | 1        |
| PAPAYAS        | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | papayas           | papayas                | Papayas                                                        | 11133914 | 7        |
| LETTUCE        | LEAF        | ALL PRODUCTION PRACTICES | FRESH MARKET              | lettuce leaf      | lettuce and romaine    | Lettuce and romaine                                            | 11121917 | 1        |
| LETTUCE        | HEAD        | ALL PRODUCTION PRACTICES | FRESH MARKET              | lettuce head      | lettuce and romaine    | Lettuce and romaine                                            | 11121917 | 1        |
| LETTUCE        | ROMAINE     | ALL PRODUCTION PRACTICES | FRESH MARKET              | lettuce romaine   | lettuce and romaine    | Lettuce and romaine                                            | 11121917 | 1        |
| MELONS         | CANTALOUP   | ALL PRODUCTION PRACTICES | FRESH MARKET              | melons cantaloup  | cantaloups             | Cantaloups                                                     | 11121908 | 5        |
| BLACKBERRIES   | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | blackberries      | blackberries           | Blackberries                                                   | 11133401 | 6        |
| BLUEBERRIES    | WILD        | ALL PRODUCTION PRACTICES | FRESH MARKET              | blueberries wild  | blueberries            | Blueberries                                                    | 11133408 | 6        |
| BLUEBERRIES    | TAME        | ALL PRODUCTION PRACTICES | FRESH MARKET              | blueberries tame  | blueberries            | Blueberries                                                    | 11133408 | 6        |
| FIGS           | ALL CLASSES | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | figs              | figs                   | Figs                                                           | 11133907 | 7        |
| NECTARINES     | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | nectarines        | nectarines             | Nectarines                                                     | 11133911 | 8        |
| PRUNES         | ALL CLASSES | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | prunes            | plums and prunes       | Plums and prunes                                               | 11133920 | 8        |
| PLUMS          | ALL CLASSES | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | plums             | plums and prunes       | Plums and prunes                                               | 11133920 | 8        |
| ASPARAGUS      | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | asparagus         | asparagus              | Asparagus                                                      | 11121902 | 4        |
| MELONS         | HONEYDEW    | ALL PRODUCTION PRACTICES | FRESH MARKET              | melons honeydew   | honeydews              | Honeydews                                                      | 11121918 | 5        |
| MELONS         | WATERMELON  | ALL PRODUCTION PRACTICES | FRESH MARKET              | melons watermelon | watermelons            | Watermelons                                                    | 11121925 | 5        |
| SQUASH         | ALL CLASSES | ALL PRODUCTION PRACTICES | ALL UTILIZATION PRACTICES | squash            | squash                 | Squash                                                         | 11121931 | 2        |
| SWEET CORN     | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | sweet corn        | sweet corn             | Sweet Corn                                                     | 11121923 | 2        |
| CHERRIES       | SWEET       | ALL PRODUCTION PRACTICES | FRESH MARKET              | cherries sweet    | cherries  sweet        | Cherries  sweet                                                | 11133922 | 8        |
| PEACHES        | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | peaches           | peaches                | Peaches                                                        | 11133916 | 8        |
| STRAWBERRIES   | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | strawberries      | strawberry farming     | Strawberry Farming                                             | 11133300 | 6        |
| BROCCOLI       | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | broccoli          | broccoli               | Broccoli                                                       | 11121905 | 1        |
| CAULIFLOWER    | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | cauliflower       | cauliflower            | Cauliflower                                                    | 11121910 | 2        |
| CUCUMBERS      | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | cucumbers         | cucumbers              | Cucumbers                                                      | 11121912 | 4        |
| SPINACH        | ALL CLASSES | ALL PRODUCTION PRACTICES | FRESH MARKET              | spinach           | spinach                | Spinach                                                        | 11121922 | 1        |
| TOMATOES       | ALL CLASSES | IN THE OPEN              | FRESH MARKET              | tomatoes          | tomatoes               | Tomatoes                                                       | 11121924 | 3        |
|                |             |                          |                           |                   |                        | Eggplant                                                       | 11121913 | 4        |
|                |             |                          |                           |                   |                        | Green Peas                                                     | 11121916 | 4        |
|                |             |                          |                           |                   |                        | Snap Beans                                                     | 11121921 | 4        |
|                |             |                          |                           |                   |                        | Okra                                                           | 11121942 | 4        |
|                |             |                          |                           |                   |                        | Loganberries                                                   | 11133405 | 6        |
|                |             |                          |                           |                   |                        | Avocados                                                       | 11133902 | 7        |
|                |             |                          |                           |                   |                        | Guavas                                                         | 11133908 | 7        |
|                |             |                          |                           |                   |                        | Mangoes                                                        | 11133910 | 7        |
|                |             |                          |                           |                   |                        | Pineapples                                                     | 11133919 | 7        |


<!---
1.	some commodities have 2019 data available, but 2018 is the most recent year for some other commodities. I pulled out the recent years data of each commodity (attached sql query), and used python to keep the most recent year’s records. If the most recent year’s records are suppressed, I use previous year’s data to replace it, or use “all prices” instead of fresh market.
2.	Guavas does not exist either in NASS quickstats or our database. 
3.	Plums & prunes: most recent data is 2015, checked online NASS quickstats and our database
4.	Plums: suppressed data both in 2017 and 2018, checked online NASS quickstats and our database
5.	Prunes: three practices available: processing, ALL UTILIZATION PRACTICES, PROCESSING, DRIED. Which one do you prefer to use?  
6.	What do you mean by “strawberry farming”?
7.	Tangerines: available with different units: $ / BOX, FOB, $ / BOX, ON TREE EQUIV,$ / BOX, PHD EQUIV. Which one to use?
8.	Loganberries: the most recent year is 2009, checked online NASS quickstats and our database

!-->
 





## Population


### Data source:
[https://www.census.gov/data/tables/time-series/demo/popest/2010s-national-total.html#par_textimage_2011805803](https://www.census.gov/data/tables/time-series/demo/popest/2010s-national-total.html#par_textimage_2011805803)

Table:
 
Annual Estimates of the Resident Population for the United States, Regions, States, and Puerto Rico: April 1, 2010 to July 1, 2019 (NST-EST2019-01)   [<1.0 MB]







<!--- production data
2012, 2019
1. most recent year  "2019"
2. removed dollar measures
3. converted to 1000 pounds
4. Prunes	PRUNES	ALL CLASSES	UTILIZED	TONS, FRESH BASIS	2018	279620
!-->
 

<!---

1. use [LUT].[MITERS].[NAICS8_v2] with the Frank's SQL query to create a table with NAICS8, commodity name and categories. 
2. This is merged with the trade data shared by Pat. 
3. aggregated by calendar year and month and by category


It would be problematic if we merge trade data with category data directly as commodity names do not exactly match between the NAICS8_v2 and trade data. This is caused by:

1. different cases, 
2. additional spaces,
3. similar names 

For example, census data uses [COMMODITY_DESC] = "MELONS" and [CLASS_DESC] = "CANTALOUP" for cantaloup, but the trade data uses  
 "melons cantaloup", while trade data uses [CommodityName]="Cantaloupe"



2. merge this concordance table with trade data based on NAICS8,so trade data contains category information.
3. based on this merged dataset, create a unique concordance table mapping 
!-->
 

# Other resources
[Nass Quick Stats Glossary:](https://quickstats.nass.usda.gov/src/glossary.pdf)
