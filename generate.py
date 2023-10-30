#!/usr/bin/python3
import argparse
from pathlib import Path


def generate_readme(directory):
    directory_path = Path(directory)
    with open(directory_path / "README.md", "w") as f:
        f.write("| Directory | Link |\n")
        # table header
        f.write("| --- | --- |\n")

        for item in directory_path.iterdir():
            if item.is_dir() and not item.name.startswith(
                "."
            ):  # if item is a directory and not hidden
                f.write("| {} | [Link](./{}) |\n".format(item.name, item.name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a readme.md file with an index of all directories."
    )
    parser.add_argument(
        "-d",
        "--directory",
        default=".",
        help="Directory to generate readme.md for. Defaults to current directory.",
    )
    args = parser.parse_args()
    generate_readme(args.directory)
