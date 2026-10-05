# Strategy & Recommendations

## Why These Tests Were Selected

### UI - Successful Single Bet Placement
This test covers the most critical end-to-end user journey: selecting an outcome, entering a stake, placing a bet, and validating the receipt and resulting balance.

It provides high business value because it validates that the main betting flow works correctly from the user's perspective.

### API - Invalid Selection Validation
This test focuses on a backend business rule that is more suitable for API-level automation.

It verifies that the API rejects unsupported betting selections and returns the expected validation response.

The two tests were intentionally chosen at different layers to avoid duplicating the same coverage. The assignment emphasizes targeted automation and clean engineering rather than exhaustive coverage.

## What Was Left Manual

The following areas were intentionally kept for manual testing:

- Visual and layout validation
- Error modal presentation and usability
- Date and odds filter behavior
- Exploratory testing
- Detailed boundary and negative UI scenarios

These areas benefit from human observation or are better suited to a broader test suite once the core automation framework is established.

## Recommendations for Scaling

### 1. CI/CD Integration
Run the automated API and UI tests automatically in the CI pipeline for every relevant change. Allure reports should be published as build artifacts.

### 2. Expand API Coverage
Add API tests for:
- Stake boundaries and precision
- Insufficient balance
- Missing or invalid match ID
- Missing/invalid user context
- Duplicate bet / concurrent placement

### 3. Clarify Requirements
Clarify conflicting requirements before expanding automation. For example, the specification states a minimum stake of €1.00 in one section and €1.01 in the validation rules.

A single agreed rule should be established so that both manual and automated tests validate the same expected behavior.