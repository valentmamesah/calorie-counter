"""
Calorie Logic Module

This module provides advanced calorie calculation functions including
daily calorie requirement calculation and food recommendations based on
calorie constraints.
"""

import random
import pandas as pd
from datetime import datetime


def hitung_kalori_harian(gender, birth_date, weight, height, activity_factor=1.375):
    """
    Calculate daily calorie requirement using Harris-Benedict equation.
    
    This function calculates the Basal Metabolic Rate (BMR) using the
    Harris-Benedict formula and then multiplies by an activity factor
    to get the Total Daily Energy Expenditure (TDEE).
    
    Args:
        gender (str): Person's gender, either 'male' or 'female'.
        birth_date (str): Birth date in format "YYYY-MM-DD".
        weight (float): Body weight in kilograms.
        height (float): Body height in centimeters.
        activity_factor (float): Activity level multiplier. Default: 1.375
                                - 1.2: Sedentary
                                - 1.375: Lightly active
                                - 1.55: Moderately active
                                - 1.725: Very active
                                - 1.9: Extremely active
    
    Returns:
        int: Daily calorie requirement rounded to nearest integer.
    """
    today = datetime.today()
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    # Harris-Benedict equations
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    return int(bmr * activity_factor)


def rekomendasi_makanan_kalori_maksimum(sisa_kalori, df_makanan, max_item=3):
    """
    Recommend food items that fit within remaining daily calorie allowance.
    
    This function selects random food items from a dataset that fit within
    the remaining calorie limit. It ensures the total calories of recommendations
    do not exceed the specified limit.
    
    Args:
        sisa_kalori (float): Remaining calorie allowance for the day.
        df_makanan (pd.DataFrame): DataFrame containing food items with columns:
                                  - 'calories': Calorie content
                                  - 'name': Food name
                                  - 'image': Food image URL
        max_item (int): Maximum number of food items to recommend. Default: 3
    
    Returns:
        tuple: A tuple containing:
               - rekomendasi (list): List of recommended food items with
                                    'name', 'calories', and 'image' keys
               - total (float): Total calories of recommended items
    
    Example:
        >>> df = pd.DataFrame({
        ...     'calories': [100, 200],
        ...     'name': ['Apple', 'Rice'],
        ...     'image': ['url1', 'url2']
        ... })
        >>> recs, total = rekomendasi_makanan_kalori_maksimum(300, df)
    """
    # Filter foods that don't exceed remaining calories
    kandidat = df_makanan[df_makanan['calories'] <= sisa_kalori].copy()
    kandidat = kandidat.sample(frac=1, random_state=42)  # Randomize

    rekomendasi = []
    total = 0

    for _, row in kandidat.iterrows():
        if total + row['calories'] <= sisa_kalori and len(rekomendasi) < max_item:
            rekomendasi.append({
                "name": row['name'],
                "calories": row['calories'],
                "image": row['image']
            })
            total += row['calories']

    return rekomendasi, total
