# Installation Guide

Complete step-by-step guide for installing and setting up the Food Calorie Counter project.

## Prerequisites

- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **Git**: For cloning the repository
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: ~2GB free space for model and dependencies

### Optional
- **GPU**: NVIDIA GPU with CUDA 11.8+ for faster inference
- **cuDNN**: For GPU acceleration

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/calorie-counter.git
cd calorie-counter
```

### 2. Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

After activation, your command prompt should show `(venv)` prefix.

### 3. Upgrade pip and setuptools

```bash
pip install --upgrade pip setuptools wheel
```

### 4. Install Dependencies

#### Basic Installation (CPU)

```bash
pip install -r requirements.txt
```

This will install:
- `ultralytics` - YOLO framework
- `torch` - CPU version
- `opencv-python` - Image processing
- `pandas` - Data handling
- `numpy` - Numerical computing

#### GPU Installation (CUDA 11.8)

If you have an NVIDIA GPU and want to use CUDA acceleration:

```bash
# Remove CPU PyTorch if already installed
pip uninstall torch -y

# Install PyTorch with CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install other dependencies
pip install -r requirements.txt
```

#### GPU Installation (CUDA 12.1)

```bash
pip uninstall torch -y
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

### 5. Verify Installation

```bash
# Check Python version
python --version

# Check main dependencies
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import cv2; print(f'OpenCV: {cv2.__version__}')"
python -c "from ultralytics import YOLO; print('YOLO: OK')"
```

### 6. Download Pre-trained Model (if not included)

The model should be at: `food_calorie_estimator/model/yolo_food.pt`

If missing, you can download it separately or retrain using:
```bash
python fine\ tuning\ food\ detection.py
```

## Troubleshooting

### Issue: ModuleNotFoundError

**Problem**: `ModuleNotFoundError: No module named 'ultralytics'`

**Solution**:
```bash
# Make sure virtual environment is activated
pip install ultralytics
```

### Issue: CUDA Not Found

**Problem**: PyTorch detects CPU instead of GPU

**Solution**:
1. Check NVIDIA GPU:
   ```bash
   nvidia-smi
   ```

2. Reinstall PyTorch with correct CUDA version:
   ```bash
   pip uninstall torch -y
   pip install torch --index-url https://download.pytorch.org/whl/cuXXX
   ```

3. Verify CUDA availability:
   ```bash
   python -c "import torch; print(torch.cuda.is_available())"
   ```

### Issue: Import Errors

**Problem**: `ImportError` when importing from `food_calorie_estimator`

**Solution**:
```bash
# Make sure you're in the project root directory
cd calorie-counter

# Check if __init__.py exists in package
ls food_calorie_estimator/__init__.py

# Try importing
python -c "from food_calorie_estimator.detector import FoodDetector"
```

### Issue: Model File Not Found

**Problem**: `FileNotFoundError: model/yolo_food.pt not found`

**Solution**:
```bash
# Check if model exists
ls -la food_calorie_estimator/model/

# If missing, download or ensure it's in correct location
# Model should be at: food_calorie_estimator/model/yolo_food.pt
```

### Issue: Memory Error

**Problem**: `RuntimeError: CUDA out of memory` or `MemoryError`

**Solution**:
1. Reduce batch size
2. Use smaller model variant
3. Close other applications
4. Increase available RAM/VRAM

## Uninstallation

To completely remove the project and virtual environment:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
# On Windows
rmdir /s venv

# On macOS/Linux
rm -rf venv

# Remove cloned repository
cd ..
rm -rf calorie-counter
```

## Docker Installation (Optional)

For consistent environment across machines:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-c", "from food_calorie_estimator.detector import FoodDetector"]
```

Build and run:
```bash
docker build -t calorie-counter .
docker run -it calorie-counter
```

## Next Steps

After installation:

1. **Read the README**: [README.md](README.md)
2. **Check examples**: Review usage examples in the documentation
3. **Test installation**: Run a simple detection
   ```python
   from food_calorie_estimator.detector import FoodDetector
   detector = FoodDetector()
   print("Installation successful!")
   ```

## Getting Help

If you encounter issues:

1. Check this guide's troubleshooting section
2. Review the [README.md](README.md)
3. Open an issue on GitHub
4. Check existing issues for similar problems

## System Requirements

### Minimum
- OS: Windows, macOS, or Linux
- CPU: 2 cores
- RAM: 4 GB
- Storage: 2 GB
- Python: 3.8+

### Recommended
- OS: Ubuntu 20.04+ / Windows 10+ / macOS 10.14+
- CPU: 4+ cores
- RAM: 8 GB+
- Storage: 4 GB+
- GPU: NVIDIA RTX 3060+ (for faster inference)
- Python: 3.10+

## Performance Tips

### For Faster Inference
1. Use GPU (CUDA 11.8+)
2. Reduce input image size
3. Increase confidence threshold (faster filtering)
4. Batch process multiple images

### For Lower Memory Usage
1. Use CPU instead of GPU
2. Use smaller model variant
3. Process images one at a time
4. Close unnecessary applications

---

**Last Updated**: January 2026
**Version**: 1.0.0
