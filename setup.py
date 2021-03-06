import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tnj",
    version="1.0.0",
    author="Yuan Shi",
    author_email="shiyuan404@hotmail.com",
    description="Thrift converting tools: json2thrift, thrift2json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shiyuan/tnj",
    packages=setuptools.find_packages(),
    install_requires=[
        'ply',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
