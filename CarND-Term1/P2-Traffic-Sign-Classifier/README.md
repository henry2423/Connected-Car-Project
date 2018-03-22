# **Traffic Sign Recognition** 

## Writeup
---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./Other/visualization1.png "Visualization1"
[image2]: ./Other/visualization2.png "Visualization2"
[image3]: ./Other/visualization3.png "Visualization3"
[image4]: ./TestImage/001.jpg "Traffic Sign 1"
[image5]: ./TestImage/002.jpg "Traffic Sign 2"
[image6]: ./TestImage/003.jpg "Traffic Sign 3"
[image7]: ./TestImage/004.jpg "Traffic Sign 4"
[image8]: ./TestImage/005.jpg "Traffic Sign 5"
[image9]: ./Other/before.png "Before"
[image10]: ./Other/after.png "After"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf. You can use this template as a guide for writing the report. The submission includes the project code.

You're reading it! And my project code is included in the same zip file.


### Data Set Summary & Exploration

#### 1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

I used the numpy library to calculate summary statistics of the traffic signs data set:

* The size of training set is 34799
* The size of the validation set is 4410
* The size of test set is 12630
* The shape of a traffic sign image is 32 * 32 * 3
* The number of unique classes/labels in the data set is 43

#### 2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. Below are bar charts showing the distribution of training set, validation set and testing set.

![Visualization of training set][image1]
![Visualization of validation set][image2]
![Visualization of test set][image3]


### Design and Test a Model Architecture

#### 1. Describe how you preprocessed the image data. What techniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, and provide example images of the additional data. Then describe the characteristics of the augmented training set like number of images in the set, number of images for each class, etc.)

How I preprocessed the image data was to normalize the images and convert them to grayscale. Normalization can make the contrast of images better. Because I wanted the model to focus on the shape instead of the color of the image so I also converted them to grayscale. Below are images before and after preprocessing.

##### Before
![Before][image9]
##### After
![After][image10]  

#### 2. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

My final model consisted of the following layers:

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x1 grayscale image   					| 
| Convolution 5x5     	| 1x1 stride, valid padding, outputs 28x28x6 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x6	 				|
| Convolution 5x5     	| 1x1 stride, valid padding, outputs 10x10x16 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x16	 				|
| Flatten		      	| 5x5x16 = 400					 				|
| Fully connected		| 400 to 120        							|
| Fully connected		| 120 to 84        								|
| Fully connected		| 84 to 43     									|
| Softmax				| 43 possible final outputs						|

#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

To train the model, I used an AdamOptimizer at a learning rate of 0.001, set batch size to 128 and number of epochs to 20 , and let learning rate equal to 0.001. 

#### 4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

My final model results were:
* training set accuracy of 99.9%
* validation set accuracy of 93.9% 
* test set accuracy of 91.5%

They were calculated by using tensorflow function tf.equal() and tf.reduce_mean() in the 6th code cell.

I chose a well known architecture known as Lenet-5 and tuned the hyperparamters such as epochs, learning rate, and batch size to improve the performance. I chose it because the grid of the image contains simple shapes like diagonal lines or circles just like data in the MNIST dataset. The final model's accuracy on the training set was nearly 100%, and both the accuracy on validation set and test set were beyond 90%. However, due to the loss, I thought it to be overfitting. What I did to overcome this problem was to use dropout layers, however, it seemed that the effect was not good enough, so I still used the CNN without dropout layers. I think that the model can be much better if I tune the parameter and use dropout layers more precisely. But until now, I have not figured out the solution yet. 
 

### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are five German traffic signs that I found on the web:

![alt text][image4] ![alt text][image5] ![alt text][image6] 
![alt text][image7] ![alt text][image8]

I think that classifying each image is an easy job if the model is good enough, because the traffic signs in all images are big and clear.

#### 2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

| Image			        				|     Prediction	        					| 
|:-------------------------------------:|:---------------------------------------------:| 
| Yield		      						| Yield		  									| 
| Stop     								| Children crossing 							|
| Right-of-way at the next intersection	| Right-of-way at the next intersection			|
| Dangerous curve to the right	      	| No entry					 					|
| Pedestrians							| General caution      							|

The model was able to correctly guess 2 of the 5 traffic signs, which gives an accuracy of 40%. However, the accuracy on the test set is nearly 92%.

#### 3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The code for making predictions on my final model is located in the 8th cell of the Ipython notebook.

For the first image, the model is sure that this is a yield sign (probability of 1.000000), and the image does contain a yield sign. The top five soft max probabilities were

| Probability         	|     Prediction	        				| 
|:---------------------:|:-----------------------------------------:| 
| 1.00         			| Yield   									| 
| 0.00     				| Speed limit (20km/h) 						|
| 0.00					| Speed limit (30km/h)						|
| 0.00	      			| Speed limit (50km/h)						|
| 0.00				    | Speed limit (60km/h)      				|

For the second image, the model is sure that this is a Children crossing sign (probability of 1.000000), but the image contains a Stop sign. The top five soft max probabilities were

| Probability         	|     Prediction	        				| 
|:---------------------:|:-----------------------------------------:| 
| 1.00         			| Children crossing   						| 
| 0.00     				| Speed limit (20km/h) 						|
| 0.00					| Speed limit (30km/h)						|
| 0.00	      			| Speed limit (50km/h)						|
| 0.00				    | Speed limit (60km/h)      				|

For the third image, the model is sure that this is a Right-of-way at the next intersection sign (probability of 0.943), and the image does contain a Right-of-way at the next intersection sign. The top five soft max probabilities were

| Probability         	|     Prediction	        				| 
|:---------------------:|:-----------------------------------------:| 
| 0.943        			| Right-of-way at the next intersection   	| 
| 0.026     			| General caution	 						|
| 0.022					| Pedestrians								|
| 0.004	      			| Beware of ice/snow						|
| 0.001				    | Double curve			      				|

For the fourth image, the model is sure that this is a No entry sign (probability of 1.000000), however, the image contains a Dangerous curve to the right sign. The top five soft max probabilities were

| Probability         	|     Prediction	        				| 
|:---------------------:|:-----------------------------------------:| 
| 1.00         			| No entry   								| 
| 0.00     				| Speed limit (20km/h) 						|
| 0.00					| Speed limit (30km/h)						|
| 0.00	      			| Speed limit (50km/h)						|
| 0.00				    | Speed limit (60km/h)      				|

For the fifth image, the model is sure that this is a General caution sign (probability of 1.000000), but the image contains a Pedestrians sign. The top five soft max probabilities were

| Probability         	|     Prediction	        				| 
|:---------------------:|:-----------------------------------------:| 
| 1.00         			| General caution   						| 
| 0.00     				| Speed limit (20km/h) 						|
| 0.00					| Speed limit (30km/h)						|
| 0.00	      			| Speed limit (50km/h)						|
| 0.00				    | Speed limit (60km/h)      				|

As seen above, the performance of this model is so poor that I should tune the parameters to meet the better result.



### (Optional) Visualizing the Neural Network (See Step 4 of the Ipython notebook for more details)
#### 1. Discuss the visual output of your trained network's feature maps. What characteristics did the neural network use to make classifications?