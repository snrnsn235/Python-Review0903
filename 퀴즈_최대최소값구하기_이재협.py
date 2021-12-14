num=[8,7,3,2,9,4,1,6,5]
max, min = 0, 10
for i in num:
    if max < i:
        max = i
    if min > i:
        min = i
print("최대값 : ", max)
print("최소값 : ", min)
