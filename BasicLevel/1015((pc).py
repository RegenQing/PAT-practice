def res(m,n,de,cai):
    grade = 100
    if de < m or cai < m:
         grade = 0
    else:
        if de >= n and cai >= n:
             grade = 1
        elif de >= n and cai < n:
             grade = 2
        elif de < n and cai < n and de >= cai:
            grade = 3
        else:
            grade = 4
    return grade

def sor(list1):
    for q in range(1,len(list1)//3):
        for i in range(1,len(list1)//3-q+1):
            if list1[3*i-2]+list1[3*i-1] < list1[3*i+1]+list1[3*i+2]:
                (list1[3 * i - 3], list1[3 * i - 2], list1[3 * i - 1], list1[3 * i], list1[3 * i + 1],
                 list1[3 * i + 2]) = (
                list1[3 * i], list1[3 * i + 1], list1[3 * i + 2], list1[3 * i - 3], list1[3 * i - 2],
                list1[3 * i - 1])
            elif list1[3*i-2]+list1[3*i-1] == list1[3*i+1]+list1[3*i+2]:
                if list1[3*i-2] < list1[3*i+1]:
                    (list1[3 * i - 3], list1[3 * i - 2], list1[3 * i - 1], list1[3 * i], list1[3 * i + 1],
                     list1[3 * i + 2]) = (list1[3 * i], list1[3 * i + 1], list1[3 * i + 2], list1[3 * i - 3], list1[3 * i - 2],
                           list1[3 * i - 1])
                elif list1[3*i-2] == list1[3*i+1] and list1[3*i-3] > list1[3*i]:
                    (list1[3 * i - 3], list1[3 * i - 2], list1[3 * i - 1], list1[3 * i], list1[3 * i + 1],
                     list1[3 * i + 2]) = (list1[3 * i], list1[3 * i + 1], list1[3 * i + 2], list1[3 * i - 3], list1[3 * i - 2],
                           list1[3 * i - 1])

    return list1

def main():
    (num,m,n) = (int(x) for x in input().split())
    inf = []
    id = []
    de = []
    cai = []
    res1 = []
    res2 = []
    res3 = []
    res4 = []
    for i in range(num):
        inf = [int(x) for x in input().split()]
        id.append(inf[0])
        de.append(inf[1])
        cai.append(inf[2])
        if res(m,n,de[i],cai[i]) == 0:
            num -= 1
        elif res(m,n,de[i],cai[i]) == 1:
            res1 += [id[i],de[i],cai[i]]
        elif res(m,n,de[i],cai[i]) == 2:
            res2 += [id[i],de[i],cai[i]]
        elif res(m,n,de[i],cai[i]) == 3:
            res3 += [id[i],de[i],cai[i]]
        elif res(m,n,de[i],cai[i]) == 4:
            res4 += [id[i],de[i],cai[i]]
    print(num)
    for i in range(0,len(res1),3):
        print(' '.join(map(str,sor(res1)[i:i+3])))
    for i in range(0,len(res2),3):
        print(' '.join(map(str, sor(res2)[i:i + 3])))
    for i in range(0,len(res3),3):
        print(' '.join(map(str, sor(res3)[i:i + 3])))
    for i in range(0, len(res4), 3):
        print(' '.join(map(str, sor(res4)[i:i + 3])))
if __name__ == '__main__':
    main()