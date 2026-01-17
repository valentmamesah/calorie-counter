"""
Food Detection Module

This module provides functionality to detect food items in images using YOLO model.
It utilizes the Ultralytics YOLO framework for efficient object detection.
"""

from ultralytics import YOLO


class FoodDetector:
    """
    A class to detect food items in images using YOLO model.
    
    Attributes:
        model (YOLO): The YOLO model instance for food detection.
    """
    
    def __init__(self, model_path="food_calorie_estimator/model/yolo_food.pt"):
        """
        Initialize the FoodDetector with a pre-trained YOLO model.
        
        Args:
            model_path (str): Path to the YOLO model weights file.
                             Default: "food_calorie_estimator/model/yolo_food.pt"
        """
        self.model = YOLO(model_path)

    def detect_food(self, image_path, conf=0.3):
        """
        Detect food items in an image.
        
        Args:
            image_path (str): Path to the image file to be analyzed.
            conf (float): Confidence threshold for detections. Default: 0.3
                         Range: 0.0 to 1.0. Higher values mean stricter detection.
        
        Returns:
            list: List of detected food items, each containing:
                  - "class": Food class name
                  - "bbox": Bounding box coordinates [x1, y1, x2, y2]
                  - "confidence": Detection confidence score
        """
        results = self.model.predict(image_path, conf=conf)
        detections = []

        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                conf_score = float(box.conf[0])
                xyxy = box.xyxy[0].tolist()  # Bounding box coordinates
                class_name = result.names[cls_id]
                
                detections.append({
                    "class": class_name,
                    "bbox": xyxy,
                    "confidence": conf_score
                })

        return detections
