# AI Web Scraper
This project is a powerful AI Web Scraper built with Ollama, Bright Data, Selenium, and other Python libraries. It allows users to scrape websites, clean and parse content dynamically based on user input, and interact with the extracted data in a user-friendly interface.

# Features
- - Website Scraping: Efficiently scrapes websites using Selenium and Bright Data for dynamic content and anti-bot protection.
- - DOM Content Extraction: Extracts raw body content and cleans it for better usability.
- - Dynamic Content Parsing: Users can enter descriptions, and the AI uses Ollama to parse the content based on those descriptions.
- - User Interface: Built using Streamlit, providing a simple and intuitive interface to interact with the scraper and view results.
- - Expandable DOM Viewer: Displays the raw and cleaned DOM content in an expandable text box for easy review.

#  Technologies Used
- Ollama: For AI-powered content parsing.
- Bright Data: For efficient data extraction, especially for websites with anti-scraping measures.
- Selenium: For scraping dynamic content that requires interaction with JavaScript.
- Streamlit: For creating the interactive web interface.
- Python Libraries: Other libraries like requests, BeautifulSoup, and pandas for content cleaning, processing, and analysis.
# Installation
Clone the repository:

   
    `git clone https://github.com/your-username/ai-webscraper.git`
   

`
pip install -r requirements.txt`

## Run the Streamlit app:


`streamlit run app.py`
# Usage
- Enter the website URL you want to scrape in the input field.
- Click on Scrape Website to extract the content.
- Once the content is scraped, you can view the raw and cleaned DOM content in an expandable section.
- Provide a description for the data you're looking for in the Enter Description box.
- Click Parse Content to let the AI parse the content based on your input.
- View the parsed result in the output section.
# Contributing
If you want to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. Contributions, issues, and feature requests are welcome.
