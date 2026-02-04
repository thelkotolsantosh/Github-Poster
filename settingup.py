from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-poster",
    version="1.0.0",
    author="Santosh thelkotlol",
    author_email="thelkotolsantosh@example.com",
    description="A simple utility to post content to GitHub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/github-poster",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "github-poster=github_poster.cli:main",
        ],
    },
)
