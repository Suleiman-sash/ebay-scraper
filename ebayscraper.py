from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# Function to scrape eBay using Selenium
def scrape_ebay(keyword):
    url = f"https://www.ebay.co.uk/sch/i.html?_nkw={keyword}"
    
    # Set up Selenium WebDriver (you might need to specify the path to your webdriver)
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Wait for page to load
    driver.implicitly_wait(5)
    
    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Find all listings
    items = soup.find_all('li', class_='s-item')
    
    # Prepare CSV file
    with open('ebay_listings.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Shipping', 'Item Condition'])
        
        for item in items:
            try:
                title = item.find('h3', class_='s-item__title').text.strip() if item.find('h3', class_='s-item__title') else 'No title available'
                price = item.find('span', class_='s-item__price').text.strip() if item.find('span', class_='s-item__price') else 'No price available'
                shipping = item.find('span', class_='s-item__shipping').text.strip() if item.find('span', class_='s-item__shipping') else 'No shipping info'
                condition = item.find('span', class_='SECONDARY_INFO').text.strip() if item.find('span', class_='SECONDARY_INFO') else 'No condition info'

                print(f"Title: {title}, Price: {price}, Shipping: {shipping}, Condition: {condition}")

                writer.writerow([title, price, shipping, condition])
            except Exception as e:
                print(f"Error scraping item: {e}")
    
    # Close the WebDriver
    driver.quit()

# Run the scraper with a test keyword

# Run the scraper with a test keyword
print(scrape_ebay("samsung"))
