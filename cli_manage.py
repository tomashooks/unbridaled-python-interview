import os

import click


@click.group()
def cli() -> None:
    pass


@cli.command()
def run_linter() -> None:
    """Get codestyle warnings"""

    os.system("python3 -m flake8")


@cli.command()
def apply_migrations():
    """Apply migrations for DB"""

    os.system("python3 -m alembic upgrade head")


@cli.command()
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
def test(args):
    """Run testing"""

    args = " ".join(args)
    os.system("python3 -m unittest " + args)


@cli.command()
def get_coverage_report() -> None:
    """Run unittests with coverage report"""
    import os

    os.system(
        "python3 -m coverage run -m unittest;"
        "python3 -m coverage combine;"
        "python3 -m coverage html -i;"
    )


@cli.command()
def run_app_dev() -> None:
    """Run app for development purposes"""
    os.system(
        "python3 -m uvicorn app.main:app --reload"
    )


if __name__ == "__main__":
    cli()
