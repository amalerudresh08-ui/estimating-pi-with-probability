# Monte Carlo Estimation of Pi — Student Research Project

## Research question
How does increasing the number of uniformly random points affect the accuracy of a Monte Carlo estimate of pi?

## What is included
- `pi_monte_carlo.py`: reproducible Python experiment (30 repetitions for each sample size)
- `replicate_results.csv`: each individual run and its result
- `summary_results.csv`: mean estimate, mean absolute error, RMSE, and theoretical standard error
- `figures/`: plots created from the recorded simulation
- `research_report.pdf`: report with the mathematical derivation and the actual results from this run

## How to run it in Google Colab
1. Open https://colab.research.google.com/
2. Choose New Notebook.
3. Upload `pi_monte_carlo.py`, or paste its contents into a code cell.
4. If needed, run `!pip install matplotlib`.
5. Run the script. It writes CSV files and creates a graph in the notebook's working directory.
6. Download the CSV files and graph from Colab if you want to preserve your own run.

## Reproducibility
The code uses a fixed master seed (`20261010`) and derives a different seed for each repetition. Re-running the same code with the same Python implementation should reproduce the same pseudo-random sequence and outputs.

## Important academic note
The simulation results in the included report are from one actual run of the supplied code. If you modify the code, run it again and update your report so it matches your own results. Do not claim the project is novel: Monte Carlo estimation of pi is a classic educational experiment. Your contribution is the documented comparison of sample sizes, repeated runs, error measures, and interpretation.
