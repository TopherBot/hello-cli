#!/usr/bin/env python3
"""hello-cli – a tiny greeting command line tool.

Provides:
- Clear argument parsing with helpful errors.
- Default greeting "World" if no name is supplied.
- Idempotent behaviour – no state is persisted.
"""

import argparse
import sys

def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command‑line arguments.

    Args:
        argv: List of arguments (excluding the program name).

    Returns:
        argparse.Namespace with a single attribute `name`.
    """
    parser = argparse.ArgumentParser(
        prog="hello-cli",
        description="Print a friendly greeting.",
        add_help=True,
    )
    parser.add_argument(
        "--name",
        type=str,
        default="World",
        help="Name to greet (default: %(default)s).",
    )
    # Proactive error detection – ensure no unknown arguments remain
    args, unknown = parser.parse_known_args(argv)
    if unknown:
        parser.error(f"unrecognized arguments: {' '.join(unknown)}")
    return args

def main() -> None:
    args = parse_args(sys.argv[1:])
    # Idempotent output – deterministic string construction
    greeting = f"Hello, {args.name}!"
    print(greeting)

if __name__ == "__main__":
    main()
