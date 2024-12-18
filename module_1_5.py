immutable_var = (1, 2, 'a', 'b',True)
print(immutable_var)
try:
    immutable_var[0]=3
except:
    print('Кортежи нельзя изменять. В них содержится не сам список, а ссылка на него.')
mutable_list = [1, 2, 'a', 'b', False]
print(mutable_list)
mutable_list[0]='Базинго'
print(mutable_list)

