import pytest
from morse import *

@pytest.mark.parametrize('message, exp', [
    ('SOS', '... --- ...'),
    ('MAI-PYTHON-2019','-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'),
    ('AVITO', '.- ...- .. - ---')
])
def test_encode(message: str, exp: str):
    assert encode(message) == exp
