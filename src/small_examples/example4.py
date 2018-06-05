def mul(x,y):
    if x == 0:
        return 0;
    else:
        m = mul(x-1,y)
        return m + y