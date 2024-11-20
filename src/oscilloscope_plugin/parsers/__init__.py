from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field
import re


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from oscilloscope_plugin.parsers.parser import OscilloscopeParser

        return OscilloscopeParser(**self.dict())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re = r"^oscilloscope.*\.txt$",
)

