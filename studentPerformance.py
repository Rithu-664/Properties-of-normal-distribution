import csv
import pandas as p
from pandas.core.algorithms import diff
import plotly.figure_factory as pff
import statistics
import plotly.graph_objects as go

df = p.read_csv('.\StudentsPerformance.csv')
writingScore = df["writingScore"].to_list()
count1 = 0
count2 = 0
count3 = 0

figure = pff.create_distplot([writingScore],["Score"])

mean = statistics.mean(writingScore)
print("Mean:",mean)

median = statistics.median(writingScore)
print("Median:",median)

mode = statistics.mode(writingScore)
print("Mode:",mode)

standardDeviation = statistics.stdev(writingScore)
print("Standard Deviation:",standardDeviation)

standardDeviation1Sum = mean + standardDeviation
standardDeviation1Difference = mean - standardDeviation

for j in writingScore:
    if j > standardDeviation1Difference and j < standardDeviation1Sum:
        count1 = count1 + 1

standardDeviation1Percentage = count1 / len(writingScore) * 100
print("Standard deviation 1 Percentage:",str(standardDeviation1Percentage) + "%")

standardDeviation2Sum = mean + (standardDeviation * 2)
standardDeviation2Difference = mean - (standardDeviation * 2)

for j in writingScore:
    if j > standardDeviation2Difference and j < standardDeviation2Sum:
        count2 = count2 + 1

standardDeviation2Percentage = count2 / len(writingScore) * 100
print("Standard deviation 2 Percentage:",str(standardDeviation2Percentage) + "%")

standardDeviation3Sum = mean + (standardDeviation * 3)
standardDeviation3Difference = mean - (standardDeviation * 3)

for j in writingScore:
    if j > standardDeviation3Difference and j < standardDeviation3Sum:
        count3 = count3 + 1

standardDeviation3Percentage = count3 / len(writingScore) * 100
print("Standard deviation 3 Percentage:",str(standardDeviation3Percentage) + "%")


figure.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))
figure.add_trace(go.Scatter(x=[standardDeviation1Sum,standardDeviation1Sum],y=[0,1],mode="lines",name="Standard Deviation 1 Sum"))
figure.add_trace(go.Scatter(x=[standardDeviation1Difference,standardDeviation1Difference],y=[0,1],mode="lines",name="Standard Deviation 1 Difference"))
figure.add_trace(go.Scatter(x=[standardDeviation2Sum,standardDeviation2Sum],y=[0,1],mode="lines",name="Standard Deviation 2 Sum"))
figure.add_trace(go.Scatter(x=[standardDeviation2Difference,standardDeviation2Difference],y=[0,1],mode="lines",name="Standard Deviation 2 Difference"))
figure.add_trace(go.Scatter(x=[standardDeviation3Sum,standardDeviation3Sum],y=[0,1],mode="lines",name="Standard Deviation 3 Sum"))
figure.add_trace(go.Scatter(x=[standardDeviation3Difference,standardDeviation3Difference],y=[0,1],mode="lines",name="Standard Deviation 3 Difference"))

figure.show()

