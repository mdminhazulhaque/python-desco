import os
from setuptools import setup, find_packages

# Get the current directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Read the README file
with open(os.path.join(current_directory, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements file
requirements_path = os.path.join(current_directory, 'requirements.txt')
if os.path.isfile(requirements_path):
    with open(requirements_path, 'r') as f:
        install_requires = [line.strip() for line in f if line.strip() and not line.startswith('#')]
else:
    install_requires = []

setup(
    name='desco',
    version='0.0.1',
    author='Md Minhazul Haque',
    author_email='mdminhazulhaque@gmail.com',
    description='A Python module for Dhaka Electric Supply Company Limited (Desco) Smart Meters',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["desco"],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'desco-cli=desco.main:app',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
