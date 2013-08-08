def revert(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

for char in revert("afeiainina"):
    print(char)
