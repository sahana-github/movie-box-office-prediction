import os

def create_structure():
    folders = [
        "data/raw", "data/processed", "notebooks", "src", "models", "scripts",
        "configs", "tests", "logs", "docker"
    ]
    files = [
        "README.md", ".gitignore", "requirements.txt", "setup.py",
        "docker/Dockerfile", "docker/docker-compose.yml"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    for file in files:
        with open(file, 'w') as f:
            pass
    print("Project structure created!")

if __name__ == "__main__":
    create_structure()
