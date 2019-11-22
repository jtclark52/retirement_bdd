from pytest_bdd import scenarios, parsers, given, when, then

from tests.full_retirement_calculator import full_retirement_date

# EXTRA_TYPES = {
#
# }
#
# CONVERTERS = {
#
# }

scenarios('../features/full_retirment_calculator.feature',"<birth_year>", "<birth_month>")

@given(parsers.cfparse('Please enter month and year of birth', "<birth_year>"))
@given('the "<birth_year>"')
def calculate_retirement_age(birth_year, birth_month, retire_age, retire_month):
    return full_retirement_date(retire_age, retire_month)

@when(parsers.cfparse('"{some:"<birth_year>"}" are provided by the user'))
@when('"<some>" are provided by the user')
def calculate_retirement_age(birth_year, retire_age, retire_month):
    assert full_retirement_date.calculate_retirement_age(birth_year) == (retire_age, retire_month)

