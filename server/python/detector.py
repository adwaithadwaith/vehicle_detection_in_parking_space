import cv2
from vehicle_detector import VehicleDetector
import json
import sys

# Get the image path and coordinates path from command-line arguments
image_path = sys.argv[1]
coordinates_path = sys.argv[2]

vd = VehicleDetector()
rois_with_vehicles = []

# Read the coordinates from the JSON file
with open(coordinates_path, 'r') as file:
    coordinates = json.load(file)

for coordinate in coordinates:
    startX = coordinate['startX']
    startY = coordinate['startY']
    endX = coordinate['endX']
    endY = coordinate['endY']
    roi_number = coordinate['roi_number']
    roi_image = cv2.imread(image_path)[startY:endY, startX:endX]

    # Perform vehicle detection on the ROI image using the VehicleDetector class
    vehicle_boxes = vd.detect_vehicles(roi_image, roi_number)
    if isinstance(vehicle_boxes, list):
        rois_with_vehicles.extend(vehicle_boxes)

print('Parked slots:', rois_with_vehicles)
