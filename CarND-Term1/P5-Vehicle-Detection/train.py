from get_feature import extract_features
from parameters import params
import numpy as np
import pickle
import os
import time
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler

if __name__=='__main__':
	

	# The parameters which will be used later is defined on parameters.py
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
	
	
	#Define empty lists to car/not car images
	cars = []
	notcars = []
	
	#Define the path containing the training image of car/not car
	car_train_folder= ['./train_data/vehicles/GTI_Far', './train_data/vehicles/GTI_Left', './train_data/vehicles/GTI_MiddleClose', './train_data/vehicles/GTI_Right', './train_data/vehicles/KITTI_extracted','./train_data/vehicles/car_mix']	
	notcar_train_folder = ['./train_data/non-vehicles/Extras', './train_data/non-vehicles/GTI','./train_data/non-vehicles/notcar_hard_neg']
	
	#Get all image in the car_train_folder
	for folder in car_train_folder:
		for image in os.listdir(folder):
				cars.append(folder+'/'+image)
				
	#Get all image in the notcar_train_folder
	for folder in notcar_train_folder:
		for image in os.listdir(folder):
				notcars.append(folder+'/'+image)	
		
	#Define the sample size to ensure the data balance
	#sample_size=8700
	#cars = cars[0:sample_size]
	#notcars = notcars [0:sample_size]
	print (len(cars))
	print (len(notcars))
	#	Get car features
	car_features = extract_features(cars, color_space, spatial_size , hist_bins, 
						orient, pix_per_cell, cell_per_block, 
	                    hog_channel, spatial_feat, hist_feat, hog_feat)
	
	#	Get not car features
	notcar_features = extract_features(notcars, color_space, spatial_size , hist_bins, 
						orient, pix_per_cell, cell_per_block, 
	                    hog_channel, spatial_feat, hist_feat, hog_feat)
	
	
	
	# Create an array stack of feature vectors
	X = np.vstack((car_features, notcar_features)).astype(np.float64)
	# Fit a per-column scaler
	X_scaler = StandardScaler().fit(X)
	# Apply the scaler to X
	X__scaler = X_scaler.transform(X)
	# Define the labels vector
	y = np.hstack((np.ones(len(car_features)), np.zeros(len(notcar_features))))
	
	
	# Split up data into randomized training and test sets
	rand_state = np.random.randint(0, 100)
	X_train, X_test, y_train, y_test = train_test_split(
	X__scaler, y, test_size=0.2, random_state=rand_state)
	
		
	print('Feature vector length:', len(X_train[0]))
	# Use a linear SVC 
	svc = LinearSVC()
	# Check the training time for the SVC
	t=time.time()
	svc.fit(X_train, y_train)
	t2 = time.time()
	print(round(t2-t, 2), 'Seconds to train SVC...')
	# Check the score of the SVC
	print('Test Accuracy of SVC = ', round(svc.score(X_test, y_test), 4))
	
	
	#Dump the classifier and scaler for later use
	pickle.dump( svc, open( "./dump_data/svc.p", "wb" ) )
	pickle.dump( X_scaler, open( "./dump_data/scaler.p", "wb" ) )
	
