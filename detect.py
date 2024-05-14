import cv2
import numpy as np

# Load YOLO model and configuration files
net = cv2.dnn.readNet("yolov4.weights", "cfg/yolov4.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Function to detect objects in a frame
def detect_objects(frame):
    height, width, channels = frame.shape
    Aire_init = height*width
    # Convert the frame to blob format
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        # Pass the blob through the network
    net.setInput(blob)
    outs = net.forward(output_layers)
    seuil = 0.8
    # Process the detections
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            if str(classes[class_id]) != "person" :
                break
            confidence = scores[class_id]
            if confidence > seuil : 
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
               
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                

    # Non-maximum suppression to remove duplicate boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw rectangles and labels on the frame
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            print("\nHumain "+str(i))
            Aire_box = w*h
            center = w//2
            Sc = w//10
            Ac = Aire_init//5
            if x < center - Sc :
                print("Aller à gauche")
            elif x > center + Sc :
                print("Aller à droite")
            else :
                print("L'humain est centré")
            if Aire_box < Ac :
                print("Avancer")
            

    return frame

# # Capture video from webcam
# cap = cv2.VideoCapture(0)

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()

#     # Detect objects in the frame
#     result_frame = detect_objects(frame)

#     # Display the result
#     cv2.imshow('Object Detection', result_frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all OpenCV windows
# cap.release()

image_path = "data/homme.jpg"
image = cv2.imread(image_path)

result_image = detect_objects(image)
cv2.imshow('object detection',result_image)



cv2.waitKey(0)

cv2.destroyAllWindows()