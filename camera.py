import tensorflow as tf

newImg = './newImg/'

import cv2
import time
import os
from PIL import Image
import shutil

f_time = open('time_memo.txt','w')

labels = []
for label in tf.gfile.GFile("output_labels.txt"):
    labels.append(label.rstrip())
with tf.gfile.FastGFile("output_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

def predict(filePath):
    image = tf.gfile.FastGFile(filePath, 'rb').read()
    predict = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image})
    top = predict[0].argsort()[-len(predict[0]):][::-1]
    for index in top:
        human_string = labels[index]
        score = predict[0][index]
        if float(score) > 0.5:
            print(human_string, score)
        if float(score) > 0.8:
            localtime = time.localtime(time.time())
            arr = [human_string,str(localtime.tm_year),str(localtime.tm_mon),str(localtime.tm_mday),
                       str(localtime.tm_hour), str(localtime.tm_min), str(localtime.tm_sec)]
            filename = '-'.join(arr)
            filename += '.jpg'
            if 'no' in human_string:
                save_path = './data/'+'no/'+filename
            else:
                save_path = './data/' + 'work/' + filename
            print(shutil.copy(filePath, save_path))
            f_time.write(str(save_path))
            f_time.write('\n')
            return

def deleteImg():
    fileArray = os.listdir(newImg)
    if len(fileArray) > 20:
        for name in fileArray:
            os.remove(newImg+name)
        # os.makedirs(newImg)
        print('success clean the folder!')
    return

if __name__ == '__main__':
    stime = time.asctime(time.localtime(time.time()))
    f_time.write('startime:  '+str(stime))
    f_time.write('\n')
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        cap = cv2.VideoCapture(0)
        start_time = time.time()
        while (True):
            ret, frame = cap.read()
            cv2.imshow('video',frame)
            if time.time() - start_time > 3:
                time_stamp = int(time.time() * 10)
                pic_name = newImg + str(time_stamp) + '.jpg'
                cv2.imwrite(pic_name, frame)
                # cv2.imshow('test',frame)
                predict(pic_name)
                start_time = time.time()
            deleteImg()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                etime = time.asctime(time.localtime(time.time()))
                f_time.write('endtime:  '+str(etime))
                f_time.write('\n')
                f_time.close()
                break
