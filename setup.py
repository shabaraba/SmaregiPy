import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smaregipy",
    version='0.3.1',
    author="shabaraba",
    author_email="work.shabaraba@gmail.com",
    description="Smaregi platform api library. It is unofficial.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shabaraba/smaregipy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        # 'console_scripts': ['sample_command = sample_command.sample_command:main']
    },
    install_requires=[
        'pytz',
        'pydantic',
    ],
    python_requires='>=3.7',
)
