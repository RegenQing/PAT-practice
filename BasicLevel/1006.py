def convert(num):
    result = [0,0,0]
    i = 0
    while num/10 > 0:
        result[i] = num%10
        num //= 10
        i += 1
    print('B'*result[2]+'S'*result[1],end='')
    if result[0] != 0:
        for i in range(result[0]):
            print(i+1,end='')

def main():
    num = int(input())
    convert(num)

if __name__ == '__main__':
    main()
