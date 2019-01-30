import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clonelab-chaitanya",
    version="0.0.2",
    author="Chaitanya",
    author_email="chaitanya2.1999@gmail.com",
    description="A python utility to clone groups and subgroups from gitlab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chaitanya-git/clonelab",
    packages=setuptools.find_packages(),
    scripts=['scripts/clonelab'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3",
        "Operating System :: POSIX",
    ],
)
