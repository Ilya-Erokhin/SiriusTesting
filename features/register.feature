# Created by illya at 10/30/2023
Feature: Register on Olympic Functionality

  Scenario: Checking that valid data has been entered into all fields and that the necessary checkboxes have been ticked.
    Given I am on the Register Page
    Then I type "Ерохин" into the last name field
    And I type "Илья" into the name field
    And I type "Александрович" into the Patronymic field
    And I type "31052001" into the Date field
    And I type "example@yandex.ru" into the Email field
    And I type "v00.000.000" into Seam Login field
    And I type "+79114093611" into the Phone field
    And I type "16520472650" into the SNILS field
    And I type "QA Engineer" into the Profession field
    And I choose Россия "RU" from country list
    And I type "Санкт-Петербург" into the City field
    And I type "Sirius" into the Name of company field
    And I type "Лицей №1" into the School field
    And I type "1A" into the Class field
    And I select Country Field
    And I press Agree with Personal Data Button
    And I press Agreement Button
    And I press I Read Rules Button
    And Ensure the button Go to Testing is enabled
    And I click Go to Testing button
    And I can see the Confirmation Page


  Scenario: Checking that all fields are required.
    Given I am on the Register Page
    Then Ensure the button Go to Testing is disabled

  Scenario: Email validation check. Entering an incorrect email address.
    Given I am on the Register Page
    When I input Invalid data in Email Field
    Then I can see the Error Message under Email Field


  Scenario: Checking the validation of the "SNILS" field. Entering incorrect values in the "SNILS" field.
    Given I am on the Register Page
    Then I type "31052001" into the Date field
    And I type Incorrect data Eleven digits into a SNILS Field
    And I can see the Error Message under SNILS Field

  Scenario: Checking error messages in the SNILS field
    Given I am on the Register Page
    Then I type "123456789" into the SNILS field
    And I can see the Error Message 11 Digits under SNILS Field
    And I type "ilia" into the SNILS field
    And I can see the Error Message Only Digits under SNILS Field


  Scenario: Checking the letters entered in the phone field.
    Given I am on the Register Page
    Then I type "Телефон" into the Phone field

  Scenario: Checking the selection of the main and additional Olympiads.
    Given I am on the Register Page
    Then I choose Additional Olympic
    And I choose Main Olympic


  Scenario: Checking the required data confirmation, user agreement and “I have read the rules” checkboxes.
    Given I am on the Register Page
    Then I type "Иванов" into the last name field
    And I type "Александр" into the name field
    And I type "Астафьевич" into the Patronymic field
    And I type "31052001" into the Date field
    And I type "example2@yandex.ru" into the Email field
    And I type "v00.000.000" into Seam Login field
    And I type "8911476722" into the Phone field
    And I type "16520472650" into the SNILS field
    And I type "Автомеханик" into the Profession field
    And I choose Россия "RU" from country list
    And I type "Петрозаводск" into the City field
    And I type "Sirius" into the Name of company field
    And I type "Школа42" into the School field
    And I type "9я" into the Class field
    And I select Country Field
    And I press Agree with Personal Data Button
    And Ensure the button Go to Testing is disabled


  Scenario: Checking the button for changing the language from Russian to English.
    Given I am on the Register Page
    When I click Lang Switcher Button
    Then I choose English language from a list
    And I can see Translated English Page