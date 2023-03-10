import sys
import logging

from .main import State, Cetele

short_cmds = {
    "s": "show",
    "e": "edit",
    "rm": "delete",
    "i": "interactive",
    "ls": "list",
    "v": "verify",
}


def parse_args(args: list) -> list:
    if "--debug" in args:
        logging.basicConfig(level=logging.DEBUG)
        args.remove("--debug")
    if len(args) == 1:
        args.append("show")
    if long_version := short_cmds.get(args[1]):
        args[1] = long_version
    return args


def main():
    args = parse_args(sys.argv)
    state = State()

    match args[1]:
        case "show":
            cetele = Cetele(state)
            print(cetele)
        case "edit" | "delete":
            assert len(args) == 3
            getattr(state, args[1])(args[2])
        case "interactive":
            state.interactive()
        case "list":
            print(state)
        case "verify":
            state.verify()
        case _:
            exit("Unexpected argument!")
