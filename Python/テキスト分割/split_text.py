import os

def split_file(file_path):
    with open(file_path, 'r',  encoding='utf-8') as f:
        file_name = os.path.basename(file_path)
        file_root, file_ext = os.path.splitext(file_name)
        count = 1
        while True:
            text = f.read(1000)
            # 改行を消す
            text = text.replace('\r', '').replace('\n', '')
            if not text:
                break
            output_file_path = f"{file_root}_{count}{file_ext}"
            with open(output_file_path, 'w') as output_file:
                output_file.write(text)
            count += 1

# 使用例
split_file('C:/Users/Takanori/Desktop/txt.txt')
