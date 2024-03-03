import numpy as np


Supply = np.array(list(map(int,input().split())))
Demand = np.array(list(map(int,input().split())))
Diliver_matrix = np.zeros((len(Supply),len(Demand)),dtype=int)
for i in range(3):
    Diliver_matrix[i] = list(map(int, input().split()))
# 39 12 20
# 24 33 62
# 4 3 6
# 5 2 7
# 8 3 5
matrix_1 = np.copy(Diliver_matrix)
res_matrix = np.zeros((len(Supply), len(Demand)), dtype=int)

for i in range(len(Supply)):
    for j in range(len(Demand)):
        if matrix_1[i][j] != 0:
            x = min([Demand[j], Supply[i]])
            res_matrix[i][j] = x
            Demand[j] -= x
            Supply[i] -= x
            if Supply[i] == 0:
                for j1 in range(3):
                    matrix_1[i][j1] = 0
            if Demand[j] == 0:
                for i1 in range(3):
                    matrix_1[i1][j] = 0

print("Phương án vận chuyển tối ưu:")
print(str(res_matrix).replace("  ", " ").replace("[ ", "["))

res = 0
for i in range(len(Supply)):
    for j in range(len(Demand)):
        res += Diliver_matrix[i][j] * res_matrix[i][j]

print("Tổng chi phí vận chuyển",res)

