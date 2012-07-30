﻿# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib2 import urlopen
from xml.etree import ElementTree

def hook(nick, ident, host, message, bot, channel):
    if re.match('\.sto', message) is None:
        return None

    result = urlopen('http://www.google.com/ig/api?stock=' + message[5:])
    root = ElementTree.fromstring(result.read())
    finance = root.find('finance')
    company = finance.find('company').get('data')
    currency = finance.find('currency').get('data')
    last = finance.find('last').get('data')
    change = finance.find('change').get('data')
    perc_change = finance.find('perc_change').get('data')
    trade_timestamp = finance.find('trade_timestamp').get('data')
    string = nick + ': '
    string += company + ' - '
    string += last + ' '
    string += currency + ' \u0003'
    if change[0] == '-':
        string += '5'
    else:
        string += '3'
    string += change + ' ('
    string += perc_change + ')\u000f as of '
    string += trade_timestamp
    return string