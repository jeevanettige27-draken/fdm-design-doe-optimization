"""Reproduce the FDM DOE summary and baseline-to-optimum comparison."""
import pandas as pd
from pathlib import Path
p=Path(__file__).resolve().parent
df=pd.read_csv(p.parent/"data"/"fdm_doe_results.csv")
keys=["layer_height_mm","print_speed_mm_s","infill_percent"]
summary=df.groupby(keys)["simulated_tensile_strength_mpa"].agg(["mean","std"]).reset_index()
print(summary.to_string(index=False))
base=summary.query("layer_height_mm==0.28 and print_speed_mm_s==65 and infill_percent==60")["mean"].iloc[0]
opt=summary.query("layer_height_mm==0.16 and print_speed_mm_s==35 and infill_percent==100")["mean"].iloc[0]
print(f"\nBaseline={base:.1f} MPa  Optimum={opt:.1f} MPa  Improvement={(opt/base-1)*100:.1f}%")
