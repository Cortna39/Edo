first = int(input())
second = int(input())
third = int(input())
if first==second==third:
    print(3)
elif len(set([first,second,third])) == 2:
    print(2)
else:
    print(0)