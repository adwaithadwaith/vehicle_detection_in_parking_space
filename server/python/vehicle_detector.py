import cv2
import numpy as np

class VehicleDetector:

    def __init__(self):
        # Load Network
        net = cv2.dnn.readNet("server/python/dnn_model/yolov4.weights", "server/python/dnn_model/yolov4.cfg")
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(832, 832), scale=1 / 255)


        # Allow classes containing Vehicles only
        self.classes_allowed = [2, 3, 5, 6, 7]

    
    
    def detect_vehicles(self, img,roi_number):
        # Detect Objects
        vehicles_boxes = []
        # available_slots = []
        class_ids, scores, boxes = self.model.detect(img, nmsThreshold=0.4)
        for class_id, score, box in zip(class_ids, scores, boxes):
            if score < 0.5:
                continue
            # parked_slots.append(roi_number)
            if class_id in self.classes_allowed:
                vehicles_boxes.append(box)
        if  vehicles_boxes:
            # No vehicles detected in the ROI
            # available_slots.append(roi_number)
            print("ROI", roi_number, "has  vehicles")
            return [roi_number]
        return vehicles_boxes

