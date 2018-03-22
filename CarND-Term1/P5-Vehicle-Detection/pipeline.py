import pickle
from search_classify import pipeline_subprocess
from moviepy.editor import VideoFileClip
from parameters import params
from collections import deque

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
	#the queue is for the temporal saving of heatmap
	heat_queue = deque(maxlen=25)
	#Process the project video
	test_clip = VideoFileClip('./project_video.mp4')
	new_clip = test_clip.fl_image(lambda x: pipeline_subprocess(x, svc, X_scaler, color_space, spatial_size, hist_bins,
																hist_range,orient, pix_per_cell, cell_per_block,
																hog_channel,spatial_feat,hist_feat, hog_feat, y_start_stop,heat_queue) ) #NOTE: this function expects color images!!
	new_clip.write_videofile('./project_video_out.mp4',audio=False)