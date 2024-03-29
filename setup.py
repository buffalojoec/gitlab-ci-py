import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gitlab_ci_py",
    version="1.0.0",
    description="Python wrapper for creating GitLab CI/CD pipelines",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jpcaulfi/gitlab-ci-py",
    author="Joseph Caulfield",
    author_email="jcaulfield135@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["gitlab_ci_py"],
    include_package_data=True,
    install_requires=["pyyaml"],
    entry_points={
        "console_scripts": [
            "gitlab_ci_py=gitlab_ci_py.__main__:main",
        ]
    },
)