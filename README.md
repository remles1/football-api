
## About The Project
Onion Architecture API for getting football statistics, with a RPC for calculating historical matches outcome odds using RabbitMQ as a broker.



### Built With

* [![Django][Django-shield]][Django-url]
* [![PostgreSQL][PostgreSQL-shield]][PostgreSQL-url]
* [![Docker][Docker-shield]][Docker-url]
* [![RabbitMQ][RabbitMQ-shield]][RabbitMQ-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/remles1/football-api.git
   ```
2. Build the container
   ```sh
   docker compose build
   ```
3. Start the container
   ```sh
	docker compose up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage:
Endpoint are located by default at ```http://localhost:8000```
Swagger: ```http://localhost:8000/docs```

### Endpoints:

-   **Countries**:
    
    -   `GET /country/all` - Get all countries.
        
    -   `GET /country/name/{name}` - Get country by name.
        
    -   `GET /country/id/{id}` - Get country by ID.
        
-   **Leagues**:
    
    -   `GET /league/all` - Get all leagues.
        
    -   `GET /league/country/{country_id}` - Get leagues by country ID.
        
    -   `GET /league/name/{name}` - Get league by name.
        
    -   `GET /league/id/{id}` - Get league by ID.
        
    -   `GET /league/stats/{id}` - Get league stats by ID.
        
-   **Cards**:
    
    -   `GET /card/all` - Get all cards.
        
    -   `GET /card/match/{match_id}` - Get cards by match ID.
        
    -   `GET /card/player/{player_api_id}` - Get cards by player ID.
        
    -   `GET /card/id/{id}` - Get card by ID.
        
-   **Goals**:
    
    -   `GET /goal/all` - Get all goals.
        
    -   `GET /goal/match/{match_id}` - Get goals by match ID.
        
    -   `GET /goal/scorer/{scorer}` - Get goals by scorer ID.
        
    -   `GET /goal/assister/{assister}` - Get goals by assister ID.
        
    -   `GET /goal/id/{id}` - Get goal by ID.
        
-   **Matches**:
    
    -   `GET /match/all` - Get all matches.
        
    -   `GET /match/league/{league_id}` - Get matches by league ID.
        
    -   `GET /match/season/{season}` - Get matches by season.
        
    -   `GET /match/date/{date}` - Get matches by date.
        
    -   `GET /match/match_api_id/{match_api_id}` - Get match by API ID.
        
    -   `GET /match/team_api_id/{team_api_id}` - Get matches by team ID.
        
    -   `GET /match/player_api_id/{player_api_id}` - Get matches by player ID.
        
-   **Players**:
    
    -   `GET /player/all` - Get all players.
        
    -   `GET /player/player_api_id/{player_api_id}` - Get player by API ID.
        
    -   `GET /player/player_name/{player_name}` - Get player by name.
        
    -   `GET /player/stats/{player_api_id}` - Get player stats by ID.
        
-   **Teams**:
    
    -   `GET /team/all` - Get all teams.
        
    -   `GET /team/team_api_id/{team_api_id}` - Get team by API ID.
        
    -   `GET /team/team_fifa_api_id/{team_fifa_api_id}` - Get team by FIFA API ID.
        
    -   `GET /team/team_long_name/{team_long_name}` - Get team by long name.
        
    -   `GET /team/stats/{team_api_id}` - Get team stats by ID.
        
-   **Odds**:
    
    -   `GET /odds/{match_api_id}` - Get odds by match API ID.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [European Soccer Database](https://www.kaggle.com/datasets/hugomathien/soccer)
* [Predicting Football Results With Statistical Modelling](https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[RabbitMQ-shield]: https://img.shields.io/static/v1?message=RabbitMQ&logo=rabbitmq&label=&color=FF6600&logoColor=white&labelColor=&style=for-the-badge
[RabbitMQ-url]: https://www.rabbitmq.com/
[Docker-shield]: https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Django-shield]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[PostgreSQL-shield]: https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/





