#!/usr/bin/env python3

import argparse
from datetime import datetime


def main(timestamp):
    if "." in timestamp:
        print("This appears to be a float timestamp.")
        timestamp = float(timestamp)
    else:
        print("This appears to be a integer timestamp.")
        timestamp = int(timestamp)

    if [arg for arg in (args.ms, args.un, args.ns) if arg is True]:
        if args.ms:
            print("Considering timestamp as milliseconds.")
            timestamp = timestamp / 1e+3
        elif args.us:
            print("Considering timestamp as microseconds.")
            timestamp = timestamp / 1e+6
        elif args.ns:
            print("Considering timestamp as nanoseconds.")
            timestamp = timestamp / 1e+9
    else:
        print("Assuming the timestamp is counting seconds.")

    print()
    print()
    print(f"Epoch in local time ({datetime.now().astimezone().tzname()}): {datetime.fromtimestamp(timestamp)}")
    print(f"Epoch in UTC: {datetime.utcfromtimestamp(timestamp)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert epoch timestamps.")
    parser.add_argument("timestamp", help="An epoch timestamp to covert")
    parser.add_argument("--ms", action="store_true",
                        help="Timestamp value is in milliseconds")
    parser.add_argument("--un", action="store_true",
                        help="Timestamp value is in microseconds")
    parser.add_argument("--ns", action="store_true",
                        help="Timestamp value is in nanoseconds")

    args = parser.parse_args()

    main(args.timestamp)
