
n = int(input())


def elep(x):

    if x % 5 == 0:
        a = x//5
    else:
        a = x//5 + 1

    return a

s = int(elep(n))

print(s)