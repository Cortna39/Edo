my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict.get('Vasya')}")
print(f"Not existing value: {my_dict.get('key1')}")
my_dict['Kamila']=1981
my_dict['Artem']= 1915
print(f"Deleted value: {my_dict.pop('Egor')}")
print(f"Modified dictionary:  ({my_dict}")
my_set = {1, '1', False,1, '1', False,}
print(f"Set: {my_set}")
my_set.update([1, 5, 10])
print(f"Modified set: {my_set}")
my_set.pop()
print(f"Modified once more set: {my_set}")