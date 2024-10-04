# AI-YOLO-DETECTION

This is YOLO implementation was used in a major group project to build an intelligent mobile robot. (Link: https://cpefr-my.sharepoint.com/:f:/g/personal/nadim_ben-hassen_cpe_fr/Es3vKBCCKbtCrGMVlK9czWEBJZku4C8nCP6BKb1qPfvW_A?e=aQCu4O)

In this section, I will detail the technical aspects and the algorithms used to allow the robot to detect and track humans in its environment in real time. 

## Purpose and Features: 

The main objective of this part of the project is to enable the robot to detect humans in its environment using the embedded webcam. Once a human is detected, the robot must be able to focus its camera on that person. This feature is crucial to ensure a smooth and natural interaction between the robot and human users. 

## Technologies Used: 

To achieve this goal, we have chosen to use computer vision techniques combined with advanced AI models. Specifically, we have chosen to implement object detection using the YOLO (You Only Look Once) model. YOLO is renowned for its speed and efficiency, which makes it perfectly suited to our real-time application. 

## Operation of YOLO: 

YOLO works by dividing the image into a grid and predicting the enclosing boxes and the probabilities of belonging to each class for each cell in this grid. This allows for fast and accurate detection of objects in the image. For our application, we trained YOLO to recognize human presence, which allows us to locate people in the robot’s field of view. 


## Implementation and Integration: 

To integrate YOLO into our project, we used deep learning libraries such as TensorFlow or PyTorch, depending on the preferences and skills of our team. We have also developed image processing modules to capture the video stream from the robot’s webcam and apply real-time object detection. 

## Conclusion
In conclusion, through the use of AI models such as YOLO and advanced image processing techniques, our intelligent companion robot will be able to detect and track humans in its environment, Thus opening the way for an immersive and intuitive user interaction.  

## Disclaimer
> [!WARNING]
> For the program to work properly, it is necessary to download the weights of the neurone network available here:
> https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
