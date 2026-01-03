import os

DATA_PATH = "data/train.csv"
MODEL_PATH = "models/model.txt"

os.makedirs("models", exist_ok=True)

with open(DATA_PATH, "r") as f:
    data = f.read()

with open(MODEL_PATH, "w") as f:
    f.write(f"trained_on_data_size={len(data)}")

print("Model training completed")
