# Reflection Answers — Wine Quality Prediction System

## 1. What is the prediction target, and why is quality excluded from input features?
The target is wine quality classification. A score of 6 or higher becomes GOOD QUALITY, while a score below 6 becomes NEEDS IMPROVEMENT. The quality score is excluded from input features because it is the value being predicted. Including it would cause target leakage. The model instead uses physicochemical measurements.

## 2. Why is recall for GOOD QUALITY important, and what could happen if it is low?
Recall for GOOD QUALITY measures how many actual good-quality samples are correctly identified. Low recall means some good samples may be classified as NEEDS IMPROVEMENT, potentially causing unnecessary additional assessment or poor production decisions.

## 3. Can the model be reliably used for another wine producer?
Not automatically. Producers may differ in production methods, ingredients, environmental conditions, and wine characteristics. The model should be tested on samples from another producer before being considered reliable.

## 4. Why should the system be treated as preliminary screening rather than a final quality decision?
Predictions can be incorrect and depend on the provided data. Laboratory testing, sensory evaluation, food-safety checks, and professional assessment remain important. The system supports quality-control staff but does not replace their decisions.

## 5. What additional data or testing would improve reliability?
Collect samples from more producers, regions, and production conditions; use cross-validation; compare models; and test with external samples not used during training. These steps help assess consistency and generalization.
