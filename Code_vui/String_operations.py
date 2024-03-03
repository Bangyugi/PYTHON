import numpy as np

arr = np.array([10, 5, 3, 0, 1, 2])

min_val = 100005
index = 0
for i in range(len(arr)):
    if (arr[i]>0 and arr[i]<min_val):
        min_val=arr[i]
        index =i

print(min_val)
print(index)
