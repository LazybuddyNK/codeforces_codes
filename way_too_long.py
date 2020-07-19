n = int(input())

l = [ input() for i in range(n)]

def word(x):
    if len(x) > 10:
            s = list(i for i in x)
            lg = len(s) - 2
            r = str(s[0] + str(lg) + s[-1])
            return r

    else:
        return x


for j in range(0, len(l)):
    print(word(l[j]))