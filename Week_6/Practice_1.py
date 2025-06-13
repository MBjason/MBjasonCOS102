import numpy as np

maths = int(input(" Enteer your grade in Maths"))
physics = int(input("Enter your grade on Physics"))
ux_design = int(input("Enter your grade UI/UX design"))
problem_solving = int(input("Enter your grade on problem solving")) 

data = {
    "Maths": maths,
    "Physics": physics,
    "Ux_design": ux_design,
    "Problem_solving": problem_solving
}


arr1 = np.array(list(data.values()))


average = np.mean(arr1)
maximum_value = np.max(arr1)
minimum_Value = np.min(arr1)

print(f"Your accumulated score is:{average}")
print(f"Your maximum Value is: {maximum_value}")
print(f"Minimum: {minimum_Value}")

print(" Your original scores are:")
for key, value in data.items():
    print(f"{key}: {value}")
