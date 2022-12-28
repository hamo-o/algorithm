# def square(n, cnt):
#     root = n**(1/2)
#     # 만약 루트 값이 정수라면 count 즉시 출력, 재귀 종료
#     if root == int(root):
#         print(cnt)
#         return
#
#     print(root, int(root), n - int(root)**2)
#     square(n - int(root)**2, cnt + 1)
#
#
# square(15663, 1)


def square(n, cnt):
    root = n**(1/2)
    i_root = int(root)
    # 만약 루트 값이 정수라면 재귀 종료
    if root == i_root:
        print(cnt)
        return

    for i in range(0, i_root//2):
        square(n - (i_root - i)**2, cnt + 1)


square(34567, 1)