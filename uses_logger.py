from settings import LOG


def main():
    """
    ロガー使用サンプル
    """
    LOG.debug('debug')
    LOG.info('info')
    LOG.warning('warning')
    LOG.error('error')
    LOG.critical('critical')


if __name__ == '__main__':
    main()
