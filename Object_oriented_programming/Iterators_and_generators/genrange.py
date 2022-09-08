def genrange(start:int,end:int):
    for x in range(start,end + 1):
        yield x

print(list(genrange(1,10)))