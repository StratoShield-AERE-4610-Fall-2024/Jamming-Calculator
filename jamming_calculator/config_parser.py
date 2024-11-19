"""Parse the configuration file."""
import yaml


def parse_config(path: str) -> dict:
    """Parse the configuration file.

    This function does not validate the YAML file.

    Parameters
    ----------
    path : str
        Path to the configuration file.

    Returns
    -------
    dict
        Parsed configuration file.
    """
    with open(path, "r") as config_file:
        return yaml.safe_load(config_file)
