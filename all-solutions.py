string = "ebraheem$ mahmood"
newString = string.replace("$","")
print(newString)


numbersRange = [1,2,3,4,5,6,7,8,9,22,1000,1431] 
#This mark is to know which one pass
mark = False 
for j in numbersRange:
    if j > 1:
        # set the range using exponentiation
        for i in range(2 , int(j ** 0.5) + 1): 
            if (j % i) == 0:
                mark = True 
                break
    #check the mark
    if mark:
        print(j, "is not a prime number")
        mark = False
    else:
        print(j, "is a prime number")


allChars = "abcdefghijklmnopqrstuvwxyz"
q3String = "My name is Ebraheem i'm 22 years old and i love food "
for char in allChars:
    counter = q3String.count(char)
    if counter >1 :
        print (char , counter)