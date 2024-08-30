from setuptools import setup, find_packages

setup(
    name="Ecommerce Site Testing",
    version="3.0",
    description="WordPress Testing",
    packages=find_packages(),
    install_requires=[
        "PyMySQL==1.1.0",
        "pyparsing==3.1.1",
        "pytest==7.4.3",
        "pytest-html==4.0.2",
        "requests==2.31.0",
        "requests-oauthlib==1.3.1",
        "selenium==4.14.0",
        "WooCommerce==3.0.0",
        "allure-pytest==2.13.2",
        "cryptography==43.0.0",
    ],
)
