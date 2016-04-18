#### python 依赖管理
python 的很多库，内部其实是 C 语言的，使用 easy_install/pip 安装的时候，往往是下载源码然后本机编译的。
如果打包了，可能会出现一些莫名奇妙的问题，比如 32、64 位的兼容问题，不同的操作系统的路径查找问题，等等。
正确的方式就是在 setup.py 文件中写明依赖的库和版本，然后到目标机器上安装，反正就一句 python setup.py install，不算复杂。

setup.py

```
# Copyright (C) 2014 pyeasy
# Author: WeizhongTu
# All rights reserved.
# MIT license
from setuptools import setup, find_packages
setup(
    name = ' ',
    version = '1.0.0',
    author = ' ',
    author_email =  ',
    packages = find_packages(),
    license='MIT',
    install_requires=[
        'xlrd',
        'networkx',
    ],
 )
 ```
把依赖包写在 install_requires 中