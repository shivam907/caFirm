import os
import requests
from bs4 import BeautifulSoup

# Step 1: Get the main page content
main_url = "https://arksandassociates.com/laws/2065/Companies_Act,_1956.aspx"
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Find all <a> tags in the table
table = soup.find('tbody')
rows = table.find_all('tr')

# Step 3: Loop through each row and fetch the link, download the page, and save it in a folder
for idx, row in enumerate(rows, start=1):
    a_tag = row.find('a')
    if a_tag and 'href' in a_tag.attrs:
        page_url = a_tag['href']
        if not page_url.startswith('http'):
            page_url = f"https://arksandassociates.com{page_url}"
        
        # Fetch the content of the linked page
        page_response = requests.get(page_url)
        page_content = page_response.content
        
        # Create a folder for each page
        folder_name = f"{idx}"
        os.makedirs(folder_name, exist_ok=True)
        
        # Save the content as index.html inside the folder
        with open(os.path.join(folder_name, "index.html"), "wb") as file:
            file.write(page_content)
        
        print(f"Downloaded and saved: {folder_name}/index.html")

print("All pages downloaded.")
