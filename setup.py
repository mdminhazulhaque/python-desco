"""
Setup configuration for the Desco Prepaid Python package.
"""

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
    with open(requirements_path, 'r', encoding="utf-8") as f:
        install_requires = [
            line.strip() 
            for line in f 
            if line.strip() and not line.startswith('#')
        ]
else:
    install_requires = ['requests', 'click', 'tabulate']

# Get version from GitHub Actions environment variables if available
version = '1.0.0'  # Default version
if 'GITHUB_RUN_NUMBER' in os.environ:
    run_number = os.environ.get('GITHUB_RUN_NUMBER')
    version = f"1.{run_number}.0"

setup(
    name='desco',
    version=version,
    author='Md Minhazul Haque',
    author_email='mdminhazulhaque@gmail.com',
    description='A Python CLI tool for Dhaka Electric Supply Company Limited (DESCO) prepaid electricity accounts',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mdminhazulhaque/python-desco',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'desco-cli=desco.main:app',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='desco electricity prepaid bangladesh utility cli',
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/mdminhazulhaque/python-desco/issues',
        'Source': 'https://github.com/mdminhazulhaque/python-desco',
    },
)
