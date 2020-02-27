def main():
    n = int(input())
    id = []
    locktime = []
    unlocktime = []
    unlocked = 0
    locked = 0
    for i in range(n):
        m = input().split()
        id.append(m[0])
        unlocktime.append(m[1].split(':'))
        locktime.append(m[2].split(':'))

    for i in range(1,len(locktime)):
        if int(locktime[locked][0]) < int(locktime[i][0]):
            locked = i
        else:
            if int(locktime[locked][0]) == int(locktime[i][0]):
                if int(locktime[locked][1]) < int(locktime[i][1]):
                    locked = i
                else:
                    if int(locktime[locked][1]) == int(locktime[i][1]):
                        if int(locktime[locked][2]) < int(locktime[i][2]):
                            locked = i

    for i in range(1,len(unlocktime)):
        if int(unlocktime[unlocked][0]) > int(unlocktime[i][0]):
            unlocked = i
        else:
            if int(unlocktime[unlocked][0]) == int(unlocktime[i][0]):
                if int(unlocktime[unlocked][1]) > int(unlocktime[i][1]):
                    unlocked = i
                else:
                    if int(unlocktime[unlocked][1]) == int(unlocktime[i][1]):
                        if int(unlocktime[unlocked][2]) > int(unlocktime[i][2]):
                            unlocked = i

    print(id[unlocked],id[locked])


if __name__ == '__main__':
    main()