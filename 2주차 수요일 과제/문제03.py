
nan_list = [list(map(int,input().split('\n'))) for i in range(0,9)]
print(*nan_list)
print(nan_list[2][0])
spy_nan=[]
print(len(nan_list))
for j in range(0, 8):
    if len(nan_list)>8:
        for i in range(0+j,8-j):
            print('안쪽',i)
            if nan_list[i][0]+nan_list[i+1][0] == 40:
                print('있는거?', nan_list[i][0] )
                spy_nan = nan_list.pop(i)
                spy_nan = nan_list.pop(i)
                break
            else:
                pass
    else:
        break
nan_list.sort()
print(nan_list)