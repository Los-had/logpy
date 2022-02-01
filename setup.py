import setuptools


setuptools.setup(
    name="logpy",
    version="0.0.1",
    author="Los-had",
    author_email="bernardesmiguel709@gmail.com",
    description="Logging library for python 3.6 above",
    license="MIT",
    long_description="Simple logging library for python 3.6 above, under MIT license",
    long_description_content_type="text/markdown",
    url="https://github.com/Los-had/logpy",
    packages=setuptools.find_packages(),
    install_requires=[
        "colorama"
    ],
    keywords="logpy logging lib loshad",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
