# Blackjack Game

A simple command-line implementation of the popular casino card game Blackjack. Play against the computer and see if you can beat the dealer!

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Contributing](#contributing)
- [License](#license)

## Description

This is a Python implementation of the classic game Blackjack. It allows you to play the game from your command line interface against a computer dealer. The game follows the standard rules of Blackjack, where the goal is to get a hand value as close to 21 as possible without exceeding it.

The game uses the `random` module to generate random cards and the `art` library to display a cool ASCII art logo at the start.

## Getting Started

### Prerequisites

To run this game, you need to have Python 3.x installed on your machine. You can download Python from the official website: https://www.python.org/downloads/

### Installation

1. Clone the repository to your local machine using the following command:git clone <https://github.com/rudravashishtha/blackjack-game-rudra.git>

2. Navigate to the cloned repository directory: cd blackjack-game

3. Run the game: python blackjack.py


## How to Play

1. The game starts by dealing two cards to both the player and the dealer.
2. The player's cards are displayed, along with the current score.
3. One of the dealer's cards is shown (the other card remains hidden).
4. The player is prompted to choose whether to hit (request another card) or stand (stop receiving cards).
5. If the player's score exceeds 21, the player loses.
6. Once the player stands, the dealer reveals their hidden card.
7. The dealer continues to hit until their score reaches 17 or higher.
8. If the dealer's score exceeds 21, the player wins.
9. The final scores of both the player and the dealer are displayed, along with the outcome of the game.

## Game Rules

- The value of numbered cards is their face value (e.g., 2 of Hearts = 2).
- The value of face cards (King, Queen, Jack) is 10.
- The value of an Ace is 1 or 11, whichever is more advantageous.
- The player loses if their score exceeds 21 (bust).
- The dealer must hit until their score is 17 or higher.
- The player wins if their score is higher than the dealer's without exceeding 21.

## Contributing

Contributions are welcome! If you find any issues or want to improve the game, feel free to submit a pull request. Please make sure to follow the existing coding style and include relevant tests.

## License

This project was inspired by [Blackjack](https://en.wikipedia.org/wiki/Blackjack), most widely played casino banking game in the world.