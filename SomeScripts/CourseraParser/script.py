with open("input.txt", "r") as file1, open("output.txt", "w") as file2, open(
    "deleted.txt", "w"
) as file3:
    for line in file1:
        if (
            "Duration:" in line
            or "получить доступ к этому заданию" in line
            or "Необходимо сдать" in line
            or "чтобы продолжить" in line
            or "просрочен" in line.lower()
            or (("вопроса" in line or "вопрос" in line) and line[0].isdigit())
            or line.find(":") == -1
        ):
            file3.write(line.strip() + "\n")
        else:
            file2.write(
                line.strip().replace("Лекция", "").replace("[доска] ", "")
                + "\n"
            )
