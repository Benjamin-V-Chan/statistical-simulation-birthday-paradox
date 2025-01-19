import random
import csv
from config import GROUP_SIZES, TRIALS, OUTPUT_SIMULATION_FILE

def simulate_birthday_paradox(group_size, trials):
    match_count = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        if len(birthdays) != len(set(birthdays)):
            match_count += 1
    return match_count, trials

def main():
    results = []
    for size in GROUP_SIZES:
        matches, trials = simulate_birthday_paradox(size, TRIALS)
        probability = matches / trials
        results.append([size, probability])
    
    with open(OUTPUT_SIMULATION_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Group Size", "Probability"])
        writer.writerows(results)

if __name__ == "__main__":
    main()
