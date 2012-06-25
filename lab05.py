print"####################################################"
print"PROBLEM 2"
n=5
def factorial(n):
    b=1
    while n:
        b=b*n
        n-=1
    return b
print factorial(5)
print"####################################################"
print"PROBLEM 3"
'''def fibonnacci(n):
    k=0
    for i in range(0,(n+1)):
        if i==1:
            print i
        if k>=2:
            while k:
                j=i+i-1
        k+=1
    return j
print fibonnacci(5)'''
print"####################################################"
print"PROBLEM 4"
'''def prime(n):
    if n%2==0:
        print "True"            #don't cut
    else:
        print "false"
    return
n=input("Enter a number :")
prime (n)'''

print"####################################################"
print"CHALLENGE PROBLEMS\nPROBLEM 4"
'''word=raw_input("Enter a string :")

def isPalindrome(word):
    rev=""
    word_len=len(word)
    for i in range(1,(word_len+1),1):
        rev=rev+word[-i]
    return rev
print "Reversed stringis :",isPalindrome(word)'''

print"####################################################"
print"CHALLENGE PROBLEMS\nPROBLEM 5"
word1="string"
word2="substring"
word2_length=len(word2)
word1_length=len(word1)
k=0
for i in range(0,word2_length,1):
    if word1[k]==word2[i]:
            k+=1
    else:
        k=0
        print "false"
        break
        
    if k==(word1_length):
            print "true"
            break
            


        

