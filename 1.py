def convertNumber(num):
    val = 0
    offset = 1
    while num > 0:
        val += (num % 3) * offset
        offset *= 10 
        num //= 3 
    return val 

num = int(input())
result = convertNumber(num)
print(result)