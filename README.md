<meta charset="UTF-8">
<h1 align="center">Wine MS <p>&#127863;</p> </h1>
<h4 align="center">Wine Recommender system for local wine vendors in Münster town.</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#directories">Directories</a> •
  <a href="#activation">Activation</a> •
  <a href="#overview">Overview</a> •
  <a href="#authorization">Authorization</a> •
</p>

---

## Description
Wine MS is recommendation system consists of large wine database with detail information along with recommendation engine for generating the most similar type according to your taste. Users are supposed to insert their preferences for wine taste and origin, which can be further modified with spider diagram for making more precise taste range. Engine will consider you choice and recommend you to most suitable wine, which you can buy in wine shops all around the Münster.

## Requirements

NodeJS & React are required for running the User Interface, while the API reqires Python version 3.10.2.

### Python packages for:

#### Scraping:
```
selenium
beautifulsoup4
xlsxwriter
lxml
```

#### Importing data to DB:
```
sqlalchemy
```

#### Matching:
```
recordlinkage
fuzzywuzzy
rapidfuzz
```

## Directories

```
scrapers
    vivino scraper/         contains scripts for running the scraping engine
    jacques.de/             contains scripts running the scraper and data cleansing
    divino/                 contains scripts for scraping the divino data

sql_injection               contains scripts for data extraction and importing to DB

Script - Data Extraction    contains scripts for data extraction and data cleansing

data-matching               contains scripts for data matching and evaluated results
    
backend
    dist/                   contains distributing parameters
    src/                    contains source files for developing the interface
    
frontend
    recommender_engine/     contains engine files for recommendation
    WineAPI/                contains Django files for developing API
    WineRecommender_API/    contains Django initial files
    
```
## Activation
Instructions for running the system

## Overview
Screenshots.

## Authorization
All data was retrieved, gathered and processed within the project scope for educational purposes. Main data sources are vivino and Münster wine sellers. The system is developed for Data Integration module at Westfälische Wilhelms Universität, and hosted on local and virtual machines. 
