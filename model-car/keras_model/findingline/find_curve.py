import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import cv2

def find_curve(left_fitx, right_fitx)
	leftx = left_fitx
	rightx = right_fitx
	# Plot up the fake data
	mark_size = 3
	plt.plot(leftx, ploty, 'o', color='red', markersize=mark_size)
	plt.plot(rightx, ploty, 'o', color='blue', markersize=mark_size)
	plt.xlim(0, 1280)
	plt.ylim(0, 720)
	plt.plot(left_fitx, ploty, color='green', linewidth=3)
	plt.plot(right_fitx, ploty, color='green', linewidth=3)
	plt.gca().invert_yaxis() # to visualize as we do the images

	y_eval = np.max(ploty)
	left_curverad = ((1 + (2*left_fit[0]*y_eval + left_fit[1])**2)**1.5) / np.absolute(2*left_fit[0])
	right_curverad = ((1 + (2*right_fit[0]*y_eval + right_fit[1])**2)**1.5) / np.absolute(2*right_fit[0])
	#print(left_curverad, right_curverad)

	# Define conversions in x and y from pixels space to meters
	ym_per_pix = 30/720 # meters per pixel in y dimension
	xm_per_pix = 3.7/700 # meters per pixel in x dimension

	# Fit new polynomials to x,y in world space
	left_fit_cr = np.polyfit(ploty*ym_per_pix, leftx*xm_per_pix, 2)
	right_fit_cr = np.polyfit(ploty*ym_per_pix, rightx*xm_per_pix, 2)
	# Calculate the new radii of curvature
	left_curverad = ((1 + (2*left_fit_cr[0]*y_eval*ym_per_pix + left_fit_cr[1])**2)**1.5) / np.absolute(2*left_fit_cr[0])
	right_curverad = ((1 + (2*right_fit_cr[0]*y_eval*ym_per_pix + right_fit_cr[1])**2)**1.5) / np.absolute(2*right_fit_cr[0])
	# Now our radius of curvature is in meters
	# print(left_curverad, 'm', right_curverad, 'm')
	# Example values: 632.1 m    626.2 m
return (left_curverad + right_curverad) / 2