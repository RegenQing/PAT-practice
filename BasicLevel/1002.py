def main():
    n = int(input())
    sum = 0
    dict = {'0':'ling','1':'yi','2':'er','3':'san','4':'si','5':'wu','6':
        'liu','7':'qi','8':'ba','9':'jiu'}
    while n/10 > 0:
        sum += n%10
        n //= 10
    number = str(sum)
    for i in range(len(number)):
        print(dict[number[i]],end='' if i == len(number)-1 else' ')
if __name__ == '__main__':
    main()