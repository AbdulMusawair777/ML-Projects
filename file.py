import os

# Define the folder structure
project_name = "ML-Projects"
folders = [
    project_name,
    f"{project_name}/data",
    f"{project_name}/notebooks",
    f"{project_name}/scripts",
    f"{project_name}/models"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create key files
files = {
    f"{project_name}/README.md": "# ML-Project\n",
    f"{project_name}/requirements.txt": "scikit-learn\npandas\nmatplotlib\n",
    f"{project_name}/scripts/housing_model.py": "# Starter script for ML model\n",
    f"{project_name}/.gitignore": "__pycache__/\n*.pyc\n"
}

# Create and write to the files
for path, content in files.items():
    with open(path, 'w') as file:
        file.write(content)

print(f"Project '{project_name}' structure created.")
