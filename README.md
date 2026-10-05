# FDM Tensile Coupon Design and DOE Optimization

Design-focused additive manufacturing portfolio project combining coupon geometry, a 2³ full-factorial DOE, and simulated tensile-strength analysis.

> **Project status:** Coursework-based academic portfolio project applying concepts from MCE 515 Additive Manufacturing at Cleveland State University. The coupon case study was developed after completing the course. All response data are simulated; no specimens were printed or physically tested.

![Coupon concept](images/coupon_concept.png)

## Objective

Evaluate how layer height, print speed, and infill density influence simulated FDM tensile strength, then identify the strongest evaluated parameter combination.

## Design and DOE

| Item | Definition |
|---|---|
| Coupon geometry | Educational dog-bone-style coupon; not a certified ASTM specimen |
| Factors | Layer height, print speed, infill density |
| Levels | 0.16/0.28 mm; 35/65 mm/s; 60/100% |
| Design | 2³ full factorial, 8 conditions, 3 simulated replicates each |
| Response | Simulated tensile strength in MPa |

## Result

The strongest simulated condition was **0.16 mm layer height, 35 mm/s print speed, and 100% infill**, with a mean response of **46.0 MPa**. The defined baseline condition (0.28 mm, 65 mm/s, 60% infill) averaged **40.0 MPa**, giving a **15.0% simulated improvement**.

## Repository contents

- `cad/coupon_outline.dxf` and `cad/concept_coupon.stl` - conceptual exchange geometry.
- `drawings/coupon_engineering_drawing.pdf` - dimensioned educational drawing.
- `data/fdm_doe_results.csv` - 24-row simulated DOE dataset.
- `analysis/doe_analysis.py` - reproducible analysis.
- `analysis/doe_summary.csv`, `main_effects.csv`, and charts - analysis outputs.
- `reports/fdm_doe_report.pdf` - technical project summary.

## Run the analysis

```bash
cd analysis
python doe_analysis.py
```

Requires Python 3 with `pandas`.

## Limitations and next steps

This project demonstrates DOE planning and analysis; it does not establish physical material properties. A physical follow-up should print randomized replicates, condition specimens consistently, test them on a calibrated universal testing machine, and report measurement uncertainty and failure location.

## License

Provided for portfolio review and learning. Do not use the coupon geometry as a certified test specimen.
