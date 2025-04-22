import abc
import typing

import chess

import async_input


class Protocol(abc.ABC):

    @abc.abstractmethod
    def handle_cmd(self, cmd: str):
        pass

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class BaseProtocol(Protocol):

    def __init__(self, send_callback: typing.Callable):
        self._send_clb = send_callback

    def start(self):
        async_input.ainput('', self._on_text_provided)

    def stop(self):
        async_input.cancel()

    def send(self, cmd: str):
        self._send_clb(cmd)

    def _on_text_provided(self, text: str):
        pass

    @staticmethod
    def _color_to_str(color):
        return 'white' if color == chess.WHITE else 'black'
