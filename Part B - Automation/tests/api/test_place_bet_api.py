from decimal import Decimal, ROUND_HALF_UP

import allure
import pytest

from api.api_requests import APIRequests


@pytest.mark.parametrize(
    "stake, expected_status, expected_error, expected_message",
    [
        (0.99, 422, "invalid_stake_min", "Stake must be at least 1.00."),
        (1.00, 200, None, None),
        (1.01, 200, None, None),
        (100.00, 200, None, None),
        (100.01, 422, "invalid_stake_max", "Stake must be at most 100.00."),
    ]
)
@allure.title("Place Bet API - Stake boundary testing")
@allure.severity(allure.severity_level.CRITICAL)
def test_place_bet_boundary_values(
    stake,
    expected_status,
    expected_error,
    expected_message
):
    """Validate that the API correctly handles stake boundary values."""

    api = APIRequests()

    # Reset the test user's balance to ensure a predictable starting state
    api.reset_balance()
    user_balance = Decimal(str(api.get_balance()["balance"]))

    # Use API data to retrieve a valid upcoming match.
    match = api.get_upcoming_match()

    # Place a bet using the boundary value under test
    response = api.place_bet(
        match_id=match["id"],
        selection="AWAY",
        stake=stake
    )

    # Verify that the API returns the expected status for the boundary value
    assert response.status_code == expected_status, (
        f"Expected status {expected_status} "
        f"but got {response.status_code}"
    )

    # Verify the expected validation response for invalid boundary values
    if expected_status == 422:
        response_data = response.json()

        assert response_data["error"] == expected_error, \
            "Validation error code is incorrect"

        assert response_data["message"] == expected_message, \
            "Validation error message is incorrect"

        return

    response_data = response.json()

    # Calculate expected values using the odds returned by the match API
    expected_odds = Decimal(str(match["odds"]["away"]))
    expected_payout = (
        Decimal(str(stake)) * expected_odds
    ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    expected_balance = user_balance - Decimal(str(stake))

    # Verify that the API returns the expected odds.
    assert Decimal(str(response_data["odds"])) == expected_odds, \
        f"Expected odds {expected_odds} but got {response_data['odds']}"

    # Verify the calculated payout.
    assert Decimal(str(response_data["payout"])) == expected_payout, \
        f"Expected payout {expected_payout} but got {response_data['payout']}"

    # Verify that the stake was deducted from the balance.
    assert Decimal(str(response_data["balance"])) == expected_balance, \
        f"Expected balance {expected_balance} but got {response_data['balance']}"

    # Verify that the API returns the required currency.
    assert response_data["currency"] == "EUR", \
        f"Expected currency EUR but got {response_data['currency']}"