def triangle():
    L = [1]
    LL = L
    while True:
        yield LL
        LL = []
        for x in range(len(L)+1):
            if x == 0 or x == len(L):
                num = 1
                LL.append(num)
            else:
                LL.append(L[x-1]+L[x])
         
        L = LL
