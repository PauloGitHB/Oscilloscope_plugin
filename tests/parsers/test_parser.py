import logging

from nomad.datamodel import EntryArchive

from oscilloscope_plugin.parsers.parser import OscilloscopeParser


def test_parse_file():
    parser = OscilloscopeParser()
    archive = EntryArchive()
    parser.parse('tests/data/example.out', archive, logging.getLogger())

    assert archive.workflow2.name == 'test'
