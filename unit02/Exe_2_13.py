#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （分割数字）编写一个程序，提示用户输入四位整数
#   并以反向顺序显示。
#++++++++++++++++++++++++++++++++++++++++++++++++

num = int(input("Enter an integer: "))

while num > 0:
    print(num % 10)
    num //= 10