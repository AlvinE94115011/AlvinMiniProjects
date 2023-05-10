# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

with open('Temperature.txt') as f:
    temp_list = []
    for line in f.readlines()[1:]: #[1:]從第二row開始讀檔
        a = line.rstrip('\n').split(', ') #strip是把每一row最後的\你去掉，split是把每一row弄成list的形式，再把數字之間多餘逗號去掉
        
        minor_list = []
        for i in a:
            minor_list.append(float(i)) #用float把數字的單引號去掉
        temp_list.append(minor_list)
        
    for i in temp_list:
        i.pop(0) #把每一個sublist的年份去掉

#Question 3
fig = plt.figure(figsize=(15, 6))
fig.add_subplot(1, 2, 1) #建立一個1x2的畫布

#Question 1
months = np.array(range(1, 13)) #用於標記x軸
years = np.array(range(2013, 2022)) #用於legend

plt.subplot(1, 2, 1) #第一個子圖
ax1 = plt.subplot(1, 2, 1) #由於底下用set ticks直接用plt.subplot會出錯，所以用ax1作爲代號
for i in range(9):
    plt.plot(months, temp_list[i], label = years[i]) #用for回圈畫9次圖，y軸為每一年12個月份的溫度，label是把它弄成該年份的legend
plt.title('Tainan Monthly Mean Temperature From 2013 to 2021')
ax1.set_xticks(months) #把x坐標軸弄得更詳細
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend(loc = "lower center") #調整legend位置

#Question 2
temp_month_list = []
for i in range(12): #設i為每一年裏面月份的index
    temp_month = []
    for j in temp_list: #設j為每一年
        temp_month.append(j[i]) #把每一年i月份的溫度append成一個temp_month串列
    temp_month_list.append(temp_month) #然後再弄成一個總temp_month_list

mean_list = []
for i in temp_month_list:
    mean_list.append(round(np.mean(i), 2)) #把每一年的該一月份溫度取平均值，再把它取小數點下2位

temp = np.array(range(16, 33, 2)) #用於標記y軸

plt.subplot(1, 2, 2) #第二個子圖
ax2 = plt.subplot(1, 2, 2)
plt.plot(months, mean_list, linestyle = 'solid', marker = 'o', markerfacecolor = 'red', markeredgecolor = 'red') #linestyle設定綫條為直綫，marker的face和edge顔色都爲紅色
for i in range(len(mean_list)):
    plt.annotate(str(mean_list[i]), xy = (months[i], mean_list[i])) #用annotate把mean_list的值標在graph裏
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
ax2.set_xticks(months) #把x坐標軸弄得更詳細
plt.xlabel('Month')
ax2.set_yticks(temp) #把y坐標軸弄得更詳細
plt.ylabel('Temperature in Degree C')
plt.axhline(y = round(np.mean(mean_list), 2), color = 'r', linestyle = '--', label = 'Mean of 9 Years') #用axhline畫虛綫，高度y為縂平均值
offset = 0.1
plt.text(1, round(np.mean(mean_list), 2)+offset, round(np.mean(mean_list), 2)) #把總平均值標在虛綫上，1是離y軸的位置，offset是離虛綫0.1的位置
plt.legend(loc = 'upper right') #調整legend位置

plt.tight_layout() #調整子圖之間排列位置
plt.show() #把圖顯示出來
#plt.savefig('lab13_03.png')