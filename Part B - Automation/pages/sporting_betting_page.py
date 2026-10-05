from config import UI_BASE_URL
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SportingBettingPage(BasePage):

    # Selectors
    DATE_FILTER_TOGGLE = (By.ID, "date-filter-toggle")
    PLACE_BET_BUTTON = (By.ID, "bet-slip-place-bet")
    STAKE_INPUT = (By.ID, "bet-slip-stake-input")
    HEADER_BALANCE = (By.ID, "header-balance")

    # Receipt
    RECEIPT_TITLE = (By.CSS_SELECTOR, "h2.modalTitle")
    RECEIPT_BET_ID = (By.ID, "modal-success-bet-id")
    RECEIPT_MATCH = (By.ID, "modal-success-match")
    RECEIPT_STAKE = (By.ID, "modal-success-stake")
    RECEIPT_ODDS = (By.ID, "modal-success-odds")
    RECEIPT_PAYOUT = (By.ID, "modal-success-payout")
    RECEIPT_TIMESTAMP = (By.ID, "modal-success-placed-at")


    # Methods
    def open(self):
        self.driver.get(UI_BASE_URL)

    def enter_stake(self, stake):
        element = self.wait_for_clickable(*self.STAKE_INPUT)
        element.clear()
        element.send_keys(stake)

    def click_place_bet(self):
        element = self.wait_for_clickable(*self.PLACE_BET_BUTTON)
        element.click()

    def select_outcome(self, match_id, outcome):
        # POSSIBLE OUTCOMES: home/draw/away
        locator = (By.ID, f"odds-{match_id}-{outcome}")
        element = self.wait_for_clickable(*locator)
        element.click()

    def get_receipt_title(self):
        return self.wait_for_elem(*self.RECEIPT_TITLE).text

    def get_receipt_match(self):
        return self.wait_for_elem(*self.RECEIPT_MATCH).text

    def get_receipt_stake(self):
        return self.wait_for_elem(*self.RECEIPT_STAKE).text

    def get_receipt_odds(self):
        return self.wait_for_elem(*self.RECEIPT_ODDS).text

    def get_receipt_payout(self):
        return self.wait_for_elem(*self.RECEIPT_PAYOUT).text

    def get_receipt_timestamp(self):
        return self.wait_for_elem(*self.RECEIPT_TIMESTAMP).text

    def get_balance(self):
        return self.wait_for_elem(*self.HEADER_BALANCE).text

    def get_receipt_bet_id(self):
        return self.wait_for_elem(*self.RECEIPT_BET_ID).text