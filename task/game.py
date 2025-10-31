pencils=int(input("How many pencils would you like to use:"))
name=input("Who will be the first (John, Jack):")
line=""
for i in range(pencils):
    line+="|"
print(line)
print(f"{name} is going first!")