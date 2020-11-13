# Jalopy Sleuth

Jalopy Sleuth is a Python-based web scraper for creating an extensive Automobile database from Auto Detective

  - Covers cars from 1981-2021
  - Year, Make, Model, Trim
  - 178 different potential fields for each trim

### Installation

Jalopy Sleuth requires Python 3.x.

Install the following dependancies.

```sh
$ pip install requests
$ pip install BeautifulSoup4
$ pip install sqlite3
```

### Instructions
To run simply call carDBSetup.py to initialize the DB then call scrape.py

```sh
$ python3 carDBSetup.py
$ python3 scrape.py
```
The database will come out as car_base.db

Warning - This is a very lengthy process.

For my personal build it took over 12 hours to complete

### Optional Parameters
You can also run for either a specific year range or for a single model to fill in any gaps

```sh
$ python3 scrape.py -f start_year end_year
Will run for a specific year range

$ python3 scrape.py -s year make model
Will run for a specific model
```

