from cProfile import label
from tkinter.tix import InputOnly
from tkinter.ttk import LabeledScale
import matplotlib.pyplot as plt

input_values = range(1, 100)
squares = [x**2 for x in input_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(input_values, squares, c = squares, cmap=plt.cm.Blues, s=30) #scatter = dots
#ax.plot(input_values, squares, c = 'red', linewidth = 3) #plot = line

ax.set_title("Squares")
ax.set_xlabel("Numbers")
ax.set_ylabel("Squares of Numbers")

ax.axis([0, 110, 0, 12100])

#plt.savefig('squares_plot.png')
plt.show()