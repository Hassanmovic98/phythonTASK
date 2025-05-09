age = int(input("Enter your age in years: "))


max_heart_rate = 220 - age


lower_target = 0.50 * max_heart_rate
upper_target = 0.85 * max_heart_rate

# Display the results
print(f"\nMaximum Heart Rate: {max_heart_rate} beats per minute")
print(f"Target Heart Rate Range: {lower_target:.1f} - {upper_target:.1f} beats per minute")
