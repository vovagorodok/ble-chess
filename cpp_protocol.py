import typing

import chess

import async_input

from protocol import BaseProtocol
from string_constants import Commands, Features, Variants, Sides


SERVICE_UUID = 'f5351050-b2c9-11ec-a0c0-b3bc53b08d33'
TX_UUID = 'f53513ca-b2c9-11ec-a0c1-639b8957db99'
RX_UUID = 'f535147e-b2c9-11ec-a0c2-8bbd706ec4e6'

SUPPORTED_FEATURES = [
    Features.MSG,
    Features.LAST_MOVE,
    Features.CHECK,
    Features.SIDE,
    Features.RESIGN]
SUPPORTED_VARIANTS = [
    Variants.STANDARD,
    Variants.CHESS_960]
PERIPHERAL_COMMANDS = (
    Commands.MOVE,
    Commands.MSG,
    Commands.RESIGN)


class CppProtocol(BaseProtocol):

    def __init__(self, send_callback: typing.Callable):
        super().__init__(send_callback)
        self.board = chess.Board()
        self.console_move = None
        self.side = None

    def on_cmd(self, cmd: str):
        if cmd.startswith(Commands.FEATURE):
            feature = self.__get_cmd_params(cmd)
            self.__send_ack(feature in SUPPORTED_FEATURES)
        elif cmd.startswith(Commands.VARIANT):
            variant = self.__get_cmd_params(cmd)
            self.__send_ack(variant in SUPPORTED_VARIANTS)
        elif cmd.startswith(Commands.SET_VARIANT):
            variant = self.__get_cmd_params(cmd)
            if variant == Variants.STANDARD:
                self.board.chess960 = False
            elif variant == Variants.CHESS_960:
                self.board.chess960 = True
            print(f'Variant: {variant}')
        elif cmd.startswith(Commands.BEGIN):
            fen = self.__get_cmd_params(cmd)
            self.board.set_fen(fen)
            self.send(f'{Commands.SYNC} {fen}')
            self.__print_state()
        elif cmd.startswith(Commands.MOVE):
            move = chess.Move.from_uci(self.__get_cmd_params(cmd))
            self.board.push(move)
            self.__print_state()
            print(f'Last move: {self.board.peek()}')
        elif cmd.startswith(Commands.PROMOTE):
            move = chess.Move.from_uci(self.__get_cmd_params(cmd))
            self.board.push(move)
            self.__print_state()
            print(f'Last move: {self.board.peek()}')
        elif cmd.startswith(Commands.OK):
            self.board.push(self.console_move)
            self.__print_state()
            print(f'Last move: {self.board.peek()}')
        elif cmd.startswith(Commands.NOK):
            print(f'Rejected move: {self.console_move}')
        elif cmd.startswith(Commands.END):
            reason = self.__get_cmd_params(cmd)
            print(f'End: {reason}')
        elif cmd.startswith(Commands.ERR):
            error = self.__get_cmd_params(cmd)
            print(f'Error: {error}')
        elif cmd.startswith(Commands.LAST_MOVE):
            move = chess.Move.from_uci(self.__get_cmd_params(cmd))
            print(f'Last move: {move}')
        elif cmd.startswith(Commands.CHECK):
            check = chess.parse_square(self.__get_cmd_params(cmd))
            print(f'Check: {chess.square_name(check)}')
        elif cmd.startswith(Commands.SIDE):
            side = self.__get_cmd_params(cmd)
            if side == Sides.WHITE:
                self.side = chess.WHITE
            elif side == Sides.BLACK:
                self.side = chess.BLACK
            elif side == Sides.BOTH:
                self.side = None

    def _on_text_provided(self, text: str):
        async_input.ainput('', self._on_text_provided)

        if text.startswith(PERIPHERAL_COMMANDS):
            self.send(text)
            return

        move = self.__get_move(text)
        if (move):
            self.console_move = move
            self.send(f'{Commands.MOVE} {text}')
            return

        print('Illegal input')

    def __print_state(self):
        print(self.board)
        print(f'Turn: {self._color_to_str(self.board.turn)}')
        if (self.side is not None):
            print('Your turn' if self.side == self.board.turn else 'Opponent turn')

    @staticmethod
    def __get_cmd_params(cmd: str):
        return cmd.split(' ', 1)[1]

    @staticmethod
    def __get_move(move: str):
        try:
            return chess.Move.from_uci(move)
        except ValueError:
            return None

    def __send_ack(self, ack: bool):
        self.send(Commands.OK if ack else Commands.NOK)
