

def change(x):
    return x + 10

thing = [change(x) for x in range(10)]
print(thing)