numbers=[2,3,1,4,5,8,3,8,2,7]
unique_number=[]
for number in numbers:  # traverse

    if number not in numbers:
        numbers.append(number)
    for x in unique_number:
        print(x)
