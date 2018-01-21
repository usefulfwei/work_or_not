# -*- coding: utf-8 -*-

# author:Lichang
import cv2
import os
from PIL import Image
import numpy as np

# arr = [r'./video/work/',r'./video/no/']
arr = [r'./video/work/']
save_arr = [r'./data/work/',r'./data/no/']
count = 0
for path in arr:
    for name in os.listdir(path):
        print(name, 'videoname')
        video_file = os.path.join(path, name)
        cap = cv2.VideoCapture(video_file)
        ret, frame = cap.read()
        while ret == True:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            if 'video/work' in video_file:
                img.save(save_arr[0] + str(count) + '_work.jpg')
            else:
                img.save(save_arr[1] + str(count) + '_no.jpg')
            print('save one')
            count += 1
            ret, frame = cap.read()
