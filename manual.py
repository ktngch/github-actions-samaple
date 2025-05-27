import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-y', type=str, dest="year", required=True)
parser.add_argument('-m', type=str, dest="month", required=True)
parser.add_argument('-d', type=str, dest="day", required=True)

args = parser.parse_args()

data = {
    "year": args.year,
    "month": args.month,
    "day": args.day
}

print(data)

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
