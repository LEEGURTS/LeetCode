import re

strs = []
strs = input("문자 입력")
strs = strs.lower()
strs = re.sub('[^a-z0-9]', '', strs)

if(strs == strs[ ::-1 ]):
    print("True")
else:
    print("False")
