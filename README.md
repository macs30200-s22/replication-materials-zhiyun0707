# MACS 30200: How did Covid-19 impact average personal income in the United States on the state-level and county-level? 
Zhiyun Hu

[![DOI](https://zenodo.org/badge/483485911.svg)](https://zenodo.org/badge/latestdoi/483485911)

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

## Findings and Results

Overall distribution of the variables, which demonstrates right-skewed distribution: 
<img width="974" alt="Screen Shot 2022-05-22 at 20 46 02" src="https://user-images.githubusercontent.com/89923088/169728121-883ea962-0e22-4157-8ef8-b3f5a822cf0c.png">


###### state-level correlation & regression results
<img width="663" alt="Screen Shot 2022-06-03 at 18 33 35" src="https://user-images.githubusercontent.com/89923088/171966839-b5d79d39-8236-4af7-b4c8-992d931fc155.png">

The Spearman Rank Correlation test demonstrates a negative correlation between the COVID-19 cases and income on the stat-level (correlation coefficient = -0.045, P = 0.751), representing that there is a negative correlation between COVID-19 cases and personal income, while the p-value indicates that the correlation relationship is not statistically significant.



<img width="777" alt="Screen Shot 2022-06-03 at 18 33 43" src="https://user-images.githubusercontent.com/89923088/171966903-d4f12b3f-bd57-4c9a-8b8e-5cd41f1a2d81.png">

The Spearman Rank correlation and corresponding p-value for COVID-19 cases and income on the state-level is -0.213 and 0.001, representing that there is a negative correlation between COVID-19 cases and personal income, while the p-value indicates that the correlation relationship is statistically significant.


<img width="969" alt="Screen Shot 2022-05-22 at 20 44 09" src="https://user-images.githubusercontent.com/89923088/169727948-33a7f941-12ce-490c-8959-cc993f2ea41a.png">

From the table we can see that COVID-19 is not a statistically significant variable, that violates the initial assumption, while education, poverty, and non-white are three statistically significant variable. This may because of the data inaccuracy and because that state-level analysis does not tease out the differences compared to county-level analysis. 


###### county-level regression results

<img width="883" alt="Screen Shot 2022-05-22 at 20 44 02" src="https://user-images.githubusercontent.com/89923088/169727953-239ea3bb-4e3e-4701-a935-75653627a737.png">

From the table we can see that COVID-19 is a statistically significant variable, which is the same as the initial hypotheiss, while education, poverty, and non-white, white, and ethinicity are also statistically significant variables. 

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
