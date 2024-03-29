days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())
gathered_plunder = 0

for day in range(1, days + 1):
    gathered_plunder += plunder_per_day
    if day % 3 == 0:
        gathered_plunder += plunder_per_day * 0.5
    if day % 5 == 0:
        gathered_plunder *= 0.7

if gathered_plunder >= expected_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    percentage = (gathered_plunder * 100) / expected_plunder
    print(f"Collected only {percentage:.2f}% of the plunder.")
