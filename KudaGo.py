import argparse
from kudago.api.kudago_client import KudagoClient

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--location', default=None, type=str, required=True,
                    help='Name of city')
parser.add_argument('-d', '--days', default=None, type=int, required=True,
                    help="Number of days")
parser.add_argument('-c', '--categories', default=None, type=str, required=True,
                    help="Types of events, separated by comma, that will requested from KudaGo Api")
parser.add_argument('-t', '--tags', default='', type=str,
                    help="Tags for events, separated by comma, for much more relevant search")
parser.add_argument('-f', '--file', default='events.json', type=str,
                    help="Name of file for saving data")
parser.add_argument('-qr', '--qrcode', default=False, type=bool,
                    help="Enable qr codes generation")

args = parser.parse_args()


def main():
    try:
        client = KudagoClient(location=args.location, categories=args.categories, tags=args.tags,
                              create_qr_img=args.qrcode)
        client.collect_events(target_days=args.days)
        client.write_events_to_file(filename=args.file)
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
