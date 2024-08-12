# ebay-scraper
README.md for eBay Scraper
This README provides all necessary details to run the eBay scraper written in Python. The scraper fetches listings from eBay based on a specified keyword and saves the data in a CSV file.
Project Title
eBay Scraper

Project Description
The eBay Scraper is a Python script that allows users to scrape product listings from eBay based on a search keyword. The script utilizes the requests library to make HTTP requests and BeautifulSoup to parse the HTML content of the eBay search results page. The scraped data is then saved into a CSV file for further analysis or use.

Requirements:
To run this project, you need:
Python 3.x installed on your machine
pip for installing Python packages

Installation
Follow these steps to set up the project:
Clone the repository (if applicable):
(in terminal or CMD)
    git clone https://github.com/Suleiman-sash/ebay-scraper.git
    cd <repository-directory>

Install required packages:
Use pip to install the necessary libraries:

 - pip install requests beautifulsoup4

How to Run the Project
Open your terminal or command prompt.
Navigate to the directory where the script is located.
Run the script with a keyword of your choice. For example, to scrape listings for "laptop":

python ebay_scraper.py

How to Use the Project
The script defines a function scrape_ebay(keyword) that takes a keyword as an argument. It performs the following actions:
Constructs the eBay search URL using the provided keyword.
Sends a GET request to the URL with a user-agent header to mimic a browser request.
Parses the HTML response to extract item titles, prices, shipping details, and item conditions.
Writes the extracted data to a CSV file named ebay_listings.csv.
Example Usage
To scrape listings for a specific keyword, simply call the function with the desired keyword:
python
scrape_ebay("laptop")

Output
The output will be saved in a CSV file named ebay_listings.csv in the same directory as the script. The CSV file will contain the following columns:
Title
Price
Shipping
Item Condition
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments
Requests Documentation
Beautiful Soup Documentation
CSV Module Documentation

