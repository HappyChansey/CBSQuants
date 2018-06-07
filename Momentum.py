import numpy as np
import pandas as pd
import matplotlib

from datetime import datetime
from dateutil.relativedelta import relativedelta

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import rc

Indices = pd.read_excel(open('/Users/xudongsong/FinQuant/Indices.xlsx', 'rb'), sheet_name=0)
Indices.index = Indices['date']
Indices = Indices.iloc[:,1:len(Indices.columns)]

StartDate = datetime.strptime('2001-01-01', '%Y-%m-%d')
EndDate = datetime.strptime(Indices.index[-1], '%Y-%m-%d')

Principal = 10000

for i in range(0, len(Indices.index), 1):

        if datetime.strptime(Indices.index[i], '%Y-%m-%d')<StartDate:
            ind = i
        else:
            break

Value = []
ValueSPY = []
Value.append(Principal)
ValueSPY.append(Principal)

Option = []
MonthlyReturn = []

Time = []
Time.append(StartDate)

while ind < len(Indices.index)-1:


    Momentum_SP500 = (Indices.iloc[ind,0]/Indices.iloc[ind-6,0]-1)/3+(Indices.iloc[ind,0]/Indices.iloc[ind-3,0]-1)/3+(Indices.iloc[ind,0]/Indices.iloc[ind-1,0]-1)/3

    Momentum_SmallCap = (Indices.iloc[ind,1]/Indices.iloc[ind-6,1]-1)/3+(Indices.iloc[ind,1]/Indices.iloc[ind-3,1]-1)/3+(Indices.iloc[ind,1]/Indices.iloc[ind-1,1]-1)/3


    if Momentum_SP500 > Momentum_SmallCap:
        if Momentum_SP500 > 0:
            option = 0
        else:
            option = 2
    else:
        if Momentum_SmallCap > 0:
            option = 1
        else:
            option = 2

    Option.append(option)

    # Backtest


    ind = ind+1

    Value.append(Value[-1]*Indices.iloc[ind,option]/Indices.iloc[ind-1,option])
    ValueSPY.append(ValueSPY[-1]*Indices.iloc[ind,0]/Indices.iloc[ind-1,0])

    Time.append(datetime.strptime(Indices.index[ind], '%Y-%m-%d'))

    MonthlyReturn.append(Indices.iloc[ind,0]/Indices.iloc[ind-1,0]-1)

plt.plot(Time, Value, Time, ValueSPY)
plt.xlabel('Time')
plt.ylabel('Value')
# plt.yscale('log')
plt.show()

print(ValueSPY[-2])
print(Value[-2])

dfghjkl




Interval_End = StartDate
Interval_Begin1 = Interval_End - relativedelta(months=1)
Interval_Begin3 = Interval_End - relativedelta(months=3)
Interval_Begin6 = Interval_End - relativedelta(months=6)

RebaInterval = 1

Value = []
Option = []
Value.append(Principal)

Time = []
Time.append(StartDate)

while Interval_End < EndDate:

    for i in range(0, len(Indices.index), 1):

        if datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_Begin6:
            ind_6 = i+1
        if  datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_Begin3:
            ind_3 = i+1
        if  datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_Begin1:
            ind_1 = i+1

        if  datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_End:
            ind_end = i+1
        else:
            break


    Momentum_SP500 = (Indices.iloc[ind_end,0]/Indices.iloc[ind_6,0]-1)/3+(Indices.iloc[ind_end,0]/Indices.iloc[ind_3,0]-1)/3+(Indices.iloc[ind_end,0]/Indices.iloc[ind_1,0]-1)/3

    Momentum_SmallCap = (Indices.iloc[ind_end,1]/Indices.iloc[ind_6,1]-1)/3+(Indices.iloc[ind_end,1]/Indices.iloc[ind_3,1]-1)/3+(Indices.iloc[ind_end,1]/Indices.iloc[ind_1,1]-1)/3


    if Momentum_SP500 > Momentum_SmallCap:
        if Momentum_SP500 > 0:
            option = 0
        else:
            option = 2
    else:
        if Momentum_SmallCap > 0:
            option = 1
        else:
            option = 2

    Option.append(option)
    # Backtest

    for i in range(0, len(Indices.index), 1):

        if  datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_End + relativedelta(months=RebaInterval):
            bt_end = i+1
        else:
            break

    for i in range(ind_end, bt_end, 1):
        Value.append(Value[-1]*Indices.iloc[i,option]/Indices.iloc[i-1,option])
        Time.append(datetime.strptime(Indices.index[i], '%Y-%m-%d'))

    Interval_End = Interval_End + relativedelta(months=RebaInterval)
    Interval_Begin1 = Interval_End - relativedelta(months=1)
    Interval_Begin3 = Interval_End - relativedelta(months=3)
    Interval_Begin6 = Interval_End - relativedelta(months=6)

