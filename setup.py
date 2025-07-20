from setuptools import setup, find_packages

setup(
    name="qml-classification",
    version="1.0.0",
    author="[Adınız]",
    author_email="[email@example.com]",
    description="Kuantum Makine Öğrenmesi ile Sınıflandırma",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/[kullaniciadi]/qml-classification",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "qiskit>=0.45.0",
        "qiskit-machine-learning>=0.7.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.0.0",
    ],
)