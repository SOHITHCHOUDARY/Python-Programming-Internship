import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print("Failed to retrieve website data.")
        return None

def extract_data(soup):
    # Find and extract the data you're interested in from the HTML content
    # For example, let's extract the titles and links of all the articles on the page
    articles = soup.find_all('article')
    data = []
    for article in articles:
        title = article.find('h2').get_text()
        link = article.find('a')['href']
        data.append({'Title': title, 'Link': link})
    return data

def save_to_csv(data, filename):
    # Save the extracted data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"Data saved to {filename} successfully.")

def main():
    url = input("Enter the URL of the website you want to scrape: ")
    filename = input("Enter the filename to save the data (e.g., data.csv): ")

    # Scrape the website
    soup = scrape_website(url)
    if soup:
        # Extract data from the scraped HTML content
        data = extract_data(soup)
        
        # Save the extracted data to a CSV file
        save_to_csv(data, filename)

if __name__ == "__main__":
    main()
