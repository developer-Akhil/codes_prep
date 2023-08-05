import sys
import os, os.path
import comtypes.client

from os import walk

input_dir = 'C:\\Users\\Akhilesh Chand\\Downloads\\test\\sample.rtf'
output_dir = 'C:\\Users\\Akhilesh Chand\\Downloads\\test.pdf'

# f = []
# for (dirpath, dirnames, filenames) in walk(input_dir):
#     print(dirnames)
#     break
# print(f)
# sys.exit()
wdFormatPDF = 17

for (subdir, dirs, files) in walk(input_dir):
    for file in files:
        in_file = os.path.join(subdir, file)
        output_file = file.split('.')[0]
        out_file = output_dir+output_file+'.pdf'
        word = comtypes.client.CreateObject('Word.Application')

        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
