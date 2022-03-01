from setuptools import find_packages, setup

setup(
    name="t2k_hangul_core",
    version="0.1.0",
    author="Travel2kashmir.com",
    maintainer_email="techworks@travel2kashmir.com",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "aiocache",
        "aiohttp",
        "dataclasses-json",
        "pandas", "sqlalchemy", "psycopg2", "dicttoxml", "pytest"
    ]
)
