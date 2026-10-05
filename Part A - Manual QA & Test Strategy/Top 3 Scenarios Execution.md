# Part A - Execution Results

## Execution Overview

The three highest-priority test scenarios were executed against the application using the assigned user context.
The execution also included targeted exploratory checks around the bet placement flow.

| Scenario                                                         | Priority | Status   | Defects Found                      |
|------------------------------------------------------------------|----------|----------|------------------------------------|
| TS-01 - Successful Single Bet Placement                          | Critical | **FAIL** | BUG-001, BUG-004, BUG-005, BUG-006 |
| TS-02 - Prevent Multiple Bet Placements from Repeated Submission | Critical | **FAIL** | BUG-002                            |
| TS-03 - Prevent Betting on Past Matches                          | Critical | **FAIL** | BUG-003                            |

---

# Part A - Execution Results & Bug Reports

## Issues Found

### BUG-001 - Kickoff Time Not Displayed

| Field                  | Details                                                                                                                                               |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Severity**           | Medium                                                                                                                                                |
| **Reproduction Steps** | 1. Open the application using the assigned user ID.<br>2. Review an upcoming football match in the match list.                                        |
| **Expected Result**    | The match displays the kickoff date and time.                                                                                                         |
| **Actual Result**      | The match displays relative date information such as `UPCOMING`, but the kickoff time is not displayed.                                               |
| **Business Impact**    | Users cannot see the exact kickoff time, making it difficult to determine when a match starts and whether it is still eligible for pre-match betting. |
| **Evidence**           | Screenshot BUG-001                                                                                                                                    |

### BUG-002 - Multiple Bets Created from Repeated Place Bet Clicks

| Field                  | Details                                                                                                                                                                                                                    |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Severity**           | Critical                                                                                                                                                                                                                   |
| **Reproduction Steps** | 1. Select a valid upcoming football match and outcome.<br>2. Enter a valid stake.<br>3. Click **Place Bet** repeatedly before the placement process completes.<br>4. Review the generated bet tickets and account balance. |
| **Expected Result**    | Only one bet is created, one ticket/receipt is generated, and the stake is deducted only once. The balance must not become negative.                                                                                       |
| **Actual Result**      | Multiple bet tickets are generated from repeated clicks and the stake is deducted multiple times, allowing the account balance to become negative.                                                                         |
| **Business Impact**    | A user can exploit repeated submissions to create unintended financial transactions and potentially obtain a negative account balance or revenue without having proper fouds.                                              |
| **Evidence**           | BUG-002 - Multiple Bets Created from Repeated Placed Bet Clicks resulted in a negative balance.                                                                                                                            |

### BUG-003 - Bets Can Be Placed on Past Matches

| Field                  | Details                                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Severity**           | Critical                                                                                                                                     |
| **Reproduction Steps** | 1. Identify a match with a kickoff date/time in the past.<br>2. Select an available outcome.<br>3. Enter a valid stake.<br>4. Place the bet. |
| **Expected Result**    | Past matches must not be eligible for betting and the bet must be blocked or rejected.                                                       |
| **Actual Result**      | The bet is successfully placed on a match whose kickoff date/time has already passed.                                                        |
| **Business Impact**    | Users can place bets on events that have already occurred, creating serious financial and business integrity risk.                           |
| **Evidence**           | BUG-003                                                                                                                                      |

### BUG-004 - Potential Payout Is Incorrect

| Field                  | Details                                                                                                                                                                                |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Severity**           | Critical                                                                                                                                                                               |
| **Reproduction Steps** | 1. Select a valid match and outcome.<br>2. Enter a valid stake.<br>3. Review the potential payout displayed in the Bet Slip.<br>4. Calculate the expected payout using `stake × odds`. |
| **Expected Result**    | The potential payout equals `stake × odds`.                                                                                                                                            |
| **Actual Result**      | The displayed potential payout does not match the expected calculation.                                                                                                                |
| **Business Impact**    | Users are shown incorrect financial information before placing a bet, which can lead to incorrect payout expectations and financial discrepancies.                                     |
| **Evidence**           | BUG-004                                                                                                                                                                                |

### BUG-005 - Match Teams Are Reversed in Receipt

| Field                  | Details                                                                                                                                                       |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Severity**           | Critical                                                                                                                                                      |
| **Reproduction Steps** | 1. Select a match from the match list.<br>2. Place a valid bet.<br>3. Review the match details displayed in the success receipt.                              |
| **Expected Result**    | The receipt displays the same home team vs away team order as shown before placement.                                                                         |
| **Actual Result**      | The home and away teams are displayed in reversed order in the receipt.                                                                                       |
| **Business Impact**    | The bet receipt contains incorrect match information, which can cause users to misunderstand which teams they bet on and undermines transaction transparency. |
| **Evidence**           | Screenshot not available due to negative balance.                                                                                                             |

### BUG-006 - Balance Not Updated After Successful Bet

| Field                  | Details                                                                                                                                                                    |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Severity**           | High                                                                                                                                                                       |
| **Reproduction Steps** | 1. Record the available balance.<br>2. Place a valid bet.<br>3. Review the balance after the bet is successfully placed.                                                   |
| **Expected Result**    | The available balance is reduced by exactly the stake amount.                                                                                                              |
| **Actual Result**      | The balance is not updated after the successful bet.                                                                                                                       |
| **Business Impact**    | The displayed account balance does not reflect the user's actual financial state, potentially allowing incorrect subsequent betting and causing financial inconsistencies. |
| **Evidence**           | Screenshot not available due to negative balance.                                                                                                                          |