x, y, z, t = map(float, input().split())

DTB = ((x + y) + z * 2 + t * 3) / 7

if DTB >= 8:
    print("GIOI")
elif DTB >= 6.5:
    print("KHA")
elif DTB >= 5:
    print("TRUNG BINH")
else:
    print("YEU")
