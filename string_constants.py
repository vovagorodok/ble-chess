class Features:
    GET_STATE = 'get_state'
    SET_STATE = 'set_state'
    STATE_STREAM = 'state_stream'
    LAST_MOVE = 'last_move'
    CHECK = 'check'
    UNDO = 'undo'
    UNDO_OFFER = 'undo_offer'
    MOVED = 'moved'
    MSG = 'msg'
    RESIGN = 'resign'
    DRAW_OFFER = 'draw_offer'
    SIDE = 'side'
    TIME = 'time'
    SCORE = 'score'
    OPTION = 'option'
    DRAW_REASON = 'draw_reason'
    VARIANT_REASON = 'variant_reason'

class Variants:
    STANDARD = 'standard'
    CHESS_960 = 'chess_960'
    THREE_CHECK = '3_check'
    ATOMIC = 'atomic'
    KING_OF_THE_HILL = 'king_of_the_hill'
    ANTI_CHESS = 'anti_chess'
    HORDE = 'horde'
    RACING_KINGS = 'racing_kings'
    CRAZY_HOUSE = 'crazy_house'

class Commands:
    OK = 'ok'
    NOK = 'nok'
    FEATURE = 'feature'
    VARIANT = 'variant'
    SET_VARIANT = 'set_variant'
    BEGIN = 'begin'
    STATE = 'state'
    SYNC = 'sync'
    UNSYNC = 'unsync'
    MOVE = 'move'
    END = 'end'
    PROMOTE = 'promote'
    ERR = 'err'
    GET_STATE = Features.GET_STATE
    SET_STATE = Features.SET_STATE
    UNSYNC_SETIBLE = 'unsync_setible'
    LAST_MOVE = Features.LAST_MOVE
    CHECK = Features.CHECK
    DROP = 'drop'
    UNDO = Features.UNDO
    UNDO_OFFER = Features.UNDO_OFFER
    MOVED = Features.MOVED
    MSG = Features.MSG
    RESIGN = Features.RESIGN
    DRAW_OFFER = Features.DRAW_OFFER
    SIDE = Features.SIDE
    TIME = Features.TIME
    SCORE = Features.SCORE
    OPTIONS_BEGIN = 'options_begin'
    OPTION = Features.OPTION
    OPTIONS_END = 'options_end'
    OPTIONS_RESET = 'options_reset'
    SET_OPTION = 'set_option'

class EndReasons:
    UNDEFINED = 'undefined'
    CHECKMATE = 'checkmate'
    DRAW = 'draw'
    TIMEOUT = 'timeout'
    RESIGN = 'resign'
    ABORT = 'abort'

class Sides:
    WHITE = 'w'
    BLACK = 'b'
    BOTH = '?'

class DrawReasons:
    DRAW_OFFER = Features.DRAW_OFFER
    STALEMATE = 'stalemate'
    THREEFOLD_REPETITION = 'threefold_repetition'
    FIFTY_MOVE = 'fifty_move'
    INSUFFICIENT_MATERIAL = 'insufficient_material'
    DEAD_POSITION = 'dead_position'

class VariantReasons:
    THREE_CHECK = Variants.THREE_CHECK
    KING_OF_THE_HILL = Variants.KING_OF_THE_HILL

class OptionTypes:
    BOOL = 'bool'
    ENUM = 'enum'
    STR = 'str'
    INT = 'int'
    FLOAT = 'float'
