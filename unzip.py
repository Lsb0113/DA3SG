import os
import zipfile

# root = './data/3RScan'
# with open('./data/3DSSG_subset/train_scans.txt') as file:
#     idx_list = file.readlines()
#
# for i in range(len(idx_list)):
#     if i==len(idx_list)-1:
#         idx_list[i] = idx_list[i]
#     idx_list[i] = idx_list[i][:-1]
#
# print(idx_list)
# for j in range(len(idx_list)):
#     file_path = os.path.join(root, idx_list[j])
#     if os.path.exists(os.path.join(file_path, 'sequence.zip')):
#         if os.path.exists(os.path.join(file_path, 'sequence')):
#             os.remove(os.path.join(file_path, 'sequence.zip'))
#         else:
#             os.makedirs(os.path.join(file_path, 'sequence'))
#             zip_path = os.path.join(file_path, 'sequence.zip')
#             with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#                 # 解压所有文件到指定目标文件夹
#                 zip_ref.extractall(os.path.join(file_path, 'sequence'))
#             os.remove(os.path.join(file_path, 'sequence.zip'))


def walkFile(file):
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历所有的文件夹
        for d in dirs:
            if os.path.exists(os.path.join(root, d, 'sequence')):  # 判断sequence文件夹是否存在
                continue
            else:  # 创建sequence文件夹，并且把压缩文件解压到指定文件夹。
                os.makedirs(os.path.join(root, d, 'sequence'))
                zip_path = os.path.join(root, d, 'sequence.zip')
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    # 解压所有文件到指定目标文件夹
                    zip_ref.extractall(os.path.join(root, d, 'sequence'))
                    os.remove(os.path.join(root, d, 'sequence.zip'))
                    # count += 1
                    # print(f'-----------{count}-------------')
                    # print(root)
        # 遍历文件
        # for f in files:
        #     print(os.path.join(root, f))


walkFile("./data/3RScan")


# # 查找文件是否存在？
# save_txt = 'no_view_txt.txt'
#
#
# def walkFile(file):
#     for root, dirs, files in os.walk(file):
#         # root 表示当前正在访问的文件夹路径
#         # dirs 表示该文件夹下的子目录名list
#         # files 表示该文件夹下的文件list
#         # 遍历所有的文件夹
#         print(dirs)
#         for d in dirs:
#             if os.path.exists(os.path.join(root, d, 'multi_view')):  # 判断sequence文件夹是否存在
#                 continue
#             else:
#                 with open(save_txt, 'a', encoding='utf-8') as f:
#                     f.write(d + '\n')
#         # 遍历文件
#         # for f in files:
#         #     print(os.path.join(root, f))
#
#
# walkFile("./data/3RScan")
