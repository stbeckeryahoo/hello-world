"""Entry point for interacting with the IGP Manager API."""

import sys

from igp.login import login


def main(args):
    if len(args) < 2:
        print("Usage: main.py <username> <password> [remember]")
        return

    username = args[0]
    password = args[1]
    remember = bool(int(args[2])) if len(args) > 2 else False

    try:
        response = login(username, password, remember)
    except Exception as exc:
        print(f"Login request failed: {exc}")
        return

    if response.get("csrfValid") and response.get("status") == 1:
        print("Login successful")
    else:
        print("Login failed")


if __name__ == "__main__":
    main(sys.argv[1:])
