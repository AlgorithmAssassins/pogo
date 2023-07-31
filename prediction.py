import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

reg = LinearRegression()
teams = pd.read_csv("teams.csv")
teams = teams[["team", "country", "year", "athletes", "age", "prev_medals", "medals"]]
teams.corr()["medals"]
sns.lmplot(x='athletes',y='medals',data=teams,fit_reg=True, ci=None) 
sns.lmplot(x='age', y='medals', data=teams, fit_reg=True, ci=None) 
teams.plot.hist(y="medals")
teams[teams.isnull().any(axis=1)].head(20)
teams = teams.dropna()
train = teams[teams["year"] < 2012].copy()
test = teams[teams["year"] >= 2012].copy()
predictors = ["athletes", "prev_medals"]
reg.fit(train[predictors], train["medals"])
predictions = reg.predict(test[predictors])
test["predictions"] = predictions
test.loc[test["predictions"] < 0, "predictions"] = 0
test["predictions"] = test["predictions"].round()
error = mean_absolute_error(test["medals"], test["predictions"])
teams.describe()["medals"]
test["predictions"] = predictions
test[test["team"] == "USA"]
test[test["team"] == "IND"]
errors = (test["medals"] - predictions).abs()
error_by_team = errors.groupby(test["team"]).mean()
medals_by_team = test["medals"].groupby(test["team"]).mean()
error_ratio =  error_by_team / medals_by_team 
error_ratio = error_ratio[np.isfinite(error_ratio)]
error_ratio.plot.hist()
error_ratio.sort_values()