import re

file_path = "species_names.h"

# Read the file
with open(file_path, "r") as f:
    lines = f.readlines()

# Process each line
updated_lines = []
for line in lines:
    # Find all _("<UPPERCASE>") patterns
    match = re.search(r'_\("([A-Z]+)"\)', line)
    if match:
        upper_name = match.group(1)
        title_name = upper_name.capitalize()
        line = line.replace(f'_("{upper_name}")', f'_("{title_name}")')
    updated_lines.append(line)

# Write back to the original file
with open(file_path, "w") as f:
    f.writelines(updated_lines)

print("species_names.h updated to Title Case successfully.")
