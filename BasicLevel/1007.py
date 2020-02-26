import time
def prime(num):
    flag = [1]*(num+1)
    flag[0] = flag[1] = 0
    result = []
    for i in range(2,num+1):
        if flag[i]:
            result.append(i)
            p = i
            while p*i <= num:
                flag[p*i] = 0
                p += 1
    return result

def main():
    num = int(input())
    start = time.time()
    count = 0
    result = prime(num)
    for i in range(len(result)-1):
        if result[i+1] - result[i] == 2:
            count += 1
    print(count)
    end = time.time()
    print(end-start)
if __name__ == '__main__':
    main()


