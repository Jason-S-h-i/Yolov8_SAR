# 简介
此文件记录整个毕设过程中模型训练的参数选择和模型结构变化

# 第一次
```python
name = '1_0212_train'
model= 'yolov8s.pt'
epochs = 300
imgsz = 1504
batch_size = 8
```

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

yolov8n.pt

模型文件名：2_0228_train

```python
name = '2_0228_train'
model= 'yolov8n.pt'
epochs = 1000
imgsz = 1504
batch_size = 8
```

训练结果： 最终在训练了297个epochs后，模型精度无提升。

# 第三次
新建全新的yolov8n训练

yolov8.yaml

模型文件名：3_0229_train
```python
name = '3_0229_train'
model= 'yolov8.yaml'
epochs = 1000
imgsz = 1504
batch_size = 8
```

训练结果： 最终在训练了354个epochs后，模型精度无提升。与迁移训练的epochs次数相差不大，测试精度未对比

# 第四次
采用yolov8n迁移训练，在接下来的几次训练中会依次训练修改imgsz之后，对模型的影响，并对比

yolov8n.pt

模型文件名：4_0301_train
```python
name = '4_0301_train'
model= 'yolov8n.pt'
epochs = 500
imgsz = 640
batch_size = 32
```

训练结果：最终在训练了402个epochs后，模型精度无提升。

# 第五次
采用yolov8n迁移训练，imgsz变化

yolov8n.pt

模型文件名：5_0302_train
```python
name = '5_0302_train'
model= 'yolov8n.pt'
epochs = 500
imgsz = 1280
batch_size = 16
```

训练结果：最终在训练了353个epochs后，模型精度无提升。

# 第六次
采用yolov8n迁移训练，imgsz变化

yolov8n.pt

模型文件名：6_0302_train
```python
name = '6_0302_train'
model= 'yolov8n.pt'
epochs = 500
imgsz = 960
batch_size = 16
```

训练结果：最终在训练了292个epochs后，模型精度无提升。

# 第七次
在头部采取了DCN替代了传统的Conv，替换head.py中的网络结构

yolov8n.pt

模型文件名：7_0317_train
```python
name = '7_0317_train'
model= 'yolov8n.pt'
epochs = 1000
imgsz = 640
batch_size = 16
```

训练结果：训练损失上下乱跳，模型不收敛

结论：解耦头部分的网络结构不要轻易替换

# 第八次
将Neck部分中降采样FPN中的conv替换为ghostconv

yolov8n_my_v1.yaml

模型文件名：8_0412_train
```python
name = '8_0412_train'
model='yolov8n_my_v1.yaml'
epochs = 700
imgsz = 640
batch_size = 8
```

训练结果：在280轮时停止训练

结论：

# 第九次
在Neck部分中添加SA模块

yolov8n_my_v2.yaml

模型文件名：9_0412_train
```python
name = '9_0412_train'
model='yolov8n_my_v2.yaml'
epochs = 700
imgsz = 640
batch_size = 8
```

训练结果：在280轮时停止训练

结论：

# 第十次
结合第八和第九次添加的模块进行实验

yolov8n_my_v3.yaml

模型文件名：10_0413_train
```python
name = '10_0413_train'
model='yolov8n_my_v3.yaml'
epochs = 700
imgsz = 640
batch_size = 8
```

训练结果：在359轮时停止训练

结论：

# 第十一次
在此次和接下来的几次训练中，将尝试使用不同的IoU进行模型训练

此次使用的loss为CIoU

yolov8n_my.yaml

模型文件名：11_0415_train
```python
name = '11_0415_train'
model='yolov8n_my.yaml'
epochs = 700
imgsz = 640
batch_size = 8
```

训练结果：在608轮时停止训练

结论：

# 第十二次
此次使用的loss为DIoU

yolov8n_my.yaml

模型文件名：12_0416_train
```python
name = '12_0416_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在511轮时停止训练

结论：

# 第十三次
此次使用的loss为GIoU

yolov8n_my.yaml

模型文件名：13_0417_train
```python
name = '13_0417_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在339轮时停止训练

结论：

# 第十四次
此次使用的loss为EIoU

yolov8n_my.yaml

模型文件名：14_0417_train
```python
name = '14_0417_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在583轮时停止训练

结论：

# 第十五次
此次使用的loss为WIoU-V3

yolov8n_my.yaml

模型文件名：15_0418_train
```python
name = '15_0418_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在656轮时停止训练

结论：

# 第十六次
此次使用的loss为WIoU-V2

yolov8n_my.yaml

模型文件名：16_0418_train
```python
name = '16_0418_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在396轮时停止训练

结论：

# 第十七次
此次使用的loss为WIoU-V1

yolov8n_my.yaml

模型文件名：17_0419_train
```python
name = '17_0419_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在276轮时停止训练

结论：

# 第十八次
此次使用的loss为IoU，做对照实验

yolov8n_my.yaml

模型文件名：18_0420_train
```python
name = '18_0420_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在594轮时停止训练

结论：

# 第十九次
此次使用的loss为SIoU

yolov8n_my.yaml

模型文件名：19_0420_train
```python
name = '19_0420_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在327轮时停止训练

结论：

# 第二十次
此次使用的loss为FocalEIoU

yolov8n_my.yaml

模型文件名：20_0420_train
```python
name = '20_0420_train'
model='yolov8n_my.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在380轮时停止训练

结论

# 第二十一次
loss=CIoU，去掉SPPF作为对比

yolov8n_my_v4.yaml

模型文件名：21_0422_train
```python
name = '21_0422_train'
model='yolov8n_my_v4.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在280轮时停止训练

