def main():
    a = list(map(float,input().split()))
    dict1 = {}
    for i in range(1,len(a),2):
        dict1[int(a[i])] = a[i+1]
    b = list(map(float,input().split()))
    dict2 = {}
    for j in range(1,len(b),2):
        dict2[int(b[j])] = b[j+1]
    res = {}
    for i in dict1:
        for j in dict2:
            if (i+j) in res.keys():
                res[i+j] += dict1[i]*dict2[j]
            else:
                res[i+j] = dict1[i]*dict2[j]
    key = sorted(res.keys(),reverse=True)
    ans = str(len(res))
    for i in res:
        if res[i] != 0:
            ans = ans +' '+str(i)+' '+'{:.1f}'.format(res[i])
    print(ans)

if __name__ == '__main__':
    main()
