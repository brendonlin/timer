from setuptools import setup, find_packages

setup(
    name="timer",
    version="0.1",
    author="Brendon Lin",
    author_email="brendon.lin@outlook.com",
    description="Timer",
    packages=find_packages(),
    install_requires=["win10toast"],
    entry_points={"console_scripts": ["timer = timer.main:main"]},
)
