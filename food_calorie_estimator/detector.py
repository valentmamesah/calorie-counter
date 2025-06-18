
from ultralytics import YOLO

class FoodDetector:
    def __init__(self, model_path="food_calorie_estimator/model/yolo_food.pt"):
        self.model = YOLO(model_path)

    def detect_food(self, image_path):
        results = self.model.predict(image_path, conf=0.3)
        classes = []
        for r in results:
            classes.extend([r.names[int(cls)] for cls in r.boxes.cls])
        return classes
