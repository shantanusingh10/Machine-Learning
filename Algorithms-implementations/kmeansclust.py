#K means Clustering for 150 flowers with randomly chosen petalLength,petalWidth,sepalLength,sepalWidth

import random

flowers = []  # flowers[petalLength,petalWidth,sepalLength,sepalWidth]

A1 = []
A2 = []
A3 = []

def MinEuclDist(a,b):
    return (a-b)**2

def Assign(c1,c2,c3,flowerV,flowerIndex):
    C1 = MinEuclDist(c1,flowerV)
    C2 = MinEuclDist(c2,flowerV)
    C3 = MinEuclDist(c3,flowerV)
    minimum = min(C1,C2,C3)
    global A1
    global A2
    global A3
    if minimum == C1:
        A1.append(flowerIndex)
    elif minimum == C2:
        A2.append(flowerIndex)
    elif minimum == C3:
        A3.append(flowerIndex)

#initialzing flowers 
for i in range(0,150):
    flowers += [[random.random(),random.random(),random.random(),random.random()]]
print("Starting Values - ")
print(flowers)

#choosing initial centers
while (True):
    centers = [random.randint(0,149),random.randint(0,149),random.randint(0,149)]      #Here need to make sure centers are different
    if(centers[0]!=centers[1] and centers[0]!=centers[2] and centers[1]!=centers[2]):
        break

print("Centers - ")
print(centers)

sumCenters = []

for i in range(0,3):
    sumCenters.append(0)
    for j in range(0,4):
        sumCenters[i] += flowers[centers[i]][j]
    sumCenters[i]/=4

s = []
for i in range(0,150):
    s.append(0)
    for j in range(0,4):
        s[i] += flowers[i][j]
    s[i]/=4

for i in range(0,150):
    if i not in centers:
        Assign(sumCenters[0],sumCenters[1],sumCenters[2],s[i],i)

print("First Clusters - ")
print(A1)
print(A2)
print(A3)

# updating centers for 1st time
mean = [[0],[0],[0]]
mean[0].append(0)
mean[0].append(0)
mean[0].append(0)
mean[1].append(0)
mean[1].append(0)
mean[1].append(0)
mean[2].append(0)
mean[2].append(0)
mean[2].append(0)

for i in A1:
    mean[0][0] += flowers[i][0]
    mean[0][1] += flowers[i][1]
    mean[0][2] += flowers[i][2]
    mean[0][3] += flowers[i][3]

for i in A2:
    mean[1][0] += flowers[i][0]
    mean[1][1] += flowers[i][1]
    mean[1][2] += flowers[i][2]
    mean[1][3] += flowers[i][3]

for i in A3:
    mean[2][0] += flowers[i][0]
    mean[2][1] += flowers[i][1]
    mean[2][2] += flowers[i][2]
    mean[2][3] += flowers[i][3]

for i in range(0,4):
    mean[0][i] /= len(A1)
    mean[1][i] /= len(A2)
    mean[2][i] /= len(A3)

# ---------------- END OF 1st Iteration ---------------------
k = 1
while (True):
    global k
    print("Iteration" + str(k) )
    k += 1
    a = 0
    b = 0
    c = 0
    for i in range(0,4):
        a += mean[0][i]
    for i in range(0,4):
        b += mean[1][i]
    for i in range(0,4):
        c += mean[2][i]
    a /= 4
    b /= 4
    c /= 4
    sumCenters[0] = a
    sumCenters[1] = b
    sumCenters[2] = c
    
    Len1 = len(A1)
    Len2 = len(A2)
    Len3 = len(A3)
    global A1
    A1 = list()
    global A2
    A2 = list()
    global A3
    A3 = list()
    
    for i in range(0,150):
        Assign(sumCenters[0],sumCenters[1],sumCenters[2],s[i],i)
    if(Len1 == len(A1) and Len2 == len(A2) and Len3 == len(A3)): # Stopping condition when there is no change in the size of clusters
        break
    print("Clusters After " + str(k))
    print(A1)
    print(A2)
    print(A3)
    
    #update the centers
    mean = [[0],[0],[0]]
    mean[0].append(0)
    mean[0].append(0)
    mean[0].append(0)
    mean[1].append(0)
    mean[1].append(0)
    mean[1].append(0)
    mean[2].append(0)
    mean[2].append(0)
    mean[2].append(0)

    for i in A1:
        mean[0][0] += flowers[i][0]
        mean[0][1] += flowers[i][1]
        mean[0][2] += flowers[i][2]
        mean[0][3] += flowers[i][3]

    for i in A2:
        mean[1][0] += flowers[i][0]
        mean[1][1] += flowers[i][1]
        mean[1][2] += flowers[i][2]
        mean[1][3] += flowers[i][3]

    for i in A3:
        mean[2][0] += flowers[i][0]
        mean[2][1] += flowers[i][1]
        mean[2][2] += flowers[i][2]
        mean[2][3] += flowers[i][3]

    for i in range(0,4):
        mean[0][i] /= len(A1)
        mean[1][i] /= len(A2)
        mean[2][i] /= len(A3)
    
print("Final Clusters - ")
print(A1)
print(A2)
print(A3)
