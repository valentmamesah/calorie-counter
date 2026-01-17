"""
API Module (Optional)

This module can be used to create a REST API for the Food Calorie Counter.
It demonstrates how to wrap the core functionality as web service endpoints.

This is an example structure. To use it with FastAPI:
    pip install fastapi uvicorn python-multipart
    uvicorn api:app --reload
"""

from typing import List, Optional
from pathlib import Path
import base64
import io
from PIL import Image

# Uncomment these imports if implementing FastAPI
# from fastapi import FastAPI, File, UploadFile, HTTPException
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# import uvicorn

from food_calorie_estimator.detector import FoodDetector
from food_calorie_estimator.calorie_estimator import hitung_total_kalori
from food_calorie_estimator.calorie_logic import (
    hitung_kalori_harian,
    rekomendasi_makanan_kalori_maksimum
)
from food_calorie_estimator.kalori_reference import KALORI_DICT
import pandas as pd
import config


class FoodDetectionResponse:
    """Response model for food detection endpoint"""
    
    def __init__(self, detections: List[dict], image_path: str = None):
        self.detections = detections
        self.count = len(detections)
        self.image_path = image_path
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "success": True,
            "count": self.count,
            "detections": self.detections,
            "image_path": self.image_path
        }


class CalorieCalculationResponse:
    """Response model for calorie calculation endpoint"""
    
    def __init__(self, total_calories: int, breakdown: dict):
        self.total_calories = total_calories
        self.breakdown = breakdown
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "success": True,
            "total_calories": self.total_calories,
            "breakdown": self.breakdown
        }


class FoodCalorieAPI:
    """
    Core API class for food detection and calorie calculation.
    Can be wrapped with FastAPI or Flask for web service.
    """
    
    def __init__(self):
        """Initialize API with detector and configuration"""
        model_config = config.get_config("model")
        self.detector = FoodDetector(model_path=str(model_config["model_path"]))
        self.nutrition_df = pd.read_csv(
            config.get_config("calorie")["nutrition_db_path"]
        )
    
    def detect_food_from_file(self, image_path: str, conf: float = 0.3) -> dict:
        """
        Detect foods from image file.
        
        Args:
            image_path (str): Path to image file
            conf (float): Confidence threshold
            
        Returns:
            dict: Detection results
        """
        try:
            detections = self.detector.detect_food(image_path, conf=conf)
            response = FoodDetectionResponse(detections, image_path)
            return response.to_dict()
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def detect_food_from_base64(self, image_b64: str, conf: float = 0.3) -> dict:
        """
        Detect foods from base64 encoded image.
        
        Args:
            image_b64 (str): Base64 encoded image
            conf (float): Confidence threshold
            
        Returns:
            dict: Detection results
        """
        try:
            # Decode base64
            image_data = base64.b64decode(image_b64)
            image = Image.open(io.BytesIO(image_data))
            
            # Save temporarily and detect
            temp_path = "/tmp/temp_image.jpg"
            image.save(temp_path)
            
            detections = self.detector.detect_food(temp_path, conf=conf)
            response = FoodDetectionResponse(detections)
            
            return response.to_dict()
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def calculate_calories(self, detections: List[dict]) -> dict:
        """
        Calculate total calories from detections.
        
        Args:
            detections (list): List of detection results
            
        Returns:
            dict: Calorie calculation results
        """
        try:
            total_cal, breakdown = hitung_total_kalori(detections, KALORI_DICT)
            response = CalorieCalculationResponse(total_cal, breakdown)
            return response.to_dict()
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def calculate_daily_requirement(
        self,
        gender: str,
        birth_date: str,
        weight: float,
        height: float,
        activity_factor: float = 1.375
    ) -> dict:
        """
        Calculate daily calorie requirement.
        
        Args:
            gender (str): 'male' or 'female'
            birth_date (str): Birth date in YYYY-MM-DD format
            weight (float): Weight in kg
            height (float): Height in cm
            activity_factor (float): Activity multiplier
            
        Returns:
            dict: Daily calorie requirement
        """
        try:
            daily_cal = hitung_kalori_harian(
                gender, birth_date, weight, height, activity_factor
            )
            return {
                "success": True,
                "daily_requirement": daily_cal,
                "unit": "kcal"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_recommendations(
        self,
        remaining_calories: float,
        max_items: int = 3
    ) -> dict:
        """
        Get food recommendations for remaining calories.
        
        Args:
            remaining_calories (float): Remaining calorie allowance
            max_items (int): Maximum recommendations
            
        Returns:
            dict: Food recommendations
        """
        try:
            recommendations, total = rekomendasi_makanan_kalori_maksimum(
                remaining_calories,
                self.nutrition_df,
                max_item=max_items
            )
            return {
                "success": True,
                "remaining_calories": remaining_calories,
                "recommendations": recommendations,
                "total_recommended": total
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


# ==========================================
# FastAPI Integration (Uncomment to use)
# ==========================================

# app = FastAPI(
#     title="Food Calorie Counter API",
#     description="Detect food items and calculate calories",
#     version="1.0.0"
# )
#
# api = FoodCalorieAPI()
#
#
# @app.post("/api/detect")
# async def detect_food(file: UploadFile = File(...)):
#     """Detect foods in uploaded image"""
#     # Save uploaded file
#     contents = await file.read()
#     temp_path = f"/tmp/{file.filename}"
#     with open(temp_path, "wb") as f:
#         f.write(contents)
#     
#     # Detect
#     result = api.detect_food_from_file(temp_path)
#     return JSONResponse(result)
#
#
# @app.post("/api/calories")
# async def calculate_calories(detections: List[dict]):
#     """Calculate calories from detections"""
#     result = api.calculate_calories(detections)
#     return JSONResponse(result)
#
#
# @app.post("/api/daily-requirement")
# async def daily_requirement(
#     gender: str,
#     birth_date: str,
#     weight: float,
#     height: float,
#     activity_factor: float = 1.375
# ):
#     """Calculate daily calorie requirement"""
#     result = api.calculate_daily_requirement(
#         gender, birth_date, weight, height, activity_factor
#     )
#     return JSONResponse(result)
#
#
# @app.post("/api/recommendations")
# async def get_recommendations(
#     remaining_calories: float,
#     max_items: int = 3
# ):
#     """Get food recommendations"""
#     result = api.get_recommendations(remaining_calories, max_items)
#     return JSONResponse(result)
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # Test API without FastAPI
    print("Food Calorie Counter API - Testing")
    print("=" * 50)
    
    api = FoodCalorieAPI()
    
    # Test detection (example)
    print("\n1. Testing detection (with example data)...")
    example_detections = [
        {"class": "Rice"},
        {"class": "Fried-Chicken"}
    ]
    
    # Test calorie calculation
    print("\n2. Testing calorie calculation...")
    cal_result = api.calculate_calories(example_detections)
    print(f"Result: {cal_result}")
    
    # Test daily requirement
    print("\n3. Testing daily requirement calculation...")
    req_result = api.calculate_daily_requirement(
        "male", "1995-05-20", 75, 175
    )
    print(f"Result: {req_result}")
    
    # Test recommendations
    print("\n4. Testing recommendations...")
    rec_result = api.get_recommendations(500)
    print(f"Found {len(rec_result.get('recommendations', []))} recommendations")
    
    print("\n✓ API testing complete!")
