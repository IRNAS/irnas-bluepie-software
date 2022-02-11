import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toolbox",
    version="0.1.0",
    author="Marko Sagadin",
    author_email="marko.sagadin42@gmail.com",
    description="Testing installation of Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IRNAS/irnas-bluepie-software",
    project_urls={
        "Bug Tracker": "https://github.com/IRNAS/irnas-bluepie-software/issues"
    },
    license="MIT",
    packages=["bluepie"],
    install_requires=["bleak"],
)
