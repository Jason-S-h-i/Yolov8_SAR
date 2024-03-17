# 简介
此文件记录整个毕设过程中模型训练的参数选择和模型结构变化

# 第一次
模型文件名：1_0212_train

epoch=300

model=yolov8s.pt

datasets=SAR-AIRcraft-1.0-yolo

batchsize=8

imgsz = 1504


新加入功能：
- 实现对指定模型的训练
- 保存每次训练模型
- 训练过程中的指标
- 实现模型的测试???
- 保存测试结果???
- 测试的指标???

针对上述功能中???的功能，会对其专门实现一个py实现其目标

## 通用测试代码

针对训练完毕的模型进行推理，对测试集进行预测，并输出相关测试结果和分析结果

1. 读取模型
2. 将测试集输入模型测试
3. 输出数据分析
4. 打印数据写入一个文件夹内

# 第二次
使用yolov8n迁移训练

模型文件名：2_0228_train

epoch=1000

model=yolov8n.pt

datasets=SAR-AIRcraft-1.0-yolo

batchsize=8

imgsz = 1504

训练结果：

最终在训练了297个epochs后，模型精度无提升。

# 第三次
新建全新的yolov8n训练

模型文件名：3_0229_train

epoch=1000

model=yolov8n.yaml

datasets=SAR-AIRcraft-1.0-yolo

batchsize=8

imgsz = 1504

训练结果：

最终在训练了354个epochs后，模型精度无提升。与迁移训练的epochs次数相差不大，测试精度未对比

# 第四次
采用yolov8n迁移训练，在接下来的几次训练中会依次训练修改imgsz之后，对模型的影响，并对比

模型文件名：4_0301_train

epoch=500

model=yolov8n.pt

datasets=SAR-AIRcraft-1.0-yolo

batchsize=32

imgsz = 640

最终在训练了402个epochs后，模型精度无提升。

# 第五次
采用yolov8n迁移训练，imgsz变化

模型文件名：5_0302_train

epoch=500

model=yolov8n.pt

datasets=SAR-AIRcraft-1.0-yolo

batchsize=16

imgsz = 1280

最终在训练了353个epochs后，模型精度无提升。

# 第六次
采用yolov8n迁移训练，imgsz变化

模型文件名：6_0302_train

epoch=500

model=yolov8n.pt

datasets=SAR-AIRcraft-1.0-yolo

batchsize=16

imgsz = 960

最终在训练了292个epochs后，模型精度无提升。

# 第七次
在头部采取了DCN替代了传统的Conv

模型文件名：7_0317_train

epoch=500

model=yolov8n.pt

datasets=SAR-AIRcraft-1.0-yolo

batchsize=8

imgsz = 640

# 第八次
改变DCN内部部分结构

# 第九次
（计划）使用yolov9的一个模型训练
