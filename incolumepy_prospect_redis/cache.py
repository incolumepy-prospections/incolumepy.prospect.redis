"""Redis."""
import redis
import logging
import time
import secrets

__author__ = "@britodfbr"  # pragma: no cover

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    r = redis.Redis(host='localhost', port=6379)
    r.set('Brazil', 'Brasília')
    logging.debug(r.get('Brasil'))

    r.mset(
        {
            'Germany': 'Berlin',
            'Paris': 'France',
            'Italy': 'Rome'}
    )
    logging.debug(r.get('Brazil'))
    logging.debug(r.get('Italy'))

    # Valide exists
    logging.debug(r.exists('Paris'))
    logging.debug(r.exists('Japan'))

    # Value with TTL
    logging.info(help(r.psetex))
    time.sleep(1)

    r.psetex('pw', 1001, secrets.token_urlsafe(8))
    logging.debug(r.get('pw'))  # get value
    logging.debug(r.get('pw'))  # get value
    time.sleep(2)
    logging.debug(r.get('pw'))  # no more value


if __name__ == '__main__':    # pragma: no cover
    main()
