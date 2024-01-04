d1, d2, d3 = map(int, input().split())

path1, path2, path3, path4 = (
    d1 + d2 + d3,
    d1 + d1 + d2 + d2,
    d1 + d3 + d3 + d1,
    d2 + d3 + d3 + d2,
)


print(min(path1, path2, path3, path4))
