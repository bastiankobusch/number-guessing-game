print ("Chest Press Rep Estimator")

#Input Data Set 1 and 2
weight1 = float(input("Weight Data Set 1 (kg): "))
reps1 = float (input("Reps Data Set 1 "))
print()
weight2 = float(input("Weight Data Set 2 (kg): "))
reps2 = float (input("Reps Data Set 2 "))
print()

#Input Target Weight
target_weight = float(input("Enter Target Weight (kg): "))
print()

#Calculate Estimated Reps
estimated_reps = reps1 + ((reps2- reps1) / (weight2 - weight1)) * (target_weight - weight1)

#Output Estimated Reps
print()
print(f"Estimated Reps: ")
print()
print(f"{target_weight} kg -> {round(estimated_reps, 1)} Reps ")
print()
print()
input("Press Enter to close application.")