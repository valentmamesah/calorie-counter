"""
Food Calorie Estimator Package

A comprehensive Python package for detecting food items in images using YOLO model
and automatically estimating their calorie content. The package is modular and
designed for easy integration into web services, mobile apps, and API endpoints.

Main Components:
    - detector: YOLO-based food detection module
    - calorie_estimator: Calorie calculation module
    - calorie_logic: Advanced calorie computation logic
    - kalori_reference: Food calorie reference database

Usage:
    >>> from food_calorie_estimator.detector import FoodDetector
    >>> from food_calorie_estimator.calorie_estimator import hitung_total_kalori
    >>> from food_calorie_estimator.kalori_reference import KALORI_DICT
    >>>
    >>> detector = FoodDetector()
    >>> detections = detector.detect_food("path/to/image.jpg")
    >>> total_cal, breakdown = hitung_total_kalori(detections, KALORI_DICT)
    >>> print(f"Total Calories: {total_cal}")
    >>> print(f"Breakdown: {breakdown}")
"""

__version__ = "1.0.0"
__author__ = "Calorie Counter Team"
__description__ = "Food Detection and Calorie Estimation System"