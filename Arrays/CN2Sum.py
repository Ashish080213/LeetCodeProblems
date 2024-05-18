def twoSum(arr, target, n):
    save = {}
    send = []
    for i, num in enumerate(arr):
        if target - num in save and save[target - num] > 0:
            send.append([arr[i],  target - num])
            save[target - num] -= 1
        else:
            if num in save:
                save[num] += 1
            else:
                save[num] = 1
    if len(send) == 0:
        return [[-1, -1]]
    else:
        return send

def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)