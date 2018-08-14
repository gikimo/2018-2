print("hello world")
name=input("what is your name")
print("hello,"+name+"!") 
Microsoft Windows [版本 10.0.17134.165]
(c) 2018 Microsoft Corporation。保留所有权利。

C:\Users\dell>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> "let's say" '"hello world!"'
'let\'s say"hello world!"'
>>> temp=42
>>> print("the tempererature is"+temp)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>>
>>> print("the temperature is " + temp)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>>  print("the temperature is " + `temp`)
  File "<stdin>", line 1
    print("the temperature is " + `temp`)
    ^
IndentationError: unexpected indent
>>> print("o")
o
>>> print("the temperature is"+`temp`)
  File "<stdin>", line 1
    print("the temperature is"+`temp`)
                               ^
SyntaxError: invalid syntax
>>> print("the temperature is"+temp)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print("the temperature is "+repr(temp))
the temperature is 42
>>> path='c:\nowhere
  File "<stdin>", line 1
    path='c:\nowhere
                   ^
SyntaxError: EOL while scanning string literal
>>> path="c:\nowhere'
  File "<stdin>", line 1
    path="c:\nowhere'
                    ^
SyntaxError: EOL while scanning string literal
>>> path='c:\nowhere'
>>>
>>> print path
  File "<stdin>", line 1
    print path
             ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(path)?
>>> print(path)
c:
owhere
>>> print r(path)
  File "<stdin>", line 1
    print r(path)
          ^
SyntaxError: invalid syntax
>>> print(r'c:\npwhere)
  File "<stdin>", line 1
    print(r'c:\npwhere)
                      ^
SyntaxError: EOL while scanning string literal
>>> print(r'c:\nowhere')
c:\nowhere
>>> print(r'hjowng\'
  File "<stdin>", line 1
    print(r'hjowng\'
                   ^
SyntaxError: EOL while scanning string literal
>>> print(r'sjfoiweff、’）
  File "<stdin>", line 1
    print(r'sjfoiweff、’）
                        ^
SyntaxError: EOL while scanning string literal
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
