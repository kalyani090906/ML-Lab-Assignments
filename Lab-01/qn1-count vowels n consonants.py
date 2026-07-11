def count(inp):
    v=0
    c=0

    for i in inp:
        if i.isalpha(): 
         if(i== 'a' or i== 'e' or i== 'i' or i== 'o' or i== 'u' or i== 'A' or i== 'E' or i== 'I' or i== 'O' or i== 'U' ):
            v=v+1
         else:
            c=c+1
    return v,c            
inp=input("Enter the string ")
v,c=count(inp)
print("Number of vowels = ",v)
print("Number of consonants = ",c)