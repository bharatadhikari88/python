import quandl
import math
import numpy

df = quandl.get('WIKI/GOOG')
x = numpy.array(df['High'])
y = numpy.array(df['Low'])

df["Shift"] =df['High'].shift(periods=10, fill_value=0, axis="index")

df['ShiftN'] = df['High'].shift(periods=-10, fill_value=0, axis="index")
out = (df[['High', "Shift", "ShiftN"]])

print(out)
