# Generate Python files from 3_6_1.py to 3_6_20.py

for i in range(1, 21):
    filename = f"beginner/module_4/summary/tasks/4_5_{i}.py"
    with open(filename, "w") as file:
        file.write("# Auto-generated Python script\n\n")

print("Files generated successfully.")
