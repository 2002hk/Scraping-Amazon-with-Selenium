# This Repo contains Python script to extract amazon product details using selenium
## Libraries used
- Selenium
- Pandas
- OS
## Workflow Summary
### Google Search & Navigation to Amazon
- Searches for "Amazon Pendrive" in Google.
- Clicks on the first search result to land on Amazon.
### Pagination Handling
- terates over all pages by modifying the Amazon search URL dynamically.
### Extracting Product Details
- Visits each product page individually.
- Stores this information in a list of dictionaries.
### Saving Data to CSV
- Converts the data into a Pandas DataFrame.
- Creates an "output" folder if it doesn’t exist.
- Saves the file as products.csv.
