# **PubMed Paper Fetcher**

A Python command-line tool that fetches research papers from the PubMed API based on a user query. It filters papers with at least one author affiliated with a pharmaceutical or biotech company and exports the results as a CSV file.

---

## **🚀 Features**

- Fetches research papers using the **PubMed API**
- Filters papers with **non-academic authors** affiliated with **pharma/biotech companies**
- Outputs results as a **CSV file** using `pandas`
- Supports **command-line arguments** for customization
- Includes **debug mode** for troubleshooting
- Uses **Poetry** for dependency management

---

## **📌 Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### **2️⃣ Install Dependencies Using Poetry**
Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed. Then run:
```bash
poetry install
```

---

## **🔧 Usage**

### **Basic Command**
Fetch papers for a specific query:
```bash
python pubmed.py "cancer research"
```

### **Save Results to a CSV File**
```bash
python pubmed.py "cancer research" -f results.csv
```

### **Enable Debug Mode**
```bash
python pubmed.py "cancer research" -d
```

### **View Help**
```bash
python pubmed.py --help
```

---

## **📝 Output Format**

The script outputs a CSV file with the following columns:

| PubmedID  | Title | PublicationDate | Non-academic Authors | Company Affiliations | Corresponding Author Email |
|-----------|------------------------|----------------|----------------------|------------------|-------------------------|
| 12345678  | Study on Biotech in Pharma | 2025-03-10 | John Doe | Pharma Inc. | johndoe@pharmainc.com |

---

## **🛠 Code Structure**

```
pubmed-paper-fetcher/
│── pubmed.py          # Main script to fetch and filter research papers
│── README.md          # Documentation
│── pyproject.toml     # Poetry configuration file
│── poetry.lock        # Poetry dependency lock file
└── requirements.txt    # Alternative dependency file (optional)
```

---

## **🔍 How It Works**

1. **Fetch Papers**:
   - Uses the **PubMed API** to search for papers based on user input.

2. **Filter Papers**:
   - Identifies **non-academic authors** based on affiliation.
   - Detects **pharma/biotech companies** using keyword heuristics.

3. **Save & Display**:
   - Saves results in a **CSV file** using `pandas`.
   - Prints output to the terminal if no file is specified.

---

## **📦 Dependencies**

The project uses the following Python libraries:

- `requests` - To interact with the PubMed API
- `pandas` - For data processing and CSV handling
- `argparse` - For command-line arguments
- `logging` - For debugging

All dependencies are managed via Poetry.

---

## **🌍 Publishing to Test PyPI (Bonus)**

To publish the module on **Test PyPI**, follow these steps:

1. Build the package:
   ```bash
   poetry build
   ```
2. Publish to Test PyPI:
   ```bash
   poetry publish -r testpypi
or
1. Install these packages manully
2. Run the below
   ```bash
   python pubmed.py "cancer research" -f results.csv

---

## **👨‍💻 Contributing**

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make changes and commit (`git commit -m "Add new feature"`)
4. Push to your fork and create a pull request

---

## **📜 License**

This project is licensed under the **MIT License**.

---

