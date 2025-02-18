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
