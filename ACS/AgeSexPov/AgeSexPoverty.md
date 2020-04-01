# American Community Survey (ACS) Population by Age by Sex by Poverty Level 

- The SQL table **[acs].[AgeSexPov]** contains population data by Age by Sex by Poverty Level at the county level. It is created based on ACS B17001 table.  

- The SQL table **[acsLookup].[AgeSexPov]** is the lookup table of the [acs].[AgeSexPov] table. The description of each column names is also available in the "Variable Descriptions" section of this document. 

- The SQL table **[acs].[AgeSexPov]** includes data in years 2012 - 2017. Each year's data were downloaded form [U.S. Census Bureau](https://data.census.gov/cedsci/ "U.S. Census Bureau"):

			
		| Year in [acs].[AgeSexPov] | American Community Survey 5-Year Estimates           |
		|---------------------------|------------------------------------------------------|
		| 2012                      | 2008-2012 American Community Survey 5-Year Estimates |
		| 2013                      | 2009-2013 American Community Survey 5-Year Estimates |
		| 2014                      | 2010-2014 American Community Survey 5-Year Estimates |
		| 2015                      | 2011-2015 American Community Survey 5-Year Estimates |
		| 2016                      | 2012-2016 American Community Survey 5-Year Estimates |
		| 2017                      | 2013-2017 American Community Survey 5-Year Estimates |


## Data Source:

