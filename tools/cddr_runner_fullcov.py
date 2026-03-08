"""
CDDR full-covariance runner
Minimal reproducible diagnostic.

Computes η = DL / ((1+z)^2 * DA)

This script assumes Pantheon+ DL data and BAO DA
inputs have already been aligned by redshift.

The goal is reproducibility, not model fitting.
"""

import numpy as np
import pandas as pd


def compute_eta(dl, da, z):
    return dl / ((1 + z) ** 2 * da)


def run_cddr(datafile):

    df = pd.read_csv(datafile)

    z = df["z"].values
    dl = df["DL"].values
    da = df["DA"].values

    eta = compute_eta(dl, da, z)

    mean_eta = np.mean(eta)
    std_eta = np.std(eta)

    print("η mean:", mean_eta)
    print("η std:", std_eta)

    return mean_eta, std_eta


if __name__ == "__main__":
    run_cddr("data/cddr_inputs.csv")
