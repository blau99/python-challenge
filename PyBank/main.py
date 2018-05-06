import os
import csv
import pandas as pd

csvpath = os.path.join("budget_data_2.csv")
with open(csvpath,'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    monthCount = 0
    totalRevenue = 0

    for row in csvreader:
        rowStr = ','.join(row)
        date,revenue = rowStr.split(',')
        revenue = int(revenue)

        monthCount = monthCount + 1
        totalRevenue = totalRevenue + revenue

    print("The total number of months included in the dataset is",monthCount)
    print("The total amount of revenue gained over the entire period is",totalRevenue)

df = pd.read_csv(csvpath)
df['Shifted'] = df['Revenue'].shift(1)
df['Change in Revenue'] = df['Revenue'] - df['Shifted']
avgRevChange = df['Change in Revenue'].mean()
maxRevChange = df['Change in Revenue'].max()
maxRevChange = df['Change in Revenue'].max()
row = df.loc[df["Change in Revenue"] == maxRevChange]
date = row['Date']
minRevChange = df['Change in Revenue'].min()
row2 = df.loc[df["Change in Revenue"] == minRevChange]
date2 = row['Date']

print("The average change in revenue between months over the entire period is",avgRevChange)
print("The greatest increase in revenue (date and amount) over the entire period is",maxRevChange)
print("The greatest decrease in revenue (date and amount) over the entire period is",minRevChange)

results = open("results.txt",'w')
results.write("The total number of months included in the dataset is "+str(monthCount)+"\n")
results.write("The total amount of revenue gained over the entire period is "+str(totalRevenue)+"\n")
results.write("The average change in revenue between months over the entire period is"+str(avgRevChange)+"\n")
results.write("The greatest increase in revenue (date and amount) over the entire period is "+str(maxRevChange)+"\n")
results.write(str(date)+"\n")
results.write("The greatest decrease in revenue (date and amount) over the entire period is " + str(minRevChange)+"\n")
results.write(str(date2))
