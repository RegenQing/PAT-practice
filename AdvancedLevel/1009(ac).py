def main():
    a = list(map(float,input().split()))
    dict1 = {}
    for i in range(1,len(a),2):
        dict1[int(a[i])] = a[i+1]
    b = list(map(float,input().split()))
    dict2 = {}
    for j in range(1,len(b),2):
        dict2[int(b[j])] = b[j+1]
    res = [[x,0] for x in range(2001)]
    for i in dict1:
        for j in dict2:
            res[i+j][1] += dict1[i]*dict2[j]
    ans = str(len([x for x in res if x[1] !=0]))
    for i in res[::-1]:
        if i[1] != 0:
            ans = ans +' '+str(i[0])+' '+'{:.1f}'.format(i[1])
    print(ans)

if __name__ == '__main__':
    main()
