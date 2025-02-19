# Generate Python files from 3_6_1.py to 3_6_20.py

for i in range(1, 21):
    filename = f"beginner/module_6/summary/tasks/6_6_{i}.py"
    with open(filename, "w") as file:
        file.write("# Auto-generated Python script\n\n")

print("Files generated successfully.")
