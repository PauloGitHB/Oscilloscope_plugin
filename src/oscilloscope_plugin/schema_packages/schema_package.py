from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:

    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage, SubSection
from nomad.datamodel.metainfo.basesections import Instrument as Nomad_Instrument, InstrumentReference
from nomad.datamodel.datamodel import (
        EntryArchive,
        EntryData
    )
configuration = config.get_plugin_entry_point(
    'oscilloscope_plugin.schema_packages:schema_package_entry_point'
)

m_package = SchemaPackage()


class Oscilloscope(Nomad_Instrument,EntryArchive,EntryData):
    name = Quantity(
        type=str,
        description = ""
    )

    Nchannel = Quantity(
        type = int,
        description = ""
    )

    bandwidth = Quantity(
        type = float,
        description = ""
    )

    Npts = Quantity(
        type = int,
        description = ""
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)



class Instrument(EntryArchive,EntryData):

    instrument = SubSection(
        section_def = Oscilloscope,
        description = "",
        repeats = False
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
