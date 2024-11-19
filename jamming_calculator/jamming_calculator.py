"""Calculate appropriate parameters for The Banshee's jamming mission.
"""
import argparse

from config_parser import parse_config


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments.

    Returns
    -------
    argparse.Namespace
        The parsed arguments object.
    """
    parser = argparse.ArgumentParser(
        description=("Calculates appropriate parameter's for The Banshee's "
                     "jamming mission."),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-c", "--config",
        nargs="?",
        default="../configs/jamming_config.yaml",
    )
    return parser.parse_args()


def main():
    """Start the script."""
    args = parse_arguments()
    config = parse_config(args.config)


if __name__ == "__main__":
    main()
