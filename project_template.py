import os
from pathlib import Path
import logging
import json
from datetime import datetime

# Logging configuration
def setup_logging(project_name):
    log_dir = Path(project_name) / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    # Main logger for both setup and lifecycle
    logger = logging.getLogger(project_name)
    logger.setLevel(logging.INFO)

    # File handler for logging to a file
    file_handler = logging.FileHandler(log_dir / "project.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    # Stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('[%(asctime)s]: %(message)s:'))
    logger.addHandler(stream_handler)

    return logger

def create_project_structure(project_name, file_list, logger):
    for filepath in file_list:
        filepath = Path(filepath)
        filedir, filename = filepath.parent, filepath.name

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logger.info(f"Creating directory: {filedir} for the file: {filename}")

        if not filepath.exists() or filepath.stat().st_size == 0:
            filepath.touch()
            logger.info(f"Creating empty file: {filepath}")
        else:
            logger.info(f"{filename} already exists")

def log_project_event(logger, event_type, description, **kwargs):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "description": description,
        **kwargs
    }
    logger.info(json.dumps(log_entry))

def main():
    project_name = 'LLM-Project'
    
    logger = setup_logging(project_name)
    
    log_project_event(logger, "PROJECT_INITIATION", f"Starting project: {project_name}")

    list_of_files = [
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",
        "dvc.yaml",
        "params.yaml",
        "requirements.txt",
        "setup.py",
        "app.py",
        "research/trials.ipynb",
        "templates/index.html",
        "logs/.gitkeep"  # Ensure logs directory is created and tracked
    ]

    create_project_structure(project_name, list_of_files, logger)

    log_project_event(logger, "PROJECT_SETUP_COMPLETE", 
                      f"Project '{project_name}' setup completed successfully",
                      files_created=len(list_of_files))

    logger.info(f"Project '{project_name}' setup completed successfully!")
    logger.info("You can now start adding your specific components and files to this structure.")

    # Example of logging a project planning event
    log_project_event(logger, "PROJECT_PLANNING", 
                      "Initial project planning completed",
                      planned_duration="3 months",
                      key_milestones=["Requirements Gathering", "Development", "Testing", "Deployment"])

if __name__ == "__main__":
    main()