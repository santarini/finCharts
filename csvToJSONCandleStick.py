import pandas
import time

df = pandas.read_csv('AAL.csv')
datesList = list(df['date'].values)
openPricesList = list(df['open'].values)
highPricesList = list(df['high'].values)
lowPricesList = list(df['low'].values)
closePricesList = list(df['close'].values)
volumeList = list(df['volume'].values)

JSfile = open("chartdataPythonCandle.js", "w")
JSfile.write(" var candleData = [")
for i in range(len(datesList)):
    JSfile.write("{o:" + str(openPricesList[i]) + ", h:" + str(highPricesList[i]) + ", l:" + str(lowPricesList[i]) + ", c:" + str(closePricesList[i]) + ", ")
    #convert date to 10am epoch stamp
    date_time = datesList[i].replace("-",".") + ' 00:00:00'
    pattern = '%Y.%m.%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    JSfile.write("t:" + str(epoch * 1000) + "},")

JSfile.write("]")

JSfile.close() 
