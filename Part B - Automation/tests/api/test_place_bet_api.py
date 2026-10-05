import allure

from api.api_requests import APIRequests


@allure.title("Place Bet API - Reject invalid selection")
@allure.severity(allure.severity_level.CRITICAL)
def test_place_bet_rejects_invalid_selection():
    """Validate that the API rejects unsupported betting selections."""

    api = APIRequests()

    # Reset the test user's balance to ensure a predictable starting state.
    api.reset_balance()

    # Use API data to retrieve a valid upcoming match.
    match = api.get_upcoming_match()

    # Send an unsupported selection to verify that the API rejects the request.
    response = api.place_bet(
        match_id=match["id"],
        selection="INVALID",
        stake=10
    )

    # Verify that the API returns the expected validation error.
    assert response.status_code == 422