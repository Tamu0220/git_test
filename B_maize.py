h,w,n = map(int,input().split())
#h,w,n = map(int,"4 4 7".split())
upper= True
init = True
x,y=(0,0)
for i in range(n):
    direct =input()
    """if i ==0:
        direct="U"
    if i ==1:
        direct="U"
    if i ==2:
        direct="U"
    if i ==3:
        direct="r"
    if i ==4:
        direct="R"
    if i ==5:
        direct="R"
    if i ==6:
        direct="R"""
    if direct.isupper():
        upper=True
    if direct.islower():
        upper=False
    if upper:
        if direct =="U":
            y += 1
        if direct =="D":
            y -= 1
        if direct =="R":
            x += 1
        if direct =="L":
            x -= 1
        if x >= w or y >= h or x<0 or y< 0:
            init=False
            break
#print(x,y)        
if not init:
    print("invalid")
else:
    print("valid")