# arXiv Articles Ranking by User Preferences

This repository contains scripts to download metadata from the arXiv Open Archives Initiative (OAI) and create a neatly formatted HTML file with articles ranked by user-defined preferences. 

---

## Features

- **Download Metadata**: Fetches metadata from arXiv via its API in XML format.
- **Generate HTML Output**: Converts the XML data into a user-friendly HTML file.
- **Customizable Filtering**: Enables personalization with a linear ranking based on user-defined keywords, authors, and subjects of interest.
- **Date Filtering**: Supports querying a range of dates or a single date.

---

## How to Use

### Run the Extraction Script
- Run the first script to fetch metadata from arXiv. Specify the date range (inclusive) as arguments:

```bash
python arXiv-metadata-extract.py '2019-11-19' '2019-11-22'
```

- The script downloads metadata in XML format and saves it as `arXiv-articles.xml`.
- If you only want metadata for a single day, you can omit the second date:

```bash
python arXiv-metadata-extract.py '2019-11-19'
```

- Open the generated HTML file in any browser to view the list with ranked articles.

---

## Customization

You can adjust the filtering preferences in `arXiv-metadata-embetter.py`:

- **Keywords**:
  - Modify the `bad_keywords` and `good_keywords` dictionaries to change the scoring of articles based on their content.
- **Authors**:
  - Update the `good_authors` list to prioritize articles from specific researchers.
- **Subjects**:
  - Edit the `good_subjects` and `subjects_to_follow` lists to prioritise certain subjects.

---

## Example Output

The generated `arXiv-articles.html` file displays:

1. **Article ID**: Links to the PDF of the article on arXiv.
2. **Subject**: Shows the category of the article.
3. **Score**: Indicates the relevance score based on your preferences.
4. **Title and Abstract**: Highlights the key details of each article. The user-defined keywords would be highlighted. 
5. **Authors**: Displays the authors' names, with top authors highlighted.

---

## Notes

- **Example File**: The file `arXiv-articles.html` is provided for illustrative purposes.
- **Python Version**: These scripts are designed to run on Python 3.
- **Dependencies**: Install the required Python packages with:
  '''bash
  pip install numpy
  '''
- **API Limitations**: The script pauses for 20 seconds between API calls to comply with arXiv's rate limits.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
