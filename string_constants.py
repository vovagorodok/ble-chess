from enum import Enum

class Feature(Enum):
    GET_STATE = "get_state"
    SET_STATE = "set_state"
    STATE_STREAM = "state_stream"
    LAST_MOVE = "last_move"
    CHECK = "check"
    UNDO = "undo"
    MOVED = "moved"
    MSG = "msg"
    RESIGN = "resign"
    DRAW_OFFER = "draw_offer"
    SIDE = "side"
    TIME = "time"
    SCORE = "score"
    OPTION = "option"
    DRAW_REASON = "draw_reason"
    VARIANT_REASON = "variant_reason"

class Variant(Enum):
    STANDARD = "standard"
    CHESS_960 = "chess_960"
    THREE_CHECK = "3_check"
    ATOMIC = "atomic"
    KING_OF_THE_HILL = "king_of_the_hill"
    ANTI_CHESS = "anti_chess"
    HORDE = "horde"
    RACING_KINGS = "racing_kings"
    CRAZY_HOUSE = "crazy_house"

class Command(Enum):
    OK = "ok"
    NOK = "nok"
    FEATURE = "feature"
    VARIANT = "variant"
    SET_VARIANT = "set_variant"
    BEGIN = "begin"
    STATE = "state"
    SYNC = "sync"
    UNSYNC = "unsync"
    MOVE = "move"
    END = "end"
    PROMOTE = "promote"
    ERR = "err"
    GET_STATE = Feature.GET_STATE.value
    SET_STATE = Feature.SET_STATE.value
    UNSYNC_SETIBLE = "unsync_setible"
    LAST_MOVE = Feature.LAST_MOVE.value
    CHECK = Feature.CHECK.value
    UNDO = Feature.UNDO.value
    MOVED = Feature.MOVED.value
    MSG = Feature.MSG.value
    RESIGN = Feature.RESIGN.value
    DRAW_OFFER = Feature.DRAW_OFFER.value
    SIDE = Feature.SIDE.value
    TIME = Feature.TIME.value
    SCORE = Feature.SCORE.value
    OPTIONS_BEGIN = "options_begin"
    OPTION = Feature.OPTION.value
    OPTIONS_END = "options_end"
    OPTIONS_RESET = "options_reset"
    SET_OPTION = "set_option"

class EndReason(Enum):
    UNDEFINED = "undefined"
    CHECKMATE = "checkmate"
    DRAW = "draw"
    TIMEOUT = "timeout"
    RESIGN = "resign"
    ABORT = "abort"

class Side(Enum):
    WHITE = "w"
    BLACK = "b"
    BOTH = "?"

class DrawReason(Enum):
    DRAW_OFFER = Feature.DRAW_OFFER.value
    STALEMATE = "stalemate"
    THREEFOLD_REPETITION = "threefold_repetition"
    FIFTY_MOVE = "fifty_move"
    INSUFFICIENT_MATERIAL = "insufficient_material"
    DEAD_POSITION = "dead_position"

class VariantReason(Enum):
    THREE_CHECK = Variant.THREE_CHECK.value
    KING_OF_THE_HILL = Variant.KING_OF_THE_HILL.value

class OptionType(Enum):
    BOOL = "bool"
    ENUM = "enum"
    STR = "str"
    INT = "int"
    FLOAT = "float"
