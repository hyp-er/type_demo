import typer

app = typer.Typer()


@app.command()
def add(x: float, y: float):
    print(f"{x} + {y} = {x+y}")

@app.command()
def subtract(x: float, y: float):
    print(f"{x} - {y} = {x-y}")

@app.command()
def multiply(x: float, y: float):
    print(f"{x} * {y} = {x*y}")

@app.command()
def divide(x: float, y: float):
    print(f"{x} / {y} = {x/y}")

if __name__ == "__main__":
    app()
