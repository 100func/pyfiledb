import setuptools

setuptools.setup(
    name='pyfiledb',
    version='0.5.2',
    author='100func',
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[
        "click",
    ],
    entry_points={
        'console_scripts': [
            'pyfiledb-cli = pyfiledb.cli.__main__:cli',
        ],
    },
)
