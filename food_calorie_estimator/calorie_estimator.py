"""
Calorie Estimation Module

This module provides functionality to calculate total calories
from detected food items based on a calorie reference dictionary.
"""


def hitung_total_kalori(detected_items, kalori_dict):
    """
    Calculate total calories from detected food items.
    
    This function takes a list of detected food items and sums up their
    calories using the provided calorie reference dictionary.
    
    Args:
        detected_items (list): List of detected food items, each containing
                             at least a "class" key with the food type name.
        kalori_dict (dict): Dictionary mapping food names to their calorie values.
    
    Returns:
        tuple: A tuple containing:
               - total_kalori (int): Total calories from all detected items
               - rincian (dict): Breakdown of calories by food type
    
    Example:
        >>> detected = [{"class": "Rice"}, {"class": "Rice"}]
        >>> ref = {"Rice": 200}
        >>> total, details = hitung_total_kalori(detected, ref)
        >>> print(total, details)
        400 {'Rice': 400}
    """
    rincian = {}
    total_kalori = 0

    for item in detected_items:
        class_name = item.get("class")  
        kalori = kalori_dict.get(class_name, 0)
        rincian[class_name] = rincian.get(class_name, 0) + kalori
        total_kalori += kalori

    return total_kalori, rincian
