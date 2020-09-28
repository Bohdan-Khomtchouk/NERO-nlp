import setuptools





with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NERO-nlp",
    version="0.0.7",
    include_package_data=True,
    author="Bohdan Khomtchouk",
    author_email="bohdan@uchicago.edu",
    description="A biomedical Named Entity (Recognition) Ontology",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)