'''
绘图


'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
绘制不同损失函数的loss曲线
'''
def plot_loss():
    # 读取训练数据
    list_loss = ['11_0415', '12_0416', '13_0417', '14_0417', '16_0418', '17_0419']
    file_path = '.\\runs\\detect'
    file_result = 'results.csv'
    box_loss = []
    cls_loss = []
    dfl_loss = []
    loss = []

    for i in range(0, len(list_loss)-1):
        file_loss = file_path + '\\' + list_loss[i] + '_train\\' + file_result
        df_csv = pd.read_csv(file_loss)
        df_array = np.array(df_csv)
        box_loss.append(df_array[..., 1])
        cls_loss.append(df_array[..., 2])
        dfl_loss.append(df_array[..., 3])
        loss.append(box_loss + cls_loss + dfl_loss)



if __name__ == "__main__":
    plot_loss()
