"""
Configuration Module

This module contains configuration settings for the Food Calorie Counter application.
Modify these settings according to your requirements.
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent

# Model Configuration
MODEL_CONFIG = {
    "model_path": PROJECT_ROOT / "food_calorie_estimator" / "model" / "yolo_food.pt",
    "confidence_threshold": 0.3,  # Default confidence threshold (0.0-1.0)
    "input_size": 640,  # YOLO input image size
}

# Detection Configuration
DETECTION_CONFIG = {
    "conf": 0.3,  # Detection confidence
    "iou": 0.45,  # IoU threshold for NMS
    "max_det": 300,  # Maximum detections per image
}

# Calorie Configuration
CALORIE_CONFIG = {
    "nutrition_db_path": PROJECT_ROOT / "nutrition.csv",
    "kalori_reference_path": PROJECT_ROOT / "food_calorie_estimator" / "kalori_reference.py",
}

# Default Activity Factors for TDEE Calculation
ACTIVITY_FACTORS = {
    "sedentary": 1.2,           # Little or no exercise
    "lightly_active": 1.375,    # Light exercise 1-3 days/week
    "moderate": 1.55,            # Moderate exercise 3-5 days/week
    "very_active": 1.725,        # Hard exercise 6-7 days/week
    "extremely_active": 1.9      # Very hard exercise daily
}

# Recommendation Configuration
RECOMMENDATION_CONFIG = {
    "max_items": 3,              # Maximum number of recommendations
    "random_state": 42,          # For reproducibility
}

# Supported Food Classes (must match model training classes)
FOOD_CLASSES = [
    'Anchovies',
    'Boiled-Egg',
    'Cah Kangkung',
    'Chicken Nugget',
    'Chicken Rendang',
    'Crispy Fried Chicken',
    'Cucumber',
    'Fried-Chicken',
    'Fried-Egg',
    'Mie Ayam',
    'Mie Bakso',
    'Peanuts',
    'Rendang',
    'Rice',
    'Sambal',
    'Telur Balado',
    'Tempe Goreng',
    'Curry'
]

# Logging Configuration
LOG_CONFIG = {
    "level": "INFO",  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "log_file": PROJECT_ROOT / "logs" / "app.log",
}

# API Configuration (if used with web service)
API_CONFIG = {
    "host": "0.0.0.0",
    "port": 8000,
    "debug": False,
    "max_upload_size": 10 * 1024 * 1024,  # 10 MB
}

# Image Processing Configuration
IMAGE_CONFIG = {
    "allowed_formats": [".jpg", ".jpeg", ".png", ".bmp"],
    "max_width": 2000,
    "max_height": 2000,
    "min_width": 64,
    "min_height": 64,
}

# Database Configuration
DATABASE_CONFIG = {
    "type": "csv",  # csv or sqlite
    "csv_path": PROJECT_ROOT / "nutrition.csv",
}


def get_config(section: str) -> dict:
    """
    Get configuration section by name.
    
    Args:
        section (str): Configuration section name
        
    Returns:
        dict: Configuration dictionary for the section
        
    Raises:
        KeyError: If section not found
    """
    configs = {
        "model": MODEL_CONFIG,
        "detection": DETECTION_CONFIG,
        "calorie": CALORIE_CONFIG,
        "activity": ACTIVITY_FACTORS,
        "recommendation": RECOMMENDATION_CONFIG,
        "log": LOG_CONFIG,
        "api": API_CONFIG,
        "image": IMAGE_CONFIG,
        "database": DATABASE_CONFIG,
    }
    
    if section not in configs:
        raise KeyError(f"Configuration section '{section}' not found")
    
    return configs[section]


def validate_config() -> bool:
    """
    Validate that all required configuration files exist.
    
    Returns:
        bool: True if all required files exist, False otherwise
    """
    required_paths = [
        MODEL_CONFIG["model_path"],
        CALORIE_CONFIG["nutrition_db_path"],
    ]
    
    missing_files = [p for p in required_paths if not p.exists()]
    
    if missing_files:
        print("⚠️  Missing configuration files:")
        for path in missing_files:
            print(f"   - {path}")
        return False
    
    return True


if __name__ == "__main__":
    # Test configuration
    print("Food Calorie Counter - Configuration Check")
    print("=" * 50)
    
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Model Path: {MODEL_CONFIG['model_path']}")
    print(f"Nutrition DB: {CALORIE_CONFIG['nutrition_db_path']}")
    
    if validate_config():
        print("\n✓ All configuration files found!")
    else:
        print("\n✗ Some configuration files are missing!")
