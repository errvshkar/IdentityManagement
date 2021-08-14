import sys
from app import identity_app


def main():
    try:
        port, host = 18078, 'localhost'
        print('Starting Art WMS on %(host)s:%(port)s',
              {'host': host, 'port': port})
        identity_app.app.run(host, port, threaded=True)
    except Exception as e:
        sys.stderr.write("ERROR: %s\n" % e)
        sys.exit(1)


if __name__ == '__main__':
    main()
