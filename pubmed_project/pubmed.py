import requests
import pandas as pd
import argparse
import logging
from typing import List, Dict

# Constants
PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
RECORDS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# Function to fetch papers from PubMed API
def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    params = {
        'db': 'pubmed',
        'term': query,
        'retmode': 'xml',
        'retmax': '100',  # Limit results for testing, adjust as needed
    }
    try:
        response = requests.get(PUBMED_BASE_URL, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching papers: {e}")
        return []

    if debug:
        logging.debug(f"Fetched data: {response.text}")

    # Mock paper data for illustration
    mock_paper_data = [
        {
            "PubmedID": "12345678",
            "Title": "Study on Biotech in Pharma",
            "PublicationDate": "2025-03-10",
            "Authors": ["John Doe", "Jane Smith"],
            "Affiliations": ["University A", "Pharma Inc."],
            "CorrespondingAuthorEmail": "johndoe@pharmainc.com"
        },
    ]
    return mock_paper_data

# Function to filter non-academic authors and company affiliations
def filter_non_academic(papers: List[Dict]) -> List[Dict]:
    for paper in papers:
        non_academic_authors = []
        companies = []
        for author, affiliation in zip(paper['Authors'], paper['Affiliations']):
            if "university" not in affiliation.lower() and "lab" not in affiliation.lower():
                non_academic_authors.append(author)
                if "pharma" in affiliation.lower() or "biotech" in affiliation.lower():
                    companies.append(affiliation)
        paper['Non-academic Authors'] = ", ".join(non_academic_authors)
        paper['Company Affiliations'] = ", ".join(companies)
    return papers

# Function to save the papers as CSV using pandas
def save_to_csv(papers: List[Dict], filename: str) -> None:
    df = pd.DataFrame(papers, columns=[
        'PubmedID', 'Title', 'PublicationDate', 'Non-academic Authors',
        'Company Affiliations', 'CorrespondingAuthorEmail'
    ])
    df.to_csv(filename, index=False)
    logging.info(f"Results saved to {filename}")

# Command-line program to handle arguments
def main():
    parser = argparse.ArgumentParser(description="Fetch research papers based on a user query from PubMed.")
    parser.add_argument("query", help="Search query for PubMed.")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information.")
    parser.add_argument("-f", "--file", help="Filename to save the results.")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    # Fetch papers
    papers = fetch_papers(args.query, debug=args.debug)
    
    if not papers:
        logging.error("No papers found.")
        return

    # Filter papers for non-academic authors and company affiliations
    filtered_papers = filter_non_academic(papers)

    # Output result
    if args.file:
        save_to_csv(filtered_papers, args.file)
    else:
        print(pd.DataFrame(filtered_papers))

if __name__ == "__main__":
    main()
