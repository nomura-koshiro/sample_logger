"""
ロギングレベル設定
"""

import logging

from logger import Logger

# 使用する場合は以下のうち、一つを記述する

# ログレベルをDEBUGに設定
LOG = Logger(logging.DEBUG, logging.DEBUG)

# ログレベルをINFOに設定
LOG = Logger(logging.INFO, logging.INFO)

# ログレベルをWARNINGに設定
LOG = Logger(logging.WARNING, logging.WARNING)

# ログレベルをERRORに設定
LOG = Logger(logging.ERROR, logging.ERROR)

# ログレベルをCRITICALに設定
LOG = Logger(logging.CRITICAL, logging.CRITICAL)

# ログレベルをDEBUGに設定
LOG = Logger(logging.DEBUG, logging.DEBUG)
