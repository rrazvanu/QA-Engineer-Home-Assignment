import requests
from datetime import date

from config import API_BASE_URL, USER_ID


class APIRequests:

    # request for retrieving matches
    def get_matches(self):
        response = requests.get(
            f"{API_BASE_URL}/matches",
            headers={"x-user-id": USER_ID}
        )
        response.raise_for_status()
        return response.json()

    # request for retrieving one upcoming match
    def get_upcoming_match(self):
        matches = self.get_matches()
        today = date.today()

        upcoming_matches = [
            match
            for match in matches
            if date.fromisoformat(match["kickoffDate"]) >= today
        ]

        if not upcoming_matches:
            raise AssertionError("No upcoming matches found")

        return min(
            upcoming_matches,
            key=lambda match: date.fromisoformat(match["kickoffDate"])
        )

    # reset user balance request
    def reset_balance(self):
        response = requests.post(
            f"{API_BASE_URL}/reset-balance",
            headers={"x-user-id": USER_ID}
        )
        response.raise_for_status()
        return response.json()

    # get user balance request
    def get_balance(self):
        response = requests.get(
            f"{API_BASE_URL}/balance",
            headers={"x-user-id": USER_ID}
        )
        response.raise_for_status()
        return response.json()

    # place bet request
    def place_bet(self, match_id, selection, stake):
        response = requests.post(
            f"{API_BASE_URL}/place-bet",
            headers={"x-user-id": USER_ID},
            json={
                "matchId": match_id,
                "selection": selection,
                "stake": stake
            }
        )
        return response
