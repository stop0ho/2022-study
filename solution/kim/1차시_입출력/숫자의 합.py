val=input()
for i in range(int(len(val)/10)+1):
    print(val[i*10:i*10+10])