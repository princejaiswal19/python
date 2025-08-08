# a="good morning"

# b=" harry"
# print(a,b)
# print(type(b))
# print(a+b)

# # slicing of strings
# a="prince"
# print(a[-5:-1])
# print(a[1:6:2])
# c=len(a)
# print(c)
# print(a.endswith("e"))
# practice set

# greet="Good Afternoon, "
# b=input("Name:")
# print(greet+b)
letter= '''Dear <|name|>, 
you have been selected as a executive memeber of csec 
Date: <|date|>
Thank You'''
name=input("Enter the participant's name:")
date=input("input the current date:")
letter=letter.replace("<|name|>", name)
letter=letter.replace("<|date|>", date)
print(letter)


