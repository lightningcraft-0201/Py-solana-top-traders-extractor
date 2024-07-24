# DexScreener Solana Top Traders Extractor

## Overview
This project is designed to extract top trader information from the DexScreener platform for the Solana blockchain. It utilizes Selenium for web scraping to gather wallet addresses and corresponding Solscan URLs of the top traders.

## Video Preview
[![Video Preview](https://github.com/zima-0201/Project-Images/blob/main/video%20preview/Py-solana-top-traders-extractor.jpeg)](https://autobuffy-ebay.s3.eu-north-1.amazonaws.com/Detroit+Axle/Py-solana-top-traders-extractor.mp4)


## Features
- **Headless Browser Automation:** Uses Selenium with headless Chrome to scrape data without opening a visible browser window.
- **Dynamic Content Handling:** Waits for the page to load fully before scraping to ensure all dynamic content is captured.
- **Robust Data Extraction:** Parses the page source to locate and extract wallet addresses accurately.
- **CSV Output:** Saves the extracted wallet addresses and Solscan URLs to a CSV file for further analysis or use.

## Requirements
- Python 3.6+
- Google Chrome browser
- ChromeDriver

## Dependencies
- `selenium`
- `webdriver-manager`

These can be installed using pip.

## Setup and Installation

1. **Clone the Repository:**
   Clone the repository from GitHub and navigate to the project directory.

2. **Install Dependencies:**
   Install the required dependencies listed in the `requirements.txt` file using pip.

3. **Run the Script:**
   Execute the Python script to start the scraping process.

## Script Workflow

1. **Configure Selenium WebDriver:**
   The script sets up the Chrome WebDriver with headless options to run the browser in the background and specifies the user-agent string.

2. **Open the DexScreener URL:**
   The script navigates to the specified DexScreener URL using Selenium's `get` method.

3. **Wait for Page Load:**
   The script uses WebDriverWait to ensure the page is fully loaded before proceeding.

4. **Extract Wallet Addresses:**
   The script parses the page source to find wallet addresses using specific substrings and extracts the required data.

5. **Save Data to CSV:**
   The extracted wallet URLs are written to a CSV file with proper UTF-8 encoding.

6. **Exception Handling:**
   The script handles exceptions that may occur during the scraping process and ensures the driver is quit to free resources.

## Output
The script generates a CSV file named `wallet_addresses.csv` containing the extracted wallet URLs in a structured format.

## Troubleshooting
- **ChromeDriver Version Issues:**
  Ensure that the version of ChromeDriver matches your installed Chrome browser version. `webdriver-manager` should handle this automatically, but check compatibility if issues arise.
- **Page Load Timeout:**
  If the page takes too long to load, consider increasing the WebDriverWait timeout value.

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements
- Selenium documentation and community for providing comprehensive guides and examples.
- DexScreener for providing valuable data.
