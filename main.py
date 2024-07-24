from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
base_url = 'https://dexscreener.com/solana/cu6jlmqyqv1hyrqnspgylqtbbrviuflybvlpcmpkkzyu'

try:
    # Open the website
    driver.get("https://io.dexscreener.com/dex/log/amm/v3/solamm/top/solana/CU6JLMqYQv1hyrQNspGyLQtbbrViuFLybVLPcMpKKzyu?q=So11111111111111111111111111111111111111112")
    
    # Wait for the page to load and element to be present
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    
    # Get page source and handle it as UTF-8 directly
    page_source = driver.page_source

    # Initialize the list of URLs
    urls = []
    index = 0
    while index < len(page_source):
        next_indices = [(page_source.find('yBX', index), 44), 
                        (page_source.find('yBV', index), 43),
                        (page_source.find('<pre>', index), 49)]
        
        # Remove not found indices
        valid_indices = [(idx, num) for idx, num in next_indices if idx != -1]
        
        # No valid prefix found
        if not valid_indices:
            break

        # Find the minimum index (earliest occurrence)
        current_index, num_letters = min(valid_indices, key=lambda x: x[0])

        # Ensure there's enough characters left in the string for a valid address
        if current_index + num_letters <= len(page_source):
            address = page_source[current_index + 3: current_index + 3 + num_letters]
            if 'e>�\x01X' in address:
                address = address.replace('e>�\x01X', '')
            urls.append(f"https://solscan.io/account/{address}")
        
        # Move past this entry to continue search
        index = current_index + 3 + num_letters

    # Write URLs to a CSV file with explicit UTF-8 encoding
    with open('wallet_addresses.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Wallet URL'])  # Write header
        for url in urls:
            writer.writerow([url])  # Write each URL on a new row

    print("Wallet URLs have been saved to 'wallet_addresses.csv'.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
