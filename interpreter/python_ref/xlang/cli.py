import click
from .parser import parse_program

@click.command()
@click.argument('script', type=click.Path(exists=True))
def main(script):
    with open(script, 'r', encoding='utf-8') as f:
        source = f.read()
    program = parse_program(source)
    for verb, args in program:
        # In a real interpreter these would dispatch to handlers
        print(f"EXEC: verb={verb} args={args}")

if __name__ == '__main__':
    main()
