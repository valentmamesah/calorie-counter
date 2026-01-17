# Food Calorie Counter

A sophisticated AI-powered system for detecting food items in images and automatically estimating their calorie content using state-of-the-art deep learning technology.

## 📋 Overview

The Food Calorie Counter is a comprehensive solution that combines:
- **YOLOv11** object detection for food recognition
- **Automated calorie estimation** based on detected food items
- **Modular Python package architecture** for easy integration
- **Extensive food database** with nutritional information

### Key Features

- 🎯 **Accurate Food Detection**: Detects 18+ Southeast Asian food items with high precision
- 🔢 **Automatic Calorie Calculation**: Instantly estimates calories from food images
- 📊 **Daily Calorie Tracking**: Calculate daily calorie requirements and recommendations
- 🔧 **Modular Design**: Easy to integrate into applications and APIs
- 🗄️ **Comprehensive Database**: 1300+ food items with detailed nutritional data
- 🎨 **Image References**: Includes food image URLs for visual reference

## 🗂️ Project Structure

```
calorie-counter/
├── food_calorie_estimator/          # Main Python package
│   ├── __init__.py                  # Package initialization
│   ├── detector.py                  # YOLO food detection module
│   ├── calorie_estimator.py         # Calorie calculation module
│   ├── calorie_logic.py             # Advanced calorie logic
│   ├── kalori_reference.py          # Food calorie reference database
│   └── model/
│       └── yolo_food.pt             # Pre-trained YOLO model weights
├── hasil fine tuning food detection/ # Training results and logs
│   └── runs/
│       └── detect/
│           └── train/               # Training artifacts
├── nutrition.csv                     # Comprehensive food nutrition database
├── fine tuning food detection.py    # Training script
├── README.md                         # This file
└── requirements.txt                 # Python dependencies
```

## 🎓 Dataset Information

### Overview
- **Total Items**: 18 food classes
- **Format**: YOLOv8 format (images + YOLO annotations)
- **Data Split**: Training / Validation / Test sets
- **Source**: Curated and augmented from Roboflow

### Food Categories
The model is trained to detect the following food items:

1. Anchovies
2. Boiled Egg
3. Cah Kangkung
4. Chicken Nugget
5. Chicken Rendang
6. Crispy Fried Chicken
7. Cucumber
8. Fried Chicken
9. Fried Egg
10. Mie Ayam (Chicken Noodles)
11. Mie Bakso (Meatball Noodles)
12. Peanuts
13. Rendang
14. Rice
15. Sambal
16. Telur Balado (Spiced Eggs)
17. Tempe Goreng (Fried Tofu)
18. Curry

### Data Augmentation
The dataset includes:
- Bounding box annotations for each food item
- Single and multi-food item images
- Augmented variations for better generalization
- Consistent YOLO format labels

## 🤖 Model Architecture

### YOLOv11n Details
- **Architecture**: YOLOv11n (Nano - lightweight)
- **Pre-training**: COCO dataset
- **Input Size**: 640×640 pixels
- **Framework**: Ultralytics

### Training Configuration
- **Epochs**: 50
- **Optimizer**: SGD/Adam (Ultralytics default)
- **Loss Functions**: YOLOv11 standard
- **Evaluation Metrics**: mAP@0.5 and mAP@0.5:0.95
- **Training Logs**: `hasil fine tuning food detection/runs/detect/train/`

### Training Results
Performance metrics are saved in:
- `results.csv` - Detailed epoch-by-epoch metrics
- `weights/best.pt` - Best model checkpoint
- `weights/last.pt` - Last model checkpoint

## 💾 Nutrition Database

The `nutrition.csv` file contains comprehensive nutritional information for 1300+ food items with:
- **ID**: Unique identifier
- **Calories**: Energy content (kcal)
- **Proteins**: Protein content (grams)
- **Fat**: Fat content (grams)
- **Carbohydrates**: Carbohydrate content (grams)
- **Name**: Food item name (in Indonesian)
- **Image**: URL reference image

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- CUDA 11.8+ (optional, for GPU acceleration)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd calorie-counter
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Key dependencies:
   - `ultralytics>=8.0.0` - YOLO framework
   - `pandas>=1.3.0` - Data manipulation
   - `opencv-python>=4.5.0` - Image processing
   - `torch>=1.9.0` - Deep learning framework

## 📖 Usage Guide

### Basic Usage

