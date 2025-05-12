import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_baseline(csv_path="results/baseline.csv"):
    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    # Group by n and device, compute average time
    grouped = df.groupby(["n", "device"])["wall_time_s"].mean().unstack()

    grouped.plot(marker='o')

    plt.title("Matrix Inversion Time: CPU vs GPU")
    plt.xlabel("Matrix Size (n)")
    plt.ylabel("Wall Time (s)")
    plt.grid(True)
    plt.legend(title="Device")
    plt.tight_layout()
    plt.savefig("results/baseline_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_baseline()