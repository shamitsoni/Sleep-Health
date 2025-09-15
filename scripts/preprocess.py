import pandas as pd

df = pd.read_csv("../data/sleep_health.csv")
df['Sleep Disorder'] = df['Sleep Disorder'].fillna('None')
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
df.to_csv("../data/sleep_health_clean.csv", index=False)
