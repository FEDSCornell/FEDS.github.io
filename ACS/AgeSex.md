# American Community Survey (ACS) Age by Sex 

This FEDS data table shows population by age and sex at the county level. It is created based on ACS PEPAGESEX table. 

Annual Estimates of the Resident Population for Selected Age Groups by Sex for the United States, States, Counties, and Puerto Rico Commonwealth and Municipios: April 1, 2010 to July 1, 2017

## Notes:
The estimates are based on the 2010 Census and reflect changes to the April 1, 2010
population due to the Count Question Resolution program and geographic program revisions.
Median age is calculated based on single year of age. For population estimates methodology
statements, see 
http://www.census.gov/programs-surveys/popest/technical-documentation/methodology.html.


The 6,222 people in Bedford city, Virginia, which was an independent city as of the 2010 Census, are not included in the April 1, 2010 Census enumerated population presented in the county estimates. In July 2013, the legal status of Bedford changed from a city to a town and it became dependent within (or part of) Bedford County, Virginia. This population of Bedford town is now included in the April 1, 2010 estimates base and all July 1 estimates for Bedford County. Because it is no longer an independent city, Bedford town is not listed in this table. As a result, the sum of the April 1, 2010 census values for Virginia counties and independent cities does not equal the 2010 Census count for Virginia, and the sum of April 1, 2010 census values for all counties and independent cities in the United States does not equal the 2010 Census count for the United States. Substantial geographic changes to counties can be found on the Census Bureau website at http://www.census.gov/geo/reference/county-changes.html.


Suggested Citation: 
Annual Estimates of the Resident Population for Selected Age Groups by Sex for the United States, States, Counties and Puerto Rico Commonwealth and Municipios: April 1, 2010 to July 1, 2017 
Source: U.S. Census Bureau, Population Division 
Release Date: June 2018

## Groups:

| Number | Age Range         |
|--------|-------------------|
| 1      | Under 5 years     |
| 2      | 5 to 9 years      |
| 3      | 10 to 14 years    |
| 4      | 15 to 19 years    |
| 5      | 20 to 24 years    |
| 6      | 25 to 29 years    |
| 7      | 30 to 34 years    |
| 8      | 35 to 39 years    |
| 9      | 40 to 44 years    |
| 10     | 45 to 49 years    |
| 11     | 50 to 54 years    |
| 12     | 55 to 59 years    |
| 13     | 60 to 64 years    |
| 14     | 65 to 69 years    |
| 15     | 70 to 74 years    |
| 16     | 75 to 79 years    |
| 17     | 80 to 84 years    |
| 18     | 85 years and over |

