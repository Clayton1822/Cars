import random
from math import sqrt

x = {
   'A':[('B',0.1,5),('C',0.9,6)],
   'B':[('D',0.2,4),('E',0.8,7)],
   'C':[('E',0.3,4),('F',0.7,6)],
   'D':[('G',0.1,4),('H',0.9,6)],
   'E':[('H',0.4,6),('I',0.6,4)],
   'F':[('I',0.2,3),('J',0.8,7)],
   'G':[('K',1.0,4)],
   'H':[('K',0.3,4),('L',0.7,8)],
   'I':[('L',0.5,6),('M',0.5,4)],
   'J':[('M',1.0,5)],
   'K':[('N',1.0,4)],
   'L':[('N',0.4,5),('O',0.6,6)],
   'M':[('O',1.0,5)],
   'N':[('P',1.0,5)],
   'O':[('P',1.0,5)],
}

def SimNextT(c):
   r = random.random()
   if r<x[c][0][1]:
       return (x[c][0][0], x[c][0][2])
   else:
       return (x[c][-1][0], x[c][-1][2])

def SimOne():
   At, destination = 'A', 'P'
   Time = 0
   while At != destination:
       nxt , cost = SimNextT(At)
       At = nxt
       Time += cost
   return Time

def avg(arr):
   y = 0.0
   y = sum(arr)*1.0
   return y/len(arr)

def sqRoot(arr):
   mu=avg(arr)
   y = 0.0
   for x in arr:
       y += (x-mu)**2
   return sqrt(y/len(arr))

# simulate 10K cars
arr = []
for _ in range(10000):
   arr.append(SimOne())
print("1 run with 10,000 cars")
print("Average time: %.3f"%(avg(arr)))
print("Deviation: %.3f "%(sqRoot(arr)))

arr = []
for _ in range(10):
   arr2 = []
   for _ in range(10000):
       arr2.append(SimOne())
   arr.append(avg(arr2))
print("10 runs of 10,000 cars")
print("Average time: %.3f"%(avg(arr)))
print("Deviation: %.3f "%(sqRoot(arr)))


arr = []
for _ in range(100000):
   arr.append(SimOne())
print("1 run with 100,000 cars")
print("Average time: %.3f"%(avg(arr)))
print("Deviation: %.3f "%(sqRoot(arr)))