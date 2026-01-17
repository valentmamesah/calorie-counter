# Contributing to Food Calorie Counter

Thank you for your interest in contributing to the Food Calorie Counter project! We welcome contributions from the community.

## How to Contribute

### 1. Reporting Bugs

If you find a bug, please open an issue with the following information:
- Clear description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python version and environment details
- Stack trace (if applicable)

### 2. Suggesting Enhancements

We'd love to hear your feature ideas! When suggesting an enhancement:
- Use a clear and descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful
- List any related issues or PRs

### 3. Pull Requests

#### Prerequisites
- Fork the repository
- Create a feature branch (`git checkout -b feature/your-feature-name`)
- Make your changes
- Write or update tests as necessary
- Ensure code follows the project's style guide

#### Pull Request Process
1. Update the README.md with details of any new features
2. Update docstrings and comments appropriately
3. Add tests for new functionality
4. Ensure all tests pass: `pytest`
5. Follow PEP 8 style guide for Python code
6. Submit your PR with a clear description

## Code Style Guide

### Python
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused on a single task
- Use type hints where applicable

### Example
```python
def hitung_kalori(food_items: list, kalori_dict: dict) -> tuple:
    """
    Calculate total calories from food items.
    
    Args:
        food_items: List of detected food items
        kalori_dict: Dictionary mapping food names to calories
        
    Returns:
        Tuple of (total_calories, breakdown_dict)
    """
    # Implementation
    pass
```

### Documentation
- Include docstrings for all modules, classes, and functions
- Use Google-style docstrings
- Include type hints in function signatures
- Add examples in docstrings where helpful

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/calorie-counter.git
   cd calorie-counter
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest  # For testing
   ```

4. Make your changes and test:
   ```bash
   pytest
   ```

## Commit Messages

- Use clear and descriptive commit messages
- Start with a verb (Add, Fix, Update, Improve, etc.)
- Reference issues when applicable (`Fixes #123`)
- Example: `Fix food detection confidence threshold issue (#123)`

## Project Structure

```
food_calorie_estimator/
├── detector.py              # YOLO food detection
├── calorie_estimator.py     # Calorie calculation
├── calorie_logic.py         # Advanced logic
└── kalori_reference.py      # Calorie reference data
```

## Testing

- Write tests for new features
- Ensure existing tests still pass
- Aim for good test coverage
- Run: `pytest`

## Documentation

- Update README.md for user-facing changes
- Update docstrings for code changes
- Keep examples up to date
- Maintain CHANGELOG if applicable

## Community

- Be respectful and inclusive
- Help others when possible
- Provide constructive feedback
- Follow the Code of Conduct

## Questions?

Feel free to open an issue for discussion or contact the maintainers.

Thank you for contributing! 🎉
