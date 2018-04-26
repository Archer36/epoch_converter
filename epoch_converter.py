#!/usr/bin/env python3

import argparse
import datetime

def main():
    print()
    print("Epoc in local time ({}): {}".format(datetime.datetime.now().astimezone().tzname(),
                                               datetime.datetime.fromtimestamp(args.epoch)))
    print("Epoc in UTC: {}".format(datetime.datetime.utcfromtimestamp(args.epoch)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert epoch timestamps.")
    parser.add_argument("epoch", type=int, help="An epoch timestamp to covert")

    args = parser.parse_args()

    main()
