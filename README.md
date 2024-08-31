# Death Rolling Game 🎲💀

This is a Flask-based web application for the popular game of Death Rolling, enhanced with emojis for a fun experience. The application is containerized using Docker for easy deployment.

## Features
- Play the Death Rolling game online
- Emoji-enhanced user interface
- Dockerized for easy setup and deployment


## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/mattmajestic/deathrolling-game.git
    cd deathrolling-game
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

3. Access the application:
    Open your web browser and go to `http://localhost:5000`

## How to Play
1. Two players take turns rolling a die.
2. The first player rolls a die with a specified number of sides.
3. The next player rolls a die with the number of sides equal to the result of the previous roll.
4. The game continues until a player rolls a 1, and that player loses the game.

## Technologies Used
- Flask
- Docker
- HTML/CSS/JavaScript for the frontend