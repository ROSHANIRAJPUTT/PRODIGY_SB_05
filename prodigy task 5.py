import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_product_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    # Modify these selectors according to the website's HTML structure
    product_elements = soup.select('.product')  # Example class selector for products
    
    for product in product_elements:
        name = product.select_one('.product-name').get_text(strip=True)  # Example class selector for product name
        price = product.select_one('.product-price').get_text(strip=True)  # Example class selector for product price
        rating = product.select_one('.product-rating').get_text(strip=True)  # Example class selector for product rating
        
        products.append({
            'name': name,
            'price': price,
            'rating': rating
        })

    return products

def save_to_csv(products, filename='products.csv'):
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    url = 'https://www.example.com/category/products'  # Replace with the actual URL
    products = scrape_product_info(url)
    
    if products:
        save_to_csv(products)
    else:
        print("No products found.")

if __name__ == '__main__':
    main()