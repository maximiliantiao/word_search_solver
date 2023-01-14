from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="word-search-solver",
    version="1.0.0",
    description="The amazing Word Search Solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maximiliantiao/word_search_solver",
    author="Maximilian Tiao",
    author_email="maximilian.tiao@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    keywords="puzzle, games",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    extras_require={  # Optional
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    entry_points={  # Optional
        "console_scripts": [
            "sample=sample:main",
        ],
    },
    project_urls={  # Optional
        "Bug Tracking": "https://github.com/maximiliantiao/word_search_solver/issues",
        "Source": "https://github.com/maximiliantiao/word_search_solver"
    },
)