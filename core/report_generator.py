import json, csv

def export_to_json(data, path="report.json"):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, path="report.csv"):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Platform", "URL"])
        for site in data:
            writer.writerow(site)
