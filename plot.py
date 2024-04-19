'''
绘图
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
绘制不同损失函数的loss曲线
Q:不同损失函数的训练轮次不同
'''
def plot_loss():
    # 读取训练数据
    list_loss = ['11_0415', '12_0416', '13_0417', '14_0417', '15_0418', '16_0418', '17_0419']
    loss_func = ['CIoU', 'DIoU', 'GIoU', 'EIoU', 'WIoU-V3', 'WIoU-V2', 'WIoU-V1']
    num_loss = len(list_loss)
    num_epochs = 700
    file_path = '.\\runs\\detect'
    file_result = 'results.csv'
    box_loss = np.zeros([num_loss, num_epochs])
    cls_loss = np.zeros([num_loss, num_epochs])
    dfl_loss = np.zeros([num_loss, num_epochs])
    loss = np.zeros([num_loss, num_epochs])

    for i in range(num_loss-1):
        file_loss = file_path + '\\' + list_loss[i] + '_train\\' + file_result
        df_csv = pd.read_csv(file_loss)
        df_array = np.array(df_csv)
        box_loss[i, :] = np.pad(df_array[..., 1], (0, num_epochs-len(df_array[..., 1])), 'constant', constant_values = (0))
        cls_loss[i, :] = np.pad(df_array[..., 2], (0, num_epochs-len(df_array[..., 2])), 'constant', constant_values = (0))
        dfl_loss[i, :] = np.pad(df_array[..., 3], (0, num_epochs-len(df_array[..., 3])), 'constant', constant_values = (0))
        loss[i, :] = box_loss[i, :] + cls_loss[i, :] + dfl_loss[i, :]

    x = np.arange(0, num_epochs)
    plt.figure(figsize=(4,3), dpi=200)

    fig = plt.subplot(111)
    fig.set_title('box loss of different loss func')
    fig.set_xlabel('epochs')
    fig.set_ylabel('box_loss')
    for i in range(num_loss-1):
        fig.plot(x, box_loss[i], label=loss_func[i])

    # fig = plt.subplot(222)
    # fig.set_title('cls loss of different loss func')
    # fig.set_xlabel('epochs')
    # fig.set_ylabel('cls_loss')
    # for i in range(num_loss - 1):
    #     fig.plot(x, box_loss[i], label=loss_func[i])
    #
    # fig = plt.subplot(223)
    # fig.set_title('dfl loss of different loss func')
    # fig.set_xlabel('epochs')
    # fig.set_ylabel('dfl_loss')
    # for i in range(num_loss - 1):
    #     fig.plot(x, box_loss[i], label=loss_func[i])
    #
    # fig = plt.subplot(224)
    # fig.set_title('loss of different loss func')
    # fig.set_xlabel('epochs')
    # fig.set_ylabel('loss')
    # for i in range(num_loss - 1):
    #     fig.plot(x, box_loss[i], label=loss_func[i])

    plt.show()



if __name__ == "__main__":
    plot_loss()
