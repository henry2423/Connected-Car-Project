# **Finding Lane Lines on the Road** 


**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

---

### Reflection

### 1. Describe my pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. 
First, I converted the images to grayscale, then I use GaussianBlur 

To draw lines: First use Canny Function to detect all edges and set the ROI, filter edges in ROI,
then use HoughLinesP function to detect lines in edges and draw on it



### 2. 


One potential shortcoming would be if road is white then it will detect many edges that not the lane

another potential shortcoming it cannot detect curve line

### 3. Suggest possible improvements to my pipeline

A possible improvement would be to divide image into two pieces by slicing in the middle, one is for right lane and the other is for left lane
So it can detect precisely.

