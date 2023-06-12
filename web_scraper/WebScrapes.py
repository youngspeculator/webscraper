import csv
from bs4 import BeautifulSoup
import requests

Product_Names = []
Product_Images = []
Product_Prices = []

# Start the index from 1
index = 1

for page_number in range(1, 25):
    url = f"https://www.f2parts.com/collection/sim-derzhateli?page={page_number}"
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')


    for name, price, image in zip(soup.findAll('a', class_='product-link'), soup.findAll('div', class_='price in-card'), soup.findAll('img', src_='')):
        Product_Name = name.get_text(strip=True)
        Product_Price = price.get_text(strip=True)
        Product_Image = image['src']

        if Product_Name not in Product_Names:
            Product_Names.append(Product_Name)
            Product_Prices.append(Product_Price)
            Product_Images.append(Product_Image)

            # Add the index to the product information
            Product_Names[-1] = f"{index}. {Product_Names[-1]}"
            index += 1

# Preparing the data for writing to CSV
data = list(zip(Product_Names, Product_Prices, Product_Images))

# Writing the data to a CSV file
filename = 'SIM_Holder.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product Name', 'Product Price', 'Product Image'])
    writer.writerows(data)

print(f"Data was scraped successfully and saved in {filename}")
