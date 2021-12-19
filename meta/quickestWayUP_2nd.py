class Record:  # to keep record of where we are and how many steps

    def __init__(self, curr=0, steps=0):
        self.curr = curr
        self.steps = steps


def minSteps(arr, n):  # bfs
    vis = [0] * n
    vis[0] = 1  # we're on first block i.e. first block visited
    que = []
    que.append(Record())  # initializes position and steps to 0
    obj = Record()
    while len(arr):
        obj = que.pop(0)  # get current position and steps
        cur = obj.curr
        if cur == 99:
            break
        tmp = cur + 1
        while tmp <= cur + 6 and tmp <= 99:
            if not vis[tmp]:
                a = Record()
                a.steps = obj.steps + 1  # increase 1 step in previous tally
                vis[tmp] = 1
                if arr[tmp] == -1:
                    a.curr = tmp
                else:
                    a.curr = arr[tmp]
                que.append(a)
            tmp += 1

    return obj.steps


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        li = [-1] * 100
        n = int(input())
        for _ in range(n):
            a, b = map(int, input().split())
            li[a - 1] = b - 1
        m = int(input())
        ls = []
        ll = []
        flag = 0
        ma = -99
        for _ in range(m):
            a, b = map(int, input().split())
            ll.append(b)
            ls.append(a)
            li[a - 1] = b - 1
        for i in range(2, 94):  # search if 6 consecutive snakes are present
            if all(j in ls for j in range(i, i + 6)):
                ma = max([k for k in range(i, i + 6)])
        for i in range(ma + 1, 99):  # then search if any ladder reaches beyond those 6 consecutive snakes
            if i in ll:
                flag = 1
        if flag == 0:
            print("-1")
        else:
            print(minSteps(li, 100))