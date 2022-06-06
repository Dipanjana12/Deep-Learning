import matplotlib.pyplot as plt

# line 1 points
x1 = [3, 4, 5, 6, 7, 8, 10, 12, 15]
y1 = [65, 74 , 75, 64, 89, 90,96, 98, 99]
# plotting the line 1 points
plt.plot(x1, y1, label="Tomita 1")

x2 = [3, 4, 5, 6, 7, 8, 10, 12, 15]
y2 = [40, 64 , 60, 62, 79, 70,86, 90, 92]
# plotting the line 1 points
plt.plot(x2, y2, label="Tomita 2")

x3 = [3, 4, 5, 6, 7, 8, 10, 12, 15]
y3 = [20, 54 , 54.66, 60, 60.55, 70,86,88, 96]
# plotting the line 1 points
plt.plot(x3, y3, label="Tomita 3")

x4 = [3, 4, 5, 6, 7, 8, 10, 12, 15]
y4 = [33.33, 48 , 55, 55.65, 56.88, 62.90,92, 84, 76]
# plotting the line 1 points
plt.plot(x4, y4, label="Tomita 4")

x5 = [3, 4, 5, 6, 7, 8, 10, 12, 15]
y5 = [33.33, 38 , 35, 45.65, 56.88, 60.90, 86, 92, 93]
# plotting the line 1 points
plt.plot(x5, y5, label="Tomita 5")

x6 = [3, 4, 5, 6, 7, 8, 10, 12, 15]
y6 = [50, 68 , 75, 75.65, 76.88, 90.90, 86, 82, 83]
# plotting the line 1 points
plt.plot(x6, y6, label="Tomita 6")

x7 = [3, 4, 5, 6, 7, 8, 10, 12, 15]
y7 = [34.33, 39 , 33, 42.65, 56.88, 80, 86, 68, 87]
# plotting the line 1 points
plt.plot(x7, y7, label="Tomita 7")







# line 2 points
#x2 = [1, 2, 3]
#y2 = [4, 1, 3]
# plotting the line 2 points
#plt.plot(x2, y2, label="line 2")

# naming the x axis
plt.xlabel('k value')
# naming the y axis
plt.ylabel('average accuracy')
# giving a title to my graph
#plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()