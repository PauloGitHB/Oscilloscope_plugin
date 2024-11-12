from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

import os
import re
from nomad.config import config
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.parsing.parser import MatchingParser
from oscilloscope_plugin.schema_packages.schema_package import Instrument, Oscilloscope

configuration = config.get_plugin_entry_point(
    'oscilloscope_plugin.parsers:parser_entry_point'
)


class OscilloscopeParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info('NewParser.parse', parameter=configuration.parameter)

        archive.workflow2 = Workflow(name='test')


        if not mainfile or not os.path.exists(mainfile):
            return

        with open(mainfile) as file:
            lines = file.readlines()


        instrument = Instrument()

        oscillo = Oscilloscope()

        oscillo.name = lines[0].strip()
        oscillo.Nchannel = int(re.search(r'\d+', lines[2]).group())
        oscillo.bandwidth = float(re.search(r'\d+', lines[3]).group())
        oscillo.Npts = int(re.search(r'[\d.]+', lines[4]).group())

        instrument.instrument = oscillo

        archive.data = instrument

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:

        super().normalize(archive, logger)