[https://data.census.gov/cedsci/table?q=B17001&tid=ACSDT5Y2012.B17001&vintage=2016&hidePreview=true&g=0100000US.050000&y=2012](https://data.census.gov/cedsci/table?q=B17001&tid=ACSDT5Y2012.B17001&vintage=2016&hidePreview=true&g=0100000US.050000&y=2012 "https://data.census.gov/cedsci/table?q=B17001&tid=ACSDT5Y2012.B17001&vintage=2016&hidePreview=true&g=0100000US.050000&y=2012")

- You can change year by clicking the "1 Year" button. 

- Each time, you can only download one year's data. 

- **Original B17001 Table:**
	
	B17001 : POVERTY STATUS IN THE PAST 12 MONTHS BY SEX BY AGE
	Supporting documentation on code lists, subject definitions, data accuracy, and statistical testing can be found on the American Community Survey website in the 
	<a href="https://www.census.gov/programs-surveys/acs/technical-documentation/code-lists.html" xmlns="http://www.thedataweb.org/aggregateDisplay">Technical Documentation</a>
	
	 section.
	<br xmlns="http://www.thedataweb.org/aggregateDisplay"/>
	
	<br xmlns="http://www.thedataweb.org/aggregateDisplay"/>
	
	Sample size and data quality measures (including coverage rates, allocation rates, and response rates) can be found on the American Community Survey website in the 
	<a href="https://www.census.gov/acs/www/methodology/sample_size_and_data_quality/" xmlns="http://www.thedataweb.org/aggregateDisplay">Methodology</a>
	
	 section.
	
	Although the American Community Survey (ACS) produces population, demographic and housing unit estimates, it is the Census Bureau's Population Estimates Program that produces and disseminates the official estimates of the population for the nation, states, counties, cities, and towns and estimates of housing units for states and counties.
	
	Data are based on a sample and are subject to sampling variability. The degree of uncertainty for an estimate arising from sampling variability is represented through the use of a margin of error. The value shown here is the 90 percent margin of error. The margin of error can be interpreted roughly as providing a 90 percent probability that the interval defined by the estimate minus the margin of error and the estimate plus the margin of error (the lower and upper confidence bounds) contains the true value. In addition to sampling variability, the ACS estimates are subject to nonsampling error (for a discussion of nonsampling variability, see 
	<a href="https://www.census.gov/programs-surveys/acs/technical-documentation.html/" xmlns="http://www.thedataweb.org/aggregateDisplay">Accuracy of the Data</a>
	
	).  The effect of nonsampling error is not represented in these tables.
	
	Estimates of urban and rural populations, housing units, and characteristics reflect boundaries of urban areas defined based on Census 2010 data. As a result, data for urban and rural areas from the ACS do not necessarily reflect the results of ongoing urbanization.
	
	Explanation of Symbols:
	<ol xmlns="http://www.thedataweb.org/aggregateDisplay">
	<li>An "**" entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</li>
	<li>An "-" entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</li>
	<li>An "-" following a median estimate means the median falls in the lowest interval of an open-ended distribution.</li>
	<li>An "+" following a median estimate means the median falls in the upper interval of an open-ended distribution.</li>
	<li>An "***" entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</li>
	<li>An "*****" entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate. </li>
	<li>An "N" entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</li>
	<li>An "(X)" means that the estimate is not applicable or not available.</li>
	</ol>
	
	Source:  U.S. Census Bureau, 2013-2017 American Community Survey 5-Year Estimates
	
	While the 2013-2017 American Community Survey (ACS) data generally reflect the February 2013 Office of Management and Budget (OMB) definitions of metropolitan and micropolitan statistical areas; in certain instances the names, codes, and boundaries of the principal cities shown in ACS tables may differ from the OMB definitions due to differences in the effective dates of the geographic entities.


## Variable Descriptions

| GEO_ID      | Measure              | Level | Income                                                 | Sex    | Age               |
|-------------|----------------------|-------|--------------------------------------------------------|--------|-------------------|
| NAME        | Geographic Area Name |       |                                                        |        |                   |
| B17001_001E | Estimate             | Total |                                                        |        |                   |
| B17001_001M | Margin of Error      | Total |                                                        |        |                   |
| B17001_002E | Estimate             | Total | Income in the past 12 months below poverty level       |        |                   |
| B17001_002M | Margin of Error      | Total | Income in the past 12 months below poverty level       |        |                   |
| B17001_003E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   |                   |
| B17001_003M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   |                   |
| B17001_004E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | Under 5 years     |
| B17001_004M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | Under 5 years     |
| B17001_005E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 5 years           |
| B17001_005M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 5 years           |
| B17001_006E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 6 to 11 years     |
| B17001_006M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 6 to 11 years     |
| B17001_007E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 12 to 14 years    |
| B17001_007M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 12 to 14 years    |
| B17001_008E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 15 years          |
| B17001_008M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 15 years          |
| B17001_009E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 16 and 17 years   |
| B17001_009M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 16 and 17 years   |
| B17001_010E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 18 to 24 years    |
| B17001_010M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 18 to 24 years    |
| B17001_011E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 25 to 34 years    |
| B17001_011M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 25 to 34 years    |
| B17001_012E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 35 to 44 years    |
| B17001_012M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 35 to 44 years    |
| B17001_013E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 45 to 54 years    |
| B17001_013M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 45 to 54 years    |
| B17001_014E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 55 to 64 years    |
| B17001_014M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 55 to 64 years    |
| B17001_015E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 65 to 74 years    |
| B17001_015M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 65 to 74 years    |
| B17001_016E | Estimate             | Total | Income in the past 12 months below poverty level       | Male   | 75 years and over |
| B17001_016M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Male   | 75 years and over |
| B17001_017E | Estimate             | Total | Income in the past 12 months below poverty level       | Female |                   |
| B17001_017M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female |                   |
| B17001_018E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | Under 5 years     |
| B17001_018M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | Under 5 years     |
| B17001_019E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 5 years           |
| B17001_019M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 5 years           |
| B17001_020E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 6 to 11 years     |
| B17001_020M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 6 to 11 years     |
| B17001_021E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 12 to 14 years    |
| B17001_021M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 12 to 14 years    |
| B17001_022E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 15 years          |
| B17001_022M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 15 years          |
| B17001_023E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 16 and 17 years   |
| B17001_023M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 16 and 17 years   |
| B17001_024E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 18 to 24 years    |
| B17001_024M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 18 to 24 years    |
| B17001_025E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 25 to 34 years    |
| B17001_025M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 25 to 34 years    |
| B17001_026E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 35 to 44 years    |
| B17001_026M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 35 to 44 years    |
| B17001_027E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 45 to 54 years    |
| B17001_027M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 45 to 54 years    |
| B17001_028E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 55 to 64 years    |
| B17001_028M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 55 to 64 years    |
| B17001_029E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 65 to 74 years    |
| B17001_029M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 65 to 74 years    |
| B17001_030E | Estimate             | Total | Income in the past 12 months below poverty level       | Female | 75 years and over |
| B17001_030M | Margin of Error      | Total | Income in the past 12 months below poverty level       | Female | 75 years and over |
| B17001_031E | Estimate             | Total | Income in the past 12 months at or above poverty level |        |                   |
| B17001_031M | Margin of Error      | Total | Income in the past 12 months at or above poverty level |        |                   |
| B17001_032E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   |                   |
| B17001_032M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   |                   |
| B17001_033E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | Under 5 years     |
| B17001_033M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | Under 5 years     |
| B17001_034E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 5 years           |
| B17001_034M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 5 years           |
| B17001_035E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 6 to 11 years     |
| B17001_035M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 6 to 11 years     |
| B17001_036E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 12 to 14 years    |
| B17001_036M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 12 to 14 years    |
| B17001_037E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 15 years          |
| B17001_037M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 15 years          |
| B17001_038E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 16 and 17 years   |
| B17001_038M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 16 and 17 years   |
| B17001_039E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 18 to 24 years    |
| B17001_039M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 18 to 24 years    |
| B17001_040E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 25 to 34 years    |
| B17001_040M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 25 to 34 years    |
| B17001_041E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 35 to 44 years    |
| B17001_041M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 35 to 44 years    |
| B17001_042E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 45 to 54 years    |
| B17001_042M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 45 to 54 years    |
| B17001_043E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 55 to 64 years    |
| B17001_043M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 55 to 64 years    |
| B17001_044E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 65 to 74 years    |
| B17001_044M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 65 to 74 years    |
| B17001_045E | Estimate             | Total | Income in the past 12 months at or above poverty level | Male   | 75 years and over |
| B17001_045M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Male   | 75 years and over |
| B17001_046E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female |                   |
| B17001_046M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female |                   |
| B17001_047E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | Under 5 years     |
| B17001_047M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | Under 5 years     |
| B17001_048E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 5 years           |
| B17001_048M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 5 years           |
| B17001_049E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 6 to 11 years     |
| B17001_049M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 6 to 11 years     |
| B17001_050E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 12 to 14 years    |
| B17001_050M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 12 to 14 years    |
| B17001_051E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 15 years          |
| B17001_051M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 15 years          |
| B17001_052E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 16 and 17 years   |
| B17001_052M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 16 and 17 years   |
| B17001_053E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 18 to 24 years    |
| B17001_053M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 18 to 24 years    |
| B17001_054E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 25 to 34 years    |
| B17001_054M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 25 to 34 years    |
| B17001_055E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 35 to 44 years    |
| B17001_055M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 35 to 44 years    |
| B17001_056E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 45 to 54 years    |
| B17001_056M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 45 to 54 years    |
| B17001_057E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 55 to 64 years    |
| B17001_057M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 55 to 64 years    |
| B17001_058E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 65 to 74 years    |
| B17001_058M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 65 to 74 years    |
| B17001_059E | Estimate             | Total | Income in the past 12 months at or above poverty level | Female | 75 years and over |
| B17001_059M | Margin of Error      | Total | Income in the past 12 months at or above poverty level | Female | 75 years and over |