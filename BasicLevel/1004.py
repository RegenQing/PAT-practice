def main():
    n = int(input())
    best = []
    worst = []
    for i in range(n):
        grade = [x for x in str(input()).split()]
        if i == 0:
           best = grade
           worst = grade
        else:
            if int(grade[2]) > int(best[2]):
                best = grade
            elif int(grade[2]) < int(worst[2]):
                    worst = grade
    print(best[0]+' '+best[1])
    print(worst[0]+' '+worst[1])

if __name__ == '__main__':
    main()