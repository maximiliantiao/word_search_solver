from setuptools import setup, find_packages

setup(
    name="word-search-solver",
    version="1.0.0",
    license='MIT',
    description="The amazing Word Search Solver",
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
    project_urls={  # Optional
        "Bug Tracking": "https://github.com/maximiliantiao/word_search_solver/issues",
        "Source": "https://github.com/maximiliantiao/word_search_solver"
    },
)