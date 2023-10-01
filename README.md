 # ITB Staff Data Scraping Script

The `itb_staff_data_scraping.py` script is a Python script for scraping staff data from the Institut Teknologi Bandung (ITB) website. It uses the BeautifulSoup library to parse web pages and extract information about staff members, including their names, expertise, school/faculty, titles, education history, and email addresses.

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- Python 3.x
- BeautifulSoup4
- Requests

You can install BeautifulSoup4 and Requests using pip:

```bash
pip install beautifulsoup4 requests
```

## Usage

1. Clone or download the script to your local machine.

2. Install the required Python libraries mentioned in the "Prerequisites" section.

3. Configure the script by specifying the `BASE_URL` variable, which should be the URL of the ITB staff listing page.

4. Run the script:

```bash
python itb_staff_data_scraping.py
```

The script will start scraping staff data from the ITB website and save the results in a CSV file named `data_dosen.csv`.

## CSV Output

The output CSV file will have the following columns:

- Name: The name of the staff member.
- Expertise: The expertise or field of study of the staff member.
- School/Faculty: The school or faculty to which the staff member belongs.
- Title: The title or position of the staff member.
- S1: Undergraduate education information (Institution and Year).
- S2: Master's degree education information (Institution and Year).
- S3: Doctorate education information (Institution and Year).
- Email: The email address of the staff member.

## Customization

You can customize the script by modifying the code to adapt it to the structure of the ITB website or to extract additional information if needed.

## Example

```bash
python itb_staff_data_scraping.py
```

This command will execute the script, scrape staff data from the ITB website, and save the results in `data_dosen.csv`.

Feel free to use this script to collect staff data from ITB or similar websites for your data analysis or research purposes.
```

You can customize this README by replacing `itb_staff_data_scraping.py` with the actual name of your script and providing additional information or examples as needed.
