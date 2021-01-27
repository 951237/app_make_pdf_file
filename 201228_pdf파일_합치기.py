from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

# 작업 파일 패스
file_1 = 'C:\\Users\\User\\Desktop\\201228110458_0001.pdf'
file_2 = 'C:\\Users\\User\\Desktop\\201228110950_0001.pdf'

# 결과파일 패스
result = 'C:\\Users\\User\\Desktop\\result.pdf'

# 파일 불러오기
file1 = PdfFileReader(open(file_1, "rb"))
file2 = PdfFileReader(open(file_2, "rb"))

# pdf writer
pdf_writer = PdfFileWriter()

# pdf파일의 총 페이지
page_num = file1.getNumPages()

# 두개의 파일 번갈아가며 합치기
for i in range(page_num):
    pdf_writer.addPage(file1.getPage(0+i))
    pdf_writer.addPage(file2.getPage((page_num-1))-i)

result_file = open(result, "wb")

pdf_writer.write(result_file)
result_file.close()
