# Quick Start Guide

Get started with Food Calorie Counter in 5 minutes! 🚀

## 1️⃣ Installation (2 minutes)

```bash
# Clone repository
git clone https://github.com/your-username/calorie-counter.git
cd calorie-counter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 2️⃣ Verify Installation (1 minute)

```bash
# Test imports
python -c "from food_calorie_estimator.detector import FoodDetector; print('✓ Installation successful!')"
```

## 3️⃣ Run Your First Detection (2 minutes)

**Option A: Use Examples Script**
```bash
python examples.py
```

**Option B: Write Your Own Code**
```python
from food_calorie_estimator.detector import FoodDetector
from food_calorie_estimator.calorie_estimator import hitung_total_kalori
from food_calorie_estimator.kalori_reference import KALORI_DICT

# Initialize detector
detector = FoodDetector()

# Detect foods in image
detections = detector.detect_food("your_image.jpg", conf=0.3)

# Calculate calories
total_cal, breakdown = hitung_total_kalori(detections, KALORI_DICT)

print(f"Total Calories: {total_cal} kcal")
print(f"Breakdown: {breakdown}")
```

## 4️⃣ Key Features to Try

### Detect Foods
```python
from food_calorie_estimator.detector import FoodDetector

detector = FoodDetector()
results = detector.detect_food("image.jpg")
```

### Calculate Daily Calorie Need
```python
from food_calorie_estimator.calorie_logic import hitung_kalori_harian

daily_cal = hitung_kalori_harian(
    gender="male",
    birth_date="1995-05-20",
    weight=75,
    height=175
)
```

### Get Food Recommendations
```python
import pandas as pd
from food_calorie_estimator.calorie_logic import rekomendasi_makanan_kalori_maksimum

df = pd.read_csv("nutrition.csv")
recs, total = rekomendasi_makanan_kalori_maksimum(500, df)
```

## 📚 Learn More

- [Full README](README.md) - Complete documentation
- [Installation Guide](INSTALL.md) - Detailed setup instructions
- [examples.py](examples.py) - 5 working examples
- [Contributing Guide](CONTRIBUTING.md) - How to contribute

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| Model not found | Check file exists at `food_calorie_estimator/model/yolo_food.pt` |
| CSV not found | Ensure `nutrition.csv` is in project root |
| CUDA errors | Use CPU: `device='cpu'` parameter |

## 📖 Common Tasks

### Use Different Confidence Threshold
```python
# Stricter detection (fewer false positives)
results = detector.detect_food("image.jpg", conf=0.7)

# Looser detection (more detections)
results = detector.detect_food("image.jpg", conf=0.1)
```

### Process Multiple Images
```python
import glob

for image_path in glob.glob("images/*.jpg"):
    detections = detector.detect_food(image_path)
    print(f"{image_path}: {len(detections)} foods detected")
```

### Save Results to CSV
```python
import pandas as pd

results = []
for detection in detections:
    results.append({
        'food': detection['class'],
        'confidence': detection['confidence']
    })

df = pd.DataFrame(results)
df.to_csv('results.csv', index=False)
```

## 💡 Pro Tips

1. **Use GPU for Speed** - Install PyTorch with CUDA support
2. **Adjust Confidence** - Tune `conf` parameter for your use case
3. **Batch Process** - Process multiple images at once for efficiency
4. **Cache Model** - Load model once, reuse for multiple images
5. **Read Config** - Check `config.py` for customization options

## 🎓 Supported Food Items

```
Anchovies, Boiled Egg, Cah Kangkung, Chicken Nugget,
Chicken Rendang, Crispy Fried Chicken, Cucumber,
Fried Chicken, Fried Egg, Mie Ayam, Mie Bakso,
Peanuts, Rendang, Rice, Sambal, Telur Balado,
Tempe Goreng, Curry
```

## 🚀 What's Next?

1. ✅ Run examples.py
2. ✅ Try with your own images
3. ✅ Read the full README
4. ✅ Explore config.py
5. ✅ Check the code comments
6. ✅ Contribute improvements!

## 📧 Need Help?

- Check [INSTALL.md](INSTALL.md) for detailed troubleshooting
- Read [README.md](README.md) for full documentation
- Open an issue on GitHub
- Check existing issues for similar problems

---

**Happy coding! 🎉**

For complete documentation, see [README.md](README.md)
