import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Lasso,Ridge,LinearRegression


# def myMLModel():
  
#   data = pd.read_csv('data.csv', header=0)
#   data.fillna(method='ffill', inplace= True)

#   X = data[["CO(GT)","PT08.S1(CO)","C6H6(GT)","PT08.S2(NMHC)","NOx(GT)","PT08.S3(NOx)","NO2(GT)","PT08.S4(NO2)","PT08.S5(O3)","T","AH"]]
#   y = data[["RH"]]
#   X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3)

#   reg=LinearRegression()
#   reg.fit(X_train, y_train)

#   y_pred=reg.predict(X_test)
#   acc_score = r2_score(y_test,y_pred)*100

#   return(data,y_pred, acc_score)

def doUserTesting(row,result):
  data = pd.read_csv('https://raw.githubusercontent.com/heetmiyani/AQI/main/Heet/data.csv', header=0)
  data.fillna(method='ffill', inplace= True)

  X = data[["CO(GT)","PT08.S1(CO)","C6H6(GT)","PT08.S2(NMHC)","NOx(GT)","PT08.S3(NOx)","NO2(GT)","PT08.S4(NO2)","PT08.S5(O3)","T","AH"]]
  y = data[["RH"]]

  if result == "Polynomial Regression":
    polyFeatures = PolynomialFeatures().fit(X)
    polyFeaturesXtrain = polyFeatures.transform(X)


    X_train,X_test,y_train,y_test = train_test_split(polyFeaturesXtrain,y,test_size=0.2,random_state=0)


    #X_test = X_test.iloc[:-1]
    #X_test.loc[len(X_test)] = row


    


    scaler = MinMaxScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)


    

    reg=LinearRegression()
    reg.fit(X_train, y_train)

    y_pred=reg.predict(X_test)
    acc_score = r2_score(y_test,y_pred)*100

    row=polyFeatures.transform([np.array(row)])

    # pred = y_pred[-1]

    scaled_row=scaler.transform(row)
    pred= reg.predict(scaled_row)[0]

    return(data,pred, acc_score)

  if result == "Ridge Regression":
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
    
    scaler = MinMaxScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    reg=Ridge()
    reg.fit(X_train, y_train)

    y_pred=reg.predict(X_test)
    acc_score = r2_score(y_test,y_pred)*100

    #pred = y_pred[-1]
    scaled_row=scaler.transform([np.array(row)])
    pred= reg.predict(scaled_row)[0]

    return(data,pred, acc_score)


  if result == "Lasso Regression":
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
    
    scaler = MinMaxScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    reg=Lasso()
    reg.fit(X_train, y_train)

    y_pred=reg.predict(X_test)
    acc_score = r2_score(y_test,y_pred)*100

    #pred = y_pred[-1]
    scaled_row=scaler.transform([np.array(row)])
    pred= reg.predict(scaled_row)[0]
    return(data,pred, acc_score)

  if result == "Linear Regression":
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
    
    scaler = MinMaxScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    reg=LinearRegression()
    reg.fit(X_train, y_train)

    y_pred=reg.predict(X_test)
    acc_score = r2_score(y_test,y_pred)*100

    #pred = y_pred[-1]
    scaled_row=scaler.transform([np.array(row)])
    pred= reg.predict(scaled_row)[0]
    return(data,pred, acc_score)

