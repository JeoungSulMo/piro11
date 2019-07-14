a = (input().split())
b = [list(i) for i in a]
print(len(b))  # len(b) = words
words = len(b)
c = []
st = []
popc = []
for o in b:
    st.append(len(o))
w1 = [] #가장 짧은 글자 길이
for p in range(min(st)):
    for j in range(len(b)):
        w1.append(b[j][p])
#print(w1) 첫글자 두번째글자 세번째 글자 단어별로 따와서 순서대로 놓기
for popj in range(min(st)):
    for popi in range(len(b)):
        w1_1 = w1.pop(0)
        popc.append(w1_1)
    if popc.count(popc[0]) == len(b):
        c.append(popc[0])
    popc = []
print(''.join(c))
