import csv
import pandas
import numpy
import statistics
from matplotlib import pyplot

f = open('anscombe.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow([" ", 'Dataset', "x", "y"])
csv_writer.writerow(["0", "I", "10", "8.04"])
csv_writer.writerow(["1", "I", "8", "6.95"])
csv_writer.writerow(["2", "I", "13", "7.58"])
csv_writer.writerow(["3", "I", "9", "8.81"])
csv_writer.writerow(["4", "I", "11", "8.33"])
csv_writer.writerow(["5", "I", "14", "9.96"])
csv_writer.writerow(["6", "I", "6", "7.24"])
csv_writer.writerow(["7", "I", "4", "4.26"])
csv_writer.writerow(["8", "I", "12", "10.84"])
csv_writer.writerow(["9", "I", "7", "4.82"])
csv_writer.writerow(["10", "I", "5", "5.68"])
file = pandas.read_csv('anscombe.csv')
Xvalues = []
Yvalues = []
Xvalues = file.x[0:11].values
print(Xvalues)
Yvalues = file.y[0:11].values
print(Yvalues)
Xmean = numpy.mean(Xvalues)
print(Xmean)
Ymean = numpy.mean(Yvalues)
print("{:.2f}".format(Ymean))
Xvariance = statistics.variance(Xvalues)
print("{:.2f}".format(Xvariance))
Yvariance = statistics.variance(Yvalues)
print("{:.2f}".format(Yvariance))

pyplot.title("anscombe dataset Ⅰ")
pyplot.xlabel("X")
pyplot.ylabel("Y")
pyplot.scatter(Xvalues, Yvalues)
pyplot.show()
