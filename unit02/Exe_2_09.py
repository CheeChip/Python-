#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （科学：风寒温度）室外有多冷？只有温度是不足以提供答案的。
#   其他因素例如风速、相对湿度和光照都对室外的寒冷程度有很大的
#   影像。在 2001 年，美国国家气象局（NWS）实行以新的利用温度
#   和风速的公式计算风寒温度，公式如下
#       t_{wc} = 35.74 + 0.6215 * t_{a} - 35.75 ^ {0.16} 
#               + 0.4275 * t_{a} * v^{0.16}
#   其中的 t_{a} 是华氏温度表示的室外温度，v是英里/小时计算的
#   风速， t_{wc} 是风寒温度。此公式不适合与风速在每小时 2 英里
#   以下或温度在 -58 华氏度以下及 41 华氏度以上。
#
#   编写一个程序，提示用户输入一个 -58 到 41 华氏度之间的温度和
#   一个大于等于 2 英里/小时的风速，然后显示风寒温度。
#++++++++++++++++++++++++++++++++++++++++++++++++

t_a = eval(input('Enter the temperature in '
        'Fahrenheit between -58 and 41: '))
v_016 = eval(input('Endter the wind speed in miles per hour: ')) ** 0.16

t_wc = 35.74 + 0.6215 * t_a - 35.75 * v_016 + 0.4275 * t_a * v_016

print('\nThe wind chill index is', round(t_wc, 5))