'''
Author: wind-listener 2775174829@qq.com
Date: 2023-09-19 20:46:58
LastEditors: zzm 2775174829@qq.com
LastEditTime: 2023-09-20 20:15:52
FilePath: \GoodsManagementDuringPandemic\MyCode\plot.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = "附件1：长春市COVID-19疫情期间病毒感染人数数据.xlsx"
data = pd.read_excel(file_path,sheet_name='新增本土感染者')

# 设置日期列为索引
selected_data = data.iloc[:, 9:]
# data.set_index('日期', inplace=True)

# 绘制感染人数增长曲线
plt.figure(figsize=(12, 6))
for column in data.columns:
    plt.plot(data.index, data[column], label=column)

plt.title('长春市COVID-19疫情期间病毒感染人数增长曲线')
plt.xlabel('日期')
plt.ylabel('感染人数')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(True)

# 显示图形
# plt.tight_layout()
plt.show()
