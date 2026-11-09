# SAD Mini-Analysis — Wine Quality Prediction System

## 1. Problem Statement
A small wine-producing company wants a preliminary method to screen red wine samples using physicochemical measurements. The system classifies samples as GOOD QUALITY or NEEDS IMPROVEMENT to support quality-control work.

## 2. System Users
- **Quality-Control Staff:** review sample predictions.
- **Production Supervisor:** use results to support production monitoring.
- **Data Analyst:** prepare the dataset, train the model, and evaluate performance.

## 3. Inputs
Fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol. The original quality score is used only to create the target category, not as a model input.

## 4. Process
The user supplies sample measurements or a CSV file. The system validates the required columns, preprocesses the measurements, applies the trained Random Forest model, and displays a predicted category.

## 5. Outputs
- GOOD QUALITY or NEEDS IMPROVEMENT prediction
- Accuracy, precision, recall, and F1-score
- Confusion matrix and classification report
- Downloadable batch prediction results

## 6. Limitations
The model uses the UCI red-wine dataset and may not generalize to other producers, wine types, regions, or production conditions. It is a preliminary screening tool, not a replacement for laboratory testing, sensory evaluation, food-safety checks, or professional quality-control decisions.
