import random
from sklearn import linear_model

def f(x):
    return x*2

def sample(N):
    datapoints = []
    targets = []
    for n in range(N):
        x = random.randint(0,100) 
        datapoints.append([x])
        targets.append(f(x))
    return datapoints, targets




def run_regression(N):
    datapoints, targets = sample(N)
    reg = linear_model.LinearRegression()
    reg.fit(datapoints, targets)
    print("Fit: \n y= {}x + {}".format(int(reg.coef_), reg.intercept_))

