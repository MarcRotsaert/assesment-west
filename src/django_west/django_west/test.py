from pathlib import Path


print(Path(__file__).parent)
x = Path(__file__).resolve().parent.parent.joinpath("template")
print(x)