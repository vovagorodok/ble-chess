import logging

from bluezero import adapter
from bluezero import peripheral

import cpp_protocol
import chess_device


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    device = chess_device.ChessDevice()
    protocol = cpp_protocol.CppProtocol(device.send)

    device.set_protocol(protocol)
    chess_peripheral = peripheral.Peripheral(__get_adapter_adress(),
                                             local_name='Chess board')
    chess_peripheral.add_service(
        srv_id=1,
        uuid=cpp_protocol.SERVICE_UUID,
        primary=True)
    chess_peripheral.add_characteristic(
        srv_id=1,
        chr_id=1,
        uuid=cpp_protocol.TX_UUID,
        value=[],
        notifying=False,
        flags=['write'],
        write_callback=device.on_data_recived)
    chess_peripheral.add_characteristic(
        srv_id=1,
        chr_id=2,
        uuid=cpp_protocol.RX_UUID,
        value=[],
        notifying=False,
        flags=['read', 'notify'],
        notify_callback=device.on_change_notify)

    chess_peripheral.on_connect = device.on_connect
    chess_peripheral.on_disconnect = device.on_disconnect

    chess_peripheral.publish()


def __get_adapter_adress():
    return list(adapter.Adapter.available())[0].address


if __name__ == "__main__":
    main()
