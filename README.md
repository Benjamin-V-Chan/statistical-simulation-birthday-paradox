# statistical-simulation-birthday-paradox

## Project Overview

The Birthday Paradox, a counterintuitive probability concept, suggests that in a group of just 23 people, there is a greater than 50% chance that two individuals share the same birthday. This project explores this phenomenon through statistical simulation, data analysis, and visualization. The goal is to understand and analyze the probability of birthday matches as group sizes increase, providing insights into the paradox and its mathematical underpinnings.

### **Mathematical Explanation**

The probability that two people do not share the same birthday is calculated by considering all possible unique birthday assignments for a given group size. For a group of `n` people, the probability of no shared birthdays can be expressed as:

```
P(no match) = (365/365) * (364/365) * (363/365) * ... * ((365 - n + 1)/365)
```

The complement of this value gives the probability of at least one shared birthday:

```
P(at least one match) = 1 - P(no match)
```

This simulation uses Monte Carlo methods to empirically estimate these probabilities by simulating random birthday assignments across many trials for varying group sizes.

---

## Folder Structure

```
statistical-simulation-birthday-paradox
├── scripts
│   ├── 01_simulation.py      # Runs simulations for various group sizes
│   ├── 02_analysis.py        # Analyzes simulation results
│   ├── 03_visualization.py   # Generates plots based on analysis
├── outputs
│   ├── simulation_results.csv # Stores results of the simulations
│   ├── analysis_results.csv   # Stores analyzed statistics
│   └── visualizations      # Folder for generated plots
├── config.py                  # Configurations for the simulation
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```
