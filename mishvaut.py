Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 10
>>> a = b
>>> b = a
>>> a
10
>>> b
10
>>> 
>>> a = 5
>>> b = 10
>>> a=b
>>> a
10
>>> b
10
>>> a=5
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
5
>>> c
5
>>> four = 4
>>> print (four*3)
12
>>> five = 4
>>> print (5)
5
>>> print (five*3)
12
>>> 
>>> >>> print("My name is " + my_name)

SyntaxError: invalid syntax
>>> print("My name is " + my_name)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print("My name is " + my_name)
NameError: name 'my_name' is not defined
>>> my_name = 'student'
>>> Print ('Hi' + my_name)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    Print ('Hi' + my_name)
NameError: name 'Print' is not defined
>>> print(“Hi” + my_name)
SyntaxError: invalid character in identifier
>>> print("Hi" + my_name)
Histudent
>>> my_age = 15
>>> print("I am" + my_age + "years old")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print("I am" + my_age + "years old")
TypeError: must be str, not int
>>> "my_age" = 15
SyntaxError: can't assign to literal
>>> "myage" = 15
SyntaxError: can't assign to literal
>>> print(I am + "my_age" + years old)
SyntaxError: invalid syntax
>>> my_age = 15
>>> print("I am" + my_age + "years old")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print("I am" + my_age + "years old")
TypeError: must be str, not int
>>> my_age = "15"
>>> print("I am" + my_age + "years old")
I am15years old
>>> score = "4"
>>> count = "5"
>>> total = "score" * "count"
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    total = "score" * "count"
TypeError: can't multiply sequence by non-int of type 'str'
>>> total = score*count
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    total = score*count
TypeError: can't multiply sequence by non-int of type 'str'
>>> total = "score"*"count"
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    total = "score"*"count"
TypeError: can't multiply sequence by non-int of type 'str'
>>> score
'4'
>>> score = 4
>>> count = 5
>>> total = score * count
>>> print (total)
20
>>> 
