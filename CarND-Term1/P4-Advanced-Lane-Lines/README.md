## Writeup 

---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./image/camera.JPG "Undistorted"
[image1-2]: ./image/camera_b.JPG "Undistorted"
[image2]: ./image/undis_image.JPG "Road Transformed"
[image2-1]: ./image/undis_image_b.JPG "Road Transformed"
[image3]: ./image/undis_image3.JPG "Binary Example"
[image4]: ./image/bird_eye.JPG "Warp Example"
[image5]: ./image/sliding_windows.JPG "Fit Visual"
[image6]: ./output_images/test2.jpg "Output"
[video1]: ./out.mp4 "Video"

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Advanced-Lane-Lines/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.  

You're reading it!

### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

this can be found in color_pipeline. use 
`cv2.findChessboardCorners(image, pattern_size)`
`cv2.calibrateCamera()`
`cv2.undistort()`

to find the corner and calibrate camera then we got this image:

![alt text][image1]

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

To demonstrate this step, I will describe how I apply the distortion correction to one of the test images like this one:
![alt text][image2]

we can see that the stop sign's change
#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

The final image  is a combination of binary thresholding the S channel (HLS) and binary thresholding the result of applying the Sobel operator in the x direction on the original image.

![alt text][image3]

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.


I use this to `src` and `dst` to  transformed image

```python

    dst = np.float32([[img_size[0], img_size[1]-10],   
			        [0, img_size[1]-10],   
				[550, 460],  
				[730, 460]])  
    src = np.float32([[img_size[0], img_size[1]],    
				[0, img_size[1]],       
			        [0, 0],      
				[img_size[0], 0]])      
```

![alt text][image4]

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

I did it in `find_lines.py`
we can identify the peaks location of the histogram of the binary image, and slide two windows to detect lane lines and fit my lane lines with a 2nd order polynomial kinda like this:

![alt text][image5]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did it in `find_curve.py`
compare two lines middle and image's middle then can know the offset from center

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in lines 51 in my code in `main.py` in the function `process()`. And the image is undistorted Here is an example of my result on a test image:

![alt text][image6]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to my video result](./out.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

I found that its speed is much slower than poject 1, maybe in real time, it need nore hardware support.
Also found that if there is shadow on the path or the path is white. its performance is not good. Mybe we can use good training data to train a model to mark annotation  on the lane to help identify.
