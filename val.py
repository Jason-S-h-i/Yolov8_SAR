'''
测试
使用训练完毕的模型，在测试集上推理，输出结果
结果要求：以打印输出的结果形式转换为csv文件
类型、实例数量、P、R、mAP50、mAP50-95
'''

from ultralytics import YOLO
import pandas as pd
import numpy as np

project = 'runs'  # 保存训练的输出
# laptop result ; desktop detect
train_name = 'detect\\22_0422_train'
val_name = 'detect\\22_0422_val'
val_model_path = '.\\' + project + '\\' + train_name + '\\weights\\best.pt'

imgsz = 640
batch_size = 8

def SaveData(input):
    name = input.names
    instance_matrix = input.confusion_matrix.matrix
    all_dict = input.results_dict
    p = input.box.p
    r = input.box.r
    mAP50 = input.box.ap50
    mAP5095 = input.box.maps

    instance = np.sum(instance_matrix, axis=0)
    all_num = np.sum(instance[:-1])

    name_csv = []
    inst_csv = []
    p_csv = []
    r_csv = []
    map50_csv = []
    map5095_csv = []

    file_csv = '\\test_result.csv'

    for i in range(8):
        if i == 0:
            name_csv.append('all')
            inst_csv.append(all_num)
            p_csv.append(all_dict['metrics/precision(B)'])
            r_csv.append(all_dict['metrics/recall(B)'])
            map50_csv.append(all_dict['metrics/mAP50(B)'])
            map5095_csv.append(all_dict['metrics/mAP50-95(B)'])
        else:
            name_csv.append(name[i-1])
            inst_csv.append(instance[i-1])
            p_csv.append(p[i-1])
            r_csv.append(r[i-1])
            map50_csv.append(mAP50[i-1])
            map5095_csv.append(mAP5095[i-1])

    p_csv = [float('{:.5f}'.format(i)) for i in p_csv]
    r_csv = [float('{:.5f}'.format(i)) for i in r_csv]
    map50_csv = [float('{:.5f}'.format(i)) for i in map50_csv]
    map5095_csv = [float('{:.5f}'.format(i)) for i in map5095_csv]

    csv = {'Class': name_csv,
           'Instances': inst_csv,
           'P': p_csv,
           'R': r_csv,
           'mAP50': map50_csv,
           'mAP50-95': map5095_csv}

    # print(csv)

    df = pd.DataFrame(csv)
    df.to_csv(project+'\\'+val_name+file_csv)



if __name__ == "__main__":  # 多进程要放入main函数中

    val_model = YOLO(val_model_path)
    # 评估模型在验证集上的性能
    val_results = val_model.val(data='SAR-AIRcraft-1.0-yolo.yaml', batch=batch_size, imgsz=imgsz, iou=0.7, conf=0.2,
                                device=0, project=project, name=val_name, plots=True, split='test', half=False)

    SaveData(val_results)



