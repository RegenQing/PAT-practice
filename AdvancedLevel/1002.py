def main():
    A = {}
    B = {}
    x = input().split()
    for i in range(int(x[0])):
        A[int(x[1+i*2])] = float(x[2+i*2])
    x = input().split()
    for i in range(int(x[0])):
        B[int(x[1+i*2])] = float(x[2+i*2])
    a = sorted(list(A.keys()), reverse = True)
    b = sorted(list(B.keys()), reverse=True)
    c = sorted(list(set(a+b)),reverse = True)
    out = {}
    for x in c :
        if x in a and x in b:
            out[x] = A[x] + B[x]
        else:
            if x in a:
                out[x] = A[x]
            else:
                out[x] = B[x]
    result = []
    num = 0
    for x in c :
        if out[x] != 0:
            num = num + 1
            result.append(x)
            result.append('{:.1f}'.format(out[x]))
    result.insert(0,str(num))
    print(' '.join(map(str,result)))
if __name__ == '__main__':
    main()