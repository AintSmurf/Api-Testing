#!/bin/bash

pytest --alluredir="./reports"
allure serve "./reports"