from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from botmily import ircify

def hook(nick, ident, host, message, bot, channel):
    if re.search('im gay', ircify.ircify(message)) is None:
        return None
    return 'same'
