import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ai_tech_support"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/audio/__init__.py",
    f"src/{project_name}/audio/recorder.py",
    f"src/{project_name}/audio/transcriber.py",
    f"src/{project_name}/support/__init__.py",
    f"src/{project_name}/support/tech_assistant.py",
    f"src/{project_name}/support/knowledge_base.py",
    f"src/{project_name}/speech/__init__.py",
    f"src/{project_name}/speech/synthesizer.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/config.py",
    f"src/{project_name}/utils/logger.py",
    f"src/{project_name}/utils/exception.py",
    "tests/__init__.py",
    "tests/test_audio.py",
    "tests/test_support.py",
    "tests/test_speech.py",
    "config/config.yaml",
    "data/product_manual.txt",
    "requirements.txt",
    "setup.py",
    "app.py",
    "main.py",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
