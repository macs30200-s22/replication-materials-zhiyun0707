import statsmodels.api as sm
regression_analysis = pd.read_csv("regression_analysis.csv")
X = regression_analysis[['cases', 'poverty', 'education', 'gender', 'non-white', 'ethnicity']]
y = regression_analysis['income']
data = sm.add_constant(X)
model = sm.OLS(y, data).fit()
summary = model.summary()
print(summary)
