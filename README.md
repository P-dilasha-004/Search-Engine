# Search Engine

## Overview

The Search Engine project is a Python-based tool that indexes and retrieves articles based on user queries. It allows users to search articles by keywords, apply various filters, and refine search results using advanced filtering techniques.

## Features

- **Article Indexing**: Organizes articles with metadata, including title, author, timestamp, length, and keywords.
- **Basic Search**: Retrieves articles based on keyword input.
- **Advanced Search Filters**:
  - Filter by article length
  - Retrieve articles by specific authors
  - Exclude articles containing certain keywords
  - Find articles from a specific year
- **Modular Code Structure**: Three separate search modules handle different functionalities.
- **Comprehensive Testing Suite**: Unit tests ensure code correctness and functionality.

## Project Structure
```bash
Search-Engine/
├── search_one.py          # Basic search functionality
├── search_two.py          # Metadata-based search operations
├── search_three.py        # Advanced search filters
├── wiki.py                # Provides article data and user input functions
├── __init__.py            # Initializes the package for the Search Engine module
├── tests/
│   ├── test_search_one.py # Tests for search_one module
│   ├── test_search_two.py # Tests for search_two module
│   ├── test_search_three.py # Tests for search_three module
└── README.md              # Project documentation
```
## Installation

### Clone the Repository

```bash
git clone https://github.com/P-dilasha-004/Search-Engine.git
cd Search-Engine
```
## Usage

### Running the Search Engine

Execute any of the search modules:

```bash
python search_one.py
```
Or
```bash
python search_two.py
```
Or
```bash
python search_three.py
```
## Performing a Search

- Enter a keyword to search for articles.
- Select advanced search options if needed.
- View refined results based on filters applied.

## Testing

Run the test suite to verify functionality:

```bash
pytest tests/
```
## Contributing

Contributions are welcome! Follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**

```bash
git checkout -b feature/your_feature_name
```
3. Implement your changes and commit them:

```bash
git commit -m "Describe your changes"
```
4. Push your changes:

```bash
git push origin feature/your_feature_name
```
5. Open a Pull Request explaining your modifications.

## License 
This project is licensed under the MIT License - see the [LICENSE](https://github.com/P-dilasha-004/Search-Engine/blob/main/LICENSE) file for details.

## Acknowlegments

This project was built as part of my class coursework to enhance my understanding of search algorithms and Python development.  

Special thanks to my instructor and classmates for their support and feedback throughout the project.  




