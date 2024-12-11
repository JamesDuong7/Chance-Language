# Chance Language Interpreter

This repository contains an interpreter for a custom programming language focused on randomness, gambling, and chance. The language provides various mechanisms to simulate random events such as slot machines, coin flips, dice rolls, and random chance events. The interpreter executes these events based on the given input program.

## Features

- **Slot Machine Simulation**: Simulates a slot machine with symbols like 🍒, 🍋, 🍉, ⭐, 💎, 🔔, 🍇, and checks for matching symbols.
- **Coin Flip**: Simulates a coin flip with two outcomes: heads and tails.
- **Random Chance**: Executes code based on a probabilistic chance.
- **Dice Roll**: Rolls a dice and compares the result against a threshold.
- **Repeat Until Success**: Repeats an action until a random event succeeds, based on a specified chance.
- **For and While Loops**: Loops can break early based on a random probability.
- **Random Range Generation**: Generate a random number within a specified range.

## Programming Language Overview

The language supports several constructs for randomness and chance-based actions:

- **Slot Machine**: A slot machine simulation that prints three symbols from a predefined list.
  
    Example:
    ```plaintext
    slotMachine();
    ```

- **Coin Flip**: Simulates a coin flip, executing different code blocks for heads or tails.
  
    Example:
    ```plaintext
    coinFlip() {
        heads {
            // Code for heads
        }
        tails {
            // Code for tails
        }
    }
    ```

- **Random Chance**: Executes code blocks based on a given probability.
  
    Example:
    ```plaintext
    randomChance(0.25) {
        // Code that has a 25% chance to execute
    }
    ```

- **Dice Roll**: Rolls a dice and executes code based on the result.
  
    Example:
    ```plaintext
    6-diceRoll(3) {
        // Code executed if the roll is within the first 3 numbers
    }
    ```

- **Random Range**: Assigns a random number within a specified range to a variable.
  
    Example:
    ```plaintext
    let x = randomRange(0, 100);
    ```

- **Repeat Until Success**: Repeats an action until a randomly determined event succeeds.

    Example:
    ```plaintext
    repeatUntilSuccess(randomChance(0.25)) {
        // Code that repeats until the random chance succeeds
    }
    ```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/JamesDuong7/Chance-Language.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Chance-Language
    ```

3. Ensure you have Python 3 installed (>= 3.6).

4. Install any required dependencies (if applicable).

## Usage

1. Write a program in the custom language and save it to a file (e.g., `program.cl`).
   
   Example program:
   ```plaintext
   slotMachine();
   let x = randomRange(0, 100);
   randomChance(0.25) {
       print("This code has a 25% chance to execute.");
   }
