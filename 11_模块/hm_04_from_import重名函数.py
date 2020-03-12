# 多个模块,同名函数,后导入的函数覆盖先前的

from hm_01_hello import hello
from hm_05_hello2 import hello as hello2

hello()
hello2()
