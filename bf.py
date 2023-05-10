# -*- coding: UTF-8 -*-
import json

def permute(list): #排列組合的函式
    if len(list) == 1: #爲了避免出錯，設置第二道防綫，儅串列的長度為1，排列組合是它自己
        return [list] #回傳本身數字
 
    result = [] #儲存所有排列組合的串列
    for i in range(len(list)):
       a = list[i] #取a為result的第一個值，持續到list裏每個值都被用到
       remain = list[:i] + list[i+1:] #使用list slicing，改變list串列為result，把i去掉從i+1開始

       for b in permute(remain): #呼叫自己
           result.append([a] + b) #產生所有排列組合，以a為每個排列組合第一個數儲進result
    return result

def BF(input): #暴力法函式
    N = len(input)
    if N == 1: #爲了避免出錯，設置第一道防綫
        assignment = [0]
        cost = input[0][0]
        return assignment, cost
    
    index = [] #儲存每個agent的序號
    for i, j in enumerate(input[0]): #用enumerate通過每個agent做job的經費找出序號
        index.append(i)
    #print(index)
    k = permute(index) #呼叫排列組合函式，是爲任務分配所有可能性
    print(k)
    
    allpos = [] #儲存各question所有經費的排列組合
    for l in k:
        pos = [] #儲存經費其中一個排列組合
        for m, a in zip(l, input): #這裏用了double for在一個line
            pos.append(a[m]) #因爲一個任務只能被一個agent執行，每份工作a指派一位agent m，a[m]就是cost
        allpos.append(pos)
    print(allpos)
    
    allsum = [] #儲存各可能性的經費總和
    for o in allpos:
        s = sum(o) #把每個經費的排列組合各自加起來
        allsum.append(s)
    print(allsum)
    
    cost = min(allsum) #取allsum中最低的經費
    
    mincostindex = allsum.index(cost) #用cost在allsum裏的index，
    assignment = k[mincostindex] #去到任務分配可能性k裏面找任務分配方式

    return assignment, cost

with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) #加載json file
    for key in data:
        input = data[key] #為每個鍵的矩陣
        #print(input)

        assignment, cost = BF(input) #呼叫暴力法函式

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', cost)
        print()