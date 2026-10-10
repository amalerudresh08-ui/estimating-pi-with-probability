"""
Monte Carlo estimation of pi
Author: [Your name]
Purpose: Reproducible experiment for a student research project.

Run in Google Colab or locally with Python 3.
Only standard Python libraries are needed for the simulation and CSV files.
Matplotlib is used for graphs: pip install matplotlib
"""
import math
import random
import csv
import statistics
import matplotlib.pyplot as plt

TRUE_PI = math.pi
SAMPLE_SIZES = [100, 1_000, 10_000, 100_000]
REPEATS = 30
MASTER_SEED = 20261010

def estimate_pi(number_of_points, seed):
    """Return a Monte Carlo estimate of pi and the inside-circle count."""
    rng = random.Random(seed)
    inside = 0

    for _ in range(number_of_points):
        x = rng.uniform(-1, 1)
        y = rng.uniform(-1, 1)

        # A point is inside the unit circle if x^2 + y^2 <= 1.
        if x*x + y*y <= 1:
            inside += 1

    estimate = 4 * inside / number_of_points
    return estimate, inside

def main():
    all_results = []
    summary = []

    # Repeat each sample size 30 times to observe randomness.
    for size_index, n in enumerate(SAMPLE_SIZES):
        estimates = []
        for repeat in range(REPEATS):
            seed = MASTER_SEED + size_index * 1000 + repeat
            estimate, inside = estimate_pi(n, seed)
            estimates.append(estimate)
            all_results.append({
                "sample_size": n,
                "repeat": repeat + 1,
                "seed": seed,
                "inside_circle": inside,
                "pi_estimate": estimate,
                "absolute_error": abs(estimate - TRUE_PI),
            })

        mean_estimate = statistics.mean(estimates)
        sd_estimate = statistics.stdev(estimates)
        mae = statistics.mean(abs(value - TRUE_PI) for value in estimates)
        rmse = math.sqrt(statistics.mean((value - TRUE_PI)**2 for value in estimates))
        theoretical_se = 4 * math.sqrt((TRUE_PI / 4) * (1 - TRUE_PI / 4) / n)

        summary.append({
            "sample_size": n,
            "repeats": REPEATS,
            "mean_estimate": mean_estimate,
            "sd_estimate": sd_estimate,
            "mean_absolute_error": mae,
            "rmse": rmse,
            "theoretical_standard_error": theoretical_se,
        })

    # Save every run and the summary as CSV files.
    with open("replicate_results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=all_results[0].keys())
        writer.writeheader()
        writer.writerows(all_results)

    with open("summary_results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=summary[0].keys())
        writer.writeheader()
        writer.writerows(summary)

    print("Results across repeated simulations")
    print("N       mean estimate   mean absolute error   RMSE")
    for item in summary:
        print(f"{item['sample_size']:<7} "
              f"{item['mean_estimate']:.6f}        "
              f"{item['mean_absolute_error']:.6f}             "
              f"{item['rmse']:.6f}")

    # Plot A: RMSE and theoretical standard error against sample size.
    sizes = [item["sample_size"] for item in summary]
    rmse_values = [item["rmse"] for item in summary]
    se_values = [item["theoretical_standard_error"] for item in summary]

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, rmse_values, marker="o", label="Observed RMSE")
    plt.plot(sizes, se_values, marker="s", label="Theoretical standard error")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of random points, N (log scale)")
    plt.ylabel("Error scale (log scale)")
    plt.title("Error versus sample size")
    plt.legend()
    plt.tight_layout()
    plt.savefig("error_vs_sample_size.png", dpi=180)
    plt.show()

if __name__ == "__main__":
    main()
