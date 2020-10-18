def sockpair(n, li):

    count = 0
    i = 0
    li.sort()

    while(i < n-1):
        if li[i] == li[i+1]:
            count = count + 1
            i += 2
        else:
            i += 1

    return count

li = list(map(int, input().rstrip().split()))
n = len(li)

pair = sockpair(n, li)
print(pair)