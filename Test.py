# This is other python file
def hanoi(n, A, B, C):
    ############################################################
    # 1) If n is not equal to 1, then compute HANOI(n-1,A,C,B).
    ############################################################
    if n != 1:
        hanoi(n-1, A, C, B)
    ############################################################
    # 2) Move 1 disk from pole A to pole C.
    ############################################################
    C.append(A.pop())
    if len(C) > 1:
        assert C[-1] < C[-2], "Invalid Operation"
    ############################################################
    # 3) If n is not equal to 1, then compute HANOI(n-1,B,A,C).
    ############################################################
    if n != 1:
        hanoi(n-1, B, A, C)


#ori.list = [7,6,5,4,3,2,1]
count = 0
ori = list(range(22, 0, -1))
aux = []
dst = []

print('BEFORE. origen:', ori, 'Auxiliar:', aux, 'Destino:', dst)
hanoi(len(ori), ori, aux, dst)
print('AFTER.  origen:', ori, 'Auxiliar:', aux, 'Destino:', dst)