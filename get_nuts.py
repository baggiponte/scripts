import requests
import typer
from pathlib import Path
from rich.console import Console

app = typer.Typer(name="NUTS2json", add_completion=False)
console = Console()


@app.command()
def topojson(
        year: int,
        scale: int,
        nuts_level: int,
        projection: int = 3035,
        download_to: str = "topojson",
        verbose: bool = False
) -> None:
    """
    Retrieve a TopoJSON file with the European Union's NUTS classification.
    This function draws the data from Eurostat's official repo Nuts2json.
    Reference: https://github.com/eurostat/Nuts2json
    """
    # build url to request data from
    base_url: str = "https://raw.githubusercontent.com/eurostat/Nuts2json/master"
    url: str = base_url + f"{year}/{projection}/{scale}M/{nuts_level}.json"

    # send a request to the url
    if verbose:
        console.print(f"Sending the request to '{url}'")
    req: requests.Response = requests.get(url)

    # define filename and download path
    filename: str = f"{projection}-{scale}-nuts_{nuts_level}.json"
    download_path: Path = Path.cwd() / download_to / filename
    if verbose:
        console.print(f"Download path: '{download_path}'")

    # if the parent dir (aka /topojson) does not exist, then create it
    if not download_path.parent.exists():
        if verbose:
            console.print(f"creating directory '{download_path.parent}'")
        download_path.parent.mkdir()

    with open(download_path, "wb") as output_file:
        output_file.write(req.content)

    if verbose:
        console.print("File downloaded!")


@app.command()
def geojson(
        scale: int,
        feature_type: str,
        nuts_level: int,
        year: int = 2021,
        projection: int = 3035,
        download_to: str = "geojson",
        verbose: bool = False
) -> None:
    """
    Retrieve a GeoJSON file with the European Union's NUTS classification.
    This function draws the data from Eurostat's official repo Nuts2json.
    Reference: https://github.com/eurostat/Nuts2json
    """

    # build url to request data from
    base_url: str = "https://raw.githubusercontent.com/eurostat/Nuts2json/master"
    url: str = base_url + f"{year}/{projection}/{scale}M/{feature_type}_{nuts_level}.json"

    if verbose:
        console.print(f"Sending the request to '{url}'")
    req: requests.Response = requests.get(url)

    # define filename and download path
    filename: str = f"{projection}-{scale}-nuts_{feature_type}_{nuts_level}.json"
    download_path: Path = Path.cwd() / download_to / filename
    if verbose:
        console.print(f"Download path: '{download_path}'")

    # if the parent dir (aka /topojson) does not exist, then create it
    if not download_path.parent.exists():
        if verbose:
            console.print(f"creating directory '{download_path.parent}'")
        download_path.parent.mkdir()

    with open(download_path, "wb") as output_file:
        output_file.write(req.content)

    if verbose:
        console.print("File downloaded!")


if __name__ == '__main__':
    app()
