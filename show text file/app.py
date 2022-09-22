
f= open('show text file\demo.txt')
content = f.readlines()
num = len(content)
if num > 10:
    for i in range(0,10):
        print(content[i])
        print()
else:
    for i in range(0,num):
        print(content[i])
        print()