from typing import List


def get_template(student: str, content: List[str]):
    header = f"""
    #set page(paper: "a4")
    #set text(fill: gradient.linear(red, blue), lang: "ru")
    
    = Лабораторная работа
    Студент: *{student}*
    """

    code_listings = {}

    for i in range(len(content)):
        code_listings[i] = f"""== Листинг №{i + 1}
        {content[i]}
        """

    return header, code_listings
