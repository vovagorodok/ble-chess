import typing

import chess

import async_input

from protocol import BaseProtocol
from string_constants import Command, Feature, Variant, Side


SERVICE_UUID = 'f5351050-b2c9-11ec-a0c0-b3bc53b08d33'
TX_UUID = 'f53513ca-b2c9-11ec-a0c1-639b8957db99'
RX_UUID = 'f535147e-b2c9-11ec-a0c2-8bbd706ec4e6'


class CppProtocol(BaseProtocol):

    def __init__(self, send_callback: typing.Callable):
        super().__init__(send_callback)
        self.board = chess.Board()
        self.console_move = None
        self.side = None

    def on_cmd(self, cmd: str):
        if cmd.startswith(Command.FEATURE):
            feature = self.__get_cmd_params(cmd)
            self.__send_ack(feature in [Feature.MSG, Feature.LAST_MOVE, Feature.CHECK, Feature.SIDE])
        elif cmd.startswith(Command.VARIANT):
            variant = self.__get_cmd_params(cmd)
            self.__send_ack(variant in [Variant.STANDARD, Variant.CHESS_960])
        elif cmd.startswith(Command.SET_VARIANT):
            variant = self.__get_cmd_params(cmd)
            if variant == Variant.STANDARD:
                self.board.chess960 = False
            elif variant == Variant.CHESS_960:
                self.board.chess960 = True
            print(f'Variant: {variant}')
        elif cmd.startswith(Command.BEGIN):
            fen = self.__get_cmd_params(cmd)
            self.board.set_fen(fen)
            self.send(f'{Command.SYNC} {fen}')
            self.__print_state()
        elif cmd.startswith(Command.MOVE):
            move = chess.Move.from_uci(self.__get_cmd_params(cmd))
            self.board.push(move)
            self.__print_state()
            print(f'Last move: {self.board.peek()}')
        elif cmd.startswith(Command.PROMOTE):
            move = chess.Move.from_uci(self.__get_cmd_params(cmd))
            self.board.push(move)
            self.__print_state()
            print(f'Last move: {self.board.peek()}')
        elif cmd.startswith(Command.OK):
            self.board.push(self.console_move)
            self.__print_state()
            print(f'Last move: {self.board.peek()}')
        elif cmd.startswith(Command.NOK):
            print(f'Rejected move: {self.console_move}')
        elif cmd.startswith(Command.END):
            reason = self.__get_cmd_params(cmd)
            print(f'End: {reason}')
        elif cmd.startswith(Command.ERR):
            error = self.__get_cmd_params(cmd)
            print(f'Error: {error}')
        elif cmd.startswith(Command.LAST_MOVE):
            move = chess.Move.from_uci(self.__get_cmd_params(cmd))
            print(f'Last move: {move}')
        elif cmd.startswith(Command.CHECK):
            check = chess.parse_square(self.__get_cmd_params(cmd))
            print(f'Check: {chess.square_name(check)}')
        elif cmd.startswith(Command.SIDE):
            side = self.__get_cmd_params(cmd)
            if side == Side.WHITE:
                self.side = chess.WHITE
            elif side == Side.BLACK:
                self.side = chess.BLACK
            elif side == Side.BOTH:
                self.side = None
            print(f'Side: {side}')
        
    def _on_text_provided(self, text: str):
        async_input.ainput('', self._on_text_provided)

        if text.startswith(Command.MSG):
            self.send(text)
            return

        move = self.__get_move(text)
        if (move):
            self.console_move = move
            self.send(f'{Command.MOVE} {text}')
            return
        
        print('Illegal input')

    def __print_state(self):
        print(self.board)
        print(f'Turn: {self._color_to_str(self.board.turn)}')
        if (self.side):
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
        self.send(Command.OK if ack else Command.NOK)
