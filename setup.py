import setuptools

with open('README.md', "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

repo_name = "Text-Summarizer"
authour_username = "Vishwavijeth"
src_repo = "textSummarizer"


setuptools.setup(
    name = src_repo,
    version = __version__,
    author = authour_username,
    description = "Text Summarizer Project",
    long_description = long_description,
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
)

