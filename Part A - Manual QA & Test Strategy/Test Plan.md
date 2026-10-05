# Part A - Test Plan

### TS-01 - Successful Single Bet Placement

**Priority:** Critical

**Risk Rationale:**  
Bet placement is the core business flow. Failures in selection, stake handling, payout calculation, balance deduction,
or receipt data could result in financial loss and an inconsistent user experience.

**Steps:**

1. Open the application using the assigned user ID.
2. Verify that an upcoming football match displays the home team, away team, kickoff date/time, and available odds.
3. Select an available outcome for the match.
4. Select an outcome for another match.
5. Enter a valid stake.
6. Place the bet.
7. Verify the bet receipt and balance.
8. Close the receipt.

**Expected Result:**

- The match displays the required kickoff date/time information.
- The selected outcome for the second match replaces the previous selection, leaving only one active selection.
- The bet is successfully placed.
- The receipt displays the correct bet ID, match, selection, stake, odds, potential payout, and placement timestamp.
- The potential payout is calculated correctly.
- The balance is reduced by the stake amount.
- Closing the receipt returns the user to the main flow with no active selection.

### TS-02 - Prevent Multiple Bet Placements from Repeated Submission

**Priority:** Critical

**Risk Rationale:**  
Bet placement is a financial transaction. Repeated submissions can create multiple bets from a single intended action,
potentially resulting in multiple stake deductions and a negative account balance. This represents a critical financial
integrity and exploitation risk.

**Steps:**

1. Select a valid upcoming football match and outcome.
2. Enter a valid stake.
3. Click **Place Bet** repeatedly before the placement process completes.
4. Review the generated bet receipts/tickets and account balance.

**Expected Result:**

- The **Place Bet** action is protected while the bet is being processed.
- Only one bet is created.
- Only one receipt/ticket is generated.
- The stake is deducted only once.
- The user's balance cannot become negative.
- The placement resolves to a single final outcome.

### TS-03 - Prevent Betting on Past Matches

**Priority:** Critical

**Risk Rationale:**  
The feature supports upcoming/pre-match events only. Allowing users to place bets on past matches could result in
invalid financial transactions and significant business risk.

**Steps:**

1. Identify a match with a kickoff date/time in the past.
2. Select an available outcome for the match.
3. Enter a valid stake.
4. Attempt to place the bet.

**Expected Result:**

- Past matches cannot be used to place a bet.
- Bet placement is blocked or rejected.
- No bet is created and no balance is deducted.

### TS-04 - Stake Validation and Boundary Conditions

**Priority:** Critical

**Risk Rationale:**  
Invalid stake values could result in incorrect or financially unsafe bet placement. The feature defines minimum,
maximum, precision, numeric, and balance constraints.

**Steps:**

1. Select a valid upcoming football match and outcome.
2. Enter a stake below the minimum value (€0.99).
3. Enter the minimum boundary value (€1.00).
4. Enter a stake above the minimum value (€1.01).
5. Enter the maximum allowed stake (€100.00).
6. Enter a stake above the maximum value (€100.01).
7. Enter a value with more than two decimal places (€10.001).
8. Enter a non-numeric value.
9. Attempt to place the bet with invalid stake values.

**Expected Result:**

- Values below the minimum stake are rejected.
- The minimum valid stake is accepted.
- Values above the maximum stake are rejected.
- The maximum valid stake is accepted.
- Values with more than two decimal places are rejected.
- Non-numeric values are rejected.
- Invalid bets cannot be placed and the balance is not affected.

### TS-05 - Insufficient Balance Validation

**Priority:** High

**Risk Rationale:**  
The stake must not exceed the user's available balance. Failure to enforce this rule could allow financially invalid
bets and cause incorrect account balance handling.

**Steps:**

1. Select a valid upcoming football match and outcome.
2. Enter a stake greater than the available balance.
3. Attempt to place the bet.

**Expected Result:**

- The bet is rejected.
- An insufficient balance message is displayed.
- No bet is placed.
- The user's balance remains unchanged.

### TS-06 - Bet Slip Selection Removal

**Priority:** High

**Risk Rationale:**  
The Bet Slip must allow users to remove their active selection or clear the entire slip before placing a bet. Incorrect
removal behavior could leave stale selections or allow an unintended bet to be placed.

**Steps:**

1. Select an outcome for an upcoming football match.
2. Verify the selection is displayed in the Bet Slip.
3. Use the per-selection remove (`x`) control.
4. Select an outcome again.
5. Use the **Remove All** control.
6. Verify the Bet Slip state.

**Expected Result:**

- The per-selection remove control removes the active selection from the Bet Slip.
- **Remove All** clears the active selection from the Bet Slip.
- After removal, the user cannot place a bet without an active selection.

## EXTRA SCENARIOS

### TS-07 - Verify Football Matches Only

**Priority:** High

**Risk Rationale:**  
The feature supports football/soccer events only. Displaying or allowing bets on events from other sports would violate
the defined product scope and could result in invalid bets.

**Steps:**

1. Open the application using the assigned user ID.
2. Review all events displayed in the match list.
3. Review the available competitions and teams.
4. Verify the event data returned by the matches API.

**Expected Result:**

- Only football/soccer matches are available for betting.
- All displayed competitions and teams correspond to football/soccer.
- No events from other sports are displayed or available for selection.

### TS-08 - Date Filter Validation

**Priority:** Medium

**Risk Rationale:**  
Incorrect date filtering could cause users to see events outside the selected date criteria or miss eligible matches.

**Steps:**

1. Set the date filter to a single day.
2. Apply the filter.
3. Set the date filter to a date range.
4. Apply the filter using a range that contains multiple match dates.
5. Test the date range boundaries.

**Expected Result:**

- A single-day filter displays only matches for the selected day.
- A date-range filter displays only matches within the selected range.
- The date range is inclusive, meaning matches on both the start and end dates are included.

### TS-09 - Odds Filter Validation

**Priority:** Medium

**Risk Rationale:**  
Incorrect odds filtering could result in matches outside the requested odds range being displayed or valid matches being
excluded.

**Steps:**

1. Set a minimum and maximum odds value.
2. Apply the filter.
3. Test values equal to the minimum and maximum boundaries.
4. Set a minimum odds value greater than the maximum odds value.
5. Apply the filter.

**Expected Result:**

- Only matches with odds within the selected range are displayed.
- The minimum and maximum boundaries are inclusive.
- An invalid range where the minimum exceeds the maximum is rejected.
- Clear validation feedback is displayed for an invalid range.