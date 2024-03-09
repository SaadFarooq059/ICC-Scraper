import scrapy
import sys

class ICC(scrapy.Spider):
    name = "rank"

    # Get the argument from command-line and extract the value
    argument = sys.argv[3].split("=", 1)[1]

    # Define start_requests based on the argument value
    def start_requests(self):
        if self.argument == "team":
            yield scrapy.Request(
                f"https://www.icc-cricket.com/rankings/{self.gender}/team-rankings/{self.format}",
                callback=self.parse_teams
            )
        elif self.argument == "players":
            yield scrapy.Request(
                f"https://www.icc-cricket.com/rankings/{self.gender}/player-rankings/{self.format}/{self.category}",
                callback=self.parse_players
            )

    def parse_teams(self, response):
        # Extracting team data from the response
        all_teams = response.css("tbody tr")
        for team in all_teams:
            yield {
                "Name": team.css("span.u-hide-phablet::text").get(),
                "Matches": team.css("td.table-body__cell.u-center-text::text").get()
                          or team.css("td.rankings-block__banner--matches::text").get(),
                "Points": team.css("td:nth-child(4)::text").get()
                          or team.css("td.rankings-block__banner--points::text").get(),
                "Rating": team.css("td.table-body__cell.u-text-right.rating::text").get()
                          or team.css("td.rankings-block__banner--rating.u-text-right::text").get()
            }

    def parse_players(self, response):
        # Extracting player data from the response
        all_players = response.css("tr.table-body")
        for player in all_players:
            yield {
                "Name": player.css("tr.table-body td.table-body__cell.rankings-table__name.name a::text").get(),
                "Team": player.css("td.table-body__cell.nationality-logo.rankings-table__team span::text").get(),
                "Ratings": player.css("td.table-body__cell.rating::text").get()
            }

# Print the argument value from the command-line
print(sys.argv[3])

# Type hints
from typing import Dict, Any

class ICC(scrapy.Spider):
    name: str = "rank"
    argument: str = sys.argv[3].split("=", 1)[1]

    def start_requests(self) -> Any:
        if self.argument == "team":
            yield scrapy.Request(
                f"https://www.icc-cricket.com/rankings/{self.gender}/team-rankings/{self.format}",
                callback=self.parse_teams
            )
        elif self.argument == "players":
            yield scrapy.Request(
                f"https://www.icc-cricket.com/rankings/{self.gender}/player-rankings/{self.format}/{self.category}",
                callback=self.parse_players
            )

    def parse_teams(self, response: scrapy.http.Response) -> Any:
        all_teams = response.css("tbody tr")
        for team in all_teams:
            yield {
                "Name": team.css("span.u-hide-phablet::text").get(),
                "Matches": team.css("td.table-body__cell.u-center-text::text").get()
                           or team.css("td.rankings-block__banner--matches::text").get(),
                "Points": team.css("td:nth-child(4)::text").get()
                           or team.css("td.rankings-block__banner--points::text").get(),
                "Rating": team.css("td.table-body__cell.u-text-right.rating::text").get()
                           or team.css("td.rankings-block__banner--rating.u-text-right::text").get()
            }

    def parse_players(self, response: scrapy.http.Response) -> Any:
        all_players = response.css("tr.table-body")
        for player in all_players:
            yield {
                "Name": player.css("tr.table-body td.table-body__cell.rankings-table__name.name a::text").get(),
                "Team": player.css("td.table-body__cell.nationality-logo.rankings-table__team span::text").get(),
                "Ratings": player.css("td.table-body__cell.rating::text").get()
            }

# Print the argument value from the command-line
print(sys.argv[3])

