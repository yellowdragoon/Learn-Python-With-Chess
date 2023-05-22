from abc import ABC, abstractclassmethod

class Piece(ABC):
    def __init__(self, color) -> None:
        self.color = color

    @abstractclassmethod
    def validate_move(self, board, from_square, to_square) -> bool:
        pass

    @abstractclassmethod
    def piece_value(self) -> int:
        pass