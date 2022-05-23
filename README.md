# MACS 30200: How did Covid-19 impact average personal income in the United States on the state-level and county-level? 
Zhiyun Hu

The code is written in Python 3.8.8 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository): 

```
pip install -r requirements.txt
```

## Step 1: Pre-process the data

###### state-level analysis
The data files that are used to conduct the regression analysis is stored in the file `regression data`.
The state Covid-19 cases data is named as `us-states.csv.`
The state income data is named as `income_state_clean.csv.`
The state control variables is named as `state_control_variable.csv`
Import the `state_level_regression_analysis.ipynb` section to reproduce the analysis. 

###### county-level analysis
The county level Covid-19 cases data is too large for upload, so please download the data from the following link: https://drive.google.com/file/d/1tX-JQJzQhEGoExx1wwarGyOTyOv3WgdR/view?usp=sharing

The county income data is named as `income_with_county.csv.`
The county control variables is named as `combine_data.csv`
Import the `county_level_regression_analysis.ipynb` section to reproduce the analysis. 


## Step 2: Run the regression

Import the `regression_analysis.py` and use the dataset `regression_analysis.csv` to run the regression analysis for state-level.
Similarly, change the dataset to `county_level_regression_analysis.csv` to run the regression analysis for county-level. 

## Research Project Overview

How does Covid-19, measured by state-level and county-level total cases, impacted average personal income in 2020 in the United States? 
Income is closely related to consumer spending, which constitutes a country's Gross Domestic Product (GDP), so understanding income and income inequality is important because it impacts a nation’s aggregate demand. Previous studies focused on demographic factors that affect income such as education, gender, marriage, race, and ethnicity. As COVID-19 pandemic broke out, the United States is one of the countries that had been affected significantly by the COVID-19, which accounted for over a quarter of the total cases around the globe. Even though researchers have analyzed the relationship between income and COVID-19, as most of them conducted the study in the initial stage of COVID-19 pandemic period, most of them used prediction modeling, few of them used official government data. The present study aims to explore the relationship between COVID-19 cases and the impact on average personal income in the United States through a cross-sectional regression model on the state-level and county-level in 2020, using dataset from United States Census for demographic factors and New York Times COVID-19 public shared GitHub dataset for COVID-19 cases. Through running regression with control variables of gender, race, ethnicity, education, and race, this study shows that on both the state and the county level, COVID-19 has a negative impact on personal income, that more COVID-19 cases in a region will lead to lower average personal income. In the OLS regression model, COVID-19 case is not statistically significant at the state level while is statistically significant at the county level. The government income support and lock down policy are effective as the dummy variable positive coefficient indicates. Due to data limitation, lack of the official data for the year 2021, this study does not address time-series or panel data analysis.

## Findings and Results

Overall distribution of the variables, which demonstrates right-skewed distribution: 
<img width="974" alt="Screen Shot 2022-05-22 at 20 46 02" src="https://user-images.githubusercontent.com/89923088/169728121-883ea962-0e22-4157-8ef8-b3f5a822cf0c.png">


###### state-level regression results
<img width="969" alt="Screen Shot 2022-05-22 at 20 44 09" src="https://user-images.githubusercontent.com/89923088/169727948-33a7f941-12ce-490c-8959-cc993f2ea41a.png">


###### county-level regression results

<img width="883" alt="Screen Shot 2022-05-22 at 20 44 02" src="https://user-images.githubusercontent.com/89923088/169727953-239ea3bb-4e3e-4701-a935-75653627a737.png">

This study aims to explore the relationship between COVID-19 cases and the impact on average personal income in the United States. The results show that on both the state and the county level, COVID-19 has a negative impact on personal income, that more COVID-19 cases in a region will lead to lower average personal income. In the OLS regression model, COVID-19 case is not statistically significant at the state level while is statistically significant at the county level, which contradicts to the original hypothesis that COVID-19 is a statistically significant variable both on the state-level and county-level. This study also incorporated the government role and the policy into consideration. To analyze how the state government played a role in reducing the COVID-19 spread and solve the increasing unemployment and salary cut, the two dummy variables: one on whether the state released additional stimulus check or not, one on the state has lock down policy or not during 2020 demonstrates that effective government policy could reduce the pandemic negative impact on per capita income.

## Cite my project

```
@misc{Hu2022,
  author = {Hu, Zhiyun.},
  title = {Covid-19 impact on average personal income in the United States on a state-level and county-level},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/macs30200-s22/replication-materials-zhiyun0707}}
  }
```
