import pandas as pd
from config import OUTPUT_SIMULATION_FILE, OUTPUT_ANALYSIS_FILE

def load_simulation_results(file_path):
    return pd.read_csv(file_path)

def compute_statistics(data):
    statistics = {
        "Mean Probability": data["Probability"].mean(),
        "Standard Deviation": data["Probability"].std(),
    }
    return statistics

def main():
    data = load_simulation_results(OUTPUT_SIMULATION_FILE)
    stats = compute_statistics(data)
    
    pd.DataFrame([stats]).to_csv(OUTPUT_ANALYSIS_FILE, index=False)

if __name__ == "__main__":
    main()
