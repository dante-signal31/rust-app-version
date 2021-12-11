#!/usr/bin/env python3
""" Console command to read a Cargo.toml and return version configured there. """

import argparse
import configparser
import os
import sys
from typing import List, Dict

CONFIG_FILE = "Cargo.toml"


def get_version(config_file: str = CONFIG_FILE) -> str:
    """ Get version configured at Cargo.toml.

    :param config_file: Path to Cargo.toml.
    :return: Version value at Cargo.toml.
    """
    config = configparser.ConfigParser()
    if os.path.exists(config_file):
        config.read(config_file)
        return config["package"]["version"]
    else:
        print(f"No Cargo.toml file found at provided path: {config_file}")
        sys.exit(1)


def parse_args(args: List[str]) -> Dict[str, str]:
    """ Parse given arguments

    :param args: Program arguments.
    :returns: A Dictionary with given arguments as keys and its respective values.
    """
    parser = argparse.ArgumentParser(
        description="Console command to read a Cargo.toml and return version configured there.",
        epilog="Follow this tool development at: "
               "<https://github.com/dante-signal31/rust-app-version"
    )
    parser.add_argument("-f", "--cargo_toml_folder",
                        type=str,
                        help="Folder path where Cargo.toml can be found. "
                             "Defaults to project root folder.",
                        metavar="CARGO_TOML_FOLDER")
    parsed_arguments = vars(parser.parse_args(args))
    filtered_parser_arguments = {key: value
                                 for key, value in parsed_arguments.items()
                                 if value is not None}
    return filtered_parser_arguments


def main(args=sys.argv[1:]) -> None:
    """ Main execution.

    Taken to its own function to ease testing.

    :param args: Application arguments. Only explicitly set at tests. Usually you'll
    leave it empty and it will populated with sys.argv values.
    """
    arguments: Dict[str, str] = parse_args(args)
    app_version = ""
    if "cargo_toml_folder" in arguments:
        app_version = get_version(
            os.path.join(arguments["cargo_toml_folder"],
                         CONFIG_FILE))
    else:
        app_version = get_version()
    # Remove quotes before printing.
    app_version = app_version[1:-1]
    print(app_version)


if __name__ == "__main__":
    main()

