# Project Structure Overview

Complete guide to the Food Calorie Counter project structure.

## 📁 Directory Layout

```
calorie-counter/
│
├── 📁 food_calorie_estimator/          # Main Python package
│   ├── __init__.py                     # Package initialization
│   ├── detector.py                     # YOLO food detection module
│   ├── calorie_estimator.py            # Basic calorie calculation
│   ├── calorie_logic.py                # Advanced calorie logic
│   ├── kalori_reference.py             # Food calorie reference database
│   └── 📁 model/
│       └── yolo_food.pt                # Pre-trained YOLO model weights
│
├── 📁 hasil fine tuning food detection/ # Training logs and results
│   └── 📁 runs/
│       └── 📁 detect/
│           └── 📁 train/
│               ├── args.yaml           # Training arguments
│               ├── results.csv         # Training metrics
│               └── 📁 weights/
│                   ├── best.pt         # Best model checkpoint
│                   └── last.pt         # Last model checkpoint
│
├── 📁 zip/                             # Archived files
│   └── test                            # Test data archive
│
├── 📝 Core Files
│   ├── README.md                       # Main documentation
│   ├── QUICKSTART.md                   # Quick start guide
│   ├── INSTALL.md                      # Detailed installation guide
│   ├── CONTRIBUTING.md                 # Contributing guidelines
│   ├── CHANGELOG.md                    # Version history
│   ├── LICENSE                         # MIT License
│   ├── CLEANUP_SUMMARY.md              # Project cleanup summary
│   ├── .gitignore                      # Git ignore rules
│   └── requirements.txt                # Python dependencies
│
├── 📄 Configuration & Examples
│   ├── config.py                       # Application configuration
│   ├── examples.py                     # Usage examples
│   ├── api.py                          # REST API module
│   └── nutrition.csv                   # Nutrition database (1300+ items)
│
└── 📊 Training Script
    └── fine tuning food detection.py   # YOLO model training script
```

## 📦 Package Contents

### `food_calorie_estimator/` - Main Package

#### `__init__.py`
- Package initialization and metadata
- Version, author, and description information
- Import statements for easy access
- Usage documentation

#### `detector.py` - Food Detection
- **Class**: `FoodDetector`
- **Methods**:
  - `__init__(model_path)` - Initialize with YOLO model
  - `detect_food(image_path, conf)` - Detect foods in image
- **Returns**: List of detections with class, bbox, confidence

#### `calorie_estimator.py` - Calorie Calculation
- **Function**: `hitung_total_kalori(detected_items, kalori_dict)`
- **Returns**: Total calories and per-item breakdown
- Handles multiple instances of same food

#### `calorie_logic.py` - Advanced Calorie Logic
- **Function**: `hitung_kalori_harian(...)` - Calculate daily calorie needs
  - Uses Harris-Benedict formula
  - Supports activity factors
- **Function**: `rekomendasi_makanan_kalori_maksimum(...)` - Food recommendations
  - Respects calorie limits
  - Returns randomized suggestions

#### `kalori_reference.py` - Calorie Database
- **Dictionary**: `KALORI_DICT` - 18 food items with calorie values
- Simple lookup for calorie estimation
- Extensible for more food items

#### `model/yolo_food.pt` - Pre-trained Model
- YOLOv11n architecture
- Trained on 18 food classes
- COCO pre-trained weights
- 640x640 input size

## 📚 Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| README.md | Comprehensive project documentation | Everyone |
| QUICKSTART.md | Get started in 5 minutes | New users |
| INSTALL.md | Detailed installation guide | Users with issues |
| CONTRIBUTING.md | How to contribute | Developers |
| CHANGELOG.md | Version history and updates | Version tracking |
| LICENSE | MIT license terms | Legal |
| CLEANUP_SUMMARY.md | What was changed/improved | Transparency |

## 🔧 Configuration Files

### `config.py`
Centralized configuration management:
- MODEL_CONFIG - Model paths and settings
- DETECTION_CONFIG - Detection parameters
- CALORIE_CONFIG - Database paths
- ACTIVITY_FACTORS - TDEE calculation factors
- IMAGE_CONFIG - Image processing settings
- API_CONFIG - Web service settings
- DATABASE_CONFIG - Data storage settings

Functions:
- `get_config(section)` - Get specific configuration
- `validate_config()` - Verify required files exist

### `requirements.txt`
Python package dependencies:
- ultralytics (YOLO)
- torch (Deep learning)
- opencv-python (Image processing)
- pandas (Data handling)
- numpy (Numerical computing)

