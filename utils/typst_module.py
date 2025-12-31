import subprocess
from utils.typst_template import get_template


def save(author, content, filename):
    typst_file = f"{filename}.typ"
    with open(typst_file, "w", encoding="utf-8") as f:
        template = get_template(author, content)
        f.write(template[0])
        for value in template[1].values():
            f.write(value)


def compile(filename):
    try:
        subprocess.run(["typst", "compile", f"{filename}.typ"])
        print("Скомпилировано")
    except Exception as e:
        print(f"Ошибка при компиляции. Error: {e}")