结论

# 第二十二次
loss=CIoU，去掉SPPF，在backbone的c2f后加上SA

yolov8n_my_v5.yaml

模型文件名：22_0422_train
```python
name = '22_0422_train'
model='yolov8n_my_v4.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```

训练结果：在447轮时停止训练

结论

# 第二十三次
loss=CIoU，在backbone的c2f后加上SA，最后一个SA换回SPPF

yolov8n_my_v6.yaml

模型文件名：23_0423_train
```python
name = '23_0423_train'
model='yolov8n_my_v6.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```
参数量：233 layers, 3012231 parameters, 3012215 gradients, 8.2 GFLOPs

训练结果：在731轮时停止训练

结论

# 第二十四次
loss=CIoU，sppf改为dcb+sa

yolov8n_my_v7.yaml

模型文件名：24_0424_train
```python
name = '24_0424_train'
model='yolov8n_my_v7.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```
参数量：227 layers, 3306625 parameters, 3306609 gradients, 8.4 GFLOPs

训练结果：在583轮时停止训练

结论

# 第二十五次
loss=CIoU，学习SE模块改造c2f，生成c2f_sa

yolov8n_my_v7.yaml

模型文件名：25_0424_train
```python
name = '25_0424_train'
model='yolov8n_my_v8.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```
参数量：245 layers, 3012249 parameters, 3012233 gradients, 8.2 GFLOPs

训练结果：在564轮时停止训练

结论

# 第二十六次
loss=CIoU，c2f_sa+dcb_sa+sppf

yolov8n_my_v9.yaml

模型文件名：26_0425_train
```python
name = '26_0425_train'
model='yolov8n_my_v9.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```
参数量：255 layers, 3471269 parameters, 3471253 gradients, 8.6 GFLOPs

训练结果：在709轮时停止训练

结论：负优化

# 第二十七次
loss=CIoU，c2f_sa+ghostconv+c2f_ghost

yolov8n_my_v10.yaml

模型文件名：27_0425_train
```python
name = '27_0425_train'
model='yolov8n_my_v10.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```
参数量：315 layers, 2938621 parameters, 2938605 gradients, 7.6 GFLOPs

训练结果：在443轮时停止训练

结论

# 第二十八次
loss=CIoU，c2f_sa+dcb_sa

yolov8n_my_v11.yaml

模型文件名：28_0426_train
```python
name = '28_0426_train'
model='yolov8n_my_v11.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```
参数量：231 layers, 3306637 parameters, 3306621 gradients, 8.4 GFLOPs

训练结果：在597轮时停止训练

结论：dcb_sa别用了

# 第二十九次
loss=CIoU，

c2f_sa+dcb_sa

yolov8n_my_v12.yaml

模型文件名：29_0426_train
```python
name = '29_0426_train'
model='yolov8n_my_v12.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```
参数量：247 layers, 3306661 parameters, 3306645 gradients, 8.4 GFLOPs

训练结果：在637轮时停止训练

结论

# 第三十次
loss=CIoU，

c2f_sa+dcb_sa

yolov8n_my_v13.yaml

模型文件名：30_0426_train
```python
name = '30_0426_train'
model='yolov8n_my_v13.yaml'
epochs = 1000
imgsz = 640
batch_size = 8
```
参数量：255 layers, 3216901 parameters, 3216885 gradients, 8.3 GFLOPs

训练结果：在343轮时停止训练

结论

# 重大错误
由于个人认知问题，没有保证对比实验的准确性，

实际上只要保证在每次训练时，epochs和其他的参数一致即可。

之前的验证的参数均为跑到最优时的参数。

对接下来实验进行规划：

网络改进部分（loss=CIoU）_第一部分_
1. baseline
2. 迁移baseline。训练完之后马上比较，看哪个在验证集上表现好，后面就用哪个
3. no sppf
4. sppf->dcb_sa
5. backbone c2f->c2f_sa
6. backbone c2f_sa+dcb_sa
7. neck conv->ghost
8. neck c2f->c2f_ghost
9. neck dcb_sa+c2f_ghost

损失函数改进部分  _第二部分_
1. GIoU
2. CIoU
3. DIoU
4. EIoU
5. WIoU-v1
6. WIoU-v2
7. WIoU-v3
8. SIoU
9. FocalEIoU
看哪个效果最好就挑哪个，其他挑选大约3-4个

# No.31

重大错误1.1 baseline

```python
name = '31_0427_train'
model='yolov8n_my.yaml'
# 不变参数
batch_size = 16
epochs = 300
imgsz = 640
lr0=0.01
lrf=0.01
optimizer=SGD
weight_decay = 0.0005
```
参数量：

# No.31

重大错误1.2 迁移baseline

```python
name = '32_0427_train'
model='yolov8n.pt'
# 不变参数
batch_size = 16
epochs = 300
imgsz = 640
lr0=0.01
lrf=0.01
optimizer=SGD
weight_decay = 0.0005
```
参数量：

# 添加模块方法
在ultralytics/nn/modules对应的文件下加入模块，以block为例。

在block.py中加入class SA

在block.py中的__all__加入"SA"的声明

在__init__.py中，from...import...中的import导入SA；并且在__all__加入"SA"的声明

在ultralytics/nn/tasks.py文件首from ultralytics.nn.modules import 加入对应模块

在parse_model函数中添加elif语句来添加对应模块的参数，加入到arg中

在ultralytics/cfg/models/v8/yolov8.yaml中加入对应模块。args为在class中声明的默认参数

# 第九次
（计划）使用yolov9的一个模型训练
