def read_inputs(path: str) -> [str]:
    with open(path, "r") as f:
        inputs = f.readlines()
    return inputs
