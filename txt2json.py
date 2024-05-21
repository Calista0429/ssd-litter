import json

def txt_to_json(txt_file, json_file):
    # 读取文本文件中的所有行，并去除空白字符
    with open(txt_file, 'r') as file:
        categories = [line.strip() for line in file.readlines() if line.strip()]

    # 为每个类别分配一个从1开始的编号
    category_dict = {category: index + 1 for index, category in enumerate(categories)}

    # 将字典写入JSON文件
    with open(json_file, 'w') as file:
        json.dump(category_dict, file, indent=4)

    print("JSON文件已生成:", json_file)

# 使用示例
txt_to_json('classes.txt', 'pascal_voc_classes.json')
