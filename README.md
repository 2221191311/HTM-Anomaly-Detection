# HTM-Anomaly-Detection
Evaluation of HTM anomaly detection using NAB dataset
# HTM-Based Streaming Anomaly Detection

## Description
This project evaluates the HTM-based anomaly detection method (`numenta`) using the Numenta Anomaly Benchmark (NAB).

The goal is to extend the evaluation beyond the NAB score by analyzing additional metrics such as precision, recall, and F1-score.

---

## Dataset
We use the **Numenta Anomaly Benchmark (NAB)** dataset, which contains:
- Real-world time-series data (traffic, cloud metrics, etc.)
- Artificial datasets with known anomalies
- Labeled anomaly windows for evaluation

---

## Model
We use the **`numenta` detector**, which represents the HTM-based method described in the selected paper.

No modification was made to the original model. The focus of this project is evaluation.

---

## Results

### NAB Benchmark Scores
- Standard NAB Score: **70.10**
- Reward Low FN Rate: **74.32**
- Reward Low FP Rate: **63.12**

### Additional Metrics (Point-Level)
These metrics were computed using TP, FP, and FN values from the benchmark output.

- Precision: **0.61**
- Recall: **0.007**
- F1-score: **0.014**

---

## Notes
- The NAB benchmark provides anomaly scores, not direct binary detections.
- Additional metrics were computed using point-level counts (TP, FP, FN).
- These are **preliminary metrics** and not window-based evaluation.

---

## Project Structure
HTM-Anomaly-Detection/
├── code/
│ └── compute_metrics.py
├── results/
│ ├── numenta_standard_scores.csv
│ └── final_results.json
└── README.md

---

## How to Run

1. Open terminal in the project folder

2. Run:

```bash
python code/compute_metrics.py results/numenta_standard_scores.csv
