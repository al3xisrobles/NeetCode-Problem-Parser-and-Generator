import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('neetcode.html', 'r') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all the accordion-container divs
accordion_containers = soup.find_all('div', class_='accordion-container')

# Initialize lists to store the data
data = []

# Loop through each accordion-container
for container in accordion_containers:
    # Find the category title
    category_title = container.find('button').find('p').text.strip()

    # Find all rows within the container
    rows = container.find_all('tr', class_='ng-star-inserted')

    # Loop through each row and extract data
    for row in rows:
        # Check if the row has the "completed" class
        status = True if 'completed' in row.get('class', []) else False

        problem_element = row.find('a', class_='table-text')
        problem = problem_element.text.strip()
        problem_link = problem_element.get('href')

        difficulty = row.find('button', id='diff-btn').b.text.strip()

        # Append the data to the list
        data.append({
            'Category': category_title,
            'Completed': status,
            'Problem': problem,
            'Link': problem_link,
            'Difficulty': difficulty,
            'CompletedWithThisScript': status
        })

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV or display the DataFrame
df.to_csv('parsed_neetcode.csv', index=False)
print(df.head())
