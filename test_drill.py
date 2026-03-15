"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    s = pd.Series([1, 2, np.nan, 4])
    cleaned = clean_column(s)
    assert cleaned.isnull().sum() == 0
    assert cleaned[2] == 2.0


def test_compute_revenue():
    q = pd.Series([10, 2])
    p = pd.Series([5, 3])
    rev = compute_revenue(q, p)
    assert rev[0] == 50
    assert rev[1] == 6
