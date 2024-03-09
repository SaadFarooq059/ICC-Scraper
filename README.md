
# ICC-Scraper

`ICC-Scraper` is a Scrapy spider designed to scrape team and player rankings from the International Cricket Council (ICC) website. It can fetch data based on the command-line argument specifying whether to scrape team rankings or player rankings.

## Features

- Scrape ICC team rankings.
- Scrape ICC player rankings.
- Command-line arguments for flexible scraping options.

## Requirements

- Python 3.6+
- Scrapy

## Installation

To set up `ICC-Scraper`, you'll need to have Python and Scrapy installed on your system. If you haven't installed Scrapy yet, you can do so by running:

```bash
pip install scrapy
```

## Usage

To use `ICC-Scraper`, clone this repository to your local machine and navigate to the project directory. The spider can be executed with a command-line argument specifying what to scrape (`team` or `players`), along with the required parameters such as `gender`, `format`, and `category` for players.

### Syntax

```bash
scrapy crawl rank -a arg=value
```

### Examples

To scrape men's team rankings:

```bash
scrapy crawl rank -a argument=team -a gender=men -a format=test
```

To scrape women's player rankings:

```bash
scrapy crawl rank -a argument=players -a gender=women -a format=odi -a category=batter
```

## Output

The scraper outputs the scraped data in a structured format, including names, matches, points, ratings for teams, and names, teams, ratings for players.

## Contributing

Contributions to `ICC-Scraper` are welcome. Please ensure you create a pull request for any changes or features you wish to add.

## License

This project is open-source and available under the [MIT License](LICENSE).

