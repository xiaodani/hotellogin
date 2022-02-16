from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import unittest

class HotelLoginTest(unittest.TestCase):

    #settings
    def setUp(self) -> None:
        self.driver = webdriver.Chrome (service=Service(ChromeDriverManager().install()))
        self.url = "https://hotel.testplanisphere.dev/ja/login.html"

        # snippet contained in image blob
        self.warningimagesnip = "stroke-linejoin='round'"
        self.tickimagesnip = "viewBox='0 0 8 8'"
        
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.quit()
        return super().tearDown()
    
    # Test case 1 - Control case プレミアム会員
    # User - ichiro@example.com
    # Pass - password
    def test_control_case_premium_member(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        self.assertEqual("ログイン | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

        elem = driver.find_element(By.ID, "email")
        elem.clear()
        elem.send_keys('ichiro@example.com')

        elem = driver.find_element(By.ID, "password")
        elem.clear()
        elem.send_keys('password')

        elem = driver.find_element(By.ID, "login-button")
        elem.click()
        
        # wait until next page loads and assert page
        WebDriverWait(driver, 2).until_not(EC.title_contains("ログイン"))
        self.assertEqual("マイページ | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

    # Test case 2 - Control case プレミアム会員
    # User - jun@example.com
    # Pass - pa55w0rd!
    def test_control_case_premium_member_extended(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        self.assertEqual("ログイン | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

        elem = driver.find_element(By.ID, "email")
        elem.clear()
        elem.send_keys('jun@example.com')

        elem = driver.find_element(By.ID, "password")
        elem.clear()
        elem.send_keys('pa55w0rd!')

        elem = driver.find_element(By.ID, "login-button")
        elem.click()
        
        # wait until next page loads and assert page
        WebDriverWait(driver, 2).until_not(EC.title_contains("ログイン"))
        self.assertEqual("マイページ | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

        # assert user details
        elem = driver.find_element(By.ID, "email")
        self.assertEqual("jun@example.com", elem.text)
        elem = driver.find_element(By.ID, "username")
        self.assertEqual("林潤", elem.text)
        elem = driver.find_element(By.ID, "rank")
        self.assertEqual("プレミアム会員", elem.text)
        elem = driver.find_element(By.ID, "address")
        self.assertEqual("大阪府大阪市北区梅田", elem.text)
        elem = driver.find_element(By.ID, "tel")
        self.assertEqual("01212341234", elem.text)
        elem = driver.find_element(By.ID, "gender")
        self.assertEqual("その他", elem.text)
        elem = driver.find_element(By.ID, "birthday")
        self.assertEqual("1988年12月17日", elem.text)
        elem = driver.find_element(By.ID, "notification")
        self.assertEqual("受け取らない", elem.text)

    # Test case 3 - Control case 一般会員
    # User - sakura@example.com
    # Pass - pass1234
    def test_control_case_general_member(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        self.assertEqual("ログイン | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

        elem = driver.find_element(By.ID, "email")
        elem.clear()
        elem.send_keys('sakura@example.com')

        elem = driver.find_element(By.ID, "password")
        elem.clear()
        elem.send_keys('pass1234')

        elem = driver.find_element(By.ID, "login-button")
        elem.click()
        
        # wait until next page loads and assert page
        WebDriverWait(driver, 2).until_not(EC.title_contains("ログイン"))
        self.assertEqual("マイページ | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

    # Test case 4 - Control case 一般会員
    # User - yoshiki@example.com
    # Pass - pass-pass
    def test_control_case_general_member_extended(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        self.assertEqual("ログイン | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

        elem = driver.find_element(By.ID, "email")
        elem.clear()
        elem.send_keys('yoshiki@example.com')

        elem = driver.find_element(By.ID, "password")
        elem.clear()
        elem.send_keys('pass-pass')

        elem = driver.find_element(By.ID, "login-button")
        elem.click()
        
        # wait until next page loads and assert page
        WebDriverWait(driver, 2).until_not(EC.title_contains("ログイン"))
        self.assertEqual("マイページ | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

        # assert user details
        elem = driver.find_element(By.ID, "email")
        self.assertEqual("yoshiki@example.com", elem.text)
        elem = driver.find_element(By.ID, "username")
        self.assertEqual("木村良樹", elem.text)
        elem = driver.find_element(By.ID, "rank")
        self.assertEqual("一般会員", elem.text)
        elem = driver.find_element(By.ID, "address")
        self.assertEqual("未登録", elem.text)
        elem = driver.find_element(By.ID, "tel")
        self.assertEqual("01298765432", elem.text)
        elem = driver.find_element(By.ID, "gender")
        self.assertEqual("未登録", elem.text)
        elem = driver.find_element(By.ID, "birthday")
        self.assertEqual("1992年8月31日", elem.text)
        elem = driver.find_element(By.ID, "notification")
        self.assertEqual("受け取る", elem.text)

    # Test case 5 - Empty input field; no user no pass
    # User - 
    # Pass -
    def test_type_no_user_no_pass(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        # assert warning messages dont show before clicking
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        email = driver.find_element(By.ID, "email")
        ipass = driver.find_element(By.ID, "password")

        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert warning images appear
        self.assertIn(self.warningimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.warningimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning messages appear 
        self.assertEqual("block",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("このフィールドを入力してください。",
        driver.find_element(By.ID, "email-message").text)
        self.assertEqual("block",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))
        self.assertEqual("このフィールドを入力してください。",
        driver.find_element(By.ID, "password-message").text)

    # Test case 6 - No user but with pass
    # User - 
    # Pass - abc
    def test_type_no_user_with_pass(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        ipass = driver.find_element(By.ID, "password")
        ipass.clear()
        ipass.send_keys('abc')

        # assert warning messages dont show before clicking
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        email = driver.find_element(By.ID, "email")

        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert tick image in pass and warning in user
        self.assertIn(self.warningimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.tickimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning messages appear 
        self.assertEqual("block",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("このフィールドを入力してください。",
        driver.find_element(By.ID, "email-message").text)
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

    # Test case 7 - No password
    # User - ichiro@example.com
    # Pass -
    def test_type_correct_user_no_pass(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)
        
        # enter valid email but no password
        email = driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys('ichiro@example.com')

        # assert warning messages dont show before clicking
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        ipass = driver.find_element(By.ID, "password")

        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert tick image in user and warning in pass
        self.assertIn(self.tickimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.warningimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning for only password message appearing 
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("block",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))
        self.assertEqual("このフィールドを入力してください。",
        driver.find_element(By.ID, "password-message").text)

    # Test case 8 - Wrong password
    # User - ichiro@example.com
    # Pass - passworD
    def test_type_correct_user_wrong_pass(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        # enter valid email but wrong password
        email = driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys('ichiro@example.com')
        ipass = driver.find_element(By.ID, "password")
        ipass.clear()
        ipass.send_keys('passworD')

        # assert warning messages dont show before clicking
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert warning images appear
        self.assertIn(self.warningimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.warningimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning messages appear 
        self.assertEqual("block",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "email-message").text)
        self.assertEqual("block",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "password-message").text)

    # Test case 9 - Wrong password to wrong password
    # User - ichiro@example.com
    # Pass - passworD => passworE
    def test_type_correct_user_wrong_pass_to_wrong_pass(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        # enter valid email but wrong password
        email = driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys('ichiro@example.com')
        ipass = driver.find_element(By.ID, "password")
        ipass.clear()
        ipass.send_keys('passworD')

        # assert warning messages dont show before clicking
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert warning images appear
        self.assertIn(self.warningimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.warningimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning messages appear 
        self.assertEqual("block",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "email-message").text)
        self.assertEqual("block",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "password-message").text)

        # type wrong password again
        ipass.send_keys(Keys.BACKSPACE)
        ipass.send_keys('E')

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert warning images remains
        self.assertIn(self.warningimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.warningimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning messages remains 
        self.assertEqual("block",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "email-message").text)
        self.assertEqual("block",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "password-message").text)

    # Test case 10 - Wrong password to right password
    # User - ichiro@example.com
    # Pass - passworD => password
    def test_type_correct_user_wrong_pass_to_correct_pass(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)

        # enter valid email but wrong password
        email = driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys('ichiro@example.com')
        ipass = driver.find_element(By.ID, "password")
        ipass.clear()
        ipass.send_keys('passworD')

        # assert warning messages dont show before clicking
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert warning images appear
        self.assertIn(self.warningimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.warningimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning messages appear 
        self.assertEqual("block",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "email-message").text)
        self.assertEqual("block",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "password-message").text)

        # type wrong password again
        ipass.send_keys(Keys.BACKSPACE)
        ipass.send_keys('d')

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        # wait until next page loads and assert page
        WebDriverWait(driver, 2).until_not(EC.title_contains("ログイン"))
        self.assertEqual("マイページ | HOTEL PLANISPHERE - テスト自動化練習サイト", driver.title)

    # Test case 11 - Invalid user no pass
    # User - abc@example.com
    # Pass -
    def test_type_invalid_user_no_pass(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)
        
        # enter valid email but no password
        email = driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys('abc@example.com')

        # assert warning messages dont show before clicking
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        ipass = driver.find_element(By.ID, "password")

        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert tick image in user and warning in pass
        self.assertIn(self.tickimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.warningimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning for only password message appearing 
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("block",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))
        self.assertEqual("このフィールドを入力してください。",
        driver.find_element(By.ID, "password-message").text)

    # Test case 12 - Invalid user with pass
    # User - abc@example.com
    # Pass - abc
    def test_type_invalid_user_with_pass(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)
        
        # enter valid email but no password
        email = driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys('abc@example.com')
        ipass = driver.find_element(By.ID, "password")
        ipass.clear()
        ipass.send_keys('abc')

        # assert warning messages dont show before clicking
        self.assertEqual("none",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("none",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################

        # assert form was validated
        self.assertEqual("was-validated", 
        driver.find_element(By.ID, "login-form").get_attribute("class"))

        # assert warning images appear
        self.assertIn(self.warningimagesnip, 
        email.value_of_css_property("background-image"))
        self.assertIn(self.warningimagesnip, 
        ipass.value_of_css_property("background-image"))

        # assert warning appears
        self.assertEqual("block",
        driver.find_element(By.ID, "email-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "email-message").text)
        self.assertEqual("block",
        driver.find_element(By.ID, "password-message").value_of_css_property("display"))
        self.assertEqual("メールアドレスまたはパスワードが違います。",
        driver.find_element(By.ID, "password-message").text)

    # Test case 13 - Simple SQL injection
    # User - ' or 1=1 --
    # Pass -
    def test_SQL_injection_user(self):
        driver = self.driver
        url = self.url
        
        driver.get(url)
        
        # enter valid email but no password
        email = driver.find_element(By.ID, "email")
        email.clear()
        email.send_keys("' or 1=1 --'")

        # click login button
        elem = driver.find_element(By.ID, "login-button")
        elem.click()

        ###############################
        # assert changes
        ###############################
        # page should still be the same
        self.assertIn("ログイン", driver.title)


if __name__ == "__main__":
    unittest.main()
