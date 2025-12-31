import argparse
import os

from utils.repo_scanner import scan_repo
from utils.typst_module import save, compile


def parse_args():
    parser = argparse.ArgumentParser(
        prog="reportify", description="cli tool for report generation", epilog="usage"
    )

    parser.add_argument("author")
    parser.add_argument("-d", "--directory", default=".")
    parser.add_argument("-o", "--output", default="reports/report")

    return parser.parse_args()


def main():
    args = parse_args()

    if not os.path.isdir(args.directory):
        print(f"Директория {args.directory} не найдена.")
        return

    content = scan_repo(f"{args.directory}", ["py"])

    save(args.author, content, args.output)
    compile(args.output)


if __name__ == "__main__":
    main()
