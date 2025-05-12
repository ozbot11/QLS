import argparse, os, time
import numpy as np
import cupy as cp
import pandas as pd
import yfinance as yf

def download_sp500_prices():
    try:
        df = yf.download("^GSPC", period="10y", interval="1d", progress=False, auto_adjust=False)
        if df.empty:
            return None
        return df['Close'].dropna()
    except Exception:
        return None

def generate_spd_matrix(n):
    A = np.random.randn(n, n)
    return A.T @ A + n * np.eye(n)

def estimate_condition_number(A, invA):
    return np.linalg.norm(A) * np.linalg.norm(invA)

def rel_error(A, invA):
    I = np.eye(A.shape[0])
    return np.linalg.norm(A @ invA - I) / np.linalg.norm(I)

def time_inv_cpu(A):
    start = time.time()
    invA = np.linalg.inv(A)
    end = time.time()
    return invA, end - start

def time_inv_gpu(A):
    A_gpu = cp.asarray(A)
    start = time.time()
    invA_gpu = cp.linalg.inv(A_gpu)
    cp.cuda.Device(0).synchronize()  # Ensure all operations are complete
    end = time.time()
    return cp.asnumpy(invA_gpu), end - start

def log_results(n, device, wall_time, error, kappa, path="results/baseline.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    row = {
        "n": n,
        "device": device,
        "wall_time_s": wall_time,
        "rel_error": error,
        "κ_estimate": kappa
    }
    df = pd.DataFrame([row])
    df.to_csv(path, mode='a', header=not os.path.exists(path), index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, required=True)
    parser.add_argument('--gpu', action='store_true')
    args = parser.parse_args()

    n = args.n
    sp500_prices = download_sp500_prices()

    if sp500_prices is not None and len(sp500_prices) >= n * n:
        A = sp500_prices.values[:n*n].reshape((n, n))
        A = A.T @ A + n * np.eye(n)  # Make SPD
    else:
        A = generate_spd_matrix(n)

    if args.gpu:
        invA, t = time_inv_gpu(A)
        device = "gpu"
    else:
        invA, t = time_inv_cpu(A)
        device = "cpu"

    error = rel_error(A, invA)
    kappa = estimate_condition_number(A, invA)
    log_results(n, device, t, error, kappa)

if __name__ == '__main__':
    main()