import pkg_resources

with open("requirements.txt", "w") as f:
    for dist in pkg_resources.working_set:
        f.write(f"{dist.project_name}=={dist.version}\n")

print("Plik requirements.txt został wygenerowany.")
