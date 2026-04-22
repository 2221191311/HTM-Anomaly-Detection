import csv
import sys

def safe_div(a, b):
    return a / b if b != 0 else 0.0

def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "../results/numenta_standard_scores.csv"

    totals_row = None

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Clean column names
        reader.fieldnames = [name.strip() for name in reader.fieldnames]

        for row in reader:
            row = {k.strip(): v.strip() for k, v in row.items()}

            if row.get("Detector", "").lower() == "totals":
                totals_row = row
                break

    if totals_row is None:
        print("Totals row not found")
        return

    tp = int(float(totals_row["TP"]))
    fp = int(float(totals_row["FP"]))
    fn = int(float(totals_row["FN"]))

    precision = safe_div(tp, tp + fp)
    recall = safe_div(tp, tp + fn)
    f1 = safe_div(2 * precision * recall, precision + recall)

    print("Precision:", round(precision, 3))
    print("Recall:", round(recall, 3))
    print("F1-score:", round(f1, 3))

if __name__ == "__main__":
    main()