#### 1. Food Detection Only
```python
from food_calorie_estimator.detector import FoodDetector

# Initialize detector
detector = FoodDetector(model_path="food_calorie_estimator/model/yolo_food.pt")

# Detect foods in image
detections = detector.detect_food("path/to/your/image.jpg", conf=0.3)

# Print results
for detection in detections:
    print(f"Food: {detection['class']}")
    print(f"Confidence: {detection['confidence']:.2%}")
    print(f"Bounding Box: {detection['bbox']}")
```

#### 2. Food Detection + Calorie Estimation
```python
from food_calorie_estimator.detector import FoodDetector
from food_calorie_estimator.calorie_estimator import hitung_total_kalori
from food_calorie_estimator.kalori_reference import KALORI_DICT

# Detect foods
detector = FoodDetector()
detections = detector.detect_food("path/to/your/image.jpg")

# Calculate calories
total_calories, breakdown = hitung_total_kalori(detections, KALORI_DICT)

print(f"Total Calories: {total_calories} kcal")
print(f"Breakdown:")
for food_type, calories in breakdown.items():
    print(f"  - {food_type}: {calories} kcal")
```

#### 3. Daily Calorie Requirement
```python
from food_calorie_estimator.calorie_logic import hitung_kalori_harian

# Calculate daily calorie requirement
daily_cal = hitung_kalori_harian(
    gender="male",
    birth_date="1995-05-20",
    weight=75,      # kg
    height=175,     # cm
    activity_factor=1.375  # Lightly active
)

print(f"Daily Calorie Requirement: {daily_cal} kcal")
```

#### 4. Food Recommendations
```python
import pandas as pd
from food_calorie_estimator.calorie_logic import rekomendasi_makanan_kalori_maksimum

# Load nutrition database
df_nutrition = pd.read_csv("nutrition.csv")

# Get recommendations for remaining calories
remaining_calories = 500
recommendations, total = rekomendasi_makanan_kalori_maksimum(
    remaining_calories,
    df_nutrition,
    max_item=3
)

print(f"Recommended Foods (up to {remaining_calories} kcal):")
for rec in recommendations:
    print(f"  - {rec['name']}: {rec['calories']} kcal")
print(f"Total: {total} kcal")
```

## 📦 Module Documentation

### detector.py
**FoodDetector** class for food item detection
- `__init__(model_path)` - Initialize with YOLO model
- `detect_food(image_path, conf=0.3)` - Detect foods in image

### calorie_estimator.py
**hitung_total_kalori** function
- Calculates total and per-item calories from detections

### calorie_logic.py
- **hitung_kalori_harian()** - Calculate daily calorie needs
- **rekomendasi_makanan_kalori_maksimum()** - Get food recommendations

### kalori_reference.py
- **KALORI_DICT** - Dictionary of 18 foods with calorie values

## 🔧 Configuration

### Detection Confidence Threshold
```python
detector.detect_food(image_path, conf=0.3)  # Adjust conf parameter
# Lower values (0.1-0.3): More detections, lower precision
# Higher values (0.5-0.9): Fewer detections, higher precision
```

### Activity Factors for TDEE Calculation
- **1.2**: Sedentary (little or no exercise)
- **1.375**: Lightly active (light exercise 1-3 days/week)
- **1.55**: Moderately active (moderate exercise 3-5 days/week)
- **1.725**: Very active (hard exercise 6-7 days/week)
- **1.9**: Extremely active (very hard exercise daily)

## 📊 Performance Metrics

The model achieves the following performance on validation set:
- Results are logged in: `hasil fine tuning food detection/runs/detect/train/results.csv`
- Includes: mAP@0.5, mAP@0.5:0.95, precision, recall per epoch

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📝 License

This project is open source and available under the MIT License.

## ✨ Future Enhancements

- [ ] Support for more food categories
- [ ] Portion size estimation
- [ ] Macro nutrient breakdown (proteins, fats, carbs)
- [ ] Real-time video analysis
- [ ] Mobile app integration
- [ ] Multi-language support
- [ ] User dietary preference profiles

## 📧 Support

For questions, issues, or suggestions, please open an issue on the GitHub repository.

## 🙏 Acknowledgments

- **Dataset**: Based on Roboflow community datasets
- **Framework**: Built with Ultralytics YOLO
- **Data**: Nutrition database curated from multiple sources

---

**Last Updated**: January 2026
**Version**: 1.0.0