## Python code:
[https://www.dropbox.com/s/nikj82k3fl3u9pj/AgeSex.py?dl=0](https://www.dropbox.com/s/nikj82k3fl3u9pj/AgeSex.py?dl=0 "https://www.dropbox.com/s/nikj82k3fl3u9pj/AgeSex.py?dl=0")

## Column Description

| Column Name               | Description                                                                          |
|---------------------------|--------------------------------------------------------------------------------------|
| GEO.id                    | Id                                                                                   |
| GEO.id2                   | Id2                                                                                  |
| GEO.display-label         | Geography                                                                            |
| ST                        | State Name                                                                           |
| county                    | County Name                                                                          |
| fips_st                   | State FIPS                                                                           |
| fips_co                   | County FIPS                                                                          |
| Year                      | Year                                                                                 |
| cen4_year_sex0_age999     | April 1, - - Census - Both Sexes; Total                                              |
| cen4_year_sex1_age999     | April 1, - - Census - Male; Total                                                    |
| cen4_year_sex2_age999     | April 1, - - Census - Female; Total                                                  |
| est4_year_sex0_age999     | April 1, - - Estimates Base - Both Sexes; Total                                      |
| est4_year_sex1_age999     | April 1, - - Estimates Base - Male; Total                                            |
| est4_year_sex2_age999     | April 1, - - Estimates Base - Female; Total                                          |
| est7_year_sex0_age999     | Population Estimate (as of July 1) - - - Both Sexes; Total                           |
| est7_year_sex1_age999     | Population Estimate (as of July 1) - - - Male; Total                                 |
| est7_year_sex2_age999     | Population Estimate (as of July 1) - - - Female; Total                               |
| cen4_year_sex0_age0to4    | April 1, - - Census - Both Sexes; Total - Under 5 years                              |
| cen4_year_sex1_age0to4    | April 1, - - Census - Male; Total - Under 5 years                                    |
| cen4_year_sex2_age0to4    | April 1, - - Census - Female; Total - Under 5 years                                  |
| est4_year_sex0_age0to4    | April 1, - - Estimates Base - Both Sexes; Total - Under 5 years                      |
| est4_year_sex1_age0to4    | April 1, - - Estimates Base - Male; Total - Under 5 years                            |
| est4_year_sex2_age0to4    | April 1, - - Estimates Base - Female; Total - Under 5 years                          |
| est7_year_sex0_age0to4    | Population Estimate (as of July 1) - - - Both Sexes; Total - Under 5 years           |
| est7_year_sex1_age0to4    | Population Estimate (as of July 1) - - - Male; Total - Under 5 years                 |
| est7_year_sex2_age0to4    | Population Estimate (as of July 1) - - - Female; Total - Under 5 years               |
| cen4_year_sex0_age5to9    | April 1, - - Census - Both Sexes; Total - 5 to 9 years                               |
| cen4_year_sex1_age5to9    | April 1, - - Census - Male; Total - 5 to 9 years                                     |
| cen4_year_sex2_age5to9    | April 1, - - Census - Female; Total - 5 to 9 years                                   |
| est4_year_sex0_age5to9    | April 1, - - Estimates Base - Both Sexes; Total - 5 to 9 years                       |
| est4_year_sex1_age5to9    | April 1, - - Estimates Base - Male; Total - 5 to 9 years                             |
| est4_year_sex2_age5to9    | April 1, - - Estimates Base - Female; Total - 5 to 9 years                           |
| est7_year_sex0_age5to9    | Population Estimate (as of July 1) - - - Both Sexes; Total - 5 to 9 years            |
| est7_year_sex1_age5to9    | Population Estimate (as of July 1) - - - Male; Total - 5 to 9 years                  |
| est7_year_sex2_age5to9    | Population Estimate (as of July 1) - - - Female; Total - 5 to 9 years                |
| cen4_year_sex0_age10to14  | April 1, - - Census - Both Sexes; Total - 10 to 14 years                             |
| cen4_year_sex1_age10to14  | April 1, - - Census - Male; Total - 10 to 14 years                                   |
| cen4_year_sex2_age10to14  | April 1, - - Census - Female; Total - 10 to 14 years                                 |
| est4_year_sex0_age10to14  | April 1, - - Estimates Base - Both Sexes; Total - 10 to 14 years                     |
| est4_year_sex1_age10to14  | April 1, - - Estimates Base - Male; Total - 10 to 14 years                           |
| est4_year_sex2_age10to14  | April 1, - - Estimates Base - Female; Total - 10 to 14 years                         |
| est7_year_sex0_age10to14  | Population Estimate (as of July 1) - - - Both Sexes; Total - 10 to 14 years          |
| est7_year_sex1_age10to14  | Population Estimate (as of July 1) - - - Male; Total - 10 to 14 years                |
| est7_year_sex2_age10to14  | Population Estimate (as of July 1) - - - Female; Total - 10 to 14 years              |
| cen4_year_sex0_age15to19  | April 1, - - Census - Both Sexes; Total - 15 to 19 years                             |
| cen4_year_sex1_age15to19  | April 1, - - Census - Male; Total - 15 to 19 years                                   |
| cen4_year_sex2_age15to19  | April 1, - - Census - Female; Total - 15 to 19 years                                 |
| est4_year_sex0_age15to19  | April 1, - - Estimates Base - Both Sexes; Total - 15 to 19 years                     |
| est4_year_sex1_age15to19  | April 1, - - Estimates Base - Male; Total - 15 to 19 years                           |
| est4_year_sex2_age15to19  | April 1, - - Estimates Base - Female; Total - 15 to 19 years                         |
| est7_year_sex0_age15to19  | Population Estimate (as of July 1) - - - Both Sexes; Total - 15 to 19 years          |
| est7_year_sex1_age15to19  | Population Estimate (as of July 1) - - - Male; Total - 15 to 19 years                |
| est7_year_sex2_age15to19  | Population Estimate (as of July 1) - - - Female; Total - 15 to 19 years              |
| cen4_year_sex0_age20to24  | April 1, - - Census - Both Sexes; Total - 20 to 24 years                             |
| cen4_year_sex1_age20to24  | April 1, - - Census - Male; Total - 20 to 24 years                                   |
| cen4_year_sex2_age20to24  | April 1, - - Census - Female; Total - 20 to 24 years                                 |
| est4_year_sex0_age20to24  | April 1, - - Estimates Base - Both Sexes; Total - 20 to 24 years                     |
| est4_year_sex1_age20to24  | April 1, - - Estimates Base - Male; Total - 20 to 24 years                           |
| est4_year_sex2_age20to24  | April 1, - - Estimates Base - Female; Total - 20 to 24 years                         |
| est7_year_sex0_age20to24  | Population Estimate (as of July 1) - - - Both Sexes; Total - 20 to 24 years          |
| est7_year_sex1_age20to24  | Population Estimate (as of July 1) - - - Male; Total - 20 to 24 years                |
| est7_year_sex2_age20to24  | Population Estimate (as of July 1) - - - Female; Total - 20 to 24 years              |
| cen4_year_sex0_age25to29  | April 1, - - Census - Both Sexes; Total - 25 to 29 years                             |
| cen4_year_sex1_age25to29  | April 1, - - Census - Male; Total - 25 to 29 years                                   |
| cen4_year_sex2_age25to29  | April 1, - - Census - Female; Total - 25 to 29 years                                 |
| est4_year_sex0_age25to29  | April 1, - - Estimates Base - Both Sexes; Total - 25 to 29 years                     |
| est4_year_sex1_age25to29  | April 1, - - Estimates Base - Male; Total - 25 to 29 years                           |
| est4_year_sex2_age25to29  | April 1, - - Estimates Base - Female; Total - 25 to 29 years                         |
| est7_year_sex0_age25to29  | Population Estimate (as of July 1) - - - Both Sexes; Total - 25 to 29 years          |
| est7_year_sex1_age25to29  | Population Estimate (as of July 1) - - - Male; Total - 25 to 29 years                |
| est7_year_sex2_age25to29  | Population Estimate (as of July 1) - - - Female; Total - 25 to 29 years              |
| cen4_year_sex0_age30to34  | April 1, - - Census - Both Sexes; Total - 30 to 34 years                             |
| cen4_year_sex1_age30to34  | April 1, - - Census - Male; Total - 30 to 34 years                                   |
| cen4_year_sex2_age30to34  | April 1, - - Census - Female; Total - 30 to 34 years                                 |
| est4_year_sex0_age30to34  | April 1, - - Estimates Base - Both Sexes; Total - 30 to 34 years                     |
| est4_year_sex1_age30to34  | April 1, - - Estimates Base - Male; Total - 30 to 34 years                           |
| est4_year_sex2_age30to34  | April 1, - - Estimates Base - Female; Total - 30 to 34 years                         |
| est7_year_sex0_age30to34  | Population Estimate (as of July 1) - - - Both Sexes; Total - 30 to 34 years          |
| est7_year_sex1_age30to34  | Population Estimate (as of July 1) - - - Male; Total - 30 to 34 years                |
| est7_year_sex2_age30to34  | Population Estimate (as of July 1) - - - Female; Total - 30 to 34 years              |
| cen4_year_sex0_age35to39  | April 1, - - Census - Both Sexes; Total - 35 to 39 years                             |
| cen4_year_sex1_age35to39  | April 1, - - Census - Male; Total - 35 to 39 years                                   |
| cen4_year_sex2_age35to39  | April 1, - - Census - Female; Total - 35 to 39 years                                 |
| est4_year_sex0_age35to39  | April 1, - - Estimates Base - Both Sexes; Total - 35 to 39 years                     |
| est4_year_sex1_age35to39  | April 1, - - Estimates Base - Male; Total - 35 to 39 years                           |
| est4_year_sex2_age35to39  | April 1, - - Estimates Base - Female; Total - 35 to 39 years                         |
| est7_year_sex0_age35to39  | Population Estimate (as of July 1) - - - Both Sexes; Total - 35 to 39 years          |
| est7_year_sex1_age35to39  | Population Estimate (as of July 1) - - - Male; Total - 35 to 39 years                |
| est7_year_sex2_age35to39  | Population Estimate (as of July 1) - - - Female; Total - 35 to 39 years              |
| cen4_year_sex0_age40to44  | April 1, - - Census - Both Sexes; Total - 40 to 44 years                             |
| cen4_year_sex1_age40to44  | April 1, - - Census - Male; Total - 40 to 44 years                                   |
| cen4_year_sex2_age40to44  | April 1, - - Census - Female; Total - 40 to 44 years                                 |
| est4_year_sex0_age40to44  | April 1, - - Estimates Base - Both Sexes; Total - 40 to 44 years                     |
| est4_year_sex1_age40to44  | April 1, - - Estimates Base - Male; Total - 40 to 44 years                           |
| est4_year_sex2_age40to44  | April 1, - - Estimates Base - Female; Total - 40 to 44 years                         |
| est7_year_sex0_age40to44  | Population Estimate (as of July 1) - - - Both Sexes; Total - 40 to 44 years          |
| est7_year_sex1_age40to44  | Population Estimate (as of July 1) - - - Male; Total - 40 to 44 years                |
| est7_year_sex2_age40to44  | Population Estimate (as of July 1) - - - Female; Total - 40 to 44 years              |
| cen4_year_sex0_age45to49  | April 1, - - Census - Both Sexes; Total - 45 to 49 years                             |
| cen4_year_sex1_age45to49  | April 1, - - Census - Male; Total - 45 to 49 years                                   |
| cen4_year_sex2_age45to49  | April 1, - - Census - Female; Total - 45 to 49 years                                 |
| est4_year_sex0_age45to49  | April 1, - - Estimates Base - Both Sexes; Total - 45 to 49 years                     |
| est4_year_sex1_age45to49  | April 1, - - Estimates Base - Male; Total - 45 to 49 years                           |
| est4_year_sex2_age45to49  | April 1, - - Estimates Base - Female; Total - 45 to 49 years                         |
| est7_year_sex0_age45to49  | Population Estimate (as of July 1) - - - Both Sexes; Total - 45 to 49 years          |
| est7_year_sex1_age45to49  | Population Estimate (as of July 1) - - - Male; Total - 45 to 49 years                |
| est7_year_sex2_age45to49  | Population Estimate (as of July 1) - - - Female; Total - 45 to 49 years              |
| cen4_year_sex0_age50to54  | April 1, - - Census - Both Sexes; Total - 50 to 54 years                             |
| cen4_year_sex1_age50to54  | April 1, - - Census - Male; Total - 50 to 54 years                                   |
| cen4_year_sex2_age50to54  | April 1, - - Census - Female; Total - 50 to 54 years                                 |
| est4_year_sex0_age50to54  | April 1, - - Estimates Base - Both Sexes; Total - 50 to 54 years                     |
| est4_year_sex1_age50to54  | April 1, - - Estimates Base - Male; Total - 50 to 54 years                           |
| est4_year_sex2_age50to54  | April 1, - - Estimates Base - Female; Total - 50 to 54 years                         |
| est7_year_sex0_age50to54  | Population Estimate (as of July 1) - - - Both Sexes; Total - 50 to 54 years          |
| est7_year_sex1_age50to54  | Population Estimate (as of July 1) - - - Male; Total - 50 to 54 years                |
| est7_year_sex2_age50to54  | Population Estimate (as of July 1) - - - Female; Total - 50 to 54 years              |
| cen4_year_sex0_age55to59  | April 1, - - Census - Both Sexes; Total - 55 to 59 years                             |
| cen4_year_sex1_age55to59  | April 1, - - Census - Male; Total - 55 to 59 years                                   |
| cen4_year_sex2_age55to59  | April 1, - - Census - Female; Total - 55 to 59 years                                 |
| est4_year_sex0_age55to59  | April 1, - - Estimates Base - Both Sexes; Total - 55 to 59 years                     |
| est4_year_sex1_age55to59  | April 1, - - Estimates Base - Male; Total - 55 to 59 years                           |
| est4_year_sex2_age55to59  | April 1, - - Estimates Base - Female; Total - 55 to 59 years                         |
| est7_year_sex0_age55to59  | Population Estimate (as of July 1) - - - Both Sexes; Total - 55 to 59 years          |
| est7_year_sex1_age55to59  | Population Estimate (as of July 1) - - - Male; Total - 55 to 59 years                |
| est7_year_sex2_age55to59  | Population Estimate (as of July 1) - - - Female; Total - 55 to 59 years              |
| cen4_year_sex0_age60to64  | April 1, - - Census - Both Sexes; Total - 60 to 64 years                             |
| cen4_year_sex1_age60to64  | April 1, - - Census - Male; Total - 60 to 64 years                                   |
| cen4_year_sex2_age60to64  | April 1, - - Census - Female; Total - 60 to 64 years                                 |
| est4_year_sex0_age60to64  | April 1, - - Estimates Base - Both Sexes; Total - 60 to 64 years                     |
| est4_year_sex1_age60to64  | April 1, - - Estimates Base - Male; Total - 60 to 64 years                           |
| est4_year_sex2_age60to64  | April 1, - - Estimates Base - Female; Total - 60 to 64 years                         |
| est7_year_sex0_age60to64  | Population Estimate (as of July 1) - - - Both Sexes; Total - 60 to 64 years          |
| est7_year_sex1_age60to64  | Population Estimate (as of July 1) - - - Male; Total - 60 to 64 years                |
| est7_year_sex2_age60to64  | Population Estimate (as of July 1) - - - Female; Total - 60 to 64 years              |
| cen4_year_sex0_age65to69  | April 1, - - Census - Both Sexes; Total - 65 to 69 years                             |
| cen4_year_sex1_age65to69  | April 1, - - Census - Male; Total - 65 to 69 years                                   |
| cen4_year_sex2_age65to69  | April 1, - - Census - Female; Total - 65 to 69 years                                 |
| est4_year_sex0_age65to69  | April 1, - - Estimates Base - Both Sexes; Total - 65 to 69 years                     |
| est4_year_sex1_age65to69  | April 1, - - Estimates Base - Male; Total - 65 to 69 years                           |
| est4_year_sex2_age65to69  | April 1, - - Estimates Base - Female; Total - 65 to 69 years                         |
| est7_year_sex0_age65to69  | Population Estimate (as of July 1) - - - Both Sexes; Total - 65 to 69 years          |
| est7_year_sex1_age65to69  | Population Estimate (as of July 1) - - - Male; Total - 65 to 69 years                |
| est7_year_sex2_age65to69  | Population Estimate (as of July 1) - - - Female; Total - 65 to 69 years              |
| cen4_year_sex0_age70to74  | April 1, - - Census - Both Sexes; Total - 70 to 74 years                             |
| cen4_year_sex1_age70to74  | April 1, - - Census - Male; Total - 70 to 74 years                                   |
| cen4_year_sex2_age70to74  | April 1, - - Census - Female; Total - 70 to 74 years                                 |
| est4_year_sex0_age70to74  | April 1, - - Estimates Base - Both Sexes; Total - 70 to 74 years                     |
| est4_year_sex1_age70to74  | April 1, - - Estimates Base - Male; Total - 70 to 74 years                           |
| est4_year_sex2_age70to74  | April 1, - - Estimates Base - Female; Total - 70 to 74 years                         |
| est7_year_sex0_age70to74  | Population Estimate (as of July 1) - - - Both Sexes; Total - 70 to 74 years          |
| est7_year_sex1_age70to74  | Population Estimate (as of July 1) - - - Male; Total - 70 to 74 years                |
| est7_year_sex2_age70to74  | Population Estimate (as of July 1) - - - Female; Total - 70 to 74 years              |
| cen4_year_sex0_age75to79  | April 1, - - Census - Both Sexes; Total - 75 to 79 years                             |
| cen4_year_sex1_age75to79  | April 1, - - Census - Male; Total - 75 to 79 years                                   |
| cen4_year_sex2_age75to79  | April 1, - - Census - Female; Total - 75 to 79 years                                 |
| est4_year_sex0_age75to79  | April 1, - - Estimates Base - Both Sexes; Total - 75 to 79 years                     |
| est4_year_sex1_age75to79  | April 1, - - Estimates Base - Male; Total - 75 to 79 years                           |
| est4_year_sex2_age75to79  | April 1, - - Estimates Base - Female; Total - 75 to 79 years                         |
| est7_year_sex0_age75to79  | Population Estimate (as of July 1) - - - Both Sexes; Total - 75 to 79 years          |
| est7_year_sex1_age75to79  | Population Estimate (as of July 1) - - - Male; Total - 75 to 79 years                |
| est7_year_sex2_age75to79  | Population Estimate (as of July 1) - - - Female; Total - 75 to 79 years              |
| cen4_year_sex0_age80to84  | April 1, - - Census - Both Sexes; Total - 80 to 84 years                             |
| cen4_year_sex1_age80to84  | April 1, - - Census - Male; Total - 80 to 84 years                                   |
| cen4_year_sex2_age80to84  | April 1, - - Census - Female; Total - 80 to 84 years                                 |
| est4_year_sex0_age80to84  | April 1, - - Estimates Base - Both Sexes; Total - 80 to 84 years                     |
| est4_year_sex1_age80to84  | April 1, - - Estimates Base - Male; Total - 80 to 84 years                           |
| est4_year_sex2_age80to84  | April 1, - - Estimates Base - Female; Total - 80 to 84 years                         |
| est7_year_sex0_age80to84  | Population Estimate (as of July 1) - - - Both Sexes; Total - 80 to 84 years          |
| est7_year_sex1_age80to84  | Population Estimate (as of July 1) - - - Male; Total - 80 to 84 years                |
| est7_year_sex2_age80to84  | Population Estimate (as of July 1) - - - Female; Total - 80 to 84 years              |
| cen4_year_sex0_age85plus  | April 1, - - Census - Both Sexes; Total - 85 years and over                          |
| cen4_year_sex1_age85plus  | April 1, - - Census - Male; Total - 85 years and over                                |
| cen4_year_sex2_age85plus  | April 1, - - Census - Female; Total - 85 years and over                              |
| est4_year_sex0_age85plus  | April 1, - - Estimates Base - Both Sexes; Total - 85 years and over                  |
| est4_year_sex1_age85plus  | April 1, - - Estimates Base - Male; Total - 85 years and over                        |
| est4_year_sex2_age85plus  | April 1, - - Estimates Base - Female; Total - 85 years and over                      |
| est7_year_sex0_age85plus  | Population Estimate (as of July 1) - - - Both Sexes; Total - 85 years and over       |
| est7_year_sex1_age85plus  | Population Estimate (as of July 1) - - - Male; Total - 85 years and over             |
| est7_year_sex2_age85plus  | Population Estimate (as of July 1) - - - Female; Total - 85 years and over           |
| cen4_year_sex0_age0to17   | April 1, - - Census - Both Sexes; Under 18 years                                     |
| cen4_year_sex1_age0to17   | April 1, - - Census - Male; Under 18 years                                           |
| cen4_year_sex2_age0to17   | April 1, - - Census - Female; Under 18 years                                         |
| est4_year_sex0_age0to17   | April 1, - - Estimates Base - Both Sexes; Under 18 years                             |
| est4_year_sex1_age0to17   | April 1, - - Estimates Base - Male; Under 18 years                                   |
| est4_year_sex2_age0to17   | April 1, - - Estimates Base - Female; Under 18 years                                 |
| est7_year_sex0_age0to17   | Population Estimate (as of July 1) - - - Both Sexes; Under 18 years                  |
| est7_year_sex1_age0to17   | Population Estimate (as of July 1) - - - Male; Under 18 years                        |
| est7_year_sex2_age0to17   | Population Estimate (as of July 1) - - - Female; Under 18 years                      |
| cen4_year_sex0_age0to4r   | April 1, - - Census - Both Sexes; Under 18 years - Under 5 years                     |
| cen4_year_sex1_age0to4r   | April 1, - - Census - Male; Under 18 years - Under 5 years                           |
| cen4_year_sex2_age0to4r   | April 1, - - Census - Female; Under 18 years - Under 5 years                         |
| est4_year_sex0_age0to4r   | April 1, - - Estimates Base - Both Sexes; Under 18 years - Under 5 years             |
| est4_year_sex1_age0to4r   | April 1, - - Estimates Base - Male; Under 18 years - Under 5 years                   |
| est4_year_sex2_age0to4r   | April 1, - - Estimates Base - Female; Under 18 years - Under 5 years                 |
| est7_year_sex0_age0to4r   | Population Estimate (as of July 1) - - - Both Sexes; Under 18 years - Under 5 years  |
| est7_year_sex1_age0to4r   | Population Estimate (as of July 1) - - - Male; Under 18 years - Under 5 years        |
| est7_year_sex2_age0to4r   | Population Estimate (as of July 1) - - - Female; Under 18 years - Under 5 years      |
| cen4_year_sex0_age5to13   | April 1, - - Census - Both Sexes; Under 18 years - 5 to 13 years                     |
| cen4_year_sex1_age5to13   | April 1, - - Census - Male; Under 18 years - 5 to 13 years                           |
| cen4_year_sex2_age5to13   | April 1, - - Census - Female; Under 18 years - 5 to 13 years                         |
| est4_year_sex0_age5to13   | April 1, - - Estimates Base - Both Sexes; Under 18 years - 5 to 13 years             |
| est4_year_sex1_age5to13   | April 1, - - Estimates Base - Male; Under 18 years - 5 to 13 years                   |
| est4_year_sex2_age5to13   | April 1, - - Estimates Base - Female; Under 18 years - 5 to 13 years                 |
| est7_year_sex0_age5to13   | Population Estimate (as of July 1) - - - Both Sexes; Under 18 years - 5 to 13 years  |
| est7_year_sex1_age5to13   | Population Estimate (as of July 1) - - - Male; Under 18 years - 5 to 13 years        |
| est7_year_sex2_age5to13   | Population Estimate (as of July 1) - - - Female; Under 18 years - 5 to 13 years      |
| cen4_year_sex0_age14to17  | April 1, - - Census - Both Sexes; Under 18 years - 14 to 17 years                    |
| cen4_year_sex1_age14to17  | April 1, - - Census - Male; Under 18 years - 14 to 17 years                          |
| cen4_year_sex2_age14to17  | April 1, - - Census - Female; Under 18 years - 14 to 17 years                        |
| est4_year_sex0_age14to17  | April 1, - - Estimates Base - Both Sexes; Under 18 years - 14 to 17 years            |
| est4_year_sex1_age14to17  | April 1, - - Estimates Base - Male; Under 18 years - 14 to 17 years                  |
| est4_year_sex2_age14to17  | April 1, - - Estimates Base - Female; Under 18 years - 14 to 17 years                |
| est7_year_sex0_age14to17  | Population Estimate (as of July 1) - - - Both Sexes; Under 18 years - 14 to 17 years |
| est7_year_sex1_age14to17  | Population Estimate (as of July 1) - - - Male; Under 18 years - 14 to 17 years       |
| est7_year_sex2_age14to17  | Population Estimate (as of July 1) - - - Female; Under 18 years - 14 to 17 years     |
| cen4_year_sex0_age18to64  | April 1, - - Census - Both Sexes; 18 to 64 years                                     |
| cen4_year_sex1_age18to64  | April 1, - - Census - Male; 18 to 64 years                                           |
| cen4_year_sex2_age18to64  | April 1, - - Census - Female; 18 to 64 years                                         |
| est4_year_sex0_age18to64  | April 1, - - Estimates Base - Both Sexes; 18 to 64 years                             |
| est4_year_sex1_age18to64  | April 1, - - Estimates Base - Male; 18 to 64 years                                   |
| est4_year_sex2_age18to64  | April 1, - - Estimates Base - Female; 18 to 64 years                                 |
| est7_year_sex0_age18to64  | Population Estimate (as of July 1) - - - Both Sexes; 18 to 64 years                  |
| est7_year_sex1_age18to64  | Population Estimate (as of July 1) - - - Male; 18 to 64 years                        |
| est7_year_sex2_age18to64  | Population Estimate (as of July 1) - - - Female; 18 to 64 years                      |
| cen4_year_sex0_age18to24  | April 1, - - Census - Both Sexes; 18 to 64 years - 18 to 24 years                    |
| cen4_year_sex1_age18to24  | April 1, - - Census - Male; 18 to 64 years - 18 to 24 years                          |
| cen4_year_sex2_age18to24  | April 1, - - Census - Female; 18 to 64 years - 18 to 24 years                        |
| est4_year_sex0_age18to24  | April 1, - - Estimates Base - Both Sexes; 18 to 64 years - 18 to 24 years            |
| est4_year_sex1_age18to24  | April 1, - - Estimates Base - Male; 18 to 64 years - 18 to 24 years                  |
| est4_year_sex2_age18to24  | April 1, - - Estimates Base - Female; 18 to 64 years - 18 to 24 years                |
| est7_year_sex0_age18to24  | Population Estimate (as of July 1) - - - Both Sexes; 18 to 64 years - 18 to 24 years |
| est7_year_sex1_age18to24  | Population Estimate (as of July 1) - - - Male; 18 to 64 years - 18 to 24 years       |
| est7_year_sex2_age18to24  | Population Estimate (as of July 1) - - - Female; 18 to 64 years - 18 to 24 years     |
| cen4_year_sex0_age25to44  | April 1, - - Census - Both Sexes; 18 to 64 years - 25 to 44 years                    |
| cen4_year_sex1_age25to44  | April 1, - - Census - Male; 18 to 64 years - 25 to 44 years                          |
| cen4_year_sex2_age25to44  | April 1, - - Census - Female; 18 to 64 years - 25 to 44 years                        |
| est4_year_sex0_age25to44  | April 1, - - Estimates Base - Both Sexes; 18 to 64 years - 25 to 44 years            |
| est4_year_sex1_age25to44  | April 1, - - Estimates Base - Male; 18 to 64 years - 25 to 44 years                  |
| est4_year_sex2_age25to44  | April 1, - - Estimates Base - Female; 18 to 64 years - 25 to 44 years                |
| est7_year_sex0_age25to44  | Population Estimate (as of July 1) - - - Both Sexes; 18 to 64 years - 25 to 44 years |
| est7_year_sex1_age25to44  | Population Estimate (as of July 1) - - - Male; 18 to 64 years - 25 to 44 years       |
| est7_year_sex2_age25to44  | Population Estimate (as of July 1) - - - Female; 18 to 64 years - 25 to 44 years     |
| cen4_year_sex0_age45to64  | April 1, - - Census - Both Sexes; 18 to 64 years - 45 to 64 years                    |
| cen4_year_sex1_age45to64  | April 1, - - Census - Male; 18 to 64 years - 45 to 64 years                          |
| cen4_year_sex2_age45to64  | April 1, - - Census - Female; 18 to 64 years - 45 to 64 years                        |
| est4_year_sex0_age45to64  | April 1, - - Estimates Base - Both Sexes; 18 to 64 years - 45 to 64 years            |
| est4_year_sex1_age45to64  | April 1, - - Estimates Base - Male; 18 to 64 years - 45 to 64 years                  |
| est4_year_sex2_age45to64  | April 1, - - Estimates Base - Female; 18 to 64 years - 45 to 64 years                |
| est7_year_sex0_age45to64  | Population Estimate (as of July 1) - - - Both Sexes; 18 to 64 years - 45 to 64 years |
| est7_year_sex1_age45to64  | Population Estimate (as of July 1) - - - Male; 18 to 64 years - 45 to 64 years       |
| est7_year_sex2_age45to64  | Population Estimate (as of July 1) - - - Female; 18 to 64 years - 45 to 64 years     |
| cen4_year_sex0_age65plus  | April 1, - - Census - Both Sexes; 65 years and over                                  |
| cen4_year_sex1_age65plus  | April 1, - - Census - Male; 65 years and over                                        |
| cen4_year_sex2_age65plus  | April 1, - - Census - Female; 65 years and over                                      |
| est4_year_sex0_age65plus  | April 1, - - Estimates Base - Both Sexes; 65 years and over                          |
| est4_year_sex1_age65plus  | April 1, - - Estimates Base - Male; 65 years and over                                |
| est4_year_sex2_age65plus  | April 1, - - Estimates Base - Female; 65 years and over                              |
| est7_year_sex0_age65plus  | Population Estimate (as of July 1) - - - Both Sexes; 65 years and over               |
| est7_year_sex1_age65plus  | Population Estimate (as of July 1) - - - Male; 65 years and over                     |
| est7_year_sex2_age65plus  | Population Estimate (as of July 1) - - - Female; 65 years and over                   |
| cen4_year_sex0_age85plusr | April 1, - - Census - Both Sexes; 85 years and over                                  |
| cen4_year_sex1_age85plusr | April 1, - - Census - Male; 85 years and over                                        |
| cen4_year_sex2_age85plusr | April 1, - - Census - Female; 85 years and over                                      |
| est4_year_sex0_age85plusr | April 1, - - Estimates Base - Both Sexes; 85 years and over                          |
| est4_year_sex1_age85plusr | April 1, - - Estimates Base - Male; 85 years and over                                |
| est4_year_sex2_age85plusr | April 1, - - Estimates Base - Female; 85 years and over                              |
| est7_year_sex0_age85plusr | Population Estimate (as of July 1) - - - Both Sexes; 85 years and over               |
| est7_year_sex1_age85plusr | Population Estimate (as of July 1) - - - Male; 85 years and over                     |
| est7_year_sex2_age85plusr | Population Estimate (as of July 1) - - - Female; 85 years and over                   |
| cen4_year_sex0_age16plus  | April 1, - - Census - Both Sexes; 16 years and over                                  |
| cen4_year_sex1_age16plus  | April 1, - - Census - Male; 16 years and over                                        |
| cen4_year_sex2_age16plus  | April 1, - - Census - Female; 16 years and over                                      |
| est4_year_sex0_age16plus  | April 1, - - Estimates Base - Both Sexes; 16 years and over                          |
| est4_year_sex1_age16plus  | April 1, - - Estimates Base - Male; 16 years and over                                |
| est4_year_sex2_age16plus  | April 1, - - Estimates Base - Female; 16 years and over                              |
| est7_year_sex0_age16plus  | Population Estimate (as of July 1) - - - Both Sexes; 16 years and over               |
| est7_year_sex1_age16plus  | Population Estimate (as of July 1) - - - Male; 16 years and over                     |
| est7_year_sex2_age16plus  | Population Estimate (as of July 1) - - - Female; 16 years and over                   |
| cen4_year_sex0_age18plus  | April 1, - - Census - Both Sexes; 18 years and over                                  |
| cen4_year_sex1_age18plus  | April 1, - - Census - Male; 18 years and over                                        |
| cen4_year_sex2_age18plus  | April 1, - - Census - Female; 18 years and over                                      |
| est4_year_sex0_age18plus  | April 1, - - Estimates Base - Both Sexes; 18 years and over                          |
| est4_year_sex1_age18plus  | April 1, - - Estimates Base - Male; 18 years and over                                |
| est4_year_sex2_age18plus  | April 1, - - Estimates Base - Female; 18 years and over                              |
| est7_year_sex0_age18plus  | Population Estimate (as of July 1) - - - Both Sexes; 18 years and over               |
| est7_year_sex1_age18plus  | Population Estimate (as of July 1) - - - Male; 18 years and over                     |
| est7_year_sex2_age18plus  | Population Estimate (as of July 1) - - - Female; 18 years and over                   |
| cen4_year_sex0_age15to44  | April 1, - - Census - Both Sexes; 15 to 44 years                                     |
| cen4_year_sex1_age15to44  | April 1, - - Census - Male; 15 to 44 years                                           |
| cen4_year_sex2_age15to44  | April 1, - - Census - Female; 15 to 44 years                                         |
| est4_year_sex0_age15to44  | April 1, - - Estimates Base - Both Sexes; 15 to 44 years                             |
| est4_year_sex1_age15to44  | April 1, - - Estimates Base - Male; 15 to 44 years                                   |
| est4_year_sex2_age15to44  | April 1, - - Estimates Base - Female; 15 to 44 years                                 |
| est7_year_sex0_age15to44  | Population Estimate (as of July 1) - - - Both Sexes; 15 to 44 years                  |
| est7_year_sex1_age15to44  | Population Estimate (as of July 1) - - - Male; 15 to 44 years                        |
| est7_year_sex2_age15to44  | Population Estimate (as of July 1) - - - Female; 15 to 44 years                      |
| cen4_year_sex0_medage     | April 1, - - Census - Both Sexes; Median age (years)                                 |
| cen4_year_sex1_medage     | April 1, - - Census - Male; Median age (years)                                       |
| cen4_year_sex2_medage     | April 1, - - Census - Female; Median age (years)                                     |
| est4_year_sex0_medage     | April 1, - - Estimates Base - Both Sexes; Median age (years)                         |
| est4_year_sex1_medage     | April 1, - - Estimates Base - Male; Median age (years)                               |
| est4_year_sex2_medage     | April 1, - - Estimates Base - Female; Median age (years)                             |
| est7_year_sex0_medage     | Population Estimate (as of July 1) - - - Both Sexes; Median age (years)              |
| est7_year_sex1_medage     | Population Estimate (as of July 1) - - - Male; Median age (years)                    |
| est7_year_sex2_medage     | Population Estimate (as of July 1) - - - Female; Median age (years)                  |

## B01001
SEX BY AGE

Universe: Total population

Although the American Community Survey (ACS) produces population, demographic and housing unit estimates, it is the Census Bureau's Population Estimates Program that produces and disseminates the official estimates of the population for the nation, states, counties, cities, and towns and estimates of housing units for states and counties.


Supporting documentation on code lists, subject definitions, data accuracy, and statistical testing can be found on the American Community Survey website in the Technical Documentation section.

Sample size and data quality measures (including coverage rates, allocation rates, and response rates) can be found on the American Community Survey website in the Methodology section.


Source:  U.S. Census Bureau, 2013-2017 American Community Survey 5-Year Estimates


Explanation of Symbols:An '\*' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.
An '-' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.
An '-' following a median estimate means the median falls in the lowest interval of an open-ended distribution.
An '+' following a median estimate means the median falls in the upper interval of an open-ended distribution.
An '\*\*\*' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.
An '*****' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate. 
An 'N' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.
An '(X)' means that the estimate is not applicable or not available.


Data are based on a sample and are subject to sampling variability. The degree of uncertainty for an estimate arising from sampling variability is represented through the use of a margin of error. The value shown here is the 90 percent margin of error. The margin of error can be interpreted roughly as providing a 90 percent probability that the interval defined by the estimate minus the margin of error and the estimate plus the margin of error (the lower and upper confidence bounds) contains the true value. In addition to sampling variability, the ACS estimates are subject to nonsampling error (for a discussion of nonsampling variability, see Accuracy of the Data).  The effect of nonsampling error is not represented in these tables.


While the 2013-2017 American Community Survey (ACS) data generally reflect the February 2013 Office of Management and Budget (OMB) definitions of metropolitan and micropolitan statistical areas; in certain instances the names, codes, and boundaries of the principal cities shown in ACS tables may differ from the OMB definitions due to differences in the effective dates of the geographic entities.


Estimates of urban and rural populations, housing units, and characteristics reflect boundaries of urban areas defined based on Census 2010 data. As a result, data for urban and rural areas from the ACS do not necessarily reflect the results of ongoing urbanization.


