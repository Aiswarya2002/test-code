vln = [1, 2, 5, 6, 8, 9]
v = [0, 1, 2, 5, 6, 8, 9]

n = int(input())
if n > 6:
    count = 7
    ce = 10
    while count <= n:
        isValid = True 
        value = ce
        while ce != 0:
            rem = ce % 10 
            if rem in v:
                ce = ce // 10
            else:
                isValid = False 
                break 
        if isValid:
            vln.append(value)
            count += 1
        ce = value + 1
    print(vln[-1])
else:
    print(vln[n-1])
    