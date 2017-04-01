Feature: Adding a company

    Scenario: Adding a company with a good abn works
        Given I access the url "/create/"
        Then I see the content "Create a new Company"
        When I create the company
        | name             | abn         | description | image |
        | Test Company One | 12345678901 |             |       |
        Then I see the content "Record successfully created"

    Scenario: Adding a company with no abn works
        Given I access the url "/create/"
        Then I see the content "Create a new Company"
        When I create the company
        | name             | abn         | description | image |
        | Test Company One |             |             |       |
        Then I see the content "Record successfully created"

    Scenario: Adding a company with bad abn fails
        Given I access the url "/create/"
        Then I see the content "Create a new Company"
        When I create the company
        | name             | abn         | description | image |
        | Test Company One | 1           |             |       |
        Then I do not see the content "Record successfully created"

