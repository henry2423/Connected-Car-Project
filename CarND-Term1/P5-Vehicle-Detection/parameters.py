#the parameters will be used in features extraction 
params = {	'color_space' : 'YCrCb' , 	# Can be RGB, HSV, LUV, HLS, YUV, YCrCb
			'spatial_size' : (32, 32),	# Spatial binning dimensions
			'hist_bins' : 32, 			# Number of histogram bins
			'hist_range' : (0, 256),	# The range of Histogram
			'orient' : 9, 				# HOG orientations
			'pix_per_cell' : 8, 		# HOG pixels per cell
			'cell_per_block' : 2, 		# HOG cells per block
			'hog_channel' : 'ALL',		# Can be 0, 1, 2, or "ALL"
			'spatial_feat' : True, 		# Spatial features on or off
			'hist_feat' : True,			# Histogram features on or off
			'hog_feat' : True,			# HOG features on or off
			'y_start_stop' : (400, 650)	# Min and max in y-axis to search sliding windows  

}