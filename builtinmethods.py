Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=("sindhuja")
>>> x.encode()
b'sindhuja'
>>> x.endswidth()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.endswidth()
AttributeError: 'str' object has no attribute 'endswidth'
>>> x.endswith()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
>>> x.endswith(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.endswith(a)
NameError: name 'a' is not defined
>>> x.endswith("a")
True
>>> x.find("d")
3
>>> x.expandtabs()
'sindhuja'
>>> x="Sindhuja"
>>> x.expandtabs()
'Sindhuja'
>>> x.format()
'Sindhuja'
>>> x.expandtabs(3)
'Sindhuja'
>>> x.format(arial)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x.format(arial)
NameError: name 'arial' is not defined
>>> x.format_map()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x.format_map()
TypeError: format_map() takes exactly one argument (0 given)
>>> x.format_map(3)
'Sindhuja'
>>> x.format_map(5)
'Sindhuja'
>>> x="apoorva sindhuja")
SyntaxError: invalid syntax
>>> x="apoorva sindhuja"
>>> x.index("d")
11
>>> x.isalnum()
False
>>> x=1234
>>> x.isalnum()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x.isalnum()
AttributeError: 'int' object has no attribute 'isalnum'
>>> x="sindhuja"
>>> x.isalnum()
True
>>> x.isalpha()
True
>>> x.isdecimal()
False
>>> x="123"
>>> x.isdecimal()
True
>>> x.digit()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x.digit()
AttributeError: 'str' object has no attribute 'digit'
>>> x.isdigit()
True
>>> x="126"
>>> x.isidentifier()
False
>>> print(sindhuja)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(sindhuja)
NameError: name 'sindhuja' is not defined
>>> print("sindhuja")
sindhuja
>>> x.isidentifier()
False
>>> x="1/2"
>>> x.isnumeric()
False
>>> x.isdecimal()
False
>>> x.isdigit()
False
>>> x="63¼"
>>> x.isnumeric()
True
>>> x.isprintable()
True
>>> x="@#"
>>> x.isprintable()
True
>>> x="\n@#"
>>> x.isprintable()
False
>>> x.isspace()
False
>>> x=("sindhuja")
>>> x.isspace()
False
>>> x.istitle()
False
>>> x="SINDHUJA"
>>> x.istitle()
False
>>> x"fjygjhi hugjh"
SyntaxError: invalid syntax
>>> x="fjygjhi hugjh"
>>> x.istitle()
False
>>> x.join()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x.join()
TypeError: join() takes exactly one argument (0 given)
>>> x.join("j")
'j'
>>> x.join("g")
'g'
>>> x.join(3)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    x.join(3)
TypeError: can only join an iterable
>>> x.join("g")
'g'
>>> x.ljust()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x.ljust()
TypeError: ljust() takes at least 1 argument (0 given)
>>> x.ljust("g")
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x.ljust("g")
TypeError: 'str' object cannot be interpreted as an integer
>>> x.ljust(4)
'fjygjhi hugjh'
>>> x.ljust(6)
'fjygjhi hugjh'
>>> x.lstrip(4)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    x.lstrip(4)
TypeError: lstrip arg must be None or str
>>> x.lstrip("g")
'fjygjhi hugjh'
>>> x.zfill()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    x.zfill()
TypeError: zfill() takes exactly one argument (0 given)
>>> x.zfill(4)
'fjygjhi hugjh'
>>> x="apoorva"
>>> x.zfill(4)
'apoorva'
>>> x="apoorva"
>>> y="sindhu"
>>> z=1234
>>> x.zfill(4)
'apoorva'
>>> z.zfill(4)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    z.zfill(4)
AttributeError: 'int' object has no attribute 'zfill'
>>> z="1234"
>>> z.zfill(4)
'1234'
>>> z.zfill(2)
'1234'
>>> z.zfill(8)
'00001234'
>>> x="apoorva"x.zfill(4)
SyntaxError: invalid syntax
>>> x="apoorva"
>>> x.zfill(9)
'00apoorva'
>>> x.upper()
'APOORVA'
>>> x.translate()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    x.translate()
TypeError: translate() takes exactly one argument (0 given)
>>> x.translate("r")
'apoorva'
>>> x="APOORVAjhjhj"
>>> x.translate("r")
'APOORVAjhjhj'
>>> x.translate("R")
'APOORVAjhjhj'
>>> x="89000jkjk"
>>> x.translate("0")
'89000jkjk'
>>> x.title()
'89000Jkjk'
>>> x.swapcase()
'89000JKJK'
>>> x.strip()
'89000jkjk'
>>> x.splitlines()
['89000jkjk']
>>> x="hbhnkl"
>>> x.splitlines()
['hbhnkl']
>>> x="hbh\nk\tl"
>>> x.splitlines()
['hbh', 'k\tl']
>>> x="hbh\tkl"
>>> x.splitlines()
['hbh\tkl']
>>> x.split()
['hbh', 'kl']
>>> x.rstrip()
'hbh\tkl'
>>> x="hbhkl"
>>> x.rstrip()
'hbhkl'
>>> x.rsplit()
['hbhkl']
>>> x="hbhhf\nvbj\tkl"
>>> x.rsplit()
['hbhhf', 'vbj', 'kl']
>>> x="hb   hhf\nvbj\tkl"
>>> x.rsplit()
['hb', 'hhf', 'vbj', 'kl']
>>> x.rpartition()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    x.rpartition()
TypeError: rpartition() takes exactly one argument (0 given)
>>> x.rpartition(4)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    x.rpartition(4)
TypeError: must be str, not int
>>> x.rpartition("f")
('hb   hh', 'f', '\nvbj\tkl')
>>> x.maketrans()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    x.maketrans()
TypeError: maketrans() takes at least 1 argument (0 given)
>>> x.maketrans("f")
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    x.maketrans("f")
TypeError: if you give only one argument to maketrans it must be a dict
>>> x.maketrans("hf")
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    x.maketrans("hf")
TypeError: if you give only one argument to maketrans it must be a dict
>>> x.maketrans("1")
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    x.maketrans("1")
TypeError: if you give only one argument to maketrans it must be a dict
>>> x.partition("f")
('hb   hh', 'f', '\nvbj\tkl')
>>> x.replace("f")
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    x.replace("f")
TypeError: replace() takes at least 2 arguments (1 given)
>>> x.replace("f","a")
'hb   hha\nvbj\tkl'
>>> x.partition("f","a")
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    x.partition("f","a")
TypeError: partition() takes exactly one argument (2 given)
>>> x.rfind()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    x.rfind()
TypeError: rfind() takes at least 1 argument (0 given)
>>> x.rfind("f")
7
>>> x.rindex("f")
7
>>> x.index("f")
7
>>> x.find("f")
7
>>> x.rjust("f")
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    x.rjust("f")
TypeError: 'str' object cannot be interpreted as an integer
>>> x.rjust("7")
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    x.rjust("7")
TypeError: 'str' object cannot be interpreted as an integer
>>> x.rjust()
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    x.rjust()
TypeError: rjust() takes at least 1 argument (0 given)
>>> 
