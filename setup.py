from setuptools import setup, Extension
from setuptools import find_packages
import interactive_augmentations


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="interactive_augmentations",
        version=interactive_augmentations.__version__,
        description="Explore Albuemntations' augmentations in Jupyter Notebook",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Wojciech Malinowski",
        author_email="wojciec.malinowski@gmail.com",
        url="https://github.com/wojciech-malinowski/interactive_augmentations",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires=">3.5.2")
