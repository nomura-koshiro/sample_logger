"""
ロギングレベル設定
"""

import logging

from logger import Logger

# 使用する場合は以下のうち、一つを記述する

# ログレベルをDEBUGに設定
LOG = Logger(logging.DEBUG, logging.DEBUG).root

# ログレベルをINFOに設定
LOG = Logger(logging.INFO, logging.INFO).root

# ログレベルをWARNINGに設定
LOG = Logger(logging.WARNING, logging.WARNING).root

# ログレベルをERRORに設定
LOG = Logger(logging.ERROR, logging.ERROR).root

# ログレベルをCRITICALに設定
LOG = Logger(logging.CRITICAL, logging.CRITICAL).root

# ログレベルをDEBUGに設定
LOG = Logger(logging.DEBUG, logging.DEBUG).root
