import argparse
import logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--token",
        required=True,
        metavar="PAT",
        help="The personal access token for the account",
    )
    parser.add_argument(
        "--category",
        required=True,
        action="append",
        help="A category to monitor. Repeat for multiple categories.",
    )
    parser.add_argument(
        "--address",
        required=True,
        action="append",
        help="Email address to nag. Repeat for multiple email addresses.",
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()
