import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="euler",
    version="0.0.1",
    author="Jose Ramirez",
    author_email="a30673083@gmail.com",
    description="The library I've built over the years to help me with project euler's problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jose-ramirez/euler",
    packages=['euler', 'euler.geom', 'euler.algebra', 'euler.numbers', 'euler.algorithms'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)