#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from typing import List, Tuple
from enum import Enum


class Opponent(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Myself(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class Cheat(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


class Points(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    WIN = 6
    DRAW = 3


def find_solution_one(data: str) -> int:
    rounds = process_data(data)
    my_score = get_my_score(rounds)

    return my_score


def find_solution_two(data: str) -> int:
    rounds = process_data(data)
    my_score = get_my_cheater_score(rounds)

    return my_score


def process_data(data: str) -> List[Tuple[str, str]]:
    # formatted to [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    return [tuple(elements.split(" ")) for elements in data.split("\n")]


def get_my_score(rounds: List[Tuple[str, str]]) -> int:
    my_score = 0

    for opponent_move, my_move in rounds:
        match opponent_move:
            case Opponent.ROCK.value:
                match my_move:
                    case Myself.ROCK.value:  # draw
                        my_score += Points.ROCK.value + Points.DRAW.value

                    case Myself.PAPER.value:  # opponent wins
                        my_score += Points.PAPER.value + Points.WIN.value

                    case Myself.SCISSORS.value:  # I win
                        my_score += Points.SCISSORS.value

            case Opponent.PAPER.value:
                match my_move:
                    case Myself.PAPER.value:  # draw
                        my_score += Points.PAPER.value + Points.DRAW.value

                    case Myself.ROCK.value:  # opponent wins
                        my_score += Points.ROCK.value

                    case Myself.SCISSORS.value:  # I win
                        my_score += Points.SCISSORS.value + Points.WIN.value

            case Opponent.SCISSORS.value:
                match my_move:
                    case Myself.SCISSORS.value:  # draw
                        my_score += Points.SCISSORS.value + Points.DRAW.value

                    case Myself.PAPER.value:  # opponent wins
                        my_score += Points.PAPER.value

                    case Myself.ROCK.value:  # I win
                        my_score += Points.ROCK.value + Points.WIN.value

    return my_score


def get_my_cheater_score(rounds: List[Tuple[str, str]]) -> int:
    my_score = 0

    for opponent_move, cheat_move in rounds:
        match opponent_move:
            case Opponent.ROCK.value:
                match cheat_move:
                    case Cheat.LOSE.value: # opponent wins
                        my_score += Points.SCISSORS.value

                    case Cheat.DRAW.value: # draw
                        my_score += Points.ROCK.value + Points.DRAW.value

                    case Cheat.WIN.value: # I win
                        my_score += Points.PAPER.value + Points.WIN.value

            case Opponent.PAPER.value:
                match cheat_move:
                    case Cheat.LOSE.value: # opponent wins
                        my_score += Points.ROCK.value

                    case Cheat.DRAW.value: # draw
                        my_score += Points.PAPER.value + Points.DRAW.value

                    case Cheat.WIN.value: # I win
                        my_score += Points.SCISSORS.value + Points.WIN.value

            case Opponent.SCISSORS.value:
                match cheat_move:
                    case Cheat.LOSE.value: # opponent wins
                        my_score += Points.PAPER.value

                    case Cheat.DRAW.value: # draw
                        my_score += Points.SCISSORS.value + Points.DRAW.value

                    case Cheat.WIN.value: # I win
                        my_score += Points.ROCK.value + Points.WIN.value

    return my_score


if __name__ == "__main__":
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, "input.txt")

    try:
        with open(filename, "r", encoding="utf-8") as fp:
            data: str = fp.read()
    except FileNotFoundError:
        print("Where is the file, idiot!?")
        sys.exit(1)

    start_time = time.perf_counter()
    my_score = find_solution_one(data)
    end_time = time.perf_counter()

    print(f"Part 1 score is {my_score}.")
    print(f"Part 1 total time of execution: {(end_time - start_time) * 1000} ms\n")

    start_time = time.perf_counter()
    my_score = find_solution_two(data)
    end_time = time.perf_counter()

    print(f"Part 2 score is {my_score}.")
    print(f"Part 2 total time of execution: {(end_time - start_time) * 1000} ms")
