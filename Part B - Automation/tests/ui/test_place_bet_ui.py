from datetime import datetime
import allure
from api.api_requests import APIRequests
from pages.sporting_betting_page import SportingBettingPage


@allure.title("Successful single bet placement")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_single_bet(driver):
    """Validate the complete single bet placement flow and resulting account state."""

    api = APIRequests()
    page = SportingBettingPage(driver)

    # Reset the test user's balance to ensure a predictable starting state.
    api.reset_balance()

    # Use API data to dynamically select a valid upcoming match.
    match = api.get_upcoming_match()
    initial_balance = api.get_balance()["balance"]

    # Perform the betting flow through the UI.
    page.open()
    page.select_outcome(match["id"], "home")

    stake = 10
    page.enter_stake(stake)

    # Build expected values from the same match data used by the application.
    expected_odds = match["odds"]["home"]
    expected_payout = stake * expected_odds
    expected_match = f'{match["homeTeam"]} vs {match["awayTeam"]}'
    expected_balance = initial_balance - stake

    # Capture the time immediately before placing the bet.
    placement_time = datetime.now()

    page.click_place_bet()

    # Verify that the successful bet receipt is displayed.
    assert page.get_receipt_title() == "Bet Placed Successfully!"

    # Validate that the receipt timestamp was generated around placement time.
    receipt_time = datetime.strptime(
        page.get_receipt_timestamp(),
        "Today, %I:%M %p"
    ).replace(
        year=placement_time.year,
        month=placement_time.month,
        day=placement_time.day
    )

    assert abs((receipt_time - placement_time).total_seconds()) <= 60

    # Validate all important values displayed on the receipt.
    assert page.get_receipt_bet_id()
    assert page.get_receipt_match() == expected_match
    assert page.get_receipt_stake() == f"€{stake:.2f}"
    assert page.get_receipt_odds() == str(expected_odds)
    assert page.get_receipt_payout() == f"€{expected_payout:.2f}"

    # Verify that the stake was deducted from the user's balance.
    actual_balance = api.get_balance()["balance"]
    assert actual_balance == expected_balance
