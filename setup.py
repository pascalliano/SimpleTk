import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpleTk",
    version="0.2.1",
    author="Pascal Fabiano",
    author_email="pascal.fabiano99@gmail.com",
    description="A package to create simple Tkinter-GUIs using a seperate textfile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=["SimpleTk"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)