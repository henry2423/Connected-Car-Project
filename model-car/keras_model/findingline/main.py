import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import glob
from os.path import join, basename

from find_line import find_lines
from color_pipeline import calibrate_camera, calibrate_image
from drawline import draw_lines


# Import everything needed to edit/save/watch video clips
# from moviepy.editor import VideoFileClip
try:
    # for Python2
    from IPython.display import html 
except ImportError:
    # for Python3
    from IPython.display import HTML 
import os
#from project1_lanedetection_process import color_frame_process
try:
    # for Python2
    from tkinter import *
except ImportError:
    # for Python3
    from Tkinter import *

    
    
def process(image):
    frame = image
    img_size = (frame.shape[1], frame.shape[0])

    src = np.float32([[img_size[0], img_size[1]-10], 
                      [0, img_size[1]-10],
                      [240, 460],  
                      [450, 460]]) 
    dst = np.float32([[img_size[0], img_size[1]],      
                      [0, img_size[1]],   
                      [0, 0],      
                      [img_size[0], 0]])    
        
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(frame, M, img_size, flags=cv2.INTER_LINEAR)
    left_fit, right_fit, left_fitx, right_fitx, ploty = find_lines(warped)
    return draw_lines(frame, warped, left_fit, right_fit,  left_fitx, right_fitx , ploty)
    
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
    f.tight_layout()
    
    ax1.imshow(warped)
    ax1.set_title('eyebird', fontsize=50)
    #ax2.imshow(warped2)
    ax2.set_title('Undistorted and Warped Image', fontsize=50)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
    #plt.show()



if __name__ == '__main__':
    resize_h, resize_w = 540, 960
    """
    test_videos_dir = join('test_videos')
    test_videos = [join(test_videos_dir, name) for name in os.listdir(test_videos_dir)]
    
    for test_video in test_videos:
        new_clip_output = join('test_videos_output', basename(test_video))
        test_clip = VideoFileClip(test_video)
        new_clip = test_clip.fl_image(lambda x: color_frame_process(image=cv2.resize(x, (resize_w, resize_h)))) #NOTE: this function expects color images!!
        new_clip.write_videofile(new_clip_output,audio=False)
        HTML('''
        <video width="640" height="300" controls>
          <source src="{0}" type="video/mp4">
        </video>
        '''.format(new_clip_output))
		"""
	
    ret, mtx, dist, rvecs, tvecs = calibrate_camera()

    testimg = cv2.imread('./test_images/test1.jpg')
    cv2.imwrite('./output_images/test1.jpg',process(testimg, ret, mtx, dist, rvecs, tvecs))
    testimg = cv2.imread('./test_images/test2.jpg')
    cv2.imwrite('./output_images/test2.jpg',process(testimg, ret, mtx, dist, rvecs, tvecs))
    testimg = cv2.imread('./test_images/test3.jpg')
    cv2.imwrite('./output_images/test3.jpg',process(testimg, ret, mtx, dist, rvecs, tvecs))
    testimg = cv2.imread('./test_images/test4.jpg')
    cv2.imwrite('./output_images/test4.jpg',process(testimg, ret, mtx, dist, rvecs, tvecs))
    testimg = cv2.imread('./test_images/test5.jpg')
    cv2.imwrite('./output_images/test5.jpg',process(testimg, ret, mtx, dist, rvecs, tvecs))
    testimg = cv2.imread('./test_images/test6.jpg')
    cv2.imwrite('./output_images/test6.jpg',process(testimg, ret, mtx, dist, rvecs, tvecs))
    
    test_clip = VideoFileClip('./project_video.mp4')
    

    new_clip = test_clip.fl_image(lambda x: process(x, ret, mtx, dist, rvecs, tvecs)) #NOTE: this function expects color images!!
    new_clip.write_videofile('./out.mp4',audio=False)
    
    
    
    
    
