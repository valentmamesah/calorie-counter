"""
Example Usage Script

This script demonstrates how to use the Food Calorie Counter package.
It shows basic detection, calorie calculation, and other key features.
"""

import pandas as pd
from food_calorie_estimator.detector import FoodDetector
from food_calorie_estimator.calorie_estimator import hitung_total_kalori
from food_calorie_estimator.calorie_logic import (
    hitung_kalori_harian,
    rekomendasi_makanan_kalori_maksimum
)
from food_calorie_estimator.kalori_reference import KALORI_DICT


def example_basic_detection():
    """Example 1: Basic food detection from image"""
    print("=" * 50)
    print("Example 1: Basic Food Detection")
    print("=" * 50)
    
    # Initialize detector
    detector = FoodDetector(model_path="food_calorie_estimator/model/yolo_food.pt")
    
    # Detect foods in image (replace with your image path)
    # detections = detector.detect_food("path/to/your/image.jpg", conf=0.3)
    
    # Simulated detections for demonstration
    detections = [
        {"class": "Rice", "bbox": [10, 20, 100, 120], "confidence": 0.95},
        {"class": "Fried-Chicken", "bbox": [120, 30, 200, 150], "confidence": 0.92}
    ]
    
    print("\nDetected Foods:")
    for i, detection in enumerate(detections, 1):
        print(f"{i}. {detection['class']}")
        print(f"   Confidence: {detection['confidence']:.2%}")
        print(f"   Bounding Box: {detection['bbox']}")
    
    print()


def example_calorie_calculation():
    """Example 2: Calculate total calories from detected foods"""
    print("=" * 50)
    print("Example 2: Calorie Calculation")
    print("=" * 50)
    
    # Simulated detections
    detections = [
        {"class": "Rice"},
        {"class": "Rice"},
        {"class": "Fried-Chicken"},
        {"class": "Sambal"}
    ]
    
    # Calculate calories
    total_calories, breakdown = hitung_total_kalori(detections, KALORI_DICT)
    
    print(f"\nTotal Calories: {total_calories} kcal")
    print("\nBreakdown by Food Type:")
    for food_type, calories in breakdown.items():
        count = sum(1 for d in detections if d['class'] == food_type)
        print(f"  - {food_type}: {calories} kcal (quantity: {count})")
    
    print()


def example_daily_calorie_requirement():
    """Example 3: Calculate daily calorie requirement"""
    print("=" * 50)
    print("Example 3: Daily Calorie Requirement")
    print("=" * 50)
    
    # Person's details
    gender = "male"
    birth_date = "1995-05-20"  # YYYY-MM-DD format
    weight = 75  # kg
    height = 175  # cm
    activity_factor = 1.375  # Lightly active
    
    # Calculate daily requirement
    daily_cal = hitung_kalori_harian(gender, birth_date, weight, height, activity_factor)
    
    print(f"\nPerson Details:")
    print(f"  Gender: {gender}")
    print(f"  Birth Date: {birth_date}")
    print(f"  Weight: {weight} kg")
    print(f"  Height: {height} cm")
    print(f"  Activity Level: {'Lightly active' if activity_factor == 1.375 else 'Other'}")
    
    print(f"\nDaily Calorie Requirement: {daily_cal} kcal/day")
    
    print()


def example_food_recommendations():
    """Example 4: Get food recommendations based on calorie limit"""
    print("=" * 50)
    print("Example 4: Food Recommendations")
    print("=" * 50)
    
    # Load nutrition database
    df_nutrition = pd.read_csv("nutrition.csv")
    
    # Remaining calories for the day
    remaining_calories = 500
    
    # Get recommendations
    recommendations, total = rekomendasi_makanan_kalori_maksimum(
        remaining_calories,
        df_nutrition,
        max_item=3
    )
    
    print(f"\nRemaining Daily Allowance: {remaining_calories} kcal")
    print(f"\nRecommended Foods:")
    
    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['name']}")
            print(f"   Calories: {rec['calories']} kcal")
            print(f"   Image: {rec['image'][:60]}...")  # First 60 chars of URL
    else:
        print("No recommendations available for this calorie limit.")
    
    print(f"\nTotal from Recommendations: {total} kcal")
    print(f"Remaining: {remaining_calories - total} kcal")
    
    print()


def example_complete_workflow():
    """Example 5: Complete workflow from image to recommendation"""
    print("=" * 50)
    print("Example 5: Complete Workflow")
    print("=" * 50)
    
    # Step 1: Detect foods
    print("\nStep 1: Detecting foods in image...")
    detections = [
        {"class": "Rice"},
        {"class": "Fried-Chicken"},
        {"class": "Sambal"}
    ]
    print(f"  ✓ Detected {len(detections)} food items")
    
    # Step 2: Calculate calories
    print("\nStep 2: Calculating calories...")
    total_eaten, breakdown = hitung_total_kalori(detections, KALORI_DICT)
    print(f"  ✓ Total calories consumed: {total_eaten} kcal")
    
    # Step 3: Calculate daily requirement
    print("\nStep 3: Calculating daily requirement...")
    daily_requirement = hitung_kalori_harian("female", "1998-03-15", 65, 165)
    print(f"  ✓ Daily requirement: {daily_requirement} kcal")
    
    # Step 4: Calculate remaining
    print("\nStep 4: Calculating remaining allowance...")
    remaining = daily_requirement - total_eaten
    print(f"  ✓ Remaining: {remaining} kcal")
    
    # Step 5: Get recommendations
    print("\nStep 5: Getting recommendations...")
    df_nutrition = pd.read_csv("nutrition.csv")
    if remaining > 0:
        recommendations, total_rec = rekomendasi_makanan_kalori_maksimum(
            remaining,
            df_nutrition,
            max_item=3
        )
        print(f"  ✓ Found {len(recommendations)} recommendations")
        for rec in recommendations:
            print(f"    - {rec['name']}: {rec['calories']} kcal")
    else:
        print(f"  ✗ Daily calorie limit exceeded!")
    
    print("\n✓ Workflow complete!")
    print()


def main():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 48 + "╗")
    print("║" + " " * 10 + "Food Calorie Counter - Usage Examples" + " " * 2 + "║")
    print("╚" + "=" * 48 + "╝")
    print("\n")
    
    try:
        example_basic_detection()
        example_calorie_calculation()
        example_daily_calorie_requirement()
        example_food_recommendations()
        example_complete_workflow()
        
        print("=" * 50)
        print("All examples completed successfully!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("\nMake sure:")
        print("  - nutrition.csv is in the current directory")
        print("  - Model file exists at food_calorie_estimator/model/yolo_food.pt")
        print("  - All dependencies are installed")


if __name__ == "__main__":
    main()
