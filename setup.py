from setuptools import setup,find_packages

setup(name="Ecommerce Site Testing",
    version="2.8",
    description="WordPress Testing",
    packages=find_packages(),
    install_requires=[
        "PyMySQL==1.0.2",
        "pyparsing==3.0.9",
        "pytest==7.1.2",
        "pytest-html == 3.1.1",
        "requests==2.28.1",
        "requests-oauthlib==1.3.1",
        "selenium==4.5.0",
        "WooCommerce==3.0.0",]
      )