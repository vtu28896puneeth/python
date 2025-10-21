import matplotlib.pyplot as plt

intervals = ['140-145', '145-150', '151-156', '157-162', '163-168', '168-173', '173-178', '179-184', '185-190', '190-195']
frequencies = [2, 5, 15, 31, 46, 53, 45, 28, 21, 4]

plt.bar(intervals, frequencies, edgecolor='red')
plt.xlabel('Height Intervals (cm)')
plt.ylabel('Frequency')
plt.title('Height Distribution Histogram')
plt.grid(True)
plt.show()
