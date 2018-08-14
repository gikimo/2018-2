print("hello world")
name=input("what is your name")
print("hello,"+name+"!") 
#字符串与数字
C:\Users\dell>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> "let's say" '"hello world!"'
'let\'s say"hello world!"'
>>> temp=42
>>> print("the temperature is "+repr(temp))
the temperature is 42
#转义\
>>> path='c:\nowhere'
>>> print(path)
c:
owhere
#原始字符串
>>> print(r'c:\nowhere')
c:\nowhere

>>> print(r'hello\')
  File "<stdin>", line 1
    print(r'hello\')
                   ^
SyntaxError: EOL while scanning string literal
>>> print(r'hello')
hello
>>> print(r'hello\\')
hello\\
>>> print(r'hello' '\\')
hello\
>>>
