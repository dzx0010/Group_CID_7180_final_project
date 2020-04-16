
#!usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CID",
    version="1.0",
    author="Isaac Mcneely De Xing Isaac Mcneely",
    author_email="dzx0010@auburn.edu",
    description="A package for compare COVID-19 genome",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dzx0010/Group_CID_7180_final_project.git",
    packages=['CID'],
    package_dir={'CID': 'CID'},
    install_requires=['numpy','biopython'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,zip_safe=False)

