


  Feature: Search functionality

  Background:
    Given I navigate to the Home page


    @implemented
    Scenario: Search for a valid product
    When I enter a valid product into the search box
    And I click on the Search button
    Then the valid product should be displayed in the search results


    @implemented
    Scenario: Search for an invalid product
    When I enter an invalid product into the search box
    And I click on the Search button
    Then a proper message should be displayed in the search results



    @implemented
    Scenario: Search without entering any product
    When I don't enter anything into the search box
    And I click on the Search button
    Then a "not found" message should be shown