### `.gitignore`
Git ignore patterns for:
- Python cache and bytecode
- Virtual environments
- IDE configurations
- YOLO/ML artifacts
- Temporary files

## 📊 Data Files

### `nutrition.csv` (1300+ items)
Comprehensive nutrition database with:
- id: Unique identifier
- calories: Energy content (kcal)
- proteins: Protein content (g)
- fat: Fat content (g)
- carbohydrate: Carb content (g)
- name: Food name (Indonesian)
- image: Image URL reference

## 🚀 Usage Files

### `examples.py`
Five complete working examples:
1. Basic food detection
2. Calorie calculation
3. Daily requirement calculation
4. Food recommendations
5. Complete workflow

Run with: `python examples.py`

### `api.py` (Optional)
REST API wrapper for core functions:
- FoodDetectionResponse class
- CalorieCalculationResponse class
- FoodCalorieAPI class with methods:
  - `detect_food_from_file()`
  - `detect_food_from_base64()`
  - `calculate_calories()`
  - `calculate_daily_requirement()`
  - `get_recommendations()`

Includes commented FastAPI integration example.

## 📈 Training Files

### `fine tuning food detection.py`
YOLOv11n training script:
- Loads Roboflow dataset
- Configures training parameters
- Trains for 50 epochs
- Saves best and last checkpoints
- Logs metrics and evaluation

### `hasil fine tuning food detection/runs/detect/train/`
Training artifacts:
- args.yaml - Training configuration
- results.csv - Epoch-by-epoch metrics
- weights/ - Model checkpoints
  - best.pt - Best model (highest accuracy)
  - last.pt - Last trained model

## 🔄 File Relationships

```
Input Image
    ↓
detector.py (FoodDetector)
    ↓
Detections (food items + confidence)
    ↓
calorie_estimator.py
    ↓
kalori_reference.py (KALORI_DICT)
    ↓
Total Calories + Breakdown
    ↓
calorie_logic.py
    ↓
Daily Requirement / Recommendations
    ↓
Output Results
```

## 🎯 Key Dependencies

```
food_calorie_estimator/
├── Depends on: ultralytics, torch, opencv-python
├── Optional: pandas (for CSV operations)
│
detector.py
├── Uses: YOLO from ultralytics
├── Loads: yolo_food.pt
│
calorie_estimator.py
├── Uses: python builtins only
├── Input: detected_items, kalori_reference
│
calorie_logic.py
├── Uses: pandas, datetime
├── Reads: nutrition.csv
│
config.py
├── Uses: pathlib, python builtins
├── Reads: file system paths
```

## 💾 File Sizes (Approximate)

| File | Size | Notes |
|------|------|-------|
| yolo_food.pt | 10-50 MB | Depends on model variant |
| nutrition.csv | 100-200 KB | 1300+ food items |
| detector.py | 2 KB | Detection module |
| calorie_estimator.py | 1 KB | Calculation module |
| calorie_logic.py | 3 KB | Advanced logic |
| README.md | 15 KB | Documentation |
| requirements.txt | 1 KB | Dependencies |

## 🔐 File Permissions

All Python files should be:
- Readable by all users
- Writable only by owner
- Executable (for scripts)

```bash
chmod 644 *.py *.md
chmod 755 food_calorie_estimator/
```

## 📝 Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| Modules | snake_case | detector.py |
| Classes | PascalCase | FoodDetector |
| Functions | snake_case | hitung_total_kalori |
| Constants | UPPER_CASE | KALORI_DICT |
| Variables | snake_case | total_calories |

## 🔍 File Organization Best Practices

1. **Keep modules focused** - Each module has single responsibility
2. **Centralize config** - All settings in config.py
3. **Separate concerns** - Detection, calculation, and logic separated
4. **Document thoroughly** - Every file has docstrings
5. **Use examples** - examples.py shows all features

## 📚 How to Navigate

**New to project?**
1. Start with QUICKSTART.md
2. Read README.md
3. Run examples.py
4. Explore package code

**Want to use it?**
1. Follow INSTALL.md
2. Check config.py for settings
3. Review examples.py for usage
4. Integrate into your project

**Want to contribute?**
1. Read CONTRIBUTING.md
2. Check code standards
3. Review existing code
4. Submit pull request

**Having issues?**
1. Check INSTALL.md troubleshooting
2. Read README.md sections
3. Review examples.py
4. Open GitHub issue

---

**Last Updated**: January 2026
**Project Version**: 1.0.0
