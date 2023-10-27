import requests

packages = [
    "PyMySQL",
    "pyparsing",
    "pytest",
    "pytest-html",
    "requests",
    "requests-oauthlib",
    "selenium",
    "WooCommerce",
    "allure-pytest"
]

old_versions = {
    "PyMySQL": "1.0.2",
    "pyparsing": "3.0.9",
    "pytest": "7.1.2",
    "pytest-html": "3.1.1",
    "requests": "2.28.1",
    "requests-oauthlib": "1.3.1",
    "selenium": "4.5.0",
    "WooCommerce": "3.0.0",
    "allure-pytest": "2.13.2"
}

updated_dependencies = {}

for package in packages:
    url = f"https://pypi.org/pypi/{package}/json"
    response = requests.get(url)
    data = response.json()
    latest_version = data["info"]["version"]
    updated_dependencies[package] = latest_version

with open("setup.py", "r") as file:
    setup_content = file.read()

for package in packages:
    setup_content = setup_content.replace(f'"{package}=={old_versions[package]}"', f'"{package}=={updated_dependencies[package]}"')

with open("setup.py", "w") as file:
    file.write(setup_content)
