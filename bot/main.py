# custom imports
from utils.helpers import setup_logger
from bot.backend import Astley

logger = setup_logger("richard")


class Rick(Astley):
    """
    A bot that detects and warns you about possible Rick rolls.
    """
    def __init__(self):
        super().__init__(command_prefix="rr!")
        self.scanners = list()

    # todo implement interface with scanners in this class





