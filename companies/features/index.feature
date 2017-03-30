Feature: Adding a company

    Scenario: Adding a company with a good abn works
        Given I access the url "/create/"
        Then I see the content "Create a new Company"
        When I create the company "TestCompanyOne" with ABN "12345678901"
        Then I see the content "Record successfully created"

    Scenario: Adding a company with no abn works
        Given I access the url "/create/"
        Then I see the content "Create a new Company"
        When I create the company "Test Company Two" with ABN ""
        Then I see the content "Record successfully created"

    Scenario: Adding a company with bad abn fails
        Given I access the url "/create/"
        Then I see the content "Create a new Company"
        When I create the company "Test Company Three" with ABN "1"
        Then I do not see the content "Record successfully created"

