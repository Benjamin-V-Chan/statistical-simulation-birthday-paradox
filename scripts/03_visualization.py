import pandas as pd
import matplotlib.pyplot as plt
from config import OUTPUT_SIMULATION_FILE, VISUALIZATIONS_FOLDER

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_probabilities(data):
    plt.figure()
    plt.plot(data["Group Size"], data["Probability"], marker="o")
    plt.title("Birthday Paradox Probabilities")
    plt.xlabel("Group Size")
    plt.ylabel("Probability of Match")
    plt.grid(True)
    plt.savefig(f"{VISUALIZATIONS_FOLDER}/probabilities_vs_group_size.png")

def main():
    data = load_data(OUTPUT_SIMULATION_FILE)
    plot_probabilities(data)

if __name__ == "__main__":
    main()
