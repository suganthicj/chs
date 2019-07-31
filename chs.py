X11=int(input())
l=input()
Y11=""
for O in l:
    if O!=" ":
        Y11=Y11+O
k=""
p=0
O=0
j=""
while O<len(Y11):
    if Y11[O]=="0" and Y11[O+1]=="0":
        O=O+1
    elif Y11[O]=="0":
        k=k+Y11[p:O]
        p=O+1
        O=O+1
    else:
        O=O+1
for i in k:
    j=j+str(i)+" "

print(j.strip())
