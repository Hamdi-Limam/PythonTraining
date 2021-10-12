# Write a CLI application to check if a passed url as arguement is return 200 status code or not.

from click.exceptions import MissingParameter
import requests, click
from requests.models import MissingSchema

@click.command()
@click.argument('url', type=click.STRING, )
def main(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 200:
            click.echo("The request has succeeded with status code 200")
        else:
            click.echo(f"Request returned status {status_code}")
    except MissingSchema:
        click.echo("Invalid URL, please enter a valid URL")
if __name__ == "__main__":
    main()