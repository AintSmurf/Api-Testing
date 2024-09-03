# E-Commerce Website Testing Framework

## Table of Contents
1. [Introduction](#1-introduction)
2. [Set Up The Framework](#2-set-up-the-framework)
   1. [Important Information](#21-important-information)
   2. [WordPress Configuration](#22-wordpress-configuration)
   3. [Set Up Credentials](#23-set-up-credentials)
   4. [Testing Environment Setup](#24-testing-environment-setup)
   5. [Makefile Automation](#25-makefile-automation)
3. [Testing Section](#3-testing-section)
   1. [Backend Testing](#31-backend-testing)
   2. [Frontend Testing](#32-frontend-testing)
4. [Docker Setup](#4-docker-setup)
   1. [Linux Container](#41-linux-container)
   2. [Windows Container](#42-windows-container)
5. [Jenkins Integration](#5-jenkins-integration)
6. [Conclusion](#6-conclusion)

## 1. Introduction
This framework is designed to provide a comprehensive testing environment for WordPress developers, enabling them to perform functional, unit, visual, end-to-end, and security testing on their websites. It leverages **pytest**, **SQL**, **Docker**, and **CI/CD pipelines** to streamline the testing process.

## 2. Set Up The Framework

### 2.1 Important Information
- **Supported Browser**: Chrome (handled automatically by Selenium)
- **Supported Platform**: WordPress sites
- **Plugin Requirement**: WooCommerce must be installed on your WordPress site.
- **Local WordPress Installation**: If using Local for WordPress, fill in the port option.

### 2.2 WordPress Configuration
1. Download the [sample_products.xml](https://wordpress.org/plugins/woocommerce/) if running WordPress locally.
2. Import the XML file in WordPress: Tools -> Import -> WordPress -> Run Importer -> Choose File -> Upload.
3. Go to Settings -> Reading -> Set "A static page" and select "Shop" as the homepage.
4. Enable registration: Settings -> General -> Check "Anyone can register".
5. Configure WooCommerce settings: WooCommerce -> Settings -> Accounts & Privacy -> Enable all options under "Guest checkout" and "Account Creation" (except the last one).

### 2.3 Set Up Credentials
Set the following environment variables:
- `WC_KEY`: WordPress public key
- `WC_SECRET`: WordPress secret key
- `DB_USER`: Database login name (default: root)
- `DB_PASSWORD`: Database password (default: root)
- `DB_SERVER`: Database host (default: localhost; use IP if on VMware or any other server)
- `DB_NAME`: Database schema name
- `SITE_URL`: URL of the site
- `PORT`: WordPress database port (optional)

### 2.4 Testing Environment Setup
1. Create a Python virtual environment:
 ```bash
   pip install virtualenv
   python -m venv <env-name>
```
2. activate virtual environment
 ```bash
   source <env-name>/bin/activate  # for Linux/macOS
   .\<env-name>\Scripts\activate  # for Windows
```
3. Install the project dependencies:
 ```bash
   python setup.py install
```
4. prepare the database:
 ```bash
   python db_seed.py
```
5. Makefile Automation
 ```bash
   make all
```
* Set up the Python environment
* Install dependencies
* Seed the database with 'db_seed.py'
* Run all tests
## 3. Testing Section
### 3.1 Backend Testing
#### Use the following commands to run tests:
* `tcid` : Test case ID
* `tcidc`: Test case ID for customers
* `tcidp`: Test case ID for products
* `tcido`: Test case ID for orders
#### Example commands:
* Run all customer tests: `pytest -m customers`
* Run all product tests: `pytest -m products`
* Run all order tests: `pytest -m orders`
### 3.2 Frontend Testing
* `tcids`: Test case ID for Selenium
* For more tests and documentation, refer to the [WooCommerce REST API Documentation](https://woocommerce.com/document/api-documentation/).
### 4. Docker Setup
## 4.1 Linux Container
1) Build the Docker image:
 ```bash
   docker build -t automation .
```
2) Run the Docker container:
 ```bash
   docker run -it automation /bin/bash
```
3) In a new terminal, copy the credentials file to the container:
 ```bash
   docker ps  # Get the container name
   docker cp Credentials.sh <container-name>:/automation
```
4) Inside the container, source the credentials:
 ```bash
   source Credentials.sh
```
5) Run the tests:
 ```bash
   pytest  # Without report
   pytest --html=report.html --self-contained-html  # With report
```
## 4.2 Windows Container
* Follow the same steps as Linux but replace '/bin/bash' with '/cmd.exe' or '/powershell.exe'
* For credentials, run:
 ```bash
   .\Credentials.ps1  # For PowerShell
   call Credentials.bat  # For Batch
```
### 5. Jenkins Integration
1) open `jenkins.txt`
2) Replace `{path to your python.exe}` with the actual path:
   * Right-click 'python.exe' in the Start menu -> Open file location -> Copy as path.
   * Update the path in `Jenkins.txt`, replacing single backslashes with double backslashes (\\).
3) Replace `{path to your credentials file}` with the actual path.
## Run in Jenkins
1) Go to your Jenkins URL.
2) Create a new item -> name it -> select Pipeline -> click OK.
3) Copy the code from `Jenkins.txt` into the pipeline section and save.
4) Click `Build` to start the process.
5) Test reports will be saved in the results folder.

### 6. Conclusion
This framework provides a robust testing solution for WordPress developers, covering both frontend and backend testing, as well as API testing. With support for Docker and CI/CD pipelines, it ensures that your WordPress site is thoroughly tested before deployme