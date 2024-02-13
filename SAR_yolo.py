from ultralytics import YOLO

# CLI tensorboard --logdir runs

# defalut.yaml imgsz change

project = 'runs'  # 保存训练的输出
name = 'detect\\train1_0212'  # project下的子文件夹 保存logs和训练的输出
train_model = '..\\model\\yolov8s.pt'
epochs = 300
imgsz = 1500
batch_size = 8
save_period = 10  # 保存模型的频次

# 从头开始创建一个新的YOLO模型
# model = YOLO('yolov8n.yaml')
# model.info()

if __name__ == "__main__":  # 多进程要放入main函数中

    # 加载预训练的YOLO模型（推荐用于训练）
    model = YOLO(train_model)

    # 使用“coco128.yaml”数据集训练模型3个周期
    results = model.train(data='SAR-AIRcraft-1.0-yolo.yaml', epochs=epochs, batch=batch_size, imgsz=imgsz, device=0,
                          save_period=save_period, project=project, name=name, plots=True)

    # 评估模型在验证集上的性能
    val_results = model.val()

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
