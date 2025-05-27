import pendulum

now = pendulum.now()
prev_month = now.subtract(months=1)

print(f"previous month -> {prev_month.year}/{prev_month.month}")
