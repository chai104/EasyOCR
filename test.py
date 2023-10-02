import easyocr
import time
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

start_time = time.time()
reader1 = easyocr.Reader(['en','th'],gpu=False)
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)

start_time = time.time()
result1 = reader1.readtext('idcard1.jpg')
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)

print (result1,sep='\n')
#print('Hello, world!')
