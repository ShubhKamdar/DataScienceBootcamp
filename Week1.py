#homework practice
#fib series= 1,1,2,3,5,8,13....


# #Question1
# a=0
# b=1
# terms=0
# print(a)
# print(b)
# while terms<10:
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     terms=terms+1

# #Question2
# a=['a',2,3,'dr',5,6,7,8,9,10,11,12,13,14,15,16]
# i=0
# while True:
#     i=i+1
#     if i%2!=0:
#         print(a[i])

#Question3
# a=['a',2,3,'dr',5,6,7,8,9,10,11,12,13,14,15,16]
# b=a[::-1]
# for z in b:
#     print(z)
# #or
# i=-1
# while True:
#     print(a[i])
#     i=i-1

## Question4
# string = """
# 	ChatGPT has created this text to provide tips on creating interesting paragraphs. 
# 	First, start with a clear topic sentence that introduces the main idea. 
# 	Then, support the topic sentence with specific details, examples, and evidence.
# 	Vary the sentence length and structure to keep the reader engaged.
# 	Finally, end with a strong concluding sentence that summarizes the main points.
# 	Remember, practice makes perfect!
# 	"""
# a=string.split()
# print(string)
# c=[]
# d=[]
# word_count={}
# for i in a:
#     if i not in c:
#         word_count[i]=1
#         c.append(i)
#     else:
#         word_count[i]+=1
#         d.append(i)
# print(word_count)
# print(len(c))

# #Question5
# argument=input('write the words whose vowels you want \n')
# a=[]
# c=[]
# b=['a','e','i','o','u']
# vowel_count={}
# for i in argument:
#     if i in b:
#         a.append(i)
# for i in a:
#     if i in c:
#         vowel_count[i]+=1
#     else:
#         vowel_count[i]=1
#         c.append(i)
# print(vowel_count)


# #Question 6
# animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
# for i in animals:
#     print(i.upper())

# #Question 7
# for i in range(1,16):
#     if i%2!=0:
#         print(i,' is odd')
#     else:
#         print(i,' is even')

# #Question 8
# a=int(input('Enter the first number \n'))
# b=int(input('Enter the second number you want to add with the first one \n'))
# c=a+b
# print(c)