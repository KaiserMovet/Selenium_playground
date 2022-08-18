import time
from sites.stones import Stones


def test_stones(stones: Stones):
    stone = stones.stone
    stone.fill("rock")
    stone.click()
    assert "bamboo" == stone.get_result()


def test_secret(stones: Stones):
    secret = stones.secret
    secret.fill("bamboo")
    secret.click()
    assert "Success!" == secret.get_result()


def test_merchant(stones: Stones):
    merchant = stones.merchant
    merchant.fill("Jessica")
    merchant.click()
    assert "Success!" == merchant.get_result()
