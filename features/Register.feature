Feature: Register Account Functionality

  Background:
    Given I navigate to the Register page


  @Register
  Scenario: Register with mandatory fields
    When I enter the mandatory fields
    And I select privacy Policy option
    And I click on the Continue button
    Then the account should get created

  @Register
  Scenario: Register with all fields
    When I enter detail into all fields all fields
    And I select Privacy Policy option
    And I click on the Continue button
    Then the account should get created


   @Register
  Scenario: Register with a duplicate email address
    When I enter details into all fields except the email field
    And I enter an existing account's email into the email field
    Then a proper warning message informing about the duplicate account should be displayed


  @Register
  Scenario: Register without providing any details
    When I don't enter anything into the fields
    And I click on the Continue button
    Then proper warning messages for every mandatory field should be displayed
