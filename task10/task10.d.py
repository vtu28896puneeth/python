import matplotlib.pyplot as plt

sizes = [35, 25, 25, 15]
mylabels = ['w', 'x', 'y', 'z']
myexplode = [0.2, 0, 0, 0]

plt.pie(sizes, labels=mylabels, explode=myexplode, shadow = True, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
