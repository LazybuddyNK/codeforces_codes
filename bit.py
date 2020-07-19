
 
n = int(input())
 
l = [ input() for i in range(n)]
 
 
def bit(x):
 
    a = 0
 
    if x == "x++" or x == "++x":
        a += 1
    elif x == "x--" or x == "--x":
        a -= 1
    else:
        a = 0
 
    return a
 
s = 0
 
for j in range(0, len(l)):
    s += int(bit(l[j].lower()))
 
print(s)