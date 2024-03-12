str=str(input("Enter a string"))
def v():
    s=["a","e","i","o","u","A","E","I","O","U"]
    count=0
    for i in str:
        if i in s:
            count+=1
    print("count of vowels is",count)
v()

