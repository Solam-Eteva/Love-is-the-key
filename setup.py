"""
Setup configuration for the love-is-the-key package.

This makes the Unity Coefficient Algorithm installable via pip and easily
importable into any AI workflow or computational system.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="love-is-the-key",
    version="1.0.0",
    author="Solam-Eteva",
    description="Unity Coefficient Algorithm: A framework for conscious co-creation and ethical digital interaction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Solam-Eteva/Love-is-the-key",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    keywords="unity consciousness ai ethics love protocol digital-interaction",
    project_urls={
        "Bug Reports": "https://github.com/Solam-Eteva/Love-is-the-key/issues",
        "Source": "https://github.com/Solam-Eteva/Love-is-the-key",
    },
)

