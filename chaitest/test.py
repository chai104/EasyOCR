import easyocr
GPU = False
#reader = easyocr.Reader(['ch_tra', 'en'])
#result = reader.readtext('chinese_tra.jpg')
#print(result)

#reader1 = easyocr.Reader(['en','th'],gpu=False,detect_network="dbnet18")
reader1 = easyocr.Reader(['en','th'],gpu=False)
result1 = reader1.readtext('../idcard1.jpg')
print (*result1,sep="\n")
#print('Hello, world!')
