import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as fpx

myFile = pd.read_csv(~/pathTo/data/sample/)

print(myFile)
print(myFile.describe())

count = myFile.count()
theMean = myFile.mean()
minVals = myFile.min()
q1 = myFile.quantile(0.25)
q1 = myFile.quantile(0.50)
q1 = myFile.quantile(0.75)
maxVals = myFile.max()

numClicks = myFile[clicks] #column called "clicks" reporting number of misclicks
plt.hist(numClicks)
plt.show()

