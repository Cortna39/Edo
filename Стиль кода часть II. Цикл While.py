my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while len(my_list)>0:
    x=my_list.pop(0)
    if x>0:
        print(x)
    elif x<0:
        break
    else:
        continue