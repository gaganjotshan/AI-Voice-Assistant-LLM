import setuptools
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "AI-Voice-Assistant-LLM"
AUTHOR_USER_NAME = "gaganjotshan"
SRC_REPO = "ai_tech_support"
AUTHOR_EMAIL = "gagan.shan7@gmail.com"

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="AI-powered Technical Support Assistant, using RAG and Mistral",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements('requirements.txt'),
    python_requires = ">=3.10,<3.11",
    classifiers=[
        "Programming Language :: Python :: >=3.10,<3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)