import pandas

df = pandas.read_csv('AAL.csv')
datesList = list(df['date'].values)
openPricesList = list(df['open'].values)
volumeList = list(df['volume'].values)

JSfile = open("chartdataPython.js", "w")
JSfile.write("var dataLabels = " + str(datesList) + ";\n") 
JSfile.write("var volumeData = " + str(volumeList) + ";\n")
JSfile.write("var priceData = " + str(openPricesList) + ";\n")
 
JSfile.close() 
