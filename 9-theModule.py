#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.导入sys模块
import sys

# sys模块的argv变量，用list存储了命令行的所有运行参数
# 运行 py 9-theModule.py gaojc 下面的语句打印 ['9-theModule.py', 'gaojc']
print("sys.argv=", sys.argv)

# 2.from…import 语句: 从模块中导入一个指定的部分到当前命名空间中
from pathlib import Path

p = Path('.')
# 列出子目录
for x in p.iterdir():
    if x.is_dir():
        print("x.is_dir=", x)
# 列出当前目录树下的所有txt文件
globFiles = list(p.glob("*.txt"))
print("globFiles=", globFiles)

file = p / '1-helloworld.py'
# 打开一个文件
with file.open() as f:
    print(f.readline())