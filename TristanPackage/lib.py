def try_me(a):
    for row in range(a):
        for col in range(a+1):
            if (row==0 and col %3 !=0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):
                print("*",end=" ")
            else:
                print(end=" ")
        print()


try_me(6)
