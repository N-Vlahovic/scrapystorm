
from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

# Variables
# Github url
github_url = 'https://github.com/N-Vlahovic/scrapystorm'
# List of required modules
install_requires = ['pydantic', 'requests']
setup(
    name='scrapystorm',
    version='0.1',
    description='Python wrapper around the ScrapeStorm API.',
    license="GNU",
    long_description=long_description,
    author='Nikolai Vlahovic',
    author_email='nikolai@nexup.com',
    url=github_url,
    download_url=github_url,
    packages=find_packages(),
    install_requires=install_requires
)
