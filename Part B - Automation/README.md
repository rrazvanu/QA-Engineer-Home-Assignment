# Part B - Automation

## Overview

Automation tests for the Single Bet Placement feature.

### Tech Stack

- Python 3.14
- Pytest
- Selenium WebDriver
- Requests
- Allure

## Tests

### UI Test

Validates the successful single bet placement flow through the UI.

### API Test

Validates that the API rejects an invalid betting selection.

## Install Dependencies

```bash
pip install -r requirements.txt

```

## Run Tests

```bash

python -m pytest --alluredir=allure-results

```

## Open the Allure report:

```bash
allure serve allure-results