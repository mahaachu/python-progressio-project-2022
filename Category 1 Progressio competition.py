import numpy
import matplotlib.pyplot as plt
x = [2,3,7,8,9,11,13,15,16,19,20,27,38,46]
y = [5,6,7,8,9,10,11,12,13,14,21,29,38,46]
mymodel = numpy.poly1d(numpy.polyfit(x, y,100))
myline = numpy.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
