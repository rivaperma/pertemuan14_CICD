import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):
    def setUp(self):
        browser_name = sys.argv[2] if len(sys.argv) > 2 else "firefox"
        
        # Inisialisasi options berdasarkan browser
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
        else:
            options = webdriver.FirefoxOptions()
            
        for i in range(3): 
            try:
                self.browser = webdriver.Remote(command_executor=server, options=options)
                break
            except Exception as e:
                if i == 2: raise e
                import time
                time.sleep(5) # Tunggu 5 detik jika gagal
        
        self.addCleanup(self.browser.quit)

    # Indentasi diperbaiki: sejajar dengan setUp
    def test_homepage(self):
        url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost"
        self.browser.get(url)
        self.browser.save_screenshot('screenshot.png')
        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertIn(expected_result, actual_result.text)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')