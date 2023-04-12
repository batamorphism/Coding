import os
import PyPDF2

# 指定したフォルダのパス
folder_path = "C:/Users/Takanori/Desktop/chatGPT_TEXT/pdf"

# フォルダ内のすべてのPDFファイル名を取得
pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

# 各PDFファイルに対して
for pdf_file in pdf_files:
    # PDFファイルを開く
    with open(os.path.join(folder_path, pdf_file), "rb") as f:
        # PyPDF2オブジェクトを作成
        pdf = PyPDF2.PdfReader(f)
        # txtファイル名を決める（拡張子を変更）
        txt_file = pdf_file.replace(".pdf", ".txt")
        # txtファイルを作成して書き込む
        with open(os.path.join(folder_path, txt_file), "w", encoding="utf-8") as f:
            # PDFの各ページに対して
            for page_num in range(len(pdf.pages)):
                # ページオブジェクトを取得
                page = pdf.pages[page_num]
                # テキストを抽出
                text = page.extract_text()
                # txtファイルに書き込む
                f.write(text)