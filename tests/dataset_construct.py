import xml.etree.ElementTree as ET
import os
import shutil
"""
完成操作：
读取每个集中的文件名
图片分类
标签 xml读取、解析、分类至TXT
"""
path_VOC_datasets = '.\\SAR-AIRcraft-1.0'  # VOC格式数据集地址
path_train_set = 'ImageSets\\Main\\train.txt'  # 训练集文件地址 
path_val_set = 'ImageSets\\Main\\val.txt'  # 验证集文件地址 
path_test_set = 'ImageSets\\Main\\test.txt'  # 测试集文件地址 
path_labels = 'Annotations'  # 标签信息地址
path_images = 'JPEGImages'  # 图片信息地址

# 地址整合
path_train_set = os.path.join(path_VOC_datasets, path_train_set)
path_val_set = os.path.join(path_VOC_datasets, path_val_set)
path_test_set = os.path.join(path_VOC_datasets, path_test_set)
path_labels = os.path.join(path_VOC_datasets, path_labels)
path_images = os.path.join(path_VOC_datasets, path_images)

path_yolo_datasets = '.\\SAR-AIRcraft-1.0-yolo' # YOLO格式数据集地址
path_train_images = 'images\\train'  # 训练集图片地址 
path_train_labels = 'labels\\train'  # 训练集标签地址 
path_val_images = 'images\\val'  # 验证集图片地址 
path_val_labels = 'labels\\val'  # 验证集标签地址 
path_test_images = 'images\\test'  # 测试集图片地址 
path_test_labels = 'labels\\test'  # 测试集标签地址 

# 地址整合
path_train_images = os.path.join(path_yolo_datasets, path_train_images)
path_train_labels = os.path.join(path_yolo_datasets, path_train_labels)
path_val_images = os.path.join(path_yolo_datasets, path_val_images)
path_val_labels = os.path.join(path_yolo_datasets, path_val_labels)
path_test_images = os.path.join(path_yolo_datasets, path_test_images)
path_test_labels = os.path.join(path_yolo_datasets, path_test_labels)

# 文件后缀名
f_image_ext = '.jpg'
f_xml_ext = '.xml'
f_txt_ext = '.txt'

# yaml文件中类别名和标号对应字典
dict_name_class = {
    'A220': 0,
    'A320/321': 1,
    'A330': 2,
    'ARJ21': 3,
    'Boeing737': 4,
    'Boeing787': 5,
    'other': 6
}

# VOC格式标号读取
# filename：文件路径
def read_file(filename):
    file = open(filename, 'r')
    text_line = file.readlines()
    for i in range(len(text_line)):
        text_line[i] = text_line[i][:-1]
    file.close()
    return text_line

# 复制图片函数
# set：列表，读取到的文件标号
# file_extension：文件扩展名
# source：原数据集地址
# target_folder：目标文件夹
def copy_file(set, file_extension, source, target_folder):
    for i in range(len(set)):
        filename = os.path.join(source, set[i]) + file_extension
        try:
            shutil.copy(filename, target_folder)
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)


#  source：xml原路径 target_folder：写入txt路径
# VOC格式xml文件读取，分析，转化为txt，并写入目标文件夹
# set：列表，读取到的文件标号
# xml_ext：文件扩展名
# source：原数据集地址
# target_folder：目标文件夹
# txt_ext：文件扩展名
def VOC_to_TXT(set, xml_ext, source, target_folder, txt_ext):
    for i in range(len(set)):
        xml_file = os.path.join(source, set[i]) + xml_ext
        txt_file = os.path.join(target_folder, set[i]) + txt_ext

        tree = ET.parse(xml_file)
        root = tree.getroot()
        width = float(root.find('size').find('width').text)
        height = float(root.find('size').find('height').text)
        all_objects = root.findall('object')
        file = open(txt_file, 'w')
        for child in all_objects:
            num = dict_name_class[child.find('name').text]
            x_max = float(child.find('bndbox').find('xmax').text)
            y_max = float(child.find('bndbox').find('ymax').text)
            x_min = float(child.find('bndbox').find('xmin').text)
            y_min = float(child.find('bndbox').find('ymin').text)
            obj_x = (x_max + x_min) / width / 2.0
            obj_y = (y_max + y_min) / height / 2.0
            obj_width = (x_max - x_min) / width / 2.0
            obj_height = (y_max - y_min) / height / 2.0
            file.write(f'{num} {obj_x} {obj_y} {obj_width} {obj_height}\n')
        file.close()


# 读取每个集中图片名称
train_set = read_file(path_train_set)
val_set = read_file(path_val_set)
test_set = read_file(path_test_set)
print("Read Name Finish!")

#复制图片
copy_file(train_set, f_image_ext, path_images, path_train_images)
copy_file(val_set, f_image_ext, path_images, path_val_images)
copy_file(test_set, f_image_ext, path_images, path_test_images)
print("Copy Images Finish!")

# 转化xml到txt
# 读取H W，读取object的name、xymin、xymax，转换、计算，写入txt
VOC_to_TXT(train_set, f_xml_ext, path_labels, path_train_labels, f_txt_ext)
VOC_to_TXT(val_set, f_xml_ext, path_labels, path_val_labels, f_txt_ext)
VOC_to_TXT(test_set, f_xml_ext, path_labels, path_test_labels, f_txt_ext)
print("Convert Labels Finish!")