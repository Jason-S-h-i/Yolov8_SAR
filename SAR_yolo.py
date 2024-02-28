from ultralytics import YOLO

# CLI tensorboard --logdir runs

# defalut.yaml imgsz change

project = 'runs'  # 保存训练的输出
train_name = 'detect\\3_0229_train'  # project下的子文件夹 保存logs和训练的输出
val_name = 'detect\\3_0229_val'  # project下的子文件夹 保存logs和训练的输出
# train_model = '..\\model\\yolov8n.pt'  # transfer
train_model = 'yolov8n.yaml'  # origin
epochs = 1000
imgsz = 1504
batch_size = 8
save_period = 20  # 保存模型的频次

# 从头开始创建一个新的YOLO模型
# model = YOLO('yolov8n.yaml')
# model.info()

if __name__ == "__main__":  # 多进程要放入main函数中

    # 加载预训练的YOLO模型（推荐用于训练）
    model = YOLO(train_model)

    # 训练模型
    results = model.train(data='SAR-AIRcraft-1.0-yolo.yaml', epochs=epochs, batch=batch_size, imgsz=imgsz, device=0,
                          save_period=save_period, project=project, name=train_name, plots=True)

    # 评估模型在验证集上的性能
    # val_results = model.val(data='SAR-AIRcraft-1.0-yolo.yaml', batch=batch_size, imgsz=imgsz, device=0, project=project, name=val_name, plots=True)

    # 使用模型对图片进行目标检测
    # test_results = model(path_test_img)

    # 将模型导出为ONNX格式
    success = model.export(format='onnx')

# 测试脚本
# from ultralytics import YOLO
# path_pretrained_model = "./ultralytics/assets/yolov8n.pt"
# path_test_img = "./ultralytics/assets/bus.jpg"
# model = YOLO(path_pretrained_model)
# results = model(path_test_img)
