import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from os.path import join, basename
# Import everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip
try:
    # for Python2
    from IPython.display import html 
except ImportError:
    # for Python3
    from IPython.display import HTML 
import os
from project1_lanedetection_process import color_frame_process
try:
    # for Python2
    from tkinter import *
except ImportError:
    # for Python3
    from Tkinter import *
#processing video copy from https://github.com/ndrplz/self-driving-car
if __name__ == '__main__':
    resize_h, resize_w = 540, 960
    
    if (False):
        img = cv2.imread('test.jpg')
        cv2.imwrite('./out.jpg',color_frame_process(image=cv2.resize(img, (resize_w, resize_h))))
        
    
    else:
        test_videos_dir = join('test_videos')
        test_videos = [join(test_videos_dir, name) for name in os.listdir(test_videos_dir)]
        
        for test_video in test_videos:
            new_clip_output = join('test_videos_output', basename(test_video))
            test_clip = VideoFileClip(test_video)
            new_clip = test_clip.fl_image(lambda x: color_frame_process(image=cv2.resize(x, (resize_w, resize_h)))) #NOTE: this function expects color images!!
            new_clip.write_videofile(new_clip_output,audio=False)
            HTML("""
            <video width="640" height="300" controls>
              <source src="{0}" type="video/mp4">
            </video>
            """.format(new_clip_output))


