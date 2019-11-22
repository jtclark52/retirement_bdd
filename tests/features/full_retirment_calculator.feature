Feature:  Full Retirement Age Calculator
	As a user,
	I want to be able to compute the full retirement age
	when I enter the year and month of birth

	Scenario Outline: Calculate retirement age using all year boundaries
		Given the "<birth_year>"
		When calculating for retirement age and month
        Then the full retirement age is equal to "<retirement_age>" and "<retirement_month>"

		Examples: Retirement Info
			| birth_year | retirement_age | retirement_month |
			| 1900	     |65		      | 0                |
            | 1901	     |65		      | 0                |
			| 1937	     |65		      | 0                |
			| 1938	     |65		      | 2                |
			| 1939	     |65		      | 4                |
			| 1940	     |65		      | 6                |
			| 1941	     |65		      | 8                |
			| 1942	     |65		      | 10               |
			| 1943	     |66		      | 0                |
			| 1944	     |66		      | 0                |
			| 1950	     |66		      | 0                |
			| 1954	     |66		      | 0                |
			| 1955	     |66		      | 2                |
			| 1956	     |66		      | 4                |
			| 1957	     |66		      | 6                |
			| 1958	     |66		      | 8                |
			| 1959	     |66		      | 10               |
			| 1970	     |67		      | 0                |
			| 2019	     |67		      | 0                |


	Scenario Outline: Gives an exception when invalid year is given
		Given the "<invalid_birth_year>"
        When calculating for retirement age and month
        Then error message should display

        Examples: Retirement Info
			| invalid_birth_year |
			| 1945*              |
			| 0                  |



    Scenario Outline: Gives an exception when year given is before 1900
		Given the "<birth_year>"
		When the birth_year is before 1900
        Then error message should display

        Examples: Retirement Info
			| birth_year |
			| 0          |
			| 1845       |
			| 1899	     |

    Scenario Outline: Gives an exception when year given is after 3000
		Given the "<birth_year>"
		When the birth_year is after 3000
        Then error message should display

        Examples: Retirement Info
			| birth_year |
			| 3001       |
			| 20000      |



	Scenario Outline: Gives an exception when birth_month given is before invalid
		Given the "<birth_year>"  and "<birth_month>"
		When the birth_month is invalid
        Then error message should display

		Examples: Retirement Info
			| birth_year | birth_month  |
			| 1945       |0		        |
			| 2019	     |13     		|




