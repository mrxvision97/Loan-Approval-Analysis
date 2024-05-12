import os


def create_project_structure(project_name):
    folders = [
        'data/raw', 'data/processed',
        'notebooks/exploratory_analysis',
        'notebooks/feature_engineering', 'notebooks/model_training',
        'notebooks/model_evaluation',
        'src/data', 'src/models', 'src/utils', 'reports/figures', 'reports/documentation'
    ]

    for folder in folders:
        os.makedirs(os.path.join(project_name, folder), exist_ok=True)

    # Create an empty README file
    with open(os.path.join(project_name, 'reports/README.md'), 'w') as f:
        f.write("# Project README\n\nThis is the README file for the project.")

    # Create an empty requirements.txt file
    with open(os.path.join(project_name, 'requirements.txt'), 'w') as f:
        pass


if __name__ == "__main__":
    project_name = "loan_approval_analysis"
    create_project_structure(project_name)
    print(f"Project structure created for '{project_name}'")
