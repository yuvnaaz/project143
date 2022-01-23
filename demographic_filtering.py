import numpy as np
import pandas as pd

df = pd.read_csv('articles.csv')

df = df.sort_values(['total_events'], ascending=[False])

output = df[["url", "text", "lang","total_events"]].head(20).values.tolist()