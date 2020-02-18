



# American Community Survey (ACS)

## Annual Age by Sex at the county level (2010 - 2017):
### Table name: PEPAGESEX

#### The table can be found from:
[https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=PEP_2017_PEPAGESEX&prodType=table](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=PEP_2017_PEPAGESEX&prodType=table "https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=PEP_2017_PEPAGESEX&prodType=table")

For one county:
![](https://blogs.cornell.edu/jingyi/files/2020/02/ageSex.png)

### Processed data

county, state fips


https://www.dropbox.com/s/db6jvqz7qj8mzyq/AgeSex10To17.xlsx?dl=0
C:\Users\jing\Dropbox\Box\FEDSshare\Data\FEDS.github.io\ACS\AgeSex


## Other

### table tool:
[https://www.census.gov/data/tables.html](https://www.census.gov/data/tables.html "https://www.census.gov/data/tables.html")

[https://www.socialexplorer.com/data/ACS2016/metadata/?ds=ACS16](https://www.socialexplorer.com/data/ACS2016/metadata/?ds=ACS16 "https://www.socialexplorer.com/data/ACS2016/metadata/?ds=ACS16")
### Table list:
[https://www.dropbox.com/s/ybkooqj3ub3egve/2018_DataProductList.xlsx?dl=0](https://www.dropbox.com/s/ybkooqj3ub3egve/2018_DataProductList.xlsx?dl=0 "https://www.dropbox.com/s/ybkooqj3ub3egve/2018_DataProductList.xlsx?dl=0")
tools to create/find tables:
[https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t "https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml?refresh=t")


B15002_co
[https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk "data")

use this table:
https://data.census.gov/cedsci/table?g=0100000US.050000&tid=ACSDT5Y2017.B01001&vintage=2018&hidePreview=true&t=%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A&y=2017

## Problems with the ACS data
if the age by sex group is not a problem, we can get county level data from 

[https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk "https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk")

1. ftp:

<span style="color: red;">While PUMS files contain cases from nearly every town and county in the nation, towns and counties (and other low-level geography) are not identified by any variables in the PUMS datasets. The most detailed unit of geography contained in the PUMS files is the Public Use Microdata Area (PUMA). </span>

Files on the FTP server are intended for advanced users.

[https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html](https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html "https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html")

[https://www2.census.gov/programs-surveys/acs/data/pums/](https://www2.census.gov/programs-surveys/acs/data/pums/ "https://www2.census.gov/programs-surveys/acs/data/pums/")

![](https://blogs.cornell.edu/jingyi/files/2020/02/ftp.png)

housing files vs person files

[https://www.dropbox.com/s/q98k2p2vlrkxpu4/psam_p02.csv?dl=0](https://www.dropbox.com/s/q98k2p2vlrkxpu4/psam_p02.csv?dl=0 "https://www.dropbox.com/s/q98k2p2vlrkxpu4/psam_p02.csv?dl=0")

no county information

2. tables

[https://data.census.gov/cedsci/table?d=ACS%205-Year%20Estimates%20Data%20Profiles&table=DP05&tid=ACSDP5Y2018.DP05&g=0400000US10_0500000US10003](https://data.census.gov/cedsci/table?d=ACS%205-Year%20Estimates%20Data%20Profiles&table=DP05&tid=ACSDP5Y2018.DP05&g=0400000US10_0500000US10003 "https://data.census.gov/cedsci/table?d=ACS%205-Year%20Estimates%20Data%20Profiles&table=DP05&tid=ACSDP5Y2018.DP05&g=0400000US10_0500000US10003")

[https://data.census.gov/cedsci/table?d=ACS%205-Year%20Estimates%20Detailed%20Tables&g=0100000US.050000&tid=ACSDT5Y2018.B01001&vintage=2018&hidePreview=true](https://data.census.gov/cedsci/table?d=ACS%205-Year%20Estimates%20Detailed%20Tables&g=0100000US.050000&tid=ACSDT5Y2018.B01001&vintage=2018&hidePreview=true "https://data.census.gov/cedsci/table?d=ACS%205-Year%20Estimates%20Detailed%20Tables&g=0100000US.050000&tid=ACSDT5Y2018.B01001&vintage=2018&hidePreview=true")
but age groups are different



3. table shells

[https://www2.census.gov/programs-surveys/acs/tech_docs/table_shells/2017/](https://www2.census.gov/programs-surveys/acs/tech_docs/table_shells/2017/ "https://www2.census.gov/programs-surveys/acs/tech_docs/table_shells/2017/")

4. other

[https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html](https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html "https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html")

# Explore the data

validate:
[https://data.census.gov/cedsci/table?q=S01&d=ACS%201-Year%20Estimates%20Subject%20Tables&tid=ACSST1Y2018.S0101](https://data.census.gov/cedsci/table?q=S01&d=ACS%201-Year%20Estimates%20Subject%20Tables&tid=ACSST1Y2018.S0101 "https://data.census.gov/cedsci/table?q=S01&d=ACS%201-Year%20Estimates%20Subject%20Tables&tid=ACSST1Y2018.S0101")


download age data from 
https://data.census.gov/cedsci/table?q=S01&d=ACS%201-Year%20Estimates%20Subject%20Tables&g=0100000US.050000&tid=ACSST1Y2018.S0101&hidePreview=true


<span style="color: red;">"There are no published single-year age estimates from the American Community Survey </span>
(ACS), so it is not possible to view the problem at the same level of detail as in the 2000 Census." (Stevenson, Betsey. "Inaccurate age and sex data in the Census PUMS files: Evidence and Implications." PARC Working Papers (2010): 29.)

Tabulations generated from Census PUMS data are
often used in a process called "post-stratification," where preliminary survey weights are set so
that the sample cases sum up to Census Bureau totals by geography, age, sex, race, ethnicity, and
other key demographic variables
## Raw Data
  - Download data from:
  [https://www2.census.gov/programs-surveys/acs/data/pums/2017/1-Year/](https://www2.census.gov/programs-surveys/acs/data/pums/2017/1-Year/)

	[https://www.census.gov/programs-surveys/acs/](https://www.census.gov/programs-surveys/acs/ "https://www.census.gov/programs-surveys/acs/")
	
	[https://www2.census.gov/programs-surveys/acs/data/pums/2017/5-Year/](https://www2.census.gov/programs-surveys/acs/data/pums/2017/5-Year/ "https://www2.census.gov/programs-surveys/acs/data/pums/2017/5-Year/")

  - Parent directory:
  https://www2.census.gov/programs-surveys/acs/data/pums/

  - ACS 2017 has 1-year and 5-year data. I use 1 year data here.
  The 5-year PUMS files are multiyear combinations of the 1-year PUMS file with appropriate adjustments to the weights and inflation adjustment factors.  This explains the differences between the datasets:
   https://www.census.gov/programs-surveys/acs/guidance/estimates.html

![Years of data release ](https://i.imgur.com/NoJoBKg.png)

>“<span style="color: red;">ACS 3-year estimates have been discontinued. </span> The 2005-2007, 2006-2008, 2007-2009, 2008-2010, 2009-2011, 2010-2012 and 2011-2013 ACS 3-year estimates will remain available to data users, but no new 3-year estimates will be produced. Every community in the nation will continue to receive a detailed statistical portrait of its social, economic, housing and demographic characteristics through 1-year and 5-year ACS products.”
https://www.census.gov/programs-surveys/acs/guidance/estimates.html


>In the case of ACS 1-year estimates, the period is the
calendar year (e.g., the 2015 ACS covers the period
from January 2015 through December 2015). In the
case of ACS multiyear estimates, the period is 5 calendar years (e.g., the 2011–2015 ACS estimates cover
the period from January 2011 through December 2015).
<span style="color: red;">Therefore, ACS estimates based on data collected from
2011–2015 should not be labeled “2013,” even though
that is the midpoint of the 5-year period.</span>
https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch03.pdf


>The primary advantage of using multiyear estimates
is the increased statistical reliability of the data compared with that of single-year estimates, particularly
for small geographic areas and small population subgroups. 

>For data users interested in obtaining detailed ACS
data for small geographic areas (areas with fewer than
65,000 residents), ACS 5-year estimates are the only
option
https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch03.pdf

>One-year estimates are particularly useful for geographic areas with rapidly changing characteristics
because they are based on the most current data—
data from the past year. 

 - Public Use Microdata Sample (PUMS) Documentation: 
 https://www.census.gov/programs-surveys/acs/technical-documentation/pums.html
## Code
 - python code is used to automatically download data and loaded to the FEDS SQL server [RawData] database
https://www.dropbox.com/s/avngxkk1ruiidxg/ACS.py?dl=0

## Age Cohort

![Pat cohort image](https://i.imgur.com/Oe3iR6k.png)

## Reference



[https://www.pagnet.org/documents/rdc/census/acs/acsresearch.pdf](https://www.pagnet.org/documents/rdc/census/acs/acsresearch.pdf "https://www.pagnet.org/documents/rdc/census/acs/acsresearch.pdf")

## SQL Table Dictionary [RawData].[acs].[ACSSourceData2017]
| NAME | RT | C | 1 | Record Type |  |  |
|------|-------------|---|----|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------|
| VAL | RT | C | 1 | H | H | Housing Record or Group Quarters Unit |
| VAL | RT | C | 1 | P | P | Person Record |
| NAME | SERIALNO | C | 13 | Housing unit/GQ person serial number |  |  |
| VAL | SERIALNO | C | 13 | 2018GQ0000001 | 2018GQ9999999 | GQ Unique identifier |
| VAL | SERIALNO | C | 13 | 2018HU0000001 | 2018HU9999999 | HU Unique identifier |
| NAME | DIVISION | C | 1 | Division code based on 2010 Census definitions |  |  |
| VAL | DIVISION | C | 1 | 0 | 0 | Puerto Rico |
| VAL | DIVISION | C | 1 | 1 | 1 | New England (Northeast region) |
| VAL | DIVISION | C | 1 | 2 | 2 | Middle Atlantic (Northeast region) |
| VAL | DIVISION | C | 1 | 3 | 3 | East North Central (Midwest region) |
| VAL | DIVISION | C | 1 | 4 | 4 | West North Central (Midwest region) |
| VAL | DIVISION | C | 1 | 5 | 5 | South Atlantic (South region) |
| VAL | DIVISION | C | 1 | 6 | 6 | East South Central (South region) |
| VAL | DIVISION | C | 1 | 7 | 7 | West South Central (South Region) |
| VAL | DIVISION | C | 1 | 8 | 8 | Mountain (West region) |
| VAL | DIVISION | C | 1 | 9 | 9 | Pacific (West region) |
| NAME | PUMA | C | 5 | Public use microdata area code (PUMA) based on 2010 Census definition (areas with population of 100,000 or more, use with ST for unique code) |  |  |
| VAL | PUMA | C | 5 | 00100 | 70301 | Public use microdata area codes |
| NAME | REGION | C | 1 | Region code based on 2010 Census definitions |  |  |
| VAL | REGION | C | 1 | 1 | 1 | Northeast |
| VAL | REGION | C | 1 | 2 | 2 | Midwest |
| VAL | REGION | C | 1 | 3 | 3 | South |
| VAL | REGION | C | 1 | 4 | 4 | West |
| VAL | REGION | C | 1 | 9 | 9 | Puerto Rico |
| NAME | ST | C | 2 | State Code based on 2010 Census definitions |  |  |
| VAL | ST | C | 2 | 01 | 01 | Alabama/AL |
| VAL | ST | C | 2 | 02 | 02 | Alaska/AK |
| VAL | ST | C | 2 | 04 | 04 | Arizona/AZ |
| VAL | ST | C | 2 | 05 | 05 | Arkansas/AR |
| VAL | ST | C | 2 | 06 | 06 | California/CA |
| VAL | ST | C | 2 | 08 | 08 | Colorado/CO |
| VAL | ST | C | 2 | 09 | 09 | Connecticut/CT |
| VAL | ST | C | 2 | 10 | 10 | Delaware/DE |
| VAL | ST | C | 2 | 11 | 11 | District of Columbia/DC |
| VAL | ST | C | 2 | 12 | 12 | Florida/FL |
| VAL | ST | C | 2 | 13 | 13 | Georgia/GA |
| VAL | ST | C | 2 | 15 | 15 | Hawaii/HI |
| VAL | ST | C | 2 | 16 | 16 | Idaho/ID |
| VAL | ST | C | 2 | 17 | 17 | Illinois/IL |
| VAL | ST | C | 2 | 18 | 18 | Indiana/IN |
| VAL | ST | C | 2 | 19 | 19 | Iowa/IA |
| VAL | ST | C | 2 | 20 | 20 | Kansas/KS |
| VAL | ST | C | 2 | 21 | 21 | Kentucky/KY |
| VAL | ST | C | 2 | 22 | 22 | Louisiana/LA |
| VAL | ST | C | 2 | 23 | 23 | Maine/ME |
| VAL | ST | C | 2 | 24 | 24 | Maryland/MD |
| VAL | ST | C | 2 | 25 | 25 | Massachusetts/MA |
| VAL | ST | C | 2 | 26 | 26 | Michigan/MI |
| VAL | ST | C | 2 | 27 | 27 | Minnesota/MN |
| VAL | ST | C | 2 | 28 | 28 | Mississippi/MS |
| VAL | ST | C | 2 | 29 | 29 | Missouri/MO |
| VAL | ST | C | 2 | 30 | 30 | Montana/MT |
| VAL | ST | C | 2 | 31 | 31 | Nebraska/NE |
| VAL | ST | C | 2 | 32 | 32 | Nevada/NV |
| VAL | ST | C | 2 | 33 | 33 | New Hampshire/NH |
| VAL | ST | C | 2 | 34 | 34 | New Jersey/NJ |
| VAL | ST | C | 2 | 35 | 35 | New Mexico/NM |
| VAL | ST | C | 2 | 36 | 36 | New York/NY |
| VAL | ST | C | 2 | 37 | 37 | North Carolina/NC |
| VAL | ST | C | 2 | 38 | 38 | North Dakota/ND |
| VAL | ST | C | 2 | 39 | 39 | Ohio/OH |
| VAL | ST | C | 2 | 40 | 40 | Oklahoma/OK |
| VAL | ST | C | 2 | 41 | 41 | Oregon/OR |
| VAL | ST | C | 2 | 42 | 42 | Pennsylvania/PA |
| VAL | ST | C | 2 | 44 | 44 | Rhode Island/RI |
| VAL | ST | C | 2 | 45 | 45 | South Carolina/SC |
| VAL | ST | C | 2 | 46 | 46 | South Dakota/SD |
| VAL | ST | C | 2 | 47 | 47 | Tennessee/TN |
| VAL | ST | C | 2 | 48 | 48 | Texas/TX |
| VAL | ST | C | 2 | 49 | 49 | Utah/UT |
| VAL | ST | C | 2 | 50 | 50 | Vermont/VT |
| VAL | ST | C | 2 | 51 | 51 | Virginia/VA |
| VAL | ST | C | 2 | 53 | 53 | Washington/WA |
| VAL | ST | C | 2 | 54 | 54 | West Virginia/WV |
| VAL | ST | C | 2 | 55 | 55 | Wisconsin/WI |
| VAL | ST | C | 2 | 56 | 56 | Wyoming/WY |
| VAL | ST | C | 2 | 72 | 72 | Puerto Rico/PR |
| NAME | ADJHSG | C | 7 | Adjustment factor for housing dollar amounts (6 implied decimal places) |  |  |
| VAL | ADJHSG | C | 7 | 1000000 | 1000000 | 2018 factor (1.000000) |
| NAME | ADJINC | C | 7 | Adjustment factor for income and earnings dollar amounts (6 implied decimal places) |  |  |
| VAL | ADJINC | C | 7 | 1013097 | 1013097 | 2018 factor (1.013097) |
| NAME | WGTP | N | 5 | Housing Unit Weight |  |  |
| VAL | WGTP | N | 5 | 0 | 0 | Group quarters place holder record |
| VAL | WGTP | N | 5 | 1 | 9999 | Integer weight of housing unit |
| NAME | NP | N | 2 | Number of persons in this household |  |  |
| VAL | NP | N | 2 | 0 | 0 | Vacant unit |
| VAL | NP | N | 2 | 1 | 1 | One person in household or any person in group quarters |
| VAL | NP | N | 2 | 2 | 20 | Number of persons in household |
| NAME | TYPE | C | 1 | Type of unit |  |  |
| VAL | TYPE | C | 1 | 1 | 1 | Housing unit |
| VAL | TYPE | C | 1 | 2 | 2 | Institutional group quarters |
| VAL | TYPE | C | 1 | 3 | 3 | Noninstitutional group quarters |
| NAME | ACCESS | C | 1 | Access to the Internet |  |  |
| VAL | ACCESS | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | ACCESS | C | 1 | 1 | 1 | Yes, by paying a cell phone company or Internet service provider |
| VAL | ACCESS | C | 1 | 2 | 2 | Yes, without paying a cell phone company or Internet service provider |
| VAL | ACCESS | C | 1 | 3 | 3 | No access to the Internet at this house, apartment, or mobile home |
| NAME | ACR | C | 1 | Lot size |  |  |
| VAL | ACR | C | 1 | b | b | N/A (GQ/not a one-family house or mobile home) |
| VAL | ACR | C | 1 | 1 | 1 | House on less than one acre |
| VAL | ACR | C | 1 | 2 | 2 | House on one to less than ten acres |
| VAL | ACR | C | 1 | 3 | 3 | House on ten or more acres |
| NAME | AGS | C | 1 | Sales of Agriculture Products (yearly sales, no adjustment factor is applied) |  |  |
| VAL | AGS | C | 1 | b | b | N/A (GQ/vacant/not a one family house or mobile home/less than 1 acre) |
| VAL | AGS | C | 1 | 1 | 1 | None |
| VAL | AGS | C | 1 | 2 | 2 | $    1 - $  999 |
| VAL | AGS | C | 1 | 3 | 3 | $ 1000 - $ 2499 |
| VAL | AGS | C | 1 | 4 | 4 | $ 2500 - $ 4999 |
| VAL | AGS | C | 1 | 5 | 5 | $ 5000 - $ 9999 |
| VAL | AGS | C | 1 | 6 | 6 | $10000+ |
| NAME | BATH | C | 1 | Bathtub or shower |  |  |
| VAL | BATH | C | 1 | b | b | N/A (GQ) |
| VAL | BATH | C | 1 | 1 | 1 | Yes |
| VAL | BATH | C | 1 | 2 | 2 | No |
| NAME | BDSP | N | 2 | Number of bedrooms |  |  |
| VAL | BDSP | N | 2 | bb | bb | N/A (GQ) |
| VAL | BDSP | N | 2 | 0 | 99 | 0 to 99 bedrooms (Top-coded) |
| NAME | BLD | C | 2 | Units in structure |  |  |
| VAL | BLD | C | 2 | bb | bb | N/A (GQ) |
| VAL | BLD | C | 2 | 01 | 01 | Mobile home or trailer |
| VAL | BLD | C | 2 | 02 | 02 | One-family house detached |
| VAL | BLD | C | 2 | 03 | 03 | One-family house attached |
| VAL | BLD | C | 2 | 04 | 04 | 2 Apartments |
| VAL | BLD | C | 2 | 05 | 05 | 3-4 Apartments |
| VAL | BLD | C | 2 | 06 | 06 | 5-9 Apartments |
| VAL | BLD | C | 2 | 07 | 07 | 10-19 Apartments |
| VAL | BLD | C | 2 | 08 | 08 | 20-49 Apartments |
| VAL | BLD | C | 2 | 09 | 09 | 50 or more apartments |
| VAL | BLD | C | 2 | 10 | 10 | Boat, RV, van, etc. |
| NAME | BROADBND | C | 1 | Cellular data plan for a smartphone or other mobile device |  |  |
| VAL | BROADBND | C | 1 | b | b | N/A (GQ/vacant/no paid access to the internet) |
| VAL | BROADBND | C | 1 | 1 | 1 | Yes |
| VAL | BROADBND | C | 1 | 2 | 2 | No |
| NAME | COMPOTHX | C | 1 | Other computer equipment |  |  |
| VAL | COMPOTHX | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | COMPOTHX | C | 1 | 1 | 1 | Yes |
| VAL | COMPOTHX | C | 1 | 2 | 2 | No |
| NAME | CONP | N | 4 | Condo fee (monthly amount, use ADJHSG to adjust CONP to constant dollars) |  |  |
| VAL | CONP | N | 4 | bbbb | bbbb | N/A (GQ/vacant units/not owned or being bought) |
| VAL | CONP | N | 4 | 0 | 9999 | $0 - $9999 (Rounded and top-coded) |
| NAME | DIALUP | C | 1 | Dial-up service |  |  |
| VAL | DIALUP | C | 1 | b | b | N/A (GQ/vacant/no paid access to the internet) |
| VAL | DIALUP | C | 1 | 1 | 1 | Yes |
| VAL | DIALUP | C | 1 | 2 | 2 | No |
| NAME | ELEFP | C | 1 | Electricity cost flag variable |  |  |
| VAL | ELEFP | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | ELEFP | C | 1 | 1 | 1 | Included in rent or in condo fee |
| VAL | ELEFP | C | 1 | 2 | 2 | No charge or electricity not used |
| VAL | ELEFP | C | 1 | 3 | 3 | Valid monthly electricity cost in ELEP |
| NAME | ELEP | N | 3 | Electricity cost (monthly cost, use ADJHSG to adjust ELEP  to constant dollars) |  |  |
| VAL | ELEP | N | 3 | bbb | bbb | N/A (GQ/vacant/included in rent or in condo fee/no charge or electricity not used ) |
| VAL | ELEP | N | 3 | 3 | 999 | $3 to $999 (Rounded and top-coded) |
| NAME | FS | C | 1 | Yearly food stamp/Supplemental Nutrition Assistance Program (SNAP) recipiency |  |  |
| VAL | FS | C | 1 | b | b | N/A (vacant) |
| VAL | FS | C | 1 | 1 | 1 | Yes |
| VAL | FS | C | 1 | 2 | 2 | No |
| NAME | FULFP | C | 1 | Fuel cost flag variable |  |  |
| VAL | FULFP | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | FULFP | C | 1 | 1 | 1 | Included in rent or in condo fee |
| VAL | FULFP | C | 1 | 2 | 2 | No charge or fuel other than gas or electricity not used |
| VAL | FULFP | C | 1 | 3 | 3 | Valid annual fuel cost in FULP |
| NAME | FULP | N | 4 | Fuel cost (yearly cost for fuels other than gas and electricity, use ADJHSG to adjust FULP to constant dollars) |  |  |
| VAL | FULP | N | 4 | bbbb | bbbb | N/A (GQ/vacant/included in rent or in condo fee/no charge or fuel other than gas or electricity not used) |
| VAL | FULP | N | 4 | 3 | 9999 | $3 to $9999 (Rounded and top-coded) |
| NAME | GASFP | C | 1 | Gas cost flag variable |  |  |
| VAL | GASFP | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | GASFP | C | 1 | 1 | 1 | Included in rent or in condo fee |
| VAL | GASFP | C | 1 | 2 | 2 | Included in electricity payment |
| VAL | GASFP | C | 1 | 3 | 3 | No charge or gas not used |
| VAL | GASFP | C | 1 | 4 | 4 | Valid monthly gas cost in GASP |
| NAME | GASP | N | 3 | Gas cost(monthly cost, use ADJHSG to adjust GASP to constant dollars) |  |  |
| VAL | GASP | N | 3 | bbb | bbb | N/A (GQ/vacant/included in rent or in condo fee/included in electricity payment/no charge or gas not used) |
| VAL | GASP | N | 3 | 4 | 999 | $4 to $999 (Rounded and top-coded) |
| NAME | HFL | C | 1 | House heating fuel |  |  |
| VAL | HFL | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | HFL | C | 1 | 1 | 1 | Utility gas |
| VAL | HFL | C | 1 | 2 | 2 | Bottled, tank, or LP gas |
| VAL | HFL | C | 1 | 3 | 3 | Electricity |
| VAL | HFL | C | 1 | 4 | 4 | Fuel oil, kerosene, etc. |
| VAL | HFL | C | 1 | 5 | 5 | Coal or coke |
| VAL | HFL | C | 1 | 6 | 6 | Wood |
| VAL | HFL | C | 1 | 7 | 7 | Solar energy |
| VAL | HFL | C | 1 | 8 | 8 | Other fuel |
| VAL | HFL | C | 1 | 9 | 9 | No fuel used |
| NAME | HISPEED | C | 1 | Broadband (high speed) Internet service such as cable, fiber optic, or DSL service |  |  |
| VAL | HISPEED | C | 1 | b | b | N/A (GQ/vacant/no paid access to the internet) |
| VAL | HISPEED | C | 1 | 1 | 1 | Yes |
| VAL | HISPEED | C | 1 | 2 | 2 | No |
| NAME | HOTWAT | C | 1 | Water heater (Puerto Rico only) |  |  |
| VAL | HOTWAT | C | 1 | b | b | N/A (GQ) |
| VAL | HOTWAT | C | 1 | 1 | 1 | Yes |
| VAL | HOTWAT | C | 1 | 2 | 2 | No |
| VAL | HOTWAT | C | 1 | 9 | 9 | Case is from the United States, HOTWAT not applicable |
| NAME | INSP | N | 5 | Fire/hazard/flood insurance (yearly amount, use ADJHSG to adjust INSP to constant dollars) |  |  |
| VAL | INSP | N | 5 | bbbbb | bbbbb | N/A (GQ/vacant/not owned or being bought) |
| VAL | INSP | N | 5 | 0 | 0 | None |
| VAL | INSP | N | 5 | 1 | 10000 | $1 to $10000 (Rounded and top-coded) |
| NAME | LAPTOP | C | 1 | Laptop or desktop |  |  |
| VAL | LAPTOP | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | LAPTOP | C | 1 | 1 | 1 | Yes |
| VAL | LAPTOP | C | 1 | 2 | 2 | No |
| NAME | MHP | N | 5 | Mobile home costs (yearly amount, use ADJHSG to adjust MHP to constant dollars) |  |  |
| VAL | MHP | N | 5 | bbbbb | bbbbb | N/A (GQ/vacant/not owned or being bought/ not mobile home) |
| VAL | MHP | N | 5 | 0 | 0 | None |
| VAL | MHP | N | 5 | 1 | 99999 | $1 to $99999 (Rounded and top-coded) |
| NAME | MRGI | C | 1 | First mortgage payment includes fire/hazard/flood insurance |  |  |
| VAL | MRGI | C | 1 | b | b | N/A (GQ/vacant/not owned or being bought/not mortgaged) |
| VAL | MRGI | C | 1 | 1 | 1 | Yes, insurance included in payment |
| VAL | MRGI | C | 1 | 2 | 2 | No, insurance paid separately or no insurance |
| NAME | MRGP | N | 5 | First mortgage payment (monthly amount, use ADJHSG to adjust MRGP to constant dollars) |  |  |
| VAL | MRGP | N | 5 | bbbbb | bbbbb | N/A (GQ/vacant/not owned or being bought/not mortgaged) |
| VAL | MRGP | N | 5 | 1 | 99999 | $1 to $99999 (Rounded and top-coded) |
| NAME | MRGT | C | 1 | First mortgage payment includes real estate taxes |  |  |
| VAL | MRGT | C | 1 | b | b | N/A (GQ/vacant/not owned or being bought/not mortgaged) |
| VAL | MRGT | C | 1 | 1 | 1 | Yes, taxes included in payment |
| VAL | MRGT | C | 1 | 2 | 2 | No, taxes paid separately or taxes not required |
| NAME | MRGX | C | 1 | First mortgage status |  |  |
| VAL | MRGX | C | 1 | b | b | N/A (GQ/vacant/not owned or being bought) |
| VAL | MRGX | C | 1 | 1 | 1 | Mortgage, deed of trust, or similar debt |
| VAL | MRGX | C | 1 | 2 | 2 | Contract to purchase |
| VAL | MRGX | C | 1 | 3 | 3 | None |
| NAME | OTHSVCEX | C | 1 | Other Internet service |  |  |
| VAL | OTHSVCEX | C | 1 | b | b | N/A (GQ/vacant/no paid access to the internet) |
| VAL | OTHSVCEX | C | 1 | 1 | 1 | Yes |
| VAL | OTHSVCEX | C | 1 | 2 | 2 | No |
| NAME | REFR | C | 1 | Refrigerator |  |  |
| VAL | REFR | C | 1 | b | b | N/A (GQ) |
| VAL | REFR | C | 1 | 1 | 1 | Yes |
| VAL | REFR | C | 1 | 2 | 2 | No |
| NAME | RMSP | N | 2 | Number of rooms |  |  |
| VAL | RMSP | N | 2 | bb | bb | N/A (GQ) |
| VAL | RMSP | N | 2 | 0 | 99 | Rooms (Top-coded) |
| NAME | RNTM | C | 1 | Meals included in rent |  |  |
| VAL | RNTM | C | 1 | b | b | N/A (GQ/vacant units, except 'for rent' and 'rented, not occupied'/owned or being bought/occupied without rent payment) |
| VAL | RNTM | C | 1 | 1 | 1 | Yes |
| VAL | RNTM | C | 1 | 2 | 2 | No |
| NAME | RNTP | N | 5 | Monthly rent (use ADJHSG to adjust RNTP to constant dollars) |  |  |
| VAL | RNTP | N | 5 | bbbbb | bbbbb | N/A (GQ/vacant units, except 'for rent' and 'rented, not occupied'/owned or being bought/occupied without rent payment) |
| VAL | RNTP | N | 5 | 1 | 99999 | $1 to $99999 (Rounded and top-coded) |
| NAME | RWAT | C | 1 | Hot and cold running water |  |  |
| VAL | RWAT | C | 1 | b | b | N/A (GQ) |
| VAL | RWAT | C | 1 | 1 | 1 | Yes |
| VAL | RWAT | C | 1 | 2 | 2 | No |
| VAL | RWAT | C | 1 | 9 | 9 | Case is from Puerto Rico, RWAT not applicable |
| NAME | RWATPR | C | 1 | Running water |  |  |
| VAL | RWATPR | C | 1 | b | b | N/A (GQ) |
| VAL | RWATPR | C | 1 | 1 | 1 | Yes |
| VAL | RWATPR | C | 1 | 2 | 2 | No |
| VAL | RWATPR | C | 1 | 9 | 9 | Case is from the United States, RWATPR not applicable |
| NAME | SATELLITE | C | 1 | Satellite Internet service |  |  |
| VAL | SATELLITE | C | 1 | b | b | N/A (GQ/vacant/no paid access to the internet) |
| VAL | SATELLITE | C | 1 | 1 | 1 | Yes |
| VAL | SATELLITE | C | 1 | 2 | 2 | No |
| NAME | SINK | C | 1 | Sink with a faucet |  |  |
| VAL | SINK | C | 1 | b | b | N/A (GQ) |
| VAL | SINK | C | 1 | 1 | 1 | Yes |
| VAL | SINK | C | 1 | 2 | 2 | No |
| NAME | SMARTPHONE | C | 1 | Smartphone |  |  |
| VAL | SMARTPHONE | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | SMARTPHONE | C | 1 | 1 | 1 | Yes |
| VAL | SMARTPHONE | C | 1 | 2 | 2 | No |
| NAME | SMP | N | 5 | Total payment on all second and junior mortgages and home equity loans (monthly amount, use ADJHSG to adjust SMP to constant dollars) |  |  |
| VAL | SMP | N | 5 | bbbbb | bbbbb | N/A (GQ/vacant/not owned or being bought/ /no second or junior mortgages or home equity loans) |
| VAL | SMP | N | 5 | 1 | 99999 | $1 to $99999 (Rounded and top-coded) |
| NAME | STOV | C | 1 | Stove or range |  |  |
| VAL | STOV | C | 1 | b | b | N/A (GQ) |
| VAL | STOV | C | 1 | 1 | 1 | Yes |
| VAL | STOV | C | 1 | 2 | 2 | No |
| NAME | TABLET | C | 1 | Tablet or other portable wireless computer |  |  |
| VAL | TABLET | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | TABLET | C | 1 | 1 | 1 | Yes |
| VAL | TABLET | C | 1 | 2 | 2 | No |
| NAME | TEL | C | 1 | Telephone service |  |  |
| VAL | TEL | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | TEL | C | 1 | 1 | 1 | Yes |
| VAL | TEL | C | 1 | 2 | 2 | No |
| NAME | TEN | C | 1 | Tenure |  |  |
| VAL | TEN | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | TEN | C | 1 | 1 | 1 | Owned with mortgage or loan (include home equity loans) |
| VAL | TEN | C | 1 | 2 | 2 | Owned free and clear |
| VAL | TEN | C | 1 | 3 | 3 | Rented |
| VAL | TEN | C | 1 | 4 | 4 | Occupied without payment of rent |
| NAME | VACS | C | 1 | Vacancy status |  |  |
| VAL | VACS | C | 1 | b | b | N/A (GQ/occupied) |
| VAL | VACS | C | 1 | 1 | 1 | For rent |
| VAL | VACS | C | 1 | 2 | 2 | Rented, not occupied |
| VAL | VACS | C | 1 | 3 | 3 | For sale only |
| VAL | VACS | C | 1 | 4 | 4 | Sold, not occupied |
| VAL | VACS | C | 1 | 5 | 5 | For seasonal/recreational/occasional use |
| VAL | VACS | C | 1 | 6 | 6 | For migrant workers |
| VAL | VACS | C | 1 | 7 | 7 | Other vacant |
| NAME | VALP | N | 7 | Property value |  |  |
| VAL | VALP | N | 7 | bbbbbbb | bbbbbbb | N/A (GQ/vacant units, except 'for-sale-only' and 'sold, not occupied'/not owned or being bought) |
| VAL | VALP | N | 7 | 1 | 9999999 | $1 to $9999999 (Rounded and top-coded) |
| NAME | VEH | C | 1 | Vehicles (1 ton or less) available |  |  |
| VAL | VEH | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | VEH | C | 1 | 0 | 0 | No vehicles |
| VAL | VEH | C | 1 | 1 | 1 | 1 vehicle |
| VAL | VEH | C | 1 | 2 | 2 | 2 vehicles |
| VAL | VEH | C | 1 | 3 | 3 | 3 vehicles |
| VAL | VEH | C | 1 | 4 | 4 | 4 vehicles |
| VAL | VEH | C | 1 | 5 | 5 | 5 vehicles |
| VAL | VEH | C | 1 | 6 | 6 | 6 or more vehicles |
| NAME | WATFP | C | 1 | Water cost flag variable |  |  |
| VAL | WATFP | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | WATFP | C | 1 | 1 | 1 | Included in rent or in condo fee |
| VAL | WATFP | C | 1 | 2 | 2 | No charge |
| VAL | WATFP | C | 1 | 3 | 3 | Valid annual water cost in WATP |
| NAME | WATP | N | 4 | Water cost (yearly cost, use ADJHSG to adjust WATP to constant dollars) |  |  |
| VAL | WATP | N | 4 | bbbb | bbbb | N/A (GQ/vacant/included in rent or in condo fee/no charge) |
| VAL | WATP | N | 4 | 3 | 9999 | $3 to $9999 (Rounded and top-coded) |
| NAME | YBL | C | 2 | When structure first built |  |  |
| VAL | YBL | C | 2 | bb | bb | N/A (GQ) |
| VAL | YBL | C | 2 | 01 | 01 | 1939 or earlier |
| VAL | YBL | C | 2 | 02 | 02 | 1940 to 1949 |
| VAL | YBL | C | 2 | 03 | 03 | 1950 to 1959 |
| VAL | YBL | C | 2 | 04 | 04 | 1960 to 1969 |
| VAL | YBL | C | 2 | 05 | 05 | 1970 to 1979 |
| VAL | YBL | C | 2 | 06 | 06 | 1980 to 1989 |
| VAL | YBL | C | 2 | 07 | 07 | 1990 to 1999 |
| VAL | YBL | C | 2 | 08 | 08 | 2000 to 2004 |
| VAL | YBL | C | 2 | 09 | 09 | 2005 |
| VAL | YBL | C | 2 | 10 | 10 | 2006 |
| VAL | YBL | C | 2 | 11 | 11 | 2007 |
| VAL | YBL | C | 2 | 12 | 12 | 2008 |
| VAL | YBL | C | 2 | 13 | 13 | 2009 |
| VAL | YBL | C | 2 | 14 | 14 | 2010 |
| VAL | YBL | C | 2 | 15 | 15 | 2011 |
| VAL | YBL | C | 2 | 16 | 16 | 2012 |
| VAL | YBL | C | 2 | 17 | 17 | 2013 |
| VAL | YBL | C | 2 | 18 | 18 | 2014 |
| VAL | YBL | C | 2 | 19 | 19 | 2015 |
| VAL | YBL | C | 2 | 20 | 20 | 2016 |
| VAL | YBL | C | 2 | 21 | 21 | 2017 |
| VAL | YBL | C | 2 | 22 | 22 | 2018 |
| NAME | FES | C | 1 | Family type and employment status |  |  |
| VAL | FES | C | 1 | b | b | N/A (GQ/vacant/not a family/same-sex married-couple families) |
| VAL | FES | C | 1 | 1 | 1 | Married-couple family: Husband and wife in LF |
| VAL | FES | C | 1 | 2 | 2 | Married-couple family: Husband in labor force, wife not in LF |
| VAL | FES | C | 1 | 3 | 3 | Married-couple family: Husband not in LF, wife in LF |
| VAL | FES | C | 1 | 4 | 4 | Married-couple family: Neither husband nor wife in LF |
| VAL | FES | C | 1 | 5 | 5 | Other family: Male householder, no wife present, in LF |
| VAL | FES | C | 1 | 6 | 6 | Other family: Male householder, no wife present, not in LF |
| VAL | FES | C | 1 | 7 | 7 | Other family: Female householder, no husband present, in LF |
| VAL | FES | C | 1 | 8 | 8 | Other family: Female householder, no husband present, not in LF |
| NAME | FINCP | N | 7 | Family income (past 12 months, use ADJINC to adjust FINCP to constant dollars) |  |  |
| VAL | FINCP | N | 7 | bbbbbbb | bbbbbbb | N/A(GQ/vacant) |
| VAL | FINCP | N | 7 | 0 | 0 | No family income |
| VAL | FINCP | N | 7 | -59999 | -59999 | Loss of -$59,999 or more |
| VAL | FINCP | N | 7 | -59998 | -1 | Loss of $1 to -$59,998 |
| VAL | FINCP | N | 7 | 1 | 9999999 | Total family income in dollars (Components are rounded) |
| NAME | FPARC | C | 1 | Family presence and age of related children |  |  |
| VAL | FPARC | C | 1 | b | b | N/A (GQ/vacant/not a family) |
| VAL | FPARC | C | 1 | 1 | 1 | With related children under 5 years only |
| VAL | FPARC | C | 1 | 2 | 2 | With related children 5 to 17 years only |
| VAL | FPARC | C | 1 | 3 | 3 | With related children under 5 years and 5 to 17 years |
| VAL | FPARC | C | 1 | 4 | 4 | No related children |
| NAME | GRNTP | N | 4 | Gross rent (monthly amount, use ADJHSG to adjust GRNTP to constant dollars) |  |  |
| VAL | GRNTP | N | 4 | bbbb | bbbb | N/A (GQ/vacant/owned or being bought/occupied without rent payment) |
| VAL | GRNTP | N | 4 | 1 | 9999 | $1 - $9999 (Components are rounded) |
| NAME | GRPIP | N | 3 | Gross rent as a percentage of household income past 12 months |  |  |
| VAL | GRPIP | N | 3 | bbb | bbb | N/A (GQ/vacant/owned or being bought/occupied without rent payment/no household income) |
| VAL | GRPIP | N | 3 | 1 | 100 | 1% to 100% |
| VAL | GRPIP | N | 3 | 101 | 101 | 101% or more |
| NAME | HHL | C | 1 | Household language |  |  |
| VAL | HHL | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | HHL | C | 1 | 1 | 1 | English only |
| VAL | HHL | C | 1 | 2 | 2 | Spanish |
| VAL | HHL | C | 1 | 3 | 3 | Other Indo-European languages |
| VAL | HHL | C | 1 | 4 | 4 | Asian and Pacific Island languages |
| VAL | HHL | C | 1 | 5 | 5 | Other language |
| NAME | HHLANP | C | 4 | Detailed household language |  |  |
| VAL | HHLANP | C | 4 | bbbb | bbbb | N/A (GQ/vacant) |
| VAL | HHLANP | C | 4 | 1000 | 1000 | Jamaican Creole English |
| VAL | HHLANP | C | 4 | 1025 | 1025 | Other English-based Creole languages |
| VAL | HHLANP | C | 4 | 1055 | 1055 | Haitian |
| VAL | HHLANP | C | 4 | 1069 | 1069 | Kabuverdianu |
| VAL | HHLANP | C | 4 | 1110 | 1110 | German |
| VAL | HHLANP | C | 4 | 1120 | 1120 | Swiss German |
| VAL | HHLANP | C | 4 | 1125 | 1125 | Pennsylvania German |
| VAL | HHLANP | C | 4 | 1130 | 1130 | Yiddish |
| VAL | HHLANP | C | 4 | 1132 | 1132 | Dutch |
| VAL | HHLANP | C | 4 | 1134 | 1134 | Afrikaans |
| VAL | HHLANP | C | 4 | 1140 | 1140 | Swedish |
| VAL | HHLANP | C | 4 | 1141 | 1141 | Danish |
| VAL | HHLANP | C | 4 | 1142 | 1142 | Norwegian |
| VAL | HHLANP | C | 4 | 1155 | 1155 | Italian |
| VAL | HHLANP | C | 4 | 1170 | 1170 | French |
| VAL | HHLANP | C | 4 | 1175 | 1175 | Cajun French |
| VAL | HHLANP | C | 4 | 1200 | 1200 | Spanish |
| VAL | HHLANP | C | 4 | 1210 | 1210 | Portuguese |
| VAL | HHLANP | C | 4 | 1220 | 1220 | Romanian |
| VAL | HHLANP | C | 4 | 1231 | 1231 | Irish |
| VAL | HHLANP | C | 4 | 1235 | 1235 | Greek |
| VAL | HHLANP | C | 4 | 1242 | 1242 | Albanian |
| VAL | HHLANP | C | 4 | 1250 | 1250 | Russian |
| VAL | HHLANP | C | 4 | 1260 | 1260 | Ukrainian |
| VAL | HHLANP | C | 4 | 1262 | 1262 | Czech |
| VAL | HHLANP | C | 4 | 1263 | 1263 | Slovak |
| VAL | HHLANP | C | 4 | 1270 | 1270 | Polish |
| VAL | HHLANP | C | 4 | 1273 | 1273 | Bulgarian |
| VAL | HHLANP | C | 4 | 1274 | 1274 | Macedonian |
| VAL | HHLANP | C | 4 | 1275 | 1275 | Serbocroatian |
| VAL | HHLANP | C | 4 | 1276 | 1276 | Bosnian |
| VAL | HHLANP | C | 4 | 1277 | 1277 | Croatian |
| VAL | HHLANP | C | 4 | 1278 | 1278 | Serbian |
| VAL | HHLANP | C | 4 | 1281 | 1281 | Lithuanian |
| VAL | HHLANP | C | 4 | 1283 | 1283 | Latvian |
| VAL | HHLANP | C | 4 | 1288 | 1288 | Armenian |
| VAL | HHLANP | C | 4 | 1290 | 1290 | Farsi |
| VAL | HHLANP | C | 4 | 1292 | 1292 | Dari |
| VAL | HHLANP | C | 4 | 1315 | 1315 | Kurdish |
| VAL | HHLANP | C | 4 | 1327 | 1327 | Pashto |
| VAL | HHLANP | C | 4 | 1340 | 1340 | India N.E.C. |
| VAL | HHLANP | C | 4 | 1350 | 1350 | Hindi |
| VAL | HHLANP | C | 4 | 1360 | 1360 | Urdu |
| VAL | HHLANP | C | 4 | 1380 | 1380 | Bengali |
| VAL | HHLANP | C | 4 | 1420 | 1420 | Punjabi |
| VAL | HHLANP | C | 4 | 1435 | 1435 | Konkani |
| VAL | HHLANP | C | 4 | 1440 | 1440 | Marathi |
| VAL | HHLANP | C | 4 | 1450 | 1450 | Gujarati |
| VAL | HHLANP | C | 4 | 1500 | 1500 | Nepali |
| VAL | HHLANP | C | 4 | 1525 | 1525 | Pakistan N.E.C. |
| VAL | HHLANP | C | 4 | 1530 | 1530 | Sinhala |
| VAL | HHLANP | C | 4 | 1540 | 1540 | Other Indo-Iranian languages |
| VAL | HHLANP | C | 4 | 1564 | 1564 | Other Indo-European languages |
| VAL | HHLANP | C | 4 | 1565 | 1565 | Finnish |
| VAL | HHLANP | C | 4 | 1582 | 1582 | Hungarian |
| VAL | HHLANP | C | 4 | 1675 | 1675 | Turkish |
| VAL | HHLANP | C | 4 | 1690 | 1690 | Mongolian |
| VAL | HHLANP | C | 4 | 1730 | 1730 | Telugu |
| VAL | HHLANP | C | 4 | 1737 | 1737 | Kannada |
| VAL | HHLANP | C | 4 | 1750 | 1750 | Malayalam |
| VAL | HHLANP | C | 4 | 1765 | 1765 | Tamil |
| VAL | HHLANP | C | 4 | 1900 | 1900 | Khmer |
| VAL | HHLANP | C | 4 | 1960 | 1960 | Vietnamese |
| VAL | HHLANP | C | 4 | 1970 | 1970 | Chinese |
| VAL | HHLANP | C | 4 | 2000 | 2000 | Mandarin |
| VAL | HHLANP | C | 4 | 2030 | 2030 | Min Nan Chinese |
| VAL | HHLANP | C | 4 | 2050 | 2050 | Cantonese |
| VAL | HHLANP | C | 4 | 2100 | 2100 | Tibetan |
| VAL | HHLANP | C | 4 | 2160 | 2160 | Burmese |
| VAL | HHLANP | C | 4 | 2270 | 2270 | Chin languages |
| VAL | HHLANP | C | 4 | 2350 | 2350 | Karen languages |
| VAL | HHLANP | C | 4 | 2430 | 2430 | Thai |
| VAL | HHLANP | C | 4 | 2475 | 2475 | Lao |
| VAL | HHLANP | C | 4 | 2525 | 2525 | Iu Mien |
| VAL | HHLANP | C | 4 | 2535 | 2535 | Hmong |
| VAL | HHLANP | C | 4 | 2560 | 2560 | Japanese |
| VAL | HHLANP | C | 4 | 2575 | 2575 | Korean |
| VAL | HHLANP | C | 4 | 2715 | 2715 | Malay |
| VAL | HHLANP | C | 4 | 2770 | 2770 | Indonesian |
| VAL | HHLANP | C | 4 | 2850 | 2850 | Other languages of Asia |
| VAL | HHLANP | C | 4 | 2910 | 2910 | Filipino |
| VAL | HHLANP | C | 4 | 2920 | 2920 | Tagalog |
| VAL | HHLANP | C | 4 | 2950 | 2950 | Cebuano |
| VAL | HHLANP | C | 4 | 3150 | 3150 | Ilocano |
| VAL | HHLANP | C | 4 | 3190 | 3190 | Other Philippine languages |
| VAL | HHLANP | C | 4 | 3220 | 3220 | Chamorro |
| VAL | HHLANP | C | 4 | 3270 | 3270 | Marshallese |
| VAL | HHLANP | C | 4 | 3350 | 3350 | Chuukese |
| VAL | HHLANP | C | 4 | 3420 | 3420 | Samoan |
| VAL | HHLANP | C | 4 | 3500 | 3500 | Tongan |
| VAL | HHLANP | C | 4 | 3570 | 3570 | Hawaiian |
| VAL | HHLANP | C | 4 | 3600 | 3600 | Other Eastern Malayo-Polynesian languages |
| VAL | HHLANP | C | 4 | 4500 | 4500 | Arabic |
| VAL | HHLANP | C | 4 | 4545 | 4545 | Hebrew |
| VAL | HHLANP | C | 4 | 4560 | 4560 | Assyrian Neo-Aramaic |
| VAL | HHLANP | C | 4 | 4565 | 4565 | Chaldean Neo-Aramaic |
| VAL | HHLANP | C | 4 | 4590 | 4590 | Amharic |
| VAL | HHLANP | C | 4 | 4640 | 4640 | Tigrinya |
| VAL | HHLANP | C | 4 | 4830 | 4830 | Oromo |
| VAL | HHLANP | C | 4 | 4840 | 4840 | Somali |
| VAL | HHLANP | C | 4 | 4880 | 4880 | Other Afro-Asiatic languages |
| VAL | HHLANP | C | 4 | 4900 | 4900 | Nilo-Saharan languages |
| VAL | HHLANP | C | 4 | 5150 | 5150 | Swahili |
| VAL | HHLANP | C | 4 | 5345 | 5345 | Ganda |
| VAL | HHLANP | C | 4 | 5525 | 5525 | Shona |
| VAL | HHLANP | C | 4 | 5645 | 5645 | Other Bantu languages |
| VAL | HHLANP | C | 4 | 5845 | 5845 | Manding languages |
| VAL | HHLANP | C | 4 | 5900 | 5900 | Other Mande languages |
| VAL | HHLANP | C | 4 | 5940 | 5940 | Fulah |
| VAL | HHLANP | C | 4 | 5950 | 5950 | Wolof |
| VAL | HHLANP | C | 4 | 6120 | 6120 | Akan (incl. Twi) |
| VAL | HHLANP | C | 4 | 6205 | 6205 | Ga |
| VAL | HHLANP | C | 4 | 6230 | 6230 | Gbe languages |
| VAL | HHLANP | C | 4 | 6290 | 6290 | Yoruba |
| VAL | HHLANP | C | 4 | 6300 | 6300 | Edoid languages |
| VAL | HHLANP | C | 4 | 6370 | 6370 | Igbo |
| VAL | HHLANP | C | 4 | 6500 | 6500 | Other Niger-Congo languages |
| VAL | HHLANP | C | 4 | 6795 | 6795 | Other languages of Africa |
| VAL | HHLANP | C | 4 | 6800 | 6800 | Aleut languages |
| VAL | HHLANP | C | 4 | 6839 | 6839 | Ojibwa |
| VAL | HHLANP | C | 4 | 6930 | 6930 | Apache languages |
| VAL | HHLANP | C | 4 | 6933 | 6933 | Navajo |
| VAL | HHLANP | C | 4 | 7019 | 7019 | Dakota languages |
| VAL | HHLANP | C | 4 | 7032 | 7032 | Muskogean languages |
| VAL | HHLANP | C | 4 | 7039 | 7039 | Keres |
| VAL | HHLANP | C | 4 | 7050 | 7050 | Cherokee |
| VAL | HHLANP | C | 4 | 7060 | 7060 | Uto-Aztecan languages |
| VAL | HHLANP | C | 4 | 7124 | 7124 | Other Native North American languages |
| VAL | HHLANP | C | 4 | 7300 | 7300 | Other Central and South American languages |
| VAL | HHLANP | C | 4 | 9500 | 9500 | English only household |
| VAL | HHLANP | C | 4 | 9999 | 9999 | Other and unspecified languages |
| NAME | HHT | C | 1 | Household/family type |  |  |
| VAL | HHT | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | HHT | C | 1 | 1 | 1 | Married couple household |
| VAL | HHT | C | 1 | 2 | 2 | Other family household: Male householder, no spouse present |
| VAL | HHT | C | 1 | 3 | 3 | Other family household: Female householder, no spouse present |
| VAL | HHT | C | 1 | 4 | 4 | Nonfamily household: Male householder: Living alone |
| VAL | HHT | C | 1 | 5 | 5 | Nonfamily household: Male householder: Not living alone |
| VAL | HHT | C | 1 | 6 | 6 | Nonfamily household: Female householder: Living alone |
| VAL | HHT | C | 1 | 7 | 7 | Nonfamily household: Female householder: Not living alone |
| NAME | HINCP | N | 7 | Household income (past 12 months, use ADJINC to adjust HINCP to constant dollars) |  |  |
| VAL | HINCP | N | 7 | bbbbbbb | bbbbbbb | N/A(GQ/vacant) |
| VAL | HINCP | N | 7 | 0 | 0 | No household income |
| VAL | HINCP | N | 7 | -59999 | -59999 | Loss of -$59,999 or more |
| VAL | HINCP | N | 7 | -59998 | -1 | Loss of $1 to -$59,998 |
| VAL | HINCP | N | 7 | 1 | 9999999 | Total household income in dollars (Components are rounded) |
| NAME | HUGCL | C | 1 | Household with grandparent living with grandchildren |  |  |
| VAL | HUGCL | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | HUGCL | C | 1 | 0 | 0 | Household without grandparent living with grandchildren |
| VAL | HUGCL | C | 1 | 1 | 1 | Household with grandparent living with grandchildren |
| NAME | HUPAC | C | 1 | HH presence and age of children |  |  |
| VAL | HUPAC | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | HUPAC | C | 1 | 1 | 1 | With children under 6 years only |
| VAL | HUPAC | C | 1 | 2 | 2 | With children 6 to 17 years only |
| VAL | HUPAC | C | 1 | 3 | 3 | With children under 6 years and 6 to 17 years |
| VAL | HUPAC | C | 1 | 4 | 4 | No children |
| NAME | HUPAOC | C | 1 | HH presence and age of own children |  |  |
| VAL | HUPAOC | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | HUPAOC | C | 1 | 1 | 1 | Presence of own children under 6 years only |
| VAL | HUPAOC | C | 1 | 2 | 2 | Presence of own children 6 to 17 years only |
| VAL | HUPAOC | C | 1 | 3 | 3 | Presence of own children under 6 years and 6 to 17 years |
| VAL | HUPAOC | C | 1 | 4 | 4 | No own children present |
| NAME | HUPARC | C | 1 | HH presence and age of related children |  |  |
| VAL | HUPARC | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | HUPARC | C | 1 | 1 | 1 | Presence of related children under 6 years only |
| VAL | HUPARC | C | 1 | 2 | 2 | Presence of related children 6 to 17 years only |
| VAL | HUPARC | C | 1 | 3 | 3 | Presence of related children under 6 years and 6 to 17 years |
| VAL | HUPARC | C | 1 | 4 | 4 | No related children present |
| NAME | KIT | C | 1 | Complete kitchen facilities |  |  |
| VAL | KIT | C | 1 | b | b | N/A (GQ) |
| VAL | KIT | C | 1 | 1 | 1 | Yes, has stove or range, refrigerator, and sink with a faucet |
| VAL | KIT | C | 1 | 2 | 2 | No |
| NAME | LNGI | C | 1 | Limited English speaking household |  |  |
| VAL | LNGI | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | LNGI | C | 1 | 1 | 1 | At least one person in the household 14 and over speaks English only or speaks English 'very well' |
| VAL | LNGI | C | 1 | 2 | 2 | No one in the household 14 and over speaks English only or speaks English 'very well' |
| NAME | MULTG | C | 1 | Multigenerational household |  |  |
| VAL | MULTG | C | 1 | b | b | N/A (GQ/Vacant/NP=0) |
| VAL | MULTG | C | 1 | 1 | 1 | No, not a multigenerational household |
| VAL | MULTG | C | 1 | 2 | 2 | Yes, is a multigenerational household |
| NAME | MV | C | 1 | When moved into this house or apartment |  |  |
| VAL | MV | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | MV | C | 1 | 1 | 1 | 12 months or less |
| VAL | MV | C | 1 | 2 | 2 | 13 to 23 months |
| VAL | MV | C | 1 | 3 | 3 | 2 to 4 years |
| VAL | MV | C | 1 | 4 | 4 | 5 to 9 years |
| VAL | MV | C | 1 | 5 | 5 | 10 to 19 years |
| VAL | MV | C | 1 | 6 | 6 | 20 to 29 years |
| VAL | MV | C | 1 | 7 | 7 | 30 years or more |
| NAME | NOC | N | 2 | Number of own children in household (unweighted) |  |  |
| VAL | NOC | N | 2 | bb | bb | N/A(GQ/vacant) |
| VAL | NOC | N | 2 | 0 | 0 | No own children |
| VAL | NOC | N | 2 | 1 | 19 | Number of own children in household |
| NAME | NPF | N | 2 | Number of persons in family (unweighted) |  |  |
| VAL | NPF | N | 2 | bb | bb | N/A (GQ/vacant/non-family household) |
| VAL | NPF | N | 2 | 2 | 20 | Number of persons in family |
| NAME | NPP | C | 1 | Grandparent headed household with no parent present |  |  |
| VAL | NPP | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | NPP | C | 1 | 0 | 0 | Not a grandparent headed household with no parent present |
| VAL | NPP | C | 1 | 1 | 1 | Grandparent headed household with no parent present |
| NAME | NR | C | 1 | Presence of nonrelative in household |  |  |
| VAL | NR | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | NR | C | 1 | 0 | 0 | None |
| VAL | NR | C | 1 | 1 | 1 | 1 or more nonrelatives |
| NAME | NRC | N | 2 | Number of related children in household (unweighted) |  |  |
| VAL | NRC | N | 2 | bb | bb | N/A (GQ/vacant) |
| VAL | NRC | N | 2 | 0 | 0 | No related children |
| VAL | NRC | N | 2 | 1 | 19 | Number of related children in household |
| NAME | OCPIP | N | 3 | Selected monthly owner costs as a percentage of household income during the past 12 months |  |  |
| VAL | OCPIP | N | 3 | bbb | bbb | N/A (GQ/vacant/not owned or being bought/ no household income) |
| VAL | OCPIP | N | 3 | 1 | 100 | 1% to 100% |
| VAL | OCPIP | N | 3 | 101 | 101 | 101% or more |
| NAME | PARTNER | C | 1 | Unmarried partner household |  |  |
| VAL | PARTNER | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | PARTNER | C | 1 | 0 | 0 | No unmarried partner in household |
| VAL | PARTNER | C | 1 | 1 | 1 | Male householder, male partner |
| VAL | PARTNER | C | 1 | 2 | 2 | Male householder, female partner |
| VAL | PARTNER | C | 1 | 3 | 3 | Female householder, female partner |
| VAL | PARTNER | C | 1 | 4 | 4 | Female householder, male partner |
| NAME | PLM | C | 1 | Complete plumbing facilities |  |  |
| VAL | PLM | C | 1 | b | b | N/A (GQ) |
| VAL | PLM | C | 1 | 1 | 1 | Yes, has hot and cold running water, and a bathtub or shower |
| VAL | PLM | C | 1 | 2 | 2 | No |
| VAL | PLM | C | 1 | 9 | 9 | Case is from Puerto Rico, PLM recode not applicable |
| NAME | PLMPRP | C | 1 | Complete plumbing facilities for Puerto Rico |  |  |
| VAL | PLMPRP | C | 1 | b | b | N/A (GQ) |
| VAL | PLMPRP | C | 1 | 1 | 1 | Yes, has running water, and a bathtub or shower |
| VAL | PLMPRP | C | 1 | 2 | 2 | No |
| VAL | PLMPRP | C | 1 | 9 | 9 | Case is from the United States, PLMPRP not applicable |
| NAME | PSF | C | 1 | Presence of subfamilies in household |  |  |
| VAL | PSF | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | PSF | C | 1 | 0 | 0 | No subfamilies |
| VAL | PSF | C | 1 | 1 | 1 | 1 or more subfamilies |
| NAME | R18 | C | 1 | Presence of persons under 18 years in household (unweighted) |  |  |
| VAL | R18 | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | R18 | C | 1 | 0 | 0 | No person under 18 in household |
| VAL | R18 | C | 1 | 1 | 1 | 1 or more persons under 18 in household |
| NAME | R60 | C | 1 | Presence of persons 60 years and over in household (unweighted) |  |  |
| VAL | R60 | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | R60 | C | 1 | 0 | 0 | No person 60 and over |
| VAL | R60 | C | 1 | 1 | 1 | 1 person 60 and over |
| VAL | R60 | C | 1 | 2 | 2 | 2 or more persons 60 and over |
| NAME | R65 | C | 1 | Presence of persons 65 years and over in household (unweighted) |  |  |
| VAL | R65 | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | R65 | C | 1 | 0 | 0 | No person 65 and over |
| VAL | R65 | C | 1 | 1 | 1 | 1 person 65 and over |
| VAL | R65 | C | 1 | 2 | 2 | 2 or more persons 65 and over |
| NAME | RESMODE | C | 1 | Response mode |  |  |
| VAL | RESMODE | C | 1 | b | b | N/A (GQ) |
| VAL | RESMODE | C | 1 | 1 | 1 | Mail |
| VAL | RESMODE | C | 1 | 2 | 2 | CATI/CAPI |
| VAL | RESMODE | C | 1 | 3 | 3 | Internet |
| NAME | SMOCP | N | 5 | Selected monthly owner costs (use ADJHSG to adjust SMOCP to constant dollars) |  |  |
| VAL | SMOCP | N | 5 | bbbbb | bbbbb | N/A (GQ/vacant/not owned or being bought) |
| VAL | SMOCP | N | 5 | 0 | 0 | None |
| VAL | SMOCP | N | 5 | 1 | 99999 | $1 - $99999 (Components are rounded) |
| NAME | SMX | C | 1 | Second or junior mortgage or home equity loan status |  |  |
| VAL | SMX | C | 1 | b | b | N/A (GQ/vacant/not owned or being bought) |
| VAL | SMX | C | 1 | 1 | 1 | Yes, a second mortgage |
| VAL | SMX | C | 1 | 2 | 2 | Yes, a home equity loan |
| VAL | SMX | C | 1 | 3 | 3 | No |
| VAL | SMX | C | 1 | 4 | 4 | Both a second mortgage and a home equity loan |
| NAME | SRNT | C | 1 | Specified rental unit |  |  |
| VAL | SRNT | C | 1 | b | b | N/A (GQ/vacant units, except 'for-rent-only' and 'rented, not occupied'/owned or being bought) |
| VAL | SRNT | C | 1 | 0 | 0 | A single-family home on 10 or more acres. |
| VAL | SRNT | C | 1 | 1 | 1 | A single-family home on less than 10 acres or any other type of building, including mobile homes, with no regard to acreage. |
| NAME | SSMC | C | 1 | Same-sex married couple households |  |  |
| VAL | SSMC | C | 1 | b | b | N/A (GQ/vacant) |
| VAL | SSMC | C | 1 | 0 | 0 | Households without a same-sex married couple |
| VAL | SSMC | C | 1 | 1 | 1 | Same-sex married-couple household where not all relevant data shown as reported |
| VAL | SSMC | C | 1 | 2 | 2 | All other same-sex married-couple households |
| NAME | SVAL | C | 1 | Specified owner unit |  |  |
| VAL | SVAL | C | 1 | b | b | N/A (GQ/ vacant units, except 'for-sale-only' and 'sold, not occupied'/not owned or being bought) |
| VAL | SVAL | C | 1 | 0 | 0 | A single family home on 10 or more acres or any other type of building, including mobile homes, with no regard to acreage. |
| VAL | SVAL | C | 1 | 1 | 1 | A single family home on less than 10 acres. |
| NAME | TAXAMT | N | 5 | Property taxes (yearly real estate taxes) |  |  |
| VAL | TAXAMT | N | 5 | bbbbb | bbbbb | N/A (GQ/vacant/not owned or being bought) |
| VAL | TAXAMT | N | 5 | 0 | 22500 | $0 to $22500 (rounded and top-coded) |
| NAME | WIF | C | 1 | Workers in family during the past 12 months |  |  |
| VAL | WIF | C | 1 | b | b | N/A (GQ/vacant/non-family household) |
| VAL | WIF | C | 1 | 0 | 0 | No workers |
| VAL | WIF | C | 1 | 1 | 1 | 1 worker |
| VAL | WIF | C | 1 | 2 | 2 | 2 workers |
| VAL | WIF | C | 1 | 3 | 3 | 3 or more workers in family |
| NAME | WKEXREL | C | 2 | Work experience of householder and spouse |  |  |
| VAL | WKEXREL | C | 2 | bb | bb | N/A (GQ/vacant/not a family) |
| VAL | WKEXREL | C | 2 | 01 | 01 | Householder and spouse worked FT |
| VAL | WKEXREL | C | 2 | 02 | 02 | Householder worked FT; spouse worked < FT |
| VAL | WKEXREL | C | 2 | 03 | 03 | Householder worked FT; spouse did not work |
| VAL | WKEXREL | C | 2 | 04 | 04 | Householder worked < FT; spouse worked FT |
| VAL | WKEXREL | C | 2 | 05 | 05 | Householder worked < FT; spouse worked < FT |
| VAL | WKEXREL | C | 2 | 06 | 06 | Householder worked < FT; spouse did not work |
| VAL | WKEXREL | C | 2 | 07 | 07 | Householder did not work; spouse worked FT |
| VAL | WKEXREL | C | 2 | 08 | 08 | Householder did not work; spouse worked < FT |
| VAL | WKEXREL | C | 2 | 09 | 09 | Householder did not work; spouse did not work |
| VAL | WKEXREL | C | 2 | 10 | 10 | Male householder worked FT; no spouse present |
| VAL | WKEXREL | C | 2 | 11 | 11 | Male householder worked < FT; no spouse present |
| VAL | WKEXREL | C | 2 | 12 | 12 | Male householder did not work; no spouse present |
| VAL | WKEXREL | C | 2 | 13 | 13 | Female householder worked FT; no spouse present |
| VAL | WKEXREL | C | 2 | 14 | 14 | Female householder worked < FT; no spouse present |
| VAL | WKEXREL | C | 2 | 15 | 15 | Female householder did not work; no spouse present |
| NAME | WORKSTAT | C | 2 | Work status of householder or spouse in family households |  |  |
| VAL | WORKSTAT | C | 2 | bb | bb | N/A (GQ/not a family household/same-sex married-couple families) |
| VAL | WORKSTAT | C | 2 | 01 | 01 | Husband and wife both in labor force, both employed or in Armed Forces |
| VAL | WORKSTAT | C | 2 | 02 | 02 | Husband and wife both in labor force, husband employed or in Armed Forces, wife unemployed |
| VAL | WORKSTAT | C | 2 | 03 | 03 | Husband in labor force and wife not in labor force, husband employed or in Armed Forces |
| VAL | WORKSTAT | C | 2 | 04 | 04 | Husband and wife both in labor force, husband unemployed, wife employed or in Armed Forces |
| VAL | WORKSTAT | C | 2 | 05 | 05 | Husband and wife both in labor force, husband unemployed, wife unemployed |
| VAL | WORKSTAT | C | 2 | 06 | 06 | Husband in labor force, husband unemployed, wife not in labor force |
| VAL | WORKSTAT | C | 2 | 07 | 07 | Husband not in labor force, wife in labor force, wife employed or in Armed Forces |
| VAL | WORKSTAT | C | 2 | 08 | 08 | Husband not in labor force, wife in labor force, wife unemployed |
| VAL | WORKSTAT | C | 2 | 09 | 09 | Neither husband nor wife in labor force |
| VAL | WORKSTAT | C | 2 | 10 | 10 | Male householder with no wife present, householder in labor force, employed or in Armed Forces |
| VAL | WORKSTAT | C | 2 | 11 | 11 | Male householder with no wife present, householder in labor force and unemployed |
| VAL | WORKSTAT | C | 2 | 12 | 12 | Male householder with no wife present, householder not in labor force |
| VAL | WORKSTAT | C | 2 | 13 | 13 | Female householder with no husband present, householder in labor force, employed or in Armed Forces |
| VAL | WORKSTAT | C | 2 | 14 | 14 | Female householder with no husband present, householder in labor force and unemployed |
| VAL | WORKSTAT | C | 2 | 15 | 15 | Female householder with no husband present, householder not in labor force |
| NAME | FACCESSP | C | 1 | Access to the Internet allocation flag |  |  |
| VAL | FACCESSP | C | 1 | b | b | N/A (GQ) |
| VAL | FACCESSP | C | 1 | 0 | 0 | No |
| VAL | FACCESSP | C | 1 | 1 | 1 | Yes |
| NAME | FACRP | C | 1 | Lot size allocation flag |  |  |
| VAL | FACRP | C | 1 | b | b | N/A (GQ) |
| VAL | FACRP | C | 1 | 0 | 0 | No |
| VAL | FACRP | C | 1 | 1 | 1 | Yes |
| NAME | FAGSP | C | 1 | Sales of Agricultural Products allocation flag |  |  |
| VAL | FAGSP | C | 1 | b | b | N/A (GQ) |
| VAL | FAGSP | C | 1 | 0 | 0 | No |
| VAL | FAGSP | C | 1 | 1 | 1 | Yes |
| NAME | FBATHP | C | 1 | Bathtub or shower allocation flag |  |  |
| VAL | FBATHP | C | 1 | b | b | N/A (GQ) |
| VAL | FBATHP | C | 1 | 0 | 0 | No |
| VAL | FBATHP | C | 1 | 1 | 1 | Yes |
| NAME | FBDSP | C | 1 | Number of bedrooms allocation flag |  |  |
| VAL | FBDSP | C | 1 | b | b | N/A (GQ) |
| VAL | FBDSP | C | 1 | 0 | 0 | No |
| VAL | FBDSP | C | 1 | 1 | 1 | Yes |
| NAME | FBLDP | C | 1 | Units in structure allocation flag |  |  |
| VAL | FBLDP | C | 1 | b | b | N/A (GQ) |
| VAL | FBLDP | C | 1 | 0 | 0 | No |
| VAL | FBLDP | C | 1 | 1 | 1 | Yes |
| NAME | FBROADBNDP | C | 1 | Cellular data plan for a smartphone or other mobile device allocation flag |  |  |
| VAL | FBROADBNDP | C | 1 | b | b | N/A (GQ) |
| VAL | FBROADBNDP | C | 1 | 0 | 0 | No |
| VAL | FBROADBNDP | C | 1 | 1 | 1 | Yes |
| NAME | FCOMPOTHXP | C | 1 | Other computer equipment allocation flag |  |  |
| VAL | FCOMPOTHXP | C | 1 | b | b | N/A (GQ) |
| VAL | FCOMPOTHXP | C | 1 | 0 | 0 | No |
| VAL | FCOMPOTHXP | C | 1 | 1 | 1 | Yes |
| NAME | FCONP | C | 1 | Condominium fee allocation flag |  |  |
| VAL | FCONP | C | 1 | b | b | N/A (GQ) |
| VAL | FCONP | C | 1 | 0 | 0 | No |
| VAL | FCONP | C | 1 | 1 | 1 | Yes |
| NAME | FDIALUPP | C | 1 | Dial-up service allocation flag |  |  |
| VAL | FDIALUPP | C | 1 | b | b | N/A (GQ) |
| VAL | FDIALUPP | C | 1 | 0 | 0 | No |
| VAL | FDIALUPP | C | 1 | 1 | 1 | Yes |
| NAME | FELEP | C | 1 | Electricity (monthly cost) allocation flag |  |  |
| VAL | FELEP | C | 1 | b | b | N/A (GQ) |
| VAL | FELEP | C | 1 | 0 | 0 | No |
| VAL | FELEP | C | 1 | 1 | 1 | Yes |
| NAME | FFINCP | C | 1 | Family income (past 12 months) allocation flag |  |  |
| VAL | FFINCP | C | 1 | b | b | N/A (GQ) |
| VAL | FFINCP | C | 1 | 0 | 0 | No |
| VAL | FFINCP | C | 1 | 1 | 1 | Yes |
| NAME | FFSP | C | 1 | Yearly food stamp/Supplemental Nutrition Assistance Program (SNAP) recipiency allocation flag |  |  |
| VAL | FFSP | C | 1 | 0 | 0 | No |
| VAL | FFSP | C | 1 | 1 | 1 | Yes |
| NAME | FFULP | C | 1 | Fuel cost (yearly cost for fuels other than gas and electricity) allocation flag |  |  |
| VAL | FFULP | C | 1 | b | b | N/A (GQ) |
| VAL | FFULP | C | 1 | 0 | 0 | No |
| VAL | FFULP | C | 1 | 1 | 1 | Yes |
| NAME | FGASP | C | 1 | Gas (monthly cost) allocation flag |  |  |
| VAL | FGASP | C | 1 | b | b | N/A (GQ) |
| VAL | FGASP | C | 1 | 0 | 0 | No |
| VAL | FGASP | C | 1 | 1 | 1 | Yes |
| NAME | FGRNTP | C | 1 | Gross rent (monthly amount) allocation flag |  |  |
| VAL | FGRNTP | C | 1 | b | b | N/A (GQ) |
| VAL | FGRNTP | C | 1 | 0 | 0 | No |
| VAL | FGRNTP | C | 1 | 1 | 1 | Yes |
| NAME | FHFLP | C | 1 | House heating fuel allocation flag |  |  |
| VAL | FHFLP | C | 1 | b | b | N/A (GQ) |
| VAL | FHFLP | C | 1 | 0 | 0 | No |
| VAL | FHFLP | C | 1 | 1 | 1 | Yes |
| NAME | FHINCP | C | 1 | Household income (past 12 months) allocation flag |  |  |
| VAL | FHINCP | C | 1 | b | b | N/A (GQ) |
| VAL | FHINCP | C | 1 | 0 | 0 | No |
| VAL | FHINCP | C | 1 | 1 | 1 | Yes |
| NAME | FHISPEEDP | C | 1 | Broadband (high speed) Internet service such as cable, fiber optic, or DSL service allocation flag |  |  |
| VAL | FHISPEEDP | C | 1 | b | b | N/A (GQ) |
| VAL | FHISPEEDP | C | 1 | 0 | 0 | No |
| VAL | FHISPEEDP | C | 1 | 1 | 1 | Yes |
| NAME | FHOTWATP | C | 1 | Water heater allocation flag (Puerto Rico only) |  |  |
| VAL | FHOTWATP | C | 1 | b | b | N/A (GQ) |
| VAL | FHOTWATP | C | 1 | 0 | 0 | No |
| VAL | FHOTWATP | C | 1 | 1 | 1 | Yes |
| NAME | FINSP | C | 1 | Fire, hazard, flood insurance (yearly amount) allocation flag |  |  |
| VAL | FINSP | C | 1 | b | b | N/A (GQ) |
| VAL | FINSP | C | 1 | 0 | 0 | No |
| VAL | FINSP | C | 1 | 1 | 1 | Yes |
| NAME | FKITP | C | 1 | Complete kitchen facilities allocation flag |  |  |
| VAL | FKITP | C | 1 | b | b | N/A (GQ) |
| VAL | FKITP | C | 1 | 0 | 0 | No |
| VAL | FKITP | C | 1 | 1 | 1 | Yes |
| NAME | FLAPTOPP | C | 1 | Laptop or desktop allocation flag |  |  |
| VAL | FLAPTOPP | C | 1 | b | b | N/A (GQ) |
| VAL | FLAPTOPP | C | 1 | 0 | 0 | No |
| VAL | FLAPTOPP | C | 1 | 1 | 1 | Yes |
| NAME | FMHP | C | 1 | Mobile home costs (yearly amount) allocation flag |  |  |
| VAL | FMHP | C | 1 | b | b | N/A (GQ) |
| VAL | FMHP | C | 1 | 0 | 0 | No |
| VAL | FMHP | C | 1 | 1 | 1 | Yes |
| NAME | FMRGIP | C | 1 | First mortgage payment includes fire, hazard, flood insurance allocation flag |  |  |
| VAL | FMRGIP | C | 1 | b | b | N/A (GQ) |
| VAL | FMRGIP | C | 1 | 0 | 0 | No |
| VAL | FMRGIP | C | 1 | 1 | 1 | Yes |
| NAME | FMRGP | C | 1 | First mortgage payment (monthly amount) allocation flag |  |  |
| VAL | FMRGP | C | 1 | b | b | N/A (GQ) |
| VAL | FMRGP | C | 1 | 0 | 0 | No |
| VAL | FMRGP | C | 1 | 1 | 1 | Yes |
| NAME | FMRGTP | C | 1 | First mortgage payment includes real estate taxes allocation flag |  |  |
| VAL | FMRGTP | C | 1 | b | b | N/A (GQ) |
| VAL | FMRGTP | C | 1 | 0 | 0 | No |
| VAL | FMRGTP | C | 1 | 1 | 1 | Yes |
| NAME | FMRGXP | C | 1 | First mortgage status allocation flag |  |  |
| VAL | FMRGXP | C | 1 | b | b | N/A (GQ) |
| VAL | FMRGXP | C | 1 | 0 | 0 | No |
| VAL | FMRGXP | C | 1 | 1 | 1 | Yes |
| NAME | FMVP | C | 1 | When moved into this house or apartment allocation flag |  |  |
| VAL | FMVP | C | 1 | b | b | N/A (GQ) |
| VAL | FMVP | C | 1 | 0 | 0 | No |
| VAL | FMVP | C | 1 | 1 | 1 | Yes |
| NAME | FOTHSVCEXP | C | 1 | Other Internet service allocation flag |  |  |
| VAL | FOTHSVCEXP | C | 1 | b | b | N/A (GQ) |
| VAL | FOTHSVCEXP | C | 1 | 0 | 0 | No |
| VAL | FOTHSVCEXP | C | 1 | 1 | 1 | Yes |
| NAME | FPLMP | C | 1 | Complete plumbing facilities allocation flag |  |  |
| VAL | FPLMP | C | 1 | b | b | N/A (GQ) |
| VAL | FPLMP | C | 1 | 0 | 0 | No |
| VAL | FPLMP | C | 1 | 1 | 1 | Yes |
| NAME | FPLMPRP | C | 1 | Complete plumbing facilities allocation flag for Puerto Rico |  |  |
| VAL | FPLMPRP | C | 1 | b | b | N/A (GQ) |
| VAL | FPLMPRP | C | 1 | 0 | 0 | No |
| VAL | FPLMPRP | C | 1 | 1 | 1 | Yes |
| NAME | FREFRP | C | 1 | Refrigerator allocation flag |  |  |
| VAL | FREFRP | C | 1 | b | b | N/A (GQ) |
| VAL | FREFRP | C | 1 | 0 | 0 | No |
| VAL | FREFRP | C | 1 | 1 | 1 | Yes |
| NAME | FRMSP | C | 1 | Number of rooms allocation flag |  |  |
| VAL | FRMSP | C | 1 | b | b | N/A (GQ) |
| VAL | FRMSP | C | 1 | 0 | 0 | No |
| VAL | FRMSP | C | 1 | 1 | 1 | Yes |
| NAME | FRNTMP | C | 1 | Meals included in rent allocation flag |  |  |
| VAL | FRNTMP | C | 1 | b | b | N/A (GQ) |
| VAL | FRNTMP | C | 1 | 0 | 0 | No |
| VAL | FRNTMP | C | 1 | 1 | 1 | Yes |
| NAME | FRNTP | C | 1 | Monthly rent allocation flag |  |  |
| VAL | FRNTP | C | 1 | b | b | N/A (GQ) |
| VAL | FRNTP | C | 1 | 0 | 0 | No |
| VAL | FRNTP | C | 1 | 1 | 1 | Yes |
| NAME | FRWATP | C | 1 | Hot and cold running water allocation flag |  |  |
| VAL | FRWATP | C | 1 | b | b | N/A (GQ) |
| VAL | FRWATP | C | 1 | 0 | 0 | No |
| VAL | FRWATP | C | 1 | 1 | 1 | Yes |
| NAME | FRWATPRP | C | 1 | Running water allocation flag for Puerto Rico |  |  |
| VAL | FRWATPRP | C | 1 | b | b | N/A (GQ) |
| VAL | FRWATPRP | C | 1 | 0 | 0 | No |
| VAL | FRWATPRP | C | 1 | 1 | 1 | Yes |
| NAME | FSATELLITEP | C | 1 | Satellite Internet service allocation flag |  |  |
| VAL | FSATELLITEP | C | 1 | b | b | N/A (GQ) |
| VAL | FSATELLITEP | C | 1 | 0 | 0 | No |
| VAL | FSATELLITEP | C | 1 | 1 | 1 | Yes |
| NAME | FSINKP | C | 1 | Sink with a faucet allocation flag |  |  |
| VAL | FSINKP | C | 1 | b | b | N/A (GQ) |
| VAL | FSINKP | C | 1 | 0 | 0 | No |
| VAL | FSINKP | C | 1 | 1 | 1 | Yes |
| NAME | FSMARTPHONP | C | 1 | Smartphone allocation flag |  |  |
| VAL | FSMARTPHONP | C | 1 | b | b | N/A (GQ) |
| VAL | FSMARTPHONP | C | 1 | 0 | 0 | No |
| VAL | FSMARTPHONP | C | 1 | 1 | 1 | Yes |
| NAME | FSMOCP | C | 1 | Selected monthly owner cost allocation flag |  |  |
| VAL | FSMOCP | C | 1 | b | b | N/A (GQ) |
| VAL | FSMOCP | C | 1 | 0 | 0 | No |
| VAL | FSMOCP | C | 1 | 1 | 1 | Yes |
| NAME | FSMP | C | 1 | Total payment on second and junior mortgages and home equity loans (monthly amount) allocation flag |  |  |
| VAL | FSMP | C | 1 | b | b | N/A (GQ) |
| VAL | FSMP | C | 1 | 0 | 0 | No |
| VAL | FSMP | C | 1 | 1 | 1 | Yes |
| NAME | FSMXHP | C | 1 | Home equity loan status allocation flag |  |  |
| VAL | FSMXHP | C | 1 | b | b | N/A (GQ) |
| VAL | FSMXHP | C | 1 | 0 | 0 | No |
| VAL | FSMXHP | C | 1 | 1 | 1 | Yes |
| NAME | FSMXSP | C | 1 | Second mortgage status allocation flag |  |  |
| VAL | FSMXSP | C | 1 | b | b | N/A (GQ) |
| VAL | FSMXSP | C | 1 | 0 | 0 | No |
| VAL | FSMXSP | C | 1 | 1 | 1 | Yes |
| NAME | FSTOVP | C | 1 | Stove or range allocation flag |  |  |
| VAL | FSTOVP | C | 1 | b | b | N/A (GQ) |
| VAL | FSTOVP | C | 1 | 0 | 0 | No |
| VAL | FSTOVP | C | 1 | 1 | 1 | Yes |
| NAME | FTABLETP | C | 1 | Tablet or other portable wireless computer allocation flag |  |  |
| VAL | FTABLETP | C | 1 | b | b | N/A (GQ) |
| VAL | FTABLETP | C | 1 | 0 | 0 | No |
| VAL | FTABLETP | C | 1 | 1 | 1 | Yes |
| NAME | FTAXP | C | 1 | Property taxes (yearly amount) allocation flag |  |  |
| VAL | FTAXP | C | 1 | b | b | N/A (GQ) |
| VAL | FTAXP | C | 1 | 0 | 0 | No |
| VAL | FTAXP | C | 1 | 1 | 1 | Yes |
| NAME | FTELP | C | 1 | Telephone service allocation flag |  |  |
| VAL | FTELP | C | 1 | b | b | N/A (GQ) |
| VAL | FTELP | C | 1 | 0 | 0 | No |
| VAL | FTELP | C | 1 | 1 | 1 | Yes |
| NAME | FTENP | C | 1 | Tenure allocation flag |  |  |
| VAL | FTENP | C | 1 | b | b | N/A (GQ) |
| VAL | FTENP | C | 1 | 0 | 0 | No |
| VAL | FTENP | C | 1 | 1 | 1 | Yes |
| NAME | FVACSP | C | 1 | Vacancy status allocation flag |  |  |
| VAL | FVACSP | C | 1 | b | b | N/A (GQ) |
| VAL | FVACSP | C | 1 | 0 | 0 | No |
| VAL | FVACSP | C | 1 | 1 | 1 | Yes |
| NAME | FVALP | C | 1 | Property value allocation flag |  |  |
| VAL | FVALP | C | 1 | b | b | N/A (GQ) |
| VAL | FVALP | C | 1 | 0 | 0 | No |
| VAL | FVALP | C | 1 | 1 | 1 | Yes |
| NAME | FVEHP | C | 1 | Vehicles available allocation flag |  |  |
| VAL | FVEHP | C | 1 | b | b | N/A (GQ) |
| VAL | FVEHP | C | 1 | 0 | 0 | No |
| VAL | FVEHP | C | 1 | 1 | 1 | Yes |
| NAME | FWATP | C | 1 | Water (yearly cost) allocation flag |  |  |
| VAL | FWATP | C | 1 | b | b | N/A (GQ) |
| VAL | FWATP | C | 1 | 0 | 0 | No |
| VAL | FWATP | C | 1 | 1 | 1 | Yes |
| NAME | FYBLP | C | 1 | When structure first built allocation flag |  |  |
| VAL | FYBLP | C | 1 | b | b | N/A (GQ) |
| VAL | FYBLP | C | 1 | 0 | 0 | No |
| VAL | FYBLP | C | 1 | 1 | 1 | Yes |
| NAME | WGTP1 | N | 5 | Housing Weight replicate 1 |  |  |
| VAL | WGTP1 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP2 | N | 5 | Housing Weight replicate 2 |  |  |
| VAL | WGTP2 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP3 | N | 5 | Housing Weight replicate 3 |  |  |
| VAL | WGTP3 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP4 | N | 5 | Housing Weight replicate 4 |  |  |
| VAL | WGTP4 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP5 | N | 5 | Housing Weight replicate 5 |  |  |
| VAL | WGTP5 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP6 | N | 5 | Housing Weight replicate 6 |  |  |
| VAL | WGTP6 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP7 | N | 5 | Housing Weight replicate 7 |  |  |
| VAL | WGTP7 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP8 | N | 5 | Housing Weight replicate 8 |  |  |
| VAL | WGTP8 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP9 | N | 5 | Housing Weight replicate 9 |  |  |
| VAL | WGTP9 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP10 | N | 5 | Housing Weight replicate 10 |  |  |
| VAL | WGTP10 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP11 | N | 5 | Housing Weight replicate 11 |  |  |
| VAL | WGTP11 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP12 | N | 5 | Housing Weight replicate 12 |  |  |
| VAL | WGTP12 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP13 | N | 5 | Housing Weight replicate 13 |  |  |
| VAL | WGTP13 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP14 | N | 5 | Housing Weight replicate 14 |  |  |
| VAL | WGTP14 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP15 | N | 5 | Housing Weight replicate 15 |  |  |
| VAL | WGTP15 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP16 | N | 5 | Housing Weight replicate 16 |  |  |
| VAL | WGTP16 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP17 | N | 5 | Housing Weight replicate 17 |  |  |
| VAL | WGTP17 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP18 | N | 5 | Housing Weight replicate 18 |  |  |
| VAL | WGTP18 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP19 | N | 5 | Housing Weight replicate 19 |  |  |
| VAL | WGTP19 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP20 | N | 5 | Housing Weight replicate 20 |  |  |
| VAL | WGTP20 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP21 | N | 5 | Housing Weight replicate 21 |  |  |
| VAL | WGTP21 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP22 | N | 5 | Housing Weight replicate 22 |  |  |
| VAL | WGTP22 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP23 | N | 5 | Housing Weight replicate 23 |  |  |
| VAL | WGTP23 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP24 | N | 5 | Housing Weight replicate 24 |  |  |
| VAL | WGTP24 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP25 | N | 5 | Housing Weight replicate 25 |  |  |
| VAL | WGTP25 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP26 | N | 5 | Housing Weight replicate 26 |  |  |
| VAL | WGTP26 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP27 | N | 5 | Housing Weight replicate 27 |  |  |
| VAL | WGTP27 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP28 | N | 5 | Housing Weight replicate 28 |  |  |
| VAL | WGTP28 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP29 | N | 5 | Housing Weight replicate 29 |  |  |
| VAL | WGTP29 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP30 | N | 5 | Housing Weight replicate 30 |  |  |
| VAL | WGTP30 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP31 | N | 5 | Housing Weight replicate 31 |  |  |
| VAL | WGTP31 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP32 | N | 5 | Housing Weight replicate 32 |  |  |
| VAL | WGTP32 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP33 | N | 5 | Housing Weight replicate 33 |  |  |
| VAL | WGTP33 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP34 | N | 5 | Housing Weight replicate 34 |  |  |
| VAL | WGTP34 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP35 | N | 5 | Housing Weight replicate 35 |  |  |
| VAL | WGTP35 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP36 | N | 5 | Housing Weight replicate 36 |  |  |
| VAL | WGTP36 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP37 | N | 5 | Housing Weight replicate 37 |  |  |
| VAL | WGTP37 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP38 | N | 5 | Housing Weight replicate 38 |  |  |
| VAL | WGTP38 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP39 | N | 5 | Housing Weight replicate 39 |  |  |
| VAL | WGTP39 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP40 | N | 5 | Housing Weight replicate 40 |  |  |
| VAL | WGTP40 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP41 | N | 5 | Housing Weight replicate 41 |  |  |
| VAL | WGTP41 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP42 | N | 5 | Housing Weight replicate 42 |  |  |
| VAL | WGTP42 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP43 | N | 5 | Housing Weight replicate 43 |  |  |
| VAL | WGTP43 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP44 | N | 5 | Housing Weight replicate 44 |  |  |
| VAL | WGTP44 | N | 5 | -9999 | 9999 | Integer weight of housing unit |
| NAME | WGTP45 | N | 5 | Housing Weight replicate 45 |  |  |
| VAL | WGTP45 | N | 5 | -9999 | 9999 | Integer weight of housing unit |