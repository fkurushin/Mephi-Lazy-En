def read_txt(path):
    with open(path, "r") as fo:
        lines = fo.readlines()
    return [line.lower().replace("\n", "").strip() for line in lines]