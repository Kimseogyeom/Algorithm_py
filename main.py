# 정렬 여부 검사 함수
def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i + 1]):
            isSorted = False;
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


def enqueue(queue, data):
    queue.append(data)


def dequeue(queue):
    if len(queue) == 0:
        print("큐가 비었음")
        return -1
    else:
        data = queue.pop(0)
        return data


def digit(d, k):
    temp = 1
    for i in range(1, k):
        temp *= 10
    d = d // temp
    d %= 10
    return d


# 기수정렬  함수
def radixSort(a, n, m, queue):
    for k in range(1, m + 1):
        for i in range(1, n + 1):
            kd = digit(a[i], k)
            enqueue(queue[kd], a[i])
        p = 0
        for i in range(10):
            while len(queue[i]) != 0:
                p += 1
                a[p] = dequeue(queue[i])


import random, time

# 배열 초기화 & 랜덤 데이터
M = 5
N = 200000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, 99999))
Q = []
for i in range(10):
    Q.append([])
print("짜증나")

# 실행 및 시간 측정
start_time = time.time()
radixSort(a, N, M, Q)
elapsed_time = time.time() - start_time
print('기수정렬 실행시간 (N=%d) : %0.3f' % (N, elapsed_time))
checkSort(a, N)