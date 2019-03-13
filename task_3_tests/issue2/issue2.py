import pytest
from morse import decode

@pytest.mark.parametrize('message, exp', [
    ('... --- ...', 'SOS'),
    ('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.',\
    'MAI-PYTHON-2019'),
    ('.- ...- .. - ---', 'AVITO')
])
def test_decode(message: str, exp: str):
    assert decode(message) == exp
