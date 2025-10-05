import pandas as pd

# Fill in blank cells and use consistent naming conventions for features
df = pd.read_csv("../data/sleep_health.csv")
df['Sleep Disorder'] = df['Sleep Disorder'].fillna('None')
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Extract data for new features

# 1. Hypertension
df[["systolic", "diastolic"]] = df["blood_pressure"].str.split("/", expand=True).astype(int)
df["hypertension"] = ((df["systolic"] >= 130) | (df["diastolic"] >= 80)).astype(int)


# Export processed data
df.to_csv("../data/sleep_health_clean.csv", index=False)
