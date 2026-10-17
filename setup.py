from setuptools import setup, find_packages

setup(
    name="apex-empire",
    version="1.0.0",
    author="Zakaria Ghibeche",
    description="A Zero-Dependency, Mobile-Optimized Modular Cybersecurity & Data Intelligence Ecosystem.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZakariaGhibeche/Ghibeche-Empire-",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
    ],
    python_requires=">=3.7",
)
