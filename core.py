from playwright.sync_api import sync_playwright
import time
import os , random
from ai_response import get_response as get_ai_response
from config import prompts
from playwright.sync_api import sync_playwright
import time
import os, random
import logging
from ai_response import get_response as get_ai_response
from config import prompts

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("messageboy.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("MessageBoy")

class MessageBoy:
    def __init__(self, username, password, mode='General', headless=False):
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None
        self.username = username
        self.password = password
        self.prev_msg = None
        self.temporary_msg = None
        self.target_page = None
        self.prompt = prompts[mode]
        logger.info(f"Initialized MessageBoy with mode: {mode}")

    def launch_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(
            viewport={'width': 1280, 'height': 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        self.page = self.context.new_page()
        logger.info("Browser launched successfully")

    def login(self):
        logger.info(f"Attempting to login as {self.username}")
        self.page.goto('https://www.instagram.com/')
        self.page.fill('input[name="username"]', self.username)
        self.page.fill('input[name="password"]', self.password)
        self.page.click('button[type="submit"]')
        time.sleep(5)
        logger.info("Login completed")

    def go_message_page(self):
        logger.info(f"Navigating to conversation: {self.target_page}")
        self.page.goto(self.target_page)
        time.sleep(5)
        logger.info("Message page loaded")

    def not_now_window(self):
        if self.page.is_visible("text=Not Now"):
            self.page.click("text=Not Now")
            time.sleep(2)
            logger.info("Dismissed 'Not Now' popup")

    def get_messages(self):
        return self.page.locator('//div[@aria-label="Double tap to like"]').all_text_contents()
    
    def set_prev_msg(self):
        self.prev_msg = self.get_messages()
        logger.debug(f"Previous messages set: {len(self.prev_msg)} messages")

    def is_new_message(self):
        current_msgs = self.get_messages()
        output = current_msgs != self.prev_msg
        
        if output:
            logger.info(f"New message detected")
            self.prev_msg = current_msgs
        
        return output

    def take_screenshot(self):
        filename = f"screenshot.png"
        self.page.screenshot(path=filename)
        logger.info(f"Screenshot saved: {filename}")
        return filename

    def get_response(self, screenshot_path):
        logger.info("Generating AI response")
        response = get_ai_response(self.prompt, screenshot_path)
        logger.info(f"AI response generated ({len(response)} chars)")
        return response

    def type_msg(self, message):
        logger.info("Typing message")
        self.page.locator('//div[@aria-placeholder="Message..."]').click()
        self.page.keyboard.type(message, delay=20)
        self.page.keyboard.press('Enter')
        time.sleep(3)
        logger.info("Message sent")

    def run(self):
        logger.info("Starting MessageBoy session")
        self.launch_browser()
        self.login()
        self.go_message_page()
        self.not_now_window()
        self.set_prev_msg()
        
        logger.info("MessageBoy is now running and monitoring for new messages")
        try:
            while True:
                if self.is_new_message():
                    time.sleep(15)
                    screenshot_path = self.take_screenshot()
                    received = self.get_messages()[-1]
                    logger.info(f"Received message: {received[:50]}{'...' if len(received) > 50 else ''}")
                    
                    response = self.get_response(screenshot_path)
                    logger.info(f"Responding with: {response[:50]}{'...' if len(response) > 50 else ''}")
                    
                    self.type_msg(response)
                    self.prev_msg = self.get_messages()
                time.sleep(5)
        except KeyboardInterrupt:
            logger.info("MessageBoy session terminated by user")
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}", exc_info=True)
        finally:
            if self.browser:
                self.browser.close()
                logger.info("Browser closed")
            if self.playwright:
                self.playwright.stop()
                logger.info("Playwright stopped")


         