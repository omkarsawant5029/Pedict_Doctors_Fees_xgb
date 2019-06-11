import numpy as np
from cleaning import cleaning
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns

file_name = 'Final_Train.xlsx'
df, X_train, X_test, y_train, y_test, X, y = cleaning(file_name)


''' Model '''
regressor = xgb.XGBRegressor()

regressor.fit(X_train, y_train)
train_predictions = regressor.predict(X_train)

test_predictions = regressor.predict(X_test)


'''
Performance
'''

def rmsle(y_pred,y_test) :
    error = np.square(np.log10(y_pred +1) - np.log10(y_test +1)).mean() ** 0.5
    Acc = 1 - error
    return Acc
print(rmsle(train_predictions, y_train))
print(rmsle(test_predictions, y_test))

rmse_train = np.sqrt(mean_squared_error(y_train, train_predictions))
print("RMSE train: %f" % (rmse_train))
rmse = np.sqrt(mean_squared_error(y_test, test_predictions))
print("RMSE test: %f" % (rmse))

cv_results = cross_val_score(regressor,X,y,scoring='neg_mean_squared_error',cv=5)
avg_cv_result = np.mean((cv_results*-1)**0.5)