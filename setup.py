from setuptools import setup, find_packages

setup(
    name="quantscape",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy"
    ],
    author="Cam Schmidt",
    description="A quantitative finance Python library for option pricing, volatility insights & Greeks computation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    url="URL to your library's repository or website",
)
