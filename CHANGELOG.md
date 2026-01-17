# Changelog

All notable changes to the Food Calorie Counter project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-17

### Added
- Initial public release of Food Calorie Counter
- YOLOv11n-based food detection system
- Support for 18 Southeast Asian food items
- Automatic calorie estimation from detected foods
- Daily calorie requirement calculation using Harris-Benedict formula
- Food recommendation system based on calorie constraints
- Comprehensive nutrition database (1300+ items)
- Full Python package with modular architecture
- Complete documentation and usage examples
- Contributing guidelines
- Pre-trained YOLO model weights

### Features
- `FoodDetector` class for food item detection in images
- `hitung_total_kalori()` function for calorie calculation
- `hitung_kalori_harian()` function for daily calorie requirement
- `rekomendasi_makanan_kalori_maksimum()` function for food recommendations
- `KALORI_DICT` reference database with 18 food items
- Support for custom confidence thresholds in detection
- Detailed bounding box information for detected items

### Documentation
- Comprehensive README with installation and usage guide
- Module-level documentation for all packages
- Inline code comments for clarity
- Function docstrings with examples
- Contributing guidelines
- This changelog

### Training
- YOLOv11n model fine-tuned on custom food detection dataset
- 50 epochs of training
- mAP@0.5 and mAP@0.5:0.95 evaluation metrics
- Training artifacts and logs included

---

## Planned Features (Future Releases)

### [Unreleased]
- [ ] Support for additional food categories (100+)
- [ ] Portion size estimation using depth estimation
- [ ] Detailed macro nutrient breakdown (proteins, fats, carbs)
- [ ] Real-time video stream analysis
- [ ] Mobile application (iOS/Android)
- [ ] Web API endpoint
- [ ] User profiles and dietary preferences
- [ ] Multi-language support
- [ ] Recipe generation based on detected foods
- [ ] Allergen detection and warnings
- [ ] Integration with fitness trackers
- [ ] Cloud storage for calorie history
- [ ] Barcode scanning for packaged foods
- [ ] Restaurant menu integration

---

## Version History

### v1.0.0
- Official release with core functionality
- Stable API and module structure
- Production-ready model

---

## Migration Guide

### From Beta to v1.0.0
No breaking changes. All APIs remain backward compatible.

---

## Support

For issues or questions about any version, please visit:
https://github.com/your-username/calorie-counter/issues

---

**Last Updated**: January 17, 2026
