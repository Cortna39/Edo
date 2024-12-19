def get_matrix( n:int, m:int , value:int)->list:
    matrix = []
    for x in range(n):
        matrix.append([])
        for z in range(m):
            matrix[-1].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)