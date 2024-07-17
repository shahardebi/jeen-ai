# Web Crawler Script

This README provides instructions on how to set up and run the Web Crawler script. The script is designed to crawl a website, starting from a given URL, to extract titles, URLs, and body content of visited pages.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

1. **Clone the Repository**

   First, clone the repository to your local machine using Git.

2. **Create venv for the script and activate it**

Before installing the dependencies, you need to activate the virtual environment. Use the appropriate command for your operating system.

- **On macOS and Linux:**

  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

- **On Windows:**

  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```

4. **Install Dependencies**

With the virtual environment activated, install the required Python packages using `pip`:

`pip install -r requirements.txt`

5. **Run the Script**

Run the script with `python script.py`
If the script was successfull the following message will be printed: Data has been saved to web_crawl_data.xlsx

6. **Open the Excel File**
   Open web_crawl_data.xlsx file and take a look on the results of the script
