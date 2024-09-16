
class PILOTTONE():
    OFF       = 1
    DCS       = 2
    DCS_ENC   = 4
    DCS_DEC   = 8
    CTCSS     = 16
    CTCSS_ENC = 32
    CTCSS_DEC = 64

    def __init__(self):
        self.OFF       = None
        self.DCS       = None
        self.DCS_ENC   = None
        self.DCS_DEC   = None
        self.CTCSS     = None
        self.CTCSS_ENC = None
        self.CTCSS_DEC = None

class MODULATION():
    # These are not the protocol codes!
    LSB  = 1
    USB  = 2
    CW   = 4
    CWR  = 8
    AM   = 16
    FM   = 32
    DIG  = 64
    PKT  = 128
    FMN  = 256
    FMW  = 512

    def __init__(self):
        self.LSB  = None
        self.USB  = None
        self.CW   = None
        self.CWR  = None
        self.AM   = None
        self.FM   = None
        self.DIG  = None
        self.PKT  = None
        self.FMN  = None
        self.FMW  = None

class COMMAND():

    # These are not the codes of the
    # cat protocol!
    LOCK_ON        = 1
    LOCK_OFF       = 2
    LOCK_TOGGLE    = 3
    
    SPLIT_ON       = 4
    SPLIT_OFF      = 5
    SPLIT_TOGGLE   = 6

    SET_FREQUENCY  = 7
    SET_MODULATION = 8

    READ_RX_STATE  = 9    # Yaesu B5 specific.
    READ_TX_STATE  = 10   # Yaesu B5 specific.
    READ_FREQ_MODE = 11   # Yaesu B5 specific.

    PTT_ON         = 12
    PTT_OFF        = 13

    def __init__(self):

        self.LOCK_ON        = None
        self.LOCK_OFF       = None
        self.LOCK_TOGGLE    = None
        self.SPLIT_ON       = None
        self.SPLIT_OFF      = None
        self.SPLIT_TOGGLE   = None
        self.SET_FREQUENCY  = None
        self.SET_MODULATION = None
        self.READ_RX_STATE  = None
        self.READ_TX_STATE  = None
        self.READ_FREQ_MODE = None
        self.PTT_ON         = None
        self.PTT_OFF        = None

class PORTTYPE():

    SERIAL   = 0x01