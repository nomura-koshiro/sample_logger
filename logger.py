"""
ロギング
"""
import datetime
import logging.config


class Logger:
    """
    ロガークラス
    """

    def __init__(self, log_level, sql_log_level):
        """
        コンストラクタ
            ログ出力内容の設定を行う

        Args:
            log_level (str):ログレベル
                                logging.DEBUG
                                logging.INFO
                                logging.WARNING
                                logging.ERROR
                                logging.CRITICAL
            sql_log_level (str): SQLログレベル
                                logging.DEBUG
                                logging.INFO
                                logging.WARNING
                                logging.ERROR
                                logging.CRITICAL
        """

        logging.config.dictConfig({
            # version
            # version	                        スキーマのバージョンで現在は 1 しか有効ではない(必須)
            'version': 1,
            # 既存ロガーの停止を阻止
            # disable_existing_loggers          設定ファイルで設定の対象になったロガーはその設定が採用される
            #                                   この設定は変更しないこと
            #                                   https://qiita.com/tkygtr6/items/134f1cb63d2868c7959a
            'disable_existing_loggers': False,
            # ログフォーマット
            # formatters	                    ログのフォーマットを設定する
            # formatters/logFormatter           ログフォーマットの定義名を logFormatter と設定している(任意)
            # formatters/logFormatter/format	logFormatter のログフォーマットを指定
            'formatters': {
                'logFormatter': {
                    'format': '%(asctime)s:%(levelname)-8s module:%(module)-18s funcName:%(funcName)-10s line:%(lineno)4s: %(message)s'
                }
            },
            # ハンドラ
            # handlers	                        ハンドラを設定する
            'handlers': {
                # コンソール出力ハンドラ
                # handlers/consoleHandler           コンソールにログを出力するハンドラの定義名を consoleHandler と設定している(任意)
                # handlers/consoleHandler/level     コンソールログ出力ハンドラで使用するログレベルを指定
                # handlers/consoleHandler/formatter コンソールログ出力ハンドラで使用するフォーマッターを指定
                # handlers/consoleHandler/class     コンソールログ出力ハンドラで使用するclassを指定
                'consoleHandler': {
                    'level': log_level,
                    'formatter': 'logFormatter',
                    'class': 'logging.StreamHandler'
                },
                # ファイル出力ハンドラ
                # handlers/fileHandler              ログファイルにログを出力するハンドラの定義名を consoleHandler と設定している(任意)
                # handlers/fileHandler/level        ログファイル出力ハンドラで使用するログレベルを指定
                # handlers/fileHandler/formatter    ログファイル出力ハンドラで使用するフォーマッターを指定
                # handlers/fileHandler/class        ログファイル出力ハンドラで使用するclassを指定
                # handlers/fileHandler/filename     ログファイル出力ハンドラで出力するログファイル名
                # handlers/fileHandler/maxBytes     ログファイル出力ハンドラで出力するログファイルの最大ファイルサイズ
                # handlers/fileHandler/encoding     ログファイルローテート数エンコーディング
                # handlers/fileHandler/backupCount  ログファイルローテート数
                'fileHandler': {
                    'level': log_level,
                    'formatter': 'logFormatter',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': 'log/{0}.log'.format(datetime.date.today()),
                    'maxBytes': 10000000,
                    'encoding': 'utf-8',
                    'backupCount': 3,
                }
            },
            # 使用するハンドラを設定
            # root                              ルートロガーの設定
            # root/handlers                     使用するハンドラを設定　上記で作成したconsoleHandler、fileHandlerを設定
            'root': {
                'handlers': ['consoleHandler', 'fileHandler']
            }
        })

        # ログレベルの設定
        logging.getLogger().setLevel(log_level)

        # SQLログ出力のレベルの設定
        logging.getLogger('sqlalchemy.engine').setLevel(sql_log_level)

        # ロガー作成
        self.root = logging.getLogger()
