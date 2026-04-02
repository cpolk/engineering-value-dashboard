import csv
from statistics import mean

INPUT_FILE = "sample_metrics.csv"

def load_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def to_float(rows, key):
    return [float(r[key]) for r in rows]

def main():
    rows = load_rows(INPUT_FILE)

    pr_cycle = mean(to_float(rows, "pr_cycle_hours"))
    deploy_freq = mean(to_float(rows, "deploys_per_week"))
    vuln_remediation = mean(to_float(rows, "vuln_remediation_days"))

    print("Engineering Value Summary")
    print("-------------------------")
    print(f"Average PR cycle time (hrs): {pr_cycle:.2f}")
    print(f"Average deployments per week: {deploy_freq:.2f}")
    print(f"Average vulnerability remediation time (days): {vuln_remediation:.2f}")

    print("\nInterpretation:")
    print("- Faster PR cycle time can indicate smoother collaboration and less delivery friction.")
    print("- Higher deployment frequency can indicate improved delivery capability.")
    print("- Lower remediation time can indicate stronger operational security responsiveness.")

if __name__ == "__main__":
    main()
