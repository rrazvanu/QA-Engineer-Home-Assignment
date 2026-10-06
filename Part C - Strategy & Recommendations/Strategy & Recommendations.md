# Strategy & Recommendations

## Why These Tests Were Selected

### UI - Successful Single Bet Placement

This test covers the most critical end-to-end user journey: selecting an outcome, entering a stake, placing a bet, and
validating the receipt and resulting balance.

It provides high business value because it validates that the main betting flow works correctly from the user's
perspective.

### Place Bet API - Boundary testing**

Validates the API handling of stake boundary values:

- `0.99` → rejected with `422`
- `1.00` → accepted with `200`
- `1.01` → accepted with `200`
- `100.00` → accepted with `200`
- `100.01` → rejected with `422`

## What Was Left Manual

The following areas were intentionally kept for manual testing:

- Visual and layout validation
- Error modal presentation and usability
- Date and odds filter behavior
- Exploratory testing
- Negative UI scenarios

These areas benefit from human observation or are better suited to a broader test suite once the core automation
framework is established.

## Recommendations for Scaling

### 1. CI/CD Integration

Run the automated API and UI tests automatically in the CI pipeline for every relevant change / to run after every new release.

### 2. Expand API Coverage

Add API tests for:

- Insufficient balance
- Missing or invalid match ID
- Missing/invalid user context
- Duplicate bet / concurrent placement

### 3. Clarify Requirements

Clarify conflicting or insufficiently defined requirements before expanding automation.

For example, the specification states a minimum stake of €1.00 in one section and €1.01 in the validation rules.

The payout calculation is defined as `stake × odds`, but the expected rounding behavior for decimal monetary values is
not explicitly specified. 

