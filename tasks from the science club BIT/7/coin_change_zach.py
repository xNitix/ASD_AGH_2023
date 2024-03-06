# mozemy rozmienic na nominaly 1,5,10,25,100, chcemy najmiej monet

def change(x):
    money = [100,25,10,5,1]
    used = [0,0,0,0,0]
    x_copy = x
    
    indx = 0
    while x_copy > 0:
        if x_copy >= money[indx]:
            x_copy -= money[indx]
            used[indx] += 1
        else:
            indx+=1
    
    return "100 x ",used[0], " ","25 x ",used[1]," ","10 x ",used[2]," ","5 x ",used[3]," ","1 x ",used[4]

print(change(765))