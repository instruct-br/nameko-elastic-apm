import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nameko-elastic-apm",
    version="0.0.1",
    author="Instruct Developers",
    author_email="contato@instruct.com.br",
    description="A Nameko extension to monitor service performances with Elastic APM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/instruct-br/nameko-elastic-apm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "elastic-apm>=5.5",
        "nameko>=2.2"
    ],
)
