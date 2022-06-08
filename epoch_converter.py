#!/usr/bin/env python3

import argparse
import datetime


def main():
    print()
    print(f"Epoch in local time ({datetime.datetime.now().astimezone().tzname()}): {datetime.datetime.fromtimestamp(args.epoch)}")
    print(f"Epoch in UTC: {datetime.datetime.utcfromtimestamp(args.epoch)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert epoch timestamps.")
    parser.add_argument("epoch", type=int, help="An epoch timestamp to covert")

    args = parser.parse_args()

    main()
