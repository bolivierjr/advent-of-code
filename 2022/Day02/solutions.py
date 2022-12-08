#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
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


class Points(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    WIN = 6
    DRAW = 3


def find_solution_one(data: str):
    rounds = process_data(data)
    _, my_score = get_score(rounds)
    return my_score


def get_score(rounds: List[Tuple[str, str]]) -> Tuple[int, int]:
    opponent_score = 0
    my_score = 0

    for opponent_move, my_move in rounds:
        match opponent_move:
            case Opponent.ROCK.value:
                match my_move:
                    case Myself.ROCK.value:  # draw
                        draw_score = Points.ROCK.value + Points.DRAW.value
                        opponent_score += draw_score
                        my_score += draw_score

                    case Myself.PAPER.value:  # opponent wins
                        opponent_score += Points.ROCK.value
                        my_score += Points.PAPER.value + Points.WIN.value

                    case Myself.SCISSORS.value:  # I win
                        opponent_score += Points.ROCK.value + Points.WIN.value
                        my_score += Points.SCISSORS.value

            case Opponent.PAPER.value:
                match my_move:
                    case Myself.PAPER.value:  # draw
                        draw_score = Points.PAPER.value + Points.DRAW.value
                        opponent_score += draw_score
                        my_score += draw_score

                    case Myself.ROCK.value:  # opponent wins
                        opponent_score += Points.PAPER.value + Points.WIN.value
                        my_score += Points.ROCK.value

                    case Myself.SCISSORS.value:  # I win
                        opponent_score += Points.PAPER.value
                        my_score += Points.SCISSORS.value + Points.WIN.value

            case Opponent.SCISSORS.value:
                match my_move:
                    case Myself.SCISSORS.value:  # draw
                        draw_score = Points.SCISSORS.value + Points.DRAW.value
                        opponent_score += draw_score
                        my_score += draw_score

                    case Myself.PAPER.value:  # opponent wins
                        opponent_score += Points.SCISSORS.value + Points.WIN.value
                        my_score += Points.PAPER.value

                    case Myself.ROCK.value:  # I win
                        opponent_score += Points.SCISSORS.value
                        my_score += Points.ROCK.value + Points.WIN.value

    return opponent_score, my_score


def process_data(data: str) -> List[Tuple[str, str]]:
    # formatted to [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    return [tuple(elements.split(" ")) for elements in data.split("\n")]


if __name__ == "__main__":
    directory: str = os.path.dirname(os.path.abspath(__file__))
    filename: str = os.path.join(directory, "input.txt")

    with open(filename, "r", encoding="utf-8") as fp:
        data: str = fp.read()

    start_time = time.perf_counter()
    my_score = find_solution_one(data)
    end_time = time.perf_counter()

    print(my_score)
