Feature: Match event tagging
  As a match analyst
  I want to tag match events
  So that events are parsed and validated correctly

  Scenario: Successfully tag a valid scoring event
    Given the application is running
    When I enter the event "sg10"
    Then the event should be recorded as a shot with an outcome of goal
    And the player number should be 10

  Scenario: Successfully tag a valid point event
    Given the application is running
    When I enter the event "sp7"
    Then the event should be recorded as a shot with an outcome of point
    And the player number should be 7

  Scenario: Reject an invalid event code
    Given the application is running
    When I enter the event "X99"
    Then an error should be returned

  Scenario: Reject an invalid player number
    Given the application is running
    When I enter the event "G99"
    Then an error should be returned
