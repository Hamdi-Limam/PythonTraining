# Write a CLI application which takes git URL as arguement pulls the code
# Note: GitPython requires git being installed on the system, and accessible via system's PATH.
from git import Repo
import click

@click.command()
@click.argument('url', type=click.STRING)
@click.argument('destination_path', type=click.STRING)
def main(url, destination_path):
    Repo.clone_from(url, to_path=destination_path)

if __name__ == "__main__":
    main()