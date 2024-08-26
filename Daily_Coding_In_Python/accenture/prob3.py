# # a = "0" 
# # print(a.isdigit())
# # print(type(a.isdigit()))
# # print(ord(a))

# # Asci characters a-z range(97, 122), A-Z 65-90  0 to 9  48 to 57
# # isdigit()

# """
# Opentext:
# Technical - 30 min
# Self Intro
# Coding Question:
# Given a sentence check whether the sentence is symmetric or not
# Symmetric means:
# The last character of the previous word should be equal to the next character and should be case insensitive
# And they asked to Modify that the first character of the sentence should be equal to the last character of the sentence

# str="Today yet"
# Output:True

# str="test last"
# Output:False

# HR - 15min
# About yourself, interests
# About opentext company
# About the current internship
# Willing to relocate? 
# What you will do in your free time?  """


# # def symmetric(sentence):
# #     sentence = sentence.lower()
# #     words = sentence.split()
    
# #     if(words[0][0] == words[1][-1] and words[0][-1] == words[1][0]):
# #         return True
    
# #     return False

# # str1 = "Today yet"
# # print(symmetric(str1))


def password(str1):
    if (len(str1) < 4 or str1[0].isdigit()):
        return 0 
    a = 0
    b = 0
    for i in str1:
        if(i ==" " or i == "/"):
            return 0
        elif(i.isdigit()):
            b+=1
        elif(i.isalpha() and i == i.upper()):
            a+=1
    if(a == 0 or b == 0):
        return 0 

    return 1

str1 = "Kuh1k"
print(password(str1))