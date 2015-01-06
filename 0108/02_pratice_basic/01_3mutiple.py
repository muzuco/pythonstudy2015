data = (2, 45, 55, 200, -100, 99, 37, 10284)
results=[]
for tmp in data:
    if tmp % 3 == 0:
        results.append(tmp)
print results
