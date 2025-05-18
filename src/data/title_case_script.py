import re

def title_case_trainer_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    def smart_title_case(name):
        # Handle names like "BILLY & ALLY" or "ADMIN SHELLEY"
        return ' '.join(word.capitalize() if word.isalpha() else word
                        for word in re.split(r'(\W+)', name))

    def replace_trainer_name(match):
        name = match.group(1)
        if not name.strip():
            return '._(""),'
        title_cased = smart_title_case(name)
        return f'.trainerName = _("{title_cased}"),'

    updated_content = re.sub(
        r'\.trainerName\s*=\s*_\("([A-Z0-9 &\'\-]+)"\),',
        replace_trainer_name,
        content
    )

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print("✔️ Trainer names updated to Title Case with multi-word support.")

# Example usage
title_case_trainer_names('trainers.h')  # Adjust path as needed
