'''
Author: wind-listener 2775174829@qq.com
Date: 2023-09-21 21:12:21
LastEditors: wind-listener 2775174829@qq.com
LastEditTime: 2023-09-21 21:29:09
FilePath: \PROJECT14_GoodsManagementDuringPandemic\MyCode\ensemble2.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import os
import pandas as pd
import matplotlib.pyplot as plt

# 初始化数据列表
dateActualNum = [0, 0]
dateNeedNum = [0]
dateProNeedNum = []

# 获取文件列表
filenames = os.listdir(r"D:\Mathematicalmodeling\2022年F题\附件4：长春市疫情期间每日生活物资相关数据")

# 遍历文件
for topFile in filenames:
    dir = os.listdir(r"D:\Mathematicalmodeling\2022年F题\附件4：长春市疫情期间每日生活物资相关数据\\" + topFile)
    
    for file in dir:
        if file.find("实发") != -1 and file.find(".xls") != -1:
            src = r"D:\Mathematicalmodeling\2022年F题\附件4：长春市疫情期间每日生活物资相关数据\\" + topFile + "\\" + file
            tempDate = file.split('日')[0]
            Date = tempDate.split('月')[0] + '.' + tempDate.split('月')[1]
            
            vegGiveTable = pd.read_excel(src, header=[1, 2])  # 以第1行~2行为表头
            序号 = 0
            
            # 获取数据
            proproDayNeed = vegGiveTable.iloc[序号, 3]
            if pd.isnull(proproDayNeed):
                proproDayNeed = 0
            dateProNeedNum.append(proproDayNeed)
            
            proDayNeed = vegGiveTable.iloc[序号, 8]
            if pd.isnull(proDayNeed):
                proDayNeed = 0
            dateNeedNum.append(proDayNeed)
            
            curDayNeed = vegGiveTable.iloc[序号, 5]
            if pd.isnull(curDayNeed):
                curDayNeed = 0
            dateActualNum.append(curDayNeed)
            
            dateNeedNum.append(0)  # 我们并不知道4.29的需求是怎样的
            dateProNeedNum.append(0)  # 我们并不知道4.28的的提起那两天提出的需求是怎样的
            dateProNeedNum.append(0)  # 我们并不知道4.29的的提起那两天提出的需求是怎样的

# 日期列表
dateList = ['4.8', '4.9', '4.10', '4.11', '4.12', '4.13', '4.14', '4.15', '4.16', '4.17', '4.18', '4.19', '4.20', '4.21', '4.22', '4.23', '4.24', '4.25', '4.26', '4.27', '4.28', '4.29']

# 绘制多曲线图
def paintMultiCurve(paraTitle, paraLabelX, paraLabelY, paraXDataList, paraYDataList, paraFloatingLabel, paraColorList, paraMarker):
    plt.figure(figsize=(10, 5.5), dpi=300)
    plt.title(paraTitle, size=20)
    plt.xlabel(paraLabelX, size=20)
    plt.ylabel(paraLabelY, size=20)
    L = len(paraXDataList)
    plt.xticks(range(0, L, L // 10))
    plt.yticks(fontproperties='SimHei', size=17)
    
    for i in range(len(paraYDataList)):
        plt.plot(paraXDataList, paraYDataList[i], color=paraColorList[i])
    
    plt.legend(paraFloatingLabel, loc="upper right")
    plt.show()

# 绘制多曲线图
paintMultiCurve(paraTitle="", paraLabelX="日期", paraLabelY="蔬菜包的重量(吨)", paraXDataList=dateList[2:], paraYDataList=[dateProNeedNum[2:], dateNeedNum[2:], dateActualNum[2:]], paraFloatingLabel=['提前两天提出的需求量', '提前一天提出的需求量', '实际当天接收总量'], paraColorList=['royalblue', 'red', 'indigo', 'darkorange', 'darkgreen'], paraMarker="")

print(dateProNeedNum[2:])
print(dateNeedNum[2:])
print(dateActualNum[2:])
