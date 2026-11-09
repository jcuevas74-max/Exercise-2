import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Wine Quality Prediction", page_icon="🍷", layout="wide")
st.title("🍷 Wine Quality Prediction System")
st.caption("Python • Streamlit • Random Forest")
if not Path("wine_quality.csv").exists() or not Path("wine_model.pkl").exists():
    st.warning("Run `python train_model.py` first to download the dataset and train the model.")
    st.stop()

df = pd.read_csv("wine_quality.csv", sep=";")
model = joblib.load("wine_model.pkl")
features = [col for col in df.columns if col != "quality"]
c1, c2, c3 = st.columns(3)
c1.metric("Wine Samples", len(df))
c2.metric("Average Quality Score", round(df.quality.mean(), 2))
c3.metric("GOOD QUALITY Samples", int((df.quality >= 6).sum()))
st.subheader("Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)

st.subheader("Predict One Wine Sample")
medians = df[features].median()
vals = {}
cols = st.columns(3)
for i, f in enumerate(features):
    with cols[i % 3]:
        vals[f] = st.number_input(f.replace("_", " ").title(),
                                  value=float(medians[f]), format="%.5f")
if st.button("Predict Quality", type="primary"):
    result = model.predict(pd.DataFrame([vals], columns=features))[0]
    st.success(f"Prediction: {result}")
    st.info("Preliminary screening only; not a final quality or food-safety decision.")

st.subheader("Batch Prediction (CSV)")
upload = st.file_uploader("Upload a CSV with all 11 input feature columns", type="csv")
if upload:
    batch = pd.read_csv(upload)
    missing = [f for f in features if f not in batch.columns]
    if missing:
        st.error("Missing columns: " + ", ".join(missing))
    else:
        batch["predicted_quality"] = model.predict(batch[features])
        st.dataframe(batch, use_container_width=True)
        st.download_button("Download Results CSV", batch.to_csv(index=False).encode(),
                          "wine_predictions.csv", "text/csv")