"""
plt.plot(Indices.iloc[:,0].values)
plt.xlabel('Time')
plt.ylabel('SP500')
plt.show()

plt.plot(Indices.iloc[:,1].values)
plt.xlabel('Time')
plt.ylabel('Small Cap')
plt.show()

plt.plot(Indices.iloc[:,2].values)
plt.xlabel('Time')
plt.ylabel('Gov Bond')
plt.show()
"""

Time1 = Time
Value1 = Value

StartDate = datetime.strptime('2001-01-01', '%Y-%m-%d')
EndDate = datetime.strptime(Indices.index[-1], '%Y-%m-%d')

Principal = 10000

Interval_End = StartDate
Interval_Begin1 = Interval_End - relativedelta(months=1)
Interval_Begin3 = Interval_End - relativedelta(months=3)
Interval_Begin6 = Interval_End - relativedelta(months=6)

RebaInterval = 1

Value = []
Value.append(Principal)

Time = []
Time.append(StartDate)

while Interval_End < EndDate:

    for i in range(0, len(Indices.index), 1):

        if datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_Begin6:
            ind_6 = i+1
        if  datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_Begin3:
            ind_3 = i+1
        if  datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_Begin1:
            ind_1 = i+1

        if  datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_End:
            ind_end = i+1
        else:
            break


    Momentum_SP500 = (Indices.iloc[ind_end,0]/Indices.iloc[ind_6,0]-1)+(Indices.iloc[ind_end,0]/Indices.iloc[ind_3,0]-1)+(Indices.iloc[ind_end,0]/Indices.iloc[ind_1,0]-1)

    Momentum_SmallCap = (Indices.iloc[ind_end,1]/Indices.iloc[ind_6,1]-1)+(Indices.iloc[ind_end,1]/Indices.iloc[ind_3,1]-1)+(Indices.iloc[ind_end,1]/Indices.iloc[ind_1,1]-1)


    if Momentum_SP500 > Momentum_SmallCap:
        if Momentum_SP500 > 0:
            option = 0
        else:
            option = 2
    else:
        if Momentum_SmallCap > 0:
            option = 1
        else:
            option = 2

    # Backtest

    for i in range(0, len(Indices.index), 1):

        if  datetime.strptime(Indices.index[i], '%Y-%m-%d')<Interval_End + relativedelta(months=RebaInterval):
            bt_end = i+1
        else:
            break

    for i in range(ind_end, bt_end, 1):
        Value.append(Value[-1]*Indices.iloc[i,option]/Indices.iloc[i-1,option])
        Time.append(datetime.strptime(Indices.index[i], '%Y-%m-%d'))

    Interval_End = Interval_End + relativedelta(months=RebaInterval)
    Interval_Begin1 = Interval_End - relativedelta(months=1)
    Interval_Begin3 = Interval_End - relativedelta(months=3)
    Interval_Begin6 = Interval_End - relativedelta(months=6)

plt.plot(Time, Value, Time1, Value1)
plt.xlabel('Time')
plt.ylabel('Value')
# plt.yscale('log')
plt.show()

print(Value[-1])
print(Option)

AnnualValue = []
AnnualValue.append(Principal)

CalDate = StartDate + relativedelta(years=1)

while CalDate < datetime.strptime(Indices.index[-1], '%Y-%m-%d'):

    for i in range(0, len(Time), 1):
        if Time[i]<CalDate:
            ind = i+1
        else:
            break

    AnnualValue.append(Value[ind])

    CalDate = CalDate + relativedelta(years=1)

AveReturn = (Value[ind]/Principal)**(1/(float(15)))-1

AnnualReturn = []

for i in range(1, len(AnnualValue), 1):

    AnnualReturn.append(AnnualValue[i]/AnnualValue[i-1]-1)

# print(AnnualReturn)

# SharpeRatio = 
# Sortino
# Max draw down
