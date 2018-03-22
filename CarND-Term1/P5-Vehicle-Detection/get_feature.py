import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

from parameters import params
from skimage.feature import hog



# Define a function to compute binned color features  
def bin_spatial(img, size=(32, 32)):
    # Use cv2.resize().ravel() to create the feature vector
    color1 = cv2.resize(img, size).ravel()
    #color2 = cv2.resize(img[:,:,1], size).ravel()
    #color3 = cv2.resize(img[:,:,2], size).ravel()
    
    # Return the feature vector
    return color1

# Define a function to compute color histogram features  
def color_hist(img, nbins=32, bins_range=(0, 256)):
    # Compute the histogram of the color channels separately
    channel1_hist = np.histogram(img[:,:,0], bins=nbins, range=bins_range)
    channel2_hist = np.histogram(img[:,:,1], bins=nbins, range=bins_range)
    channel3_hist = np.histogram(img[:,:,2], bins=nbins, range=bins_range)
    # Concatenate the histograms into a single feature vector
    hist_features = np.concatenate((channel1_hist[0], channel2_hist[0], channel3_hist[0]))
    # Return the individual histograms, bin_centers and feature vector
    return hist_features

	# Define a function to return HOG features and visualization
def get_hog_features(img, orient, pix_per_cell, cell_per_block, 
                        vis=False, feature_vec=True):
    # Call with two outputs if vis==True
    if vis == True:
        features, hog_image = hog(img, orientations=orient, pixels_per_cell=(pix_per_cell, pix_per_cell),
                                  cells_per_block=(cell_per_block, cell_per_block), block_norm= 'L2-Hys',
                                  transform_sqrt=True, 
                                  visualise=vis, feature_vector=feature_vec)
        return features, hog_image
    # Otherwise call with one output
    else:      
        features = hog(img, orientations=orient, pixels_per_cell=(pix_per_cell, pix_per_cell),
                       cells_per_block=(cell_per_block, cell_per_block),block_norm= 'L2-Hys',
                       transform_sqrt=True, 
                       visualise=vis, feature_vector=feature_vec)
        return features
	

	
# Define a function to extract features from a single image window
# This function is very similar to extract_features()
# just for a single image rather than list of images
def single_img_features(img, cspace='RGB', spatial_size=(32, 32),
                        hist_bins=32, orient=9, 
                        pix_per_cell=8, cell_per_block=2, hog_channel='ALL',
                        spatial_feat=True, hist_feat=True, hog_feat=True):    
    #1) Define an empty list to receive features
    img_features = []
    
    #2) Apply color conversion if other than 'RGB'
    image=np.copy(img)
    #3) apply color conversion if other than 'RGB'
    if cspace != 'RGB':
        if cspace == 'HSV':
            feature_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        elif cspace == 'LUV':
            feature_image = cv2.cvtColor(image, cv2.COLOR_RGB2LUV)
        elif cspace == 'HLS':
            feature_image = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
        elif cspace == 'YUV':
            feature_image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
        elif cspace == 'YCrCb':
            feature_image = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
    else: feature_image = np.copy(image)      
    
	#4) If flag is set, apply bin_spatial() to get spatial color features
    if spatial_feat == True:
        spatial_features = bin_spatial(feature_image, size=spatial_size)
		# Append the new feature vector to the features list
        img_features.append(spatial_features)
    
	# If flag is set, apply color_hist() to get histogram features
    if hist_feat == True:
        hist_features = color_hist(feature_image, nbins=hist_bins)
		# Append the new feature vector to the features list
        img_features.append(hist_features)
    
    #5) If flag is set, call get_hog_features() with vis=False, feature_vec=True	
    if hog_feat == True:
    
        if hog_channel == 'ALL':
            hog_features = []
			# If hog_channel='ALL',looping the three channels
            for channel in range(feature_image.shape[2]):
                hog_features.extend(get_hog_features(feature_image[:,:,channel], 
                                    orient, pix_per_cell, cell_per_block, 
                                    vis=False, feature_vec=True))
            #hog_features = np.ravel(hog_features)        
        else:
            hog_features = get_hog_features(feature_image[:,:,hog_channel], orient, 
                        pix_per_cell, cell_per_block, vis=False, feature_vec=True)
        # Append the new feature vector to the features list
        img_features.append(hog_features)
    #6) Return concatenated array of features
    return np.concatenate(img_features)
	
# Define a function to extract features from a list of images
# Have this function call bin_spatial() and color_hist()
def extract_features(imgs, cspace='RGB', spatial_size=(32, 32),
                        hist_bins=32, orient=9, 
                        pix_per_cell=8, cell_per_block=2, hog_channel='ALL',
                        spatial_feat=True, hist_feat=True, hog_feat=True):
    # Create a list to append feature vectors to
    features = []
    # Iterate through the list of images

    for img in imgs:
        # Read ,resize,and convert color in each one by one
        image = cv2.imread(img)
        image = cv2.resize(image, (64, 64))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #Get feature of single image		
        file_features = single_img_features(image, cspace, spatial_size,
						hist_bins, orient, 
						pix_per_cell, cell_per_block, hog_channel,
						spatial_feat, hist_feat, hog_feat)
		# Append the new feature vector to the features list	
        features.append(file_features)

	
		# Return list of feature vectors
    return features

if __name__ == '__main__':

	#the parameters which will be used later is defined on parameters.py
	spatial_size = params['spatial_size'] 
	hist_bins = params['hist_bins']
	orient = params['orient']
	pix_per_cell  = params['pix_per_cell']
	cell_per_block = params['cell_per_block']
	
	
	#Read the single image for test
	image = cv2.imread('./train_data/vehicles/GTI_Far/image0000.png')
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	
	#Execute the get_hog_features() function to ensure the correct extration of hog features
	hog_features, hog_image = get_hog_features(image[ :, :,0], orient, pix_per_cell, cell_per_block, 
	                    vis=True, feature_vec=True)
	plt.imsave('./features_image/hog_image.png',hog_image)
	
	#Execute the bin_spatial() function to ensure the correct extration of spatial_features
	spatial_plot_fig=plt.figure()
	spatial_features=bin_spatial(image,spatial_size)
	plt.plot(spatial_features)
	spatial_plot_fig.savefig('./features_image/spatial_plot.png')
	
	#Execute the color_hist() function to ensure the correct extration of histogram features
	color_hist_fig=plt.figure()
	color_hist_features = color_hist(image,hist_bins,(0,256))
	plt.hist(color_hist_features)
	color_hist_fig.savefig('./features_image/color_hist.png')