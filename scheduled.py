import pendulum
import json

now = pendulum.now()
prev_month = now.subtract(months=1)

data = {
    "year": prev_month.year,
    "month": prev_month.month,
    "day": prev_month.day
}

print(data)

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
