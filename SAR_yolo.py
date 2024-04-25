from ultralytics import YOLO
from utils import SendEmail

# CLI tensorboard --logdir runs\detect\5_0302_train29

# defalut.yaml imgsz change

'''
每次训练前检查：
输出文件夹名
训练模型名
epochs
batch_size
'''

mode_val = False
project = 'runs'  # 保存训练的输出
train_name = 'detect\\17_0419_train'  # project下的子文件夹 保存logs和训练的输出
val_name = 'detect\\17_0419_val'  # project下的子文件夹 保存logs和训练的输出
train_model_path = '..\\model\\yolov8n.pt'  # transfer
val_model_path = '.\\' + project + '\\' + train_name + '\\weights\\best.pt'
train_model = './ultralytics/cfg/models/v8/yolov8n_my_v10.yaml'  # origin
epochs = 1000
imgsz = 640
batch_size = 8
save_period = 20  # 保存模型的频次

subject = 'Model Train Complete!!!'
body = '你的模型训练完了，快去看看吧！！！\n时间不等人，抓紧吧！！！\nJason_SHI from qqmail'

# 从头开始创建一个新的YOLO
# model = YOLO('yolov8n.yaml')
# model.info()

if __name__ == "__main__":  # 多进程要放入main函数中

    # 加载预训练的YOLO模型（推荐用于训练）
    train_model = YOLO(train_model)
    # 训练模型
    results = train_model.train(data='SAR-AIRcraft-1.0-yolo.yaml', epochs=epochs, batch=batch_size, imgsz=imgsz, device=0,
                          save_period=save_period, project=project, name=train_name, plots=True, verbose=False)
    if mode_val:
        val_model = YOLO(val_model_path)
        # 评估模型在验证集上的性能
        val_results = val_model.val(data='SAR-AIRcraft-1.0-yolo.yaml', batch=batch_size, imgsz=imgsz, iou=0.7, conf=0.2,
                                    device=0, project=project, name=val_name, plots=True, split='test', half=False)

    SendEmail(subject=subject, body=body)

    # 将模型导出为ONNX格式
    # success = train_model.export(format='onnx')

