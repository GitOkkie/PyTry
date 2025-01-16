#!/usr/bin/env python3

def kaprekar(start):
    count=0
    n=start

    while n!=6174:

        s=f'{n:04d}'
        n1=''.join(sorted(s))
        n2=''.join(reversed(n1))
        n=int(n2)-int(n1)

        if n==start or n==0:
            return None
        else:
            count+=1

    return count

grid={}

for x in range(100):
    for y in range(100):
        grid[x,y] = kaprekar(x+100*y)

if __name__ == '__main__':

    for x,y in grid:
        print (x, y, " = ", grid[x,y])
