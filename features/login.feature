Feature: Login Functionality

  Background:
    Given I navigate to the Login page


   @login
  Scenario: Login with valid credentials
    When I enter a valid email address and a valid password into the fields
    And I click on the Login button
    Then I should get logged in
   @login


  Scenario: Login with an invalid email and a valid password
    When I enter an invalid email and a valid password into the fields
    And I click on the Login button
    Then I should get a proper warning message


  @login
  Scenario: Login with a valid email and an invalid password
    When I enter a valid email and an invalid password into the fields
    And I click on the Login button
    Then I should get a proper warning message


  @login
  Scenario: Login with invalid credentials
    When I enter an invalid email and an invalid password into the fields
    And I click on the Login button
    Then I should get a proper warning message


  @login
  Scenario: Login without entering any credentials
    When I don't enter anything into the email and password fields
    And I click on the Login button
    Then I should get a proper warning message