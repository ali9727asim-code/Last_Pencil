names=["John","Jack"]
def display(pencils):
    line=""
    for i in range(pencils):
        line+="|"
    print(line)
pencils=int(input("How many pencils would you like to use:"))
name=input("Who will be the first (John, Jack):")
display(pencils)
indx = names.index(name)
while True:
    print(f"{names[indx]}'s turn:")
    n=int(input())
    pencils-=n
    if pencils<=0:
        break
    display(pencils)
    indx=1-indx

