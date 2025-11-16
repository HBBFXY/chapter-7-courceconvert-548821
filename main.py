# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)  # 存储Python所有保留字的集合

# 以下内容自行完成
# 示例功能：读取文件并将非保留字转为大写
def convert_file(source_file, target_file):
    with open(source_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    processed_lines = []
    for line in lines:
        words = line.split()
        new_words = []
        for word in words:
            # 判断是否为保留字，非保留字转大写
            if word not in reserved_words:
                word = word.upper()
            new_words.append(word)
        processed_lines.append(" ".join(new_words) + "\n")
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.writelines(processed_lines)

# 调用示例（需根据实际需求调整文件名）
convert_file("random_int.py", "converted_random_int.py")
