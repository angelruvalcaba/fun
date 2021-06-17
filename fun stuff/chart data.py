import math
import statistics

tbl1 = [[-0.01, 0.02, 0.04], 
[0.22, 0.22, 0.25], 
[1.06, 1.14, 1.00], 
[2.15, 1.94, 2.06],
[6.96, 7.85, 7.93],
[10.3, 10.3, 11.0],
[16.8, 15.7, 18.6],
[18.4, 18.3, 17.3],
[19.9, 18.9, 19.5],
[21.0, 21.6, 20.0]]
means = []
sd = []
N = 4
for i in range(len(tbl1)):
	mean = sum(tbl1[i])/len(tbl1[i])
	means.append(mean)
	std = statistics.stdev(tbl1[i])
	sd.append(std)
print(sd)
print(means)
tbl2 = [[0.03, -0.02, 0.01],
[3.66, 3.8, 3.43],
[11.9, 10.8, 10.1],
[13.6, 13.3, 13.8],
[18.1, 19.5, 17.3],
[19.6, 17.6, 19.2],
[18.1, 21.2, 20.6],
[18.5, 21.9, 21.7],
[18.8,20.6, 19.4],
[20.4, 19.4, 18.6]]
means2 =[]
sd2 = []
for i in range(len(tbl2)):
	mean2 = sum(tbl2[i])/len(tbl2[i])
	means2.append(mean2)
	std2 = statistics.stdev(tbl2[i])
	sd2.append(std2)
print(sd2)
print(means2)