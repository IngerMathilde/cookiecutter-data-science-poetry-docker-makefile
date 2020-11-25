# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
import os


@click.command()
@click.argument('data_dir', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def main(data_dir):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    external_dir = os.path.join(data_dir, "external")
    raw_dir = os.path.join(data_dir, "raw")
    interim_dir = os.path.join(data_dir, "interim")
    processed_dir = os.path.join(data_dir, "processed")


if __name__ == '__main__':


    main()
