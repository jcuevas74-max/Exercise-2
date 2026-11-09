# Dataset Information

**Dataset:** UCI Wine Quality Dataset — Red Wine  
**UCI page:** https://archive.ics.uci.edu/dataset/186/wine+quality  
**CSV download:** https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

The red wine dataset has 1,599 samples, 11 physicochemical input features, and an original quality score (12 columns total).

Input features: fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol.

Target rule:
- Quality score >= 6: GOOD QUALITY
- Quality score < 6: NEEDS IMPROVEMENT

The original quality score is excluded from input features to avoid target leakage.
