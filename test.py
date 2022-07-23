my_list = list(map(int, input("Type number with space: ").split()))
max = my_list[0]
min = my_list[0]
for i in my_list:
    if i> max:
        max=i
    if i<min:
        min=i
print("The Maximum Number is:", max)
print("The Minimum Number is:", min)

