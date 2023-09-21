'''
Author: wind-listener 2775174829@qq.com
Date: 2023-09-21 21:31:22
LastEditors: wind-listener 2775174829@qq.com
LastEditTime: 2023-09-21 21:43:56
FilePath: \PROJECT14_GoodsManagementDuringPandemic\MyCode\ensemble3.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import re
import pandas as pd
from openpyxl import load_workbook
import glob

# 获取所有Excel文件的文件名
file_paths = glob.glob('附件5：长春市疫情期间每日各区蔬菜包相关数据\*.xls')  # 根据实际的文件名和路径来修改

# 创建一个Excel写入器，用于将数据写入一个新文件
with pd.ExcelWriter('合并后的文件.xlsx', engine='openpyxl') as writer:
    for file_path in file_paths:
        # 读取每个Excel文件的数据
        df = pd.read_excel(file_path)
        # 将数据写入到Excel文件，每个文件作为一个新的Sheet页
        sheet_name = file_path.split('.xls')[0].split('\\')[1]# 提取有效的Sheet名称，将无效字符替换为下划线
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
    # 保存合并后的Excel文件
    writer.save()

print("Excel文件合并完成并保存为 '合并后的文件.xlsx'")
