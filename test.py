import numpy as np
import pandas as pd

df = pd.read_csv("data/raw/games_march2025_full.csv", 
        on_bad_lines='warn')

print(df)