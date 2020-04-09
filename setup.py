import setuptools

setuptools.setup(
    name="NewPy", # Replace with your own username
    version="0.0.1",
    author="Jerry Crum",
    author_email="jcrum@nd.edu",
    description="A package that aids in making Newman Projections with exact angles.",
    url="https://github.com/jtcrum/newpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
