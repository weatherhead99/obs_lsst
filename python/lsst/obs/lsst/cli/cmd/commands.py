# This file is part of obs_lsst.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import click

from lsst.daf.butler.cli.opt import (
    config_option,
    config_file_option,
    locations_argument,
    options_file_option,
    repo_argument,
    regex_option,
    run_option,
    transfer_option,
)
from lsst.pipe.base.cli.opt import instrument_argument
from lsst.daf.butler.cli.utils import ButlerCommand
from ... import script


defaultRegex = r".*Photodiode_Readings.*txt\b"


@click.command(cls=ButlerCommand, short_help="Ingest photodiode data.")
@repo_argument(required=True)
@instrument_argument(required=True, help="INSTRUMENT is the name of the instrument to use.")
@locations_argument(help="LOCATIONS specifies files to ingest and/or locations to search for files.",
                    required=True)
@regex_option(default=defaultRegex,
              help="Regex string used to find photodiode data in directories listed in LOCATIONS. "
              f"Defaults to {defaultRegex}")
@config_option(metavar="TEXT=TEXT", multiple=True)
@config_file_option(type=click.Path(exists=True, writable=False, file_okay=True, dir_okay=False))
@run_option(required=False)
@transfer_option(default="copy")
@click.option(
    "--track-file-attrs/--no-track-file-attrs",
    default=True,
    help="Indicate to the datastore whether file attributes such as file size"
    " or checksum should be tracked or not. Whether this parameter is honored"
    " depends on the specific datastore implentation.",
)
@options_file_option()
def ingest_photodiode(*args, **kwargs):
    """Ingest photodiode data from a directory into the butler registry."""
    script.ingestPhotodiode(*args, **kwargs)
