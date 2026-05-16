# hello-cli

A minimal Python command‑line utility that prints a friendly greeting.

## Features
- Zero‑dependency, runs on any Python 3.8+ interpreter.
- Shows proactive error detection (invalid arguments).
- Idempotent: running the script multiple times produces the same result without side effects.

## Usage
```bash
python hello.py [--name NAME]
```
If `--name` is omitted, it defaults to `World`.

## Example
```bash
$ python hello.py --name Alice
Hello, Alice!
```

## License
MIT – see the `LICENSE` file in the repository.
