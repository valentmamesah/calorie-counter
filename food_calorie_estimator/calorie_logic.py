
import random
import pandas as pd
from datetime import datetime

def hitung_kalori_harian(gender, birth_date, weight, height, activity_factor=1.375):
    today = datetime.today()
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    umur = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * umur + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * umur - 161

    return int(bmr * activity_factor)

def rekomendasi_makanan_kalori_maksimum(sisa_kalori, df_makanan, max_item=3):
    """
    Pilih kombinasi makanan acak yang total kalorinya tidak melebihi sisa kalori.
    """
    kandidat = df_makanan[df_makanan['calories'] <= sisa_kalori].copy()
    kandidat = kandidat.sample(frac=1, random_state=42)  # acak

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
