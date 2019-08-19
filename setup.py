import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpleTk",
    version="0.3.0",
    author="Pascal Fabiano",
    author_email="pascal.fabiano99@gmail.com",
    description="A package to create simple Tkinter-GUIs using a seperate textfile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pascalliano/SimpleTk",
    packages=["SimpleTk"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
