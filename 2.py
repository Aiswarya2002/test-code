def findOcccurance(string, c):
    count = 0 
    for i in string:
        if i == c:
            count += 1 
    return count 

inp1 = input()
inp2 = input()
count = findOcccurance(inp1, inp2[-1])
print(count)