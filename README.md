# MACS 30200 Research Paper Initial Findings
Zhiyun Hu

## Research Project Overview

How does Covid-19, measured by state-level and county-level total cases divided by the total population impacted average personal income 
in 2020 in the United States? 
The research will use both state-level and county-level daily Covid-19 cases data 
(provided by New York Times public available dataset published on the GitHub) from January 21, 2020, 
through December 31, 2020, in 3220 counties from all 50 
states including Puerto Rico and the District of Columbia along 
with the United States Census Bureau published dataset for 2020 county-level 
population to calculate the proportion of people who have got Covid-19. 
Average personal income in 2020 was extracted from the United States 
Department of Commerce Bureau of Economic Analysis, Personal Income 
by County, Metro, and Other Areas.

## Initial Findings
My initial findings focus on state-level mulivariate regression analysis, with income as my dependent variable, covid-19 cases in each state as my
independent variable, with poverty (population below the state poverty level), education (population that have earned Bachelor's degree), gender
(female population), white (white population), black (black population), ethnicity (Hispanic population), laborforce (labor force population) as 
my control variables. 

<img width="727" alt="Screen Shot 2022-04-24 at 19 02 19" src="https://user-images.githubusercontent.com/89923088/165002433-d5140e34-f21a-43be-9575-0b2966c6283c.png">

As indicated by the OLS regression analysis, we can see that Covid-19 has a negative coefficient of -0.0099, which means that an additional case in 
a state will lead to $-0.0099 decrease in a average personal income in a state. In other words, per 1,000 increase in Covid-19 cases 
will lead to $9.9 dollar decrease in a state. However, as the p-value indicates, Covid-19 is not a statistically signifiant variable in the regression,
which reject my hypothesis that Covid-19 has a negative impact and is statistically significant in the regression model. 

## How Findings is relevant to my Research Question




