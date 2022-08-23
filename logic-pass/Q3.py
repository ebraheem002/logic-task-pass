allChars = "abcdefghijklmnopqrstuvwxyz"
q3String = "My name is Ebraheem i'm 22 years old and i love food "
for char in allChars:
    counter = q3String.count(char)
    if counter >1 :
        print (char , counter)