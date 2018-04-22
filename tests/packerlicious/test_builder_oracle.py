import pytest

import packerlicious.builder as builder


class TestOracleClassicBuilder(object):

    def test_required_fields_missing(self):
        b = builder.OracleClassic()

        with pytest.raises(ValueError) as excinfo:
            b.to_dict()
        assert 'required' in str(excinfo.value)


class TestOracleOCIBuilder(object):

    def test_required_fields_missing(self):
        b = builder.OracleOCI()

        with pytest.raises(ValueError) as excinfo:
            b.to_dict()
        assert 'required' in str(excinfo.value)
