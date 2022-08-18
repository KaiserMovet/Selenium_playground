from selenium.webdriver.common.by import By


class StonesPaths:
    STONE_FIELD = (
        By.XPATH,
        "/html/body/div[1]/section/div/div/div/div[2]/div/input[1]",
    )
    STONE_CLICK = (
        By.XPATH,
        "/html/body/div[1]/section/div/div/div/div[2]/div/button[1]",
    )
    STONE_ANSWER = (
        By.XPATH,
        '//*[@id="passwordBanner"]/h4',
    )

    SECRET_FIELD = (
        By.XPATH,
        '//*[@id="r2Input"]',
    )
    SECRET_CLICK = (
        By.XPATH,
        "/html/body/div[1]/section/div/div/div/div[2]/div/button[2]",
    )
    SECRET_ANSWER = (
        By.XPATH,
        "/html/body/div[1]/section/div/div/div/div[2]/div/div[2]/h4",
    )

    MERCHANT_FIELD = (
        By.XPATH,
        "/html/body/div[1]/section/div/div/div/div[2]/div/input[3]",
    )
    MERCHANT_CLICK = (
        By.XPATH,
        "/html/body/div[1]/section/div/div/div/div[2]/div/button[3]",
    )
    MERCHANT_ANSWER = (
        By.XPATH,
        "/html/body/div[1]/section/div/div/div/div[2]/div/div[5]/h4",
    )


class StoneField:
    def __init__(self, driver, field_path, click_path, result_path):
        self.field_path = field_path
        self.click_path = click_path
        self.result_path = result_path
        self.driver = driver

    @property
    def field(self):
        return self.driver.find_element(*self.field_path)

    @property
    def button(self):
        return self.driver.find_element(*self.click_path)

    @property
    def answer(self):
        return self.driver.find_element(*self.result_path)

    def fill(self, msg: str):
        self.field.send_keys(msg)

    def click(self):
        self.button.click()

    def get_result(self):
        return self.answer.get_attribute("innerHTML")


class Stones:

    URL = "https://techstepacademy.com/trial-of-the-stones"

    def __init__(self, driver):
        self.driver = driver
        driver.get(self.URL)

    @property
    def stone(self):
        return StoneField(
            self.driver,
            StonesPaths.STONE_FIELD,
            StonesPaths.STONE_CLICK,
            StonesPaths.STONE_ANSWER,
        )

    @property
    def secret(self):
        return StoneField(
            self.driver,
            StonesPaths.SECRET_FIELD,
            StonesPaths.SECRET_CLICK,
            StonesPaths.SECRET_ANSWER,
        )

    @property
    def merchant(self):
        return StoneField(
            self.driver,
            StonesPaths.MERCHANT_FIELD,
            StonesPaths.MERCHANT_CLICK,
            StonesPaths.MERCHANT_ANSWER,
        )

    pass
