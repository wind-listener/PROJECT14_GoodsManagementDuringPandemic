'''
Author: wind-listener 2775174829@qq.com
Date: 2023-09-21 20:54:10
LastEditors: wind-listener 2775174829@qq.com
LastEditTime: 2023-09-21 21:01:07
FilePath: \PROJECT14_GoodsManagementDuringPandemic\MyCode\ensemble.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import pandas as pd
import glob

# 获取所有Excel文件的文件名
file_paths = glob.glob('附件5：长春市疫情期间每日各区蔬菜包相关数据\*.xls')  # 根据实际的文件名和路径来修改

# 创建一个空的DataFrame，用于存储整合后的数据
merged_data = pd.DataFrame()

# 遍历每个Excel文件，将数据读取到DataFrame并合并
for file_path in file_paths:
    df = pd.read_excel(file_path)  # 读取Excel文件
    merged_data = pd.concat([merged_data, df], ignore_index=True)  # 合并数据

# 在合并后的数据中按日期和地区进行分组汇总
grouped_data = merged_data.groupby(['日期', '地区']).sum().reset_index()

# 将整合后的数据保存到一个新的Excel文件中
grouped_data.to_excel('整合后的数据.xlsx', index=False)  # 修改保存文件名和路径

print("数据整合完成并已保存到 '整合后的数据.xlsx'")
