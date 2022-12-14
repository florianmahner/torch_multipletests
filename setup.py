try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

requires = ["torch", "torchvision", "numpy", "statsmodels"]

setup(
    name="torch_multipletests",
    version="0.0.1",
    author="Florian P. Mahner",
    author_email="florian.mahner@gmail.com",
    license="LICENSE",
    long_description=open("README.md").read(),
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requires,
)
