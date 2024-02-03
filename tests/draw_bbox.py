import os
import xml.etree.ElementTree as ET
import cv2

abs_path = 'D:\\Hardware\\Project\\Graduation_Project\\software'

path_VOC_datasets = 'datasets\\SAR-AIRcraft-1.0'  # VOC格式数据集地址
path_train_set = 'ImageSets\\Main\\train.txt'  # 训练集文件地址
path_val_set = 'ImageSets\\Main\\val.txt'  # 验证集文件地址
path_test_set = 'ImageSets\\Main\\test.txt'  # 测试集文件地址
path_labels = 'Annotations'  # 标签信息地址
path_images = 'JPEGImages'  # 图片信息地址

# 地址整合
path_train_set = os.path.join(abs_path, path_VOC_datasets, path_train_set)
path_val_set = os.path.join(abs_path, path_VOC_datasets, path_val_set)
path_test_set = os.path.join(abs_path, path_VOC_datasets, path_test_set)
path_labels = os.path.join(abs_path, path_VOC_datasets, path_labels)
path_images = os.path.join(abs_path, path_VOC_datasets, path_images)

path_bbox_datasets = 'datasets\\SAR-AIRcraft-1.0-BBOX' # YOLO格式数据集地址
path_train_images = 'train'  # 训练集图片地址
path_val_images = 'val'  # 验证集图片地址
path_test_images = 'test'  # 测试集图片地址

path_train_images = os.path.join(abs_path, path_bbox_datasets, path_train_images)
path_val_images = os.path.join(abs_path, path_bbox_datasets, path_val_images)
path_test_images = os.path.join(abs_path, path_bbox_datasets, path_test_images)


# yaml文件中类别名和标号对应字典
dict_name_color = {
    'A220': (0, 69, 255),# OrangeRed1
    'A320/321': (180, 110, 255),# HotPink1
    'A330': (79, 165, 255),# Tan1
    'ARJ21': (238, 58, 178),# DarkOrchid2
    'Boeing737': (50, 205, 154),#YellowGreen
    'Boeing787': (255, 144, 30),#DodgerBlue
    'other': (114, 128, 250)# Salmon
}

dict_name_classname = {
    'A220': '1.',
    'A320/321': '2.',
    'A330': '3.',
    'ARJ21': '4.',
    'Boeing737': '5.',
    'Boeing787': '6.',
    'other': '7.'
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


def make_bbox(set, xml_folder, jpg_folder, target_folder):
    for i in range(len(set)):
        xml_file = os.path.join(xml_folder, set[i]) + '.xml'
        jpg_file = os.path.join(jpg_folder, set[i]) + '.jpg'
        bbox_file = os.path.join(target_folder, set[i]) + '.jpg'
        image = cv2.imread(jpg_file)

        tree = ET.parse(xml_file)
        root = tree.getroot()
        all_objects = root.findall('object')
        for child in all_objects:
            name = child.find('name').text
            color = dict_name_color[name]
            x_max = int(child.find('bndbox').find('xmax').text)
            y_max = int(child.find('bndbox').find('ymax').text)
            x_min = int(child.find('bndbox').find('xmin').text)
            y_min = int(child.find('bndbox').find('ymin').text)

            cv2.rectangle(image, [x_min, y_min], [x_max, y_max], color, 4)
            font = cv2.FONT_HERSHEY_SIMPLEX
            text = dict_name_classname[name] + name
            cv2.putText(image, text, (x_min, y_min-10), font, 0.8, color, 2)
            cv2.imwrite(bbox_file, image)


# 读取每个集中图片名称
train_set = read_file(path_train_set)
val_set = read_file(path_val_set)
test_set = read_file(path_test_set)
print("Read Name Finish!")



# test_img=['0000001','0000002','0000003','0000004','0000005']
# make_bbox(test_img, path_labels, path_images, path_train_images)
make_bbox(train_set, path_labels, path_images, path_train_images)
make_bbox(val_set, path_labels, path_images, path_val_images)
make_bbox(test_set, path_labels, path_images, path_test_images)
print("Draw BBOX Finish!")




