import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pickle
import os
import string
import random
from parameters import params
from get_feature import single_img_features
from scipy.ndimage.measurements import label
from collections import deque



def id_generator(size=18, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
# Define a function you will pass an image 
# and the list of windows to be searched (output of slide_windows())
def search_windows(img, windows, clf, scaler, color_space='RGB', 
                    spatial_size=(32, 32), hist_bins=32, 
                    hist_range=(0, 256), orient=9, 
                    pix_per_cell=8, cell_per_block=2, 
                    hog_channel=0, spatial_feat=True, 
                    hist_feat=True, hog_feat=True):

    #1) Create an empty list to receive positive detection windows
    on_windows = []
    #2) Iterate over all windows in the list
    for window in windows:
        #3) Extract the test window from original image
        test_img = cv2.resize(img[window[0][1]:window[1][1], window[0][0]:window[1][0]], (64, 64))
        
        #4) Extract features for that window using single_img_features()
        features = single_img_features(test_img, cspace=color_space, 
                            spatial_size=spatial_size, hist_bins=hist_bins, 
                            orient=orient, pix_per_cell=pix_per_cell, 
                            cell_per_block=cell_per_block, 
                            hog_channel=hog_channel, spatial_feat=spatial_feat, 
                            hist_feat=hist_feat, hog_feat=hog_feat)
        #5) Scale extracted features to be fed to classifier
        test_features = scaler.transform(np.array(features).reshape(1, -1))
        #6) Predict using your classifier
        prediction = clf.predict(test_features)
        #7) If positive (prediction == 1) then save the window
        if prediction == 1:
			#This directory is for the collection for the positive prediction 
			#but containing negative result
			#I clasified them by hand to have hard negative mining
            #test_img_dir='./hard_negative/'+id_generator()+'.png'
            #plt.imsave(test_img_dir,test_img)
            on_windows.append(window)
    #8) Return windows for positive detections
    return on_windows


# Define a function that takes an image,
# start and stop positions in both x and y,
def multi_scale_slide_window(img, x_start_stop=[None, None], y_start_stop=[None, None]):
	#Define an empty list to receive windows
	window_scales = []

	#Same image will have 3 different scale of sliding windows to enhance the detection quality 
	windows_128 = slide_window(img, x_start_stop, y_start_stop, xy_window=(128, 128))
	windows_64 = slide_window(img, x_start_stop, y_start_stop, xy_window=(64, 64))
	windows_32 = slide_window(img, x_start_stop, y_start_stop, xy_window=(32, 32))

	#Concatenate the 3 type windows to form a windows list
	return windows_128+windows_64+windows_32

# Define a function that takes an image,
# start and stop positions in both x and y, 
# window size (x and y dimensions),  
# and overlap fraction (for both x and y)	
def slide_window(img, x_start_stop=[None, None], y_start_stop=[None, None], 
                    xy_window=(64, 64), xy_overlap=(0.8, 0.8)):
    # If x and/or y start/stop positions not defined, set to image size
    if x_start_stop[0] == None:
        x_start_stop[0] = 0
    if x_start_stop[1] == None:
        x_start_stop[1] = img.shape[1]
    if y_start_stop[0] == None:
        y_start_stop[0] = 0
    if y_start_stop[1] == None:
        y_start_stop[1] = img.shape[0]
    # Compute the span of the region to be searched    
    xspan = x_start_stop[1] - x_start_stop[0]
    yspan = y_start_stop[1] - y_start_stop[0]
    # Compute the number of pixels per step in x/y
    nx_pix_per_step = np.int(xy_window[0]*(1 - xy_overlap[0]))
    ny_pix_per_step = np.int(xy_window[1]*(1 - xy_overlap[1]))
    # Compute the number of windows in x/y
    nx_buffer = np.int(xy_window[0]*(xy_overlap[0]))
    ny_buffer = np.int(xy_window[1]*(xy_overlap[1]))
    nx_windows = np.int((xspan-nx_buffer)/nx_pix_per_step) 
    ny_windows = np.int((yspan-ny_buffer)/ny_pix_per_step) 
    # Initialize a list to append window positions to
    window_list = []
	
    
	#Define the parameter wii be used in the later loop
    x_window_size = xy_window[0]	#The length in x-axis of a window
    y_window_size = xy_window[1]	#The length in y-axis of a window
    starty = y_start_stop[0]		#The top left y of a window
	# Loop through finding x and y window positions
    # Note: you could vectorize this step, but in practice
    # you'll be considering windows one by one with your
    # classifier, so looping makes sense
    while starty + y_window_size < y_start_stop[1]:
    	# The top left x of a window
    	startx = x_start_stop[0]
    	while startx < x_start_stop[1]:
			# Compute the bottom right of a window
    		endx=startx+x_window_size
    		endy=starty+y_window_size
    		# Append the new window to the window lists
    		window_list.append(((startx, starty), (endx, endy)))
			# Compute the new top left x of a window
    		startx = startx + nx_pix_per_step
		#increse the scale of windows in the new row
    	x_window_size = int(x_window_size*1.3)
    	y_window_size = int(y_window_size*1.3)
		# Compute the new number of pixels per step in x/y
    	nx_pix_per_step = np.int(x_window_size*(1 - xy_overlap[0]))
    	ny_pix_per_step = np.int(y_window_size*(1 - xy_overlap[1]))
		#Compute the new top left y of a window
    	starty = starty + ny_pix_per_step
	# Return list of window positions
    return window_list

def add_heat(heatmap, bbox_list):
    # Iterate through list of bboxes
    for box in bbox_list:
        # Add += 1 for all pixels inside each bbox
        # Assuming each "box" takes the form ((x1, y1), (x2, y2))
        heatmap[box[0][1]:box[1][1], box[0][0]:box[1][0]] += 1

    # Return updated heatmap
    return heatmap
    
def apply_threshold(heatmap, threshold):
    # Zero out pixels below the threshold	
    heatmap[heatmap <= threshold] = 0
    # apply threshold and morphological closure to remove noise
    #ret, heatmap_threshold = cv2.threshold(heatmap, threshold, 255, type=cv2.THRESH_BINARY)
    #heatmap_threshold = cv2.morphologyEx(heatmap_threshold, op=cv2.MORPH_CLOSE,
    #kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13)), iterations=1)
	
	# Return thresholded map
    return heatmap
	
# Define a function to draw bounding boxes
def draw_boxes(img, bboxes, color=(0, 0, 255), thick=2):
    # Make a copy of the image
    imcopy = np.copy(img)
    # Iterate through the bounding boxes
    for bbox in bboxes:
        # Draw a rectangle given bbox coordinates
        cv2.rectangle(imcopy, bbox[0], bbox[1], color, thick)
		
    # Return the image copy with boxes drawn
    return imcopy

def draw_labeled_vehicle(img, labels):
    # Iterate through all detected cars
    for car_number in range(1, labels[1]+1):
        # Find pixels with each car_number label value
        nonzero = (labels[0] == car_number).nonzero()
        # Identify x and y values of those pixels
        nonzeroy = np.array(nonzero[0])
        nonzerox = np.array(nonzero[1])
        # Define a bounding box based on min/max x and y
        bbox = ((np.min(nonzerox), np.min(nonzeroy)), (np.max(nonzerox), np.max(nonzeroy)))
        # Draw the box on the image
        cv2.rectangle(img, bbox[0], bbox[1], (0,0,255), 6)
    # Return the image
    return img	

#Define a function processing the queue for the heatmap
def cache_heat_deque(heatmap, box_deque):
	
	for bbox_list in box_deque:
		for box in bbox_list:
		# Add += 1 for all pixels inside each bbox
		# Assuming each "box" takes the form ((x1, y1), (x2, y2))
			heatmap[box[0][1]:box[1][1], box[0][0]:box[1][0]] += 1
		
	# Return updated heatmap
	return heatmap
#Define a function that can process the video image
def pipeline_subprocess(image, clf, scaler, color_space='RGB', spatial_size=(32,32), hist_bins=32, hist_range=(0,256), 
						orient=9, pix_per_cell=8, cell_per_block=2, hog_channel='ALL', spatial_feat=True,
						hist_feat=True, hog_feat=True, y_start_stop=[None,None],heat_queue=deque(maxlen=25)):
	
	#1) Get the slide windows from the 3 scales of slide windows
	windows = multi_scale_slide_window(image, x_start_stop=[None, None], y_start_stop = y_start_stop)
	#2) Get the hot windows from the search funtion based on the pre_training classifier, scaler and the windows from #1)	
	hot_windows = search_windows(image, windows, clf, scaler, color_space, 
					spatial_size, hist_bins, hist_range, 
					orient, pix_per_cell, 
					cell_per_block, 
					hog_channel, spatial_feat, 
					hist_feat, hog_feat)                       
	
	#Add new window list to the queue
	heat_queue.append(hot_windows)

	heat = np.zeros_like(image[:,:,0]).astype(np.float)
	
	# Add heat to each box in box list in the queue
	heat = cache_heat_deque(heat,heat_queue)

	# Apply threshold to help remove false positives
	heat = apply_threshold(heat,45)
	
	# Visualize the heatmap when displaying    
	heatmap = np.clip(heat, 0, 255)
	
	# Find final boxes from heatmap using label function
	labels = label(heatmap)
	draw_img = draw_labeled_vehicle(np.copy(image), labels)
	# Return the image
	return draw_img

if __name__ == '__main__':
	
	# load a pe-trained svc model from a serialized (pickle) file
	svc = pickle.load( open("./dump_data/svc.p", "rb" ) )
	X_scaler = pickle.load( open("./dump_data/scaler.p", "rb" ) )
	
	#the parameters which will be used later is defined on parameters.py
	color_space = params['color_space']  
	spatial_size = params['spatial_size'] 
	hist_bins = params['hist_bins']
	hist_range = params['hist_range']
	orient = params['orient']
	pix_per_cell  = params['pix_per_cell']
	cell_per_block = params['cell_per_block']
	hog_channel = params['hog_channel']
	spatial_feat = params['spatial_feat']
	hist_feat = params['hist_feat']
	hog_feat = params['hog_feat']
	y_start_stop = params['y_start_stop']
	
	#1) Read the single image for test to ensure the correct execution of each function
	image = cv2.imread('./test_images/test1.jpg')
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	draw_image = np.copy(image)
	
	#2) Get the slide windows image from the 3 scales of slide windows
	windows = multi_scale_slide_window(image, x_start_stop=[None, None], y_start_stop = y_start_stop)
	window_img = draw_boxes(draw_image, windows, color=(0, 0, 255), thick=2)
	plt.imsave('./windows_image/slide_window.jpg',window_img)
	
	#3) Get the hot windows image from the search funtion based on the pre_training classifier, scaler and the windows from #2)
	hot_windows = search_windows(image, windows, svc, X_scaler, color_space, 
						spatial_size, hist_bins, hist_range, 
						orient, pix_per_cell, 
						cell_per_block, 
						hog_channel, spatial_feat, 
						hist_feat, hog_feat)   
	
	hot_window_img = draw_boxes(draw_image, hot_windows, color=(0, 0, 255), thick=2)
	plt.imsave('./windows_image/hot_window.jpg',hot_window_img)
	
	#4) Get the heatmap image based on the hot_windows from #3)
	#print (len(hot_windows))
	
	heat = np.zeros_like(image[:,:,0]).astype(np.float)
	
	# Add heat to each box in box list
	heat = add_heat(heat,hot_windows)
	
	# Apply threshold to help remove false positives
	heat = apply_threshold(heat,4)
	
	# Visualize the heatmap when displaying    
	heatmap = np.clip(heat, 0, 255)
	plt.imsave('./windows_image/heatmap.jpg',heatmap, cmap='hot')
	
	#5) Get the final detect image based on the heatmap from #4)
	# Find final boxes from heatmap using label function
	labels = label(heatmap)
	draw_img = draw_labeled_vehicle(np.copy(image), labels)
	plt.imsave('./windows_image/final_detect.jpg',draw_img)
	
	# Iterate through all test images in the test_images directory,then save them in the output_images directory
	for file in os.listdir('./test_images'):
		image = cv2.imread(os.path.join('./test_images', file))
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		draw_img = pipeline_subprocess(image, svc, X_scaler, color_space, spatial_size, hist_bins, hist_range, 
										orient, pix_per_cell, cell_per_block, hog_channel, spatial_feat,
										hist_feat, hog_feat, y_start_stop)
		store_image_dir = "./output_images/" + file
		print ('writing...')
		plt.imsave(store_image_dir,draw_img)
					
	