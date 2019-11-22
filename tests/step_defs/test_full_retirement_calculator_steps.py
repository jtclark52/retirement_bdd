from pytest_bdd import scenarios, parsers, given, when, then
import pytest
from tests.full_retirement_calculator import full_retirement_date

# EXTRA_TYPES = {
#
# }
#
# CONVERTERS = {
#
# }

scenarios('Calculate retirement age using all year boundaries',"<birth_year>")
@given(parsers.cfparse('Please enter year of birth', "<birth_year>"))
@given('the "<birth_year>"')
def calculate_retirement_age(birth_year, retire_age, retire_month):
    return full_retirement_date(retire_age, retire_month)

@when(parsers.cfparse('"{some:"<birth_year>"}" are provided by the user'))
@when('"<some>" are provided by the user')
def test_calculate_retirement_age(birth_year, retire_age, retire_month):
    assert full_retirement_date.calculate_retirement_age(birth_year) == (retire_age, retire_month)


scenarios('Gives an exception when invalid year is given',"<invalid_birth_year>")

@given(parsers.cfparse('Please enter year of birth', "<Invalid_birth_year>"))
@given('the "<invalid_birth_year>"')
def calculate_retirement_age(birth_year, retire_age, retire_month):
    return full_retirement_date(retire_age, retire_month)

@when(parsers.cfparse('"{some:"<invalid_birth_year>"}" are provided by the user'))
@when('"<some>" are provided by the user')
def test_negative_calculate_retirement_age(birth_year, retire_age, retire_month):
    with pytest.raises(AssertionError): assert full_retirement_date.calculate_retirement_age(birth_year) == (retire_age, retire_month)


scenarios('Gives an exception when year given is before 1900',"<birth_year>")

@given(parsers.cfparse('Please enter year of birth', "<birth_year>"))
@given('the "<birth_year>"')
def calculate_retirement_age(birth_year, retire_age, retire_month):
    return full_retirement_date(retire_age, retire_month)

@when(parsers.cfparse('"{some:"<birth_year>"}" are provided by the user'))
@when('"<some>" are provided by the user')
def test_outofrange_0_calculate_retirement_age(birth_year, retire_age, retire_month):
    with pytest.raises(ValueError, match='Birth year must be no earlier than 1900'):
        assert full_retirement_date.calculate_retirement_age(birth_year) == (retire_age, retire_month)


scenarios('Gives an exception when year given is after 3000', "<birth_year>")

@given(parsers.cfparse('Please enter year of birth', "<birth_year>"))
@given('the "<birth_year>"')
def calculate_retirement_age(birth_year, retire_age, retire_month):
    return full_retirement_date(retire_age, retire_month)

@when(parsers.cfparse('"{some:"<birth_year>"}" are provided by the user'))
@when('"<some>" are provided by the user')
def test_outofrange_1_calculate_retirement_age(birth_year, retire_age, retire_month):
    with pytest.raises(ValueError, match='Birth year must be earlier than 3000'):
        assert full_retirement_date.calculate_retirement_age(birth_year) == (retire_age, retire_month)


scenarios('Gives an exception when birth_month given is before invalid', "<birth_year>", "<birth_month>")

@given(parsers.cfparse('Please enter year of birth and month of birth', "<birth_year>", "<birth_month>"))
@given('the "<birth_year>", , "<birth_month>"')
def calculate_retirement_age(birth_year, birth_month, retire_age, retire_month):
    return full_retirement_date(retire_age, retire_month)

@when(parsers.cfparse('"<birth_year>"}" and "<birth_month>" are provided by the user'))
@when('"<birth_year>"}" and "<birth_month>" are provided by the user')
def test_validate_birth_month(birth_y, birth_m, age_y, age_m, retire_y, retire_m):
    with pytest.raises(ValueError, match='Birth month "13" must be between 1 and 12'):
        assert full_retirement_date.calculate_retirement_date(birth_y, birth_m, age_y, age_m)== (retire_y, retire_m)
