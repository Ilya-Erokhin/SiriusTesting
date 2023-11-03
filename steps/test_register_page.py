from behave import *
from pages.RegisterPage import RegisterPage


# Lang Switcher
@when('I click Lang Switcher Button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.select_lang_switcher_button()

@then('I choose English language from a list')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.choose_eng_lang()

@then('I can see Translated English Page')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.translated_page_text_is_displayed()

@given('I am on the Register Page')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.driver.get(context.register_page.base_url)

# Last Name
@then('I type "{text}" into the last name field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_lats_name_field(text)


# First Name
@then('I type "{text}" into the name field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_first_name_field(text)

# Patronymic
@then('I type "{text}" into the Patronymic field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_patronymic_field(text)

# Email
@then('I type "{email}" into the Email field')
def step_impl(context, email):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_email_field(email)

@when('I input Invalid data in Email Field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_email_field('illyaerokhin')

@then('I can see the Error Message under Email Field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.check_message_incorrect_email()

# Seam Login
@then('I type "{text}" into Seam Login field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_seam_login_field(text)

# Phone
@then('I type "{text}" into the Phone field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_phone_field(text)

# Date
@then('I type "{date}" into the Date field')
def step_impl(context, date):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_digits_into_date_field(date)

# Insurance SNILS
@then('I type "{text}" into the SNILS field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_snils_field(text)

@then('I type Incorrect data Eleven digits into a SNILS Field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_seam_login_field('1234567891011')

@then('I can see the Error Message under SNILS Field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.message_incorrect_seam_login()

@then('I can see the Error Message 11 Digits under SNILS Field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.snils_error_message_eleven_digits()

@then('I can see the Error Message Only Digits under SNILS Field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.snils_error_message_only_digits()

# Profession
@then('I type "{text}" into the Profession field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_profession_field(text)

# Country
@then('I select Country Field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.select_country_field()

@then('I can see the List of Countries field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.list_country_is_displayed()

@then('I choose Россия "{country}" from country list')
def step_impl(context, country):
    context.register_page = RegisterPage(context.driver)
    context.register_page.select_and_choose_country_from_dropdown(country)

# City
@then('I type "{text}" into the City field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_city_field(text)

# Name Of Company
@then('I type "{text}" into the Name of company field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_name_of_company_field(text)

# School
@then('I type "{text}" into the School field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_school_field(text)

# Class
@then('I type "{text}" into the Class field')
def step_impl(context, text):
    context.register_page = RegisterPage(context.driver)
    context.register_page.input_text_into_class_field(text)

# Chose Mail Olympic
@then('I choose Main Olympic')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.select_main_olympic()

# Chose Additional Olympic
@then('I choose Additional Olympic')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.select_additional_olympic()

# Press Agreement Button
@then('I press Agreement Button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_confirm_checkbox()

# Press Agree with Personal Data Button
@then('I press Agree with Personal Data Button')

def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_user_agreement_personal_data()

# Press Read the Rules Button
@then('I press I Read Rules Button')

def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_read_rules()

# Button Go to Testing
@then('I click Go to Testing button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_button_go_to_testing()

@then('Ensure the button Go to Testing is disabled')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    is_button_disabled = context.register_page.check_disabled_button()
    context.register_page.driver.quit()

    assert is_button_disabled, 'Кнопка "Перейти к Тестированию" НЕ заблокирована'

@then('Ensure the button Go to Testing is enabled')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    is_button_disabled = context.register_page.check_enabled_button()

    assert is_button_disabled, 'Кнопка "Перейти к Тестированию" Заблокирована'

# Confirmation Page
@then('I can see the Confirmation Page')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.confirm_page_is_displayed()
