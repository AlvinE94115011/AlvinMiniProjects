# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

with open('oddExperiment.txt') as f:
    x = []
    y = []
    for line in f.readlines()[1:]: #[1:]從第二row開始讀檔
        a = line.rstrip('\n').split(' ') #strip是把每一row最後的\你去掉，split是把每一row弄成list的形式
        x.append(float(a[1])) #用float把數字的單引號去掉
        y.append(float(a[0]))

a = np.polyfit(x, y, 1) #拟合成一条1次函數直綫
b = np.poly1d(a) #拼接成x的1階方程式
c = np.polyfit(x, y, 2) #拟合成一条2次函數曲线
d = np.poly1d(c) #拼接成x的2階方程式

LSE1_unrounded = np.square(np.subtract(y, b(x))).mean() #此部分為1階方程式，用numpy由實際y和方程式的預測散點圖的差值，找least square error
LSE1 = round(LSE1_unrounded, 5) #取小數點下5位
corr_matrix1 = np.corrcoef(y, b(x)) #用numpy corrcoef做係數矩陣
Rsquare1_unrounded = (corr_matrix1[0, 1])**2 #對比兩個y的串列做決定係數R2
Rsquare1 = round(Rsquare1_unrounded, 5) #取小數點下5位

LSE2_unrounded = np.square(np.subtract(y, d(x))).mean() #此部分為2階方程式
LSE2 = round(LSE2_unrounded, 5)
corr_matrix2 = np.corrcoef(y, d(x))
Rsquare2_unrounded = (corr_matrix2[0, 1])**2
Rsquare2 = round(Rsquare2_unrounded, 5)

plt.title('oddExperiment Data')
plt.scatter(x, y, label = 'Data') #用scatter繪製散點圖
plt.plot([], [], color = 'r', label = 'Fit of degree 1, LSE = '+str(LSE1)) #可以用兩個空的方括號來爲legend添加一個字串，標記為LSE
plt.plot([], [], color = 'rebeccapurple', label = 'Fit of degree 2, LSE = '+str(LSE2))
plt.plot(x, b(x), color = 'r', label = 'Fit of degree 1, R2 = '+str(Rsquare1)) #繪製1階最佳配適線
plt.plot(x, d(x), color = 'rebeccapurple', label = 'Fit of degree 2, R2 = '+str(Rsquare2)) #繪製2階最佳配適線
plt.legend(loc = 'upper center') #調整legend位置

plt.show()
#plt.savefig('lab13_plus.png')