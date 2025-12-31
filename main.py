from utils.repo_scanner import scan_repo
from utils.typst_module import save, compile


author = "Niyaz Ibragimov"
content = scan_repo(".", ["py"])
filename = "reports/report"


def main():
    save(author, content, filename)
    compile(filename)


if __name__ == "__main__":
    main()
