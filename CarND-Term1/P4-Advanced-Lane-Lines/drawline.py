import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import cv2

def find_curve(left_fit, right_fit, left_fitx, right_fitx, ploty):
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


def draw_lines(image, warped, left_fit, right_fit,  left_fitx, right_fitx, ploty):
	# Create an image to draw the lines on 
	#image = comb_thresh(image)
	warp_zero = np.zeros_like(warped).astype(np.uint8)
	color_warp = np.dstack((warp_zero, warp_zero, warp_zero))
	img_size = (image.shape[1], image.shape[0])
	# Recast the x and y points into usable format for cv2.fillPoly()
	pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
	pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
	pts = np.hstack((pts_left, pts_right))
	plt.plot(pts_left[0][0])
	
	
	plt.plot(pts_left[0][719][0], pts_left[0][719][1], color='green', linestyle='dashed', marker='o',
		 markerfacecolor='blue', markersize=12)
	plt.plot(pts_right[0][0][0], pts_right[0][0][1], color='green', linestyle='dashed', marker='o',
		 markerfacecolor='blue', markersize=12)
	
	line_mid = (pts_left[0][719][0] + pts_right[0][0][0]) / 2
	car_mid = (0 + img_size[0]) / 2
	leave_from_center = abs(line_mid - car_mid)
	
	find_curve(left_fit, right_fit, left_fitx, right_fitx, ploty)
	
	
	# Draw the lane onto the warped blank image
	cv2.fillPoly(color_warp, np.int_([pts]), (0,255, 0))
	"""
	mark_size = 3
	plt.plot(leftx, ploty, 'o', color='red', markersize=mark_size)
	plt.plot(rightx, ploty, 'o', color='blue', markersize=mark_size)
	"""
	# Warp the blank back to original image space using inverse perspective matrix (Minv)

	dst = np.float32([[img_size[0], img_size[1]-10],  
					  [0, img_size[1]-10], 
					 [550, 460],  
					  [730, 460]])  
	src = np.float32([[img_size[0], img_size[1]],    
					[0, img_size[1]],      
				   [0, 0],       
					  [img_size[0], 0]])   
	M = cv2.getPerspectiveTransform(src, dst)
	newwarp = cv2.warpPerspective(color_warp, M, (image.shape[1], image.shape[0])) 
	# Combine the result with the original image
	result = cv2.addWeighted(image, 1, newwarp, 0.3, 0)
	cv2.putText(result, 'curvature radius: {:.02f}m'.format(find_curve(left_fit, right_fit, left_fitx, right_fitx, ploty)), (860, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)
	cv2.putText(result, 'leave from center: {:.02f}m'.format(leave_from_center/700), (860, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)
	return result
	#plt.imshow(result)
	
	
	
	
	
	
