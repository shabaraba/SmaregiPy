import setuptools

from SmaregiPlatformApi import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SmaregiPlatformApi",
    version=__version__,
    author="shabaraba",
    author_email="work.shabaraba@gmail.com",
    description="Smaregi platform api library. It is unofficial.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shabaraba/smaregiplatformApi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        # 'console_scripts': ['sample_command = sample_command.sample_command:main']
    },
    python_requires='>=3.7',
)
