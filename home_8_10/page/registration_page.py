from selene import browser, be, have
import os.path
import tests


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.visible).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.visible).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.visible).type(value)

    def choose_a_gender(self):
        browser.element('[for=gender-radio-3]').should(be.visible).click()

    def fill_telephone_number(self, value):
        browser.element('#userNumber').should(be.visible).type(value)

    def choose_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').should(be.visible).click()
        browser.element(f'.react-datepicker__month-select > option:nth-child({month})').should(be.visible).click()
        browser.element('.react-datepicker__year-select').should(be.visible).click()
        browser.element(f'.react-datepicker__year-select > option:nth-child({year})').should(be.visible).click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{day}').should(be.visible).click()

    def choose_a_subject(self, value):
        browser.element('#subjectsInput').should(be.visible).type(value).press_enter()

    def choose_a_hobby(self):
        browser.element('label[for=hobbies-checkbox-1]').should(be.visible).click()
        browser.element('label[for=hobbies-checkbox-2]').should(be.visible).click()

    def add_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), f'picture/{file_name}')))

    def type_current_address(self, value):
        browser.element('#currentAddress').should(be.visible).type(value)

    def choose_state(self, value):
        browser.element("#react-select-3-input").should(be.visible).type(value).press_enter()

    def choose_city(self, value):
        browser.element("#react-select-4-input").should(be.visible).type(value).press_enter()

    def submit_form(self):
        browser.element("#submit").should(be.visible).click()

    def student_should_by_reg(self, full_name, email, gender, phone_number, date_of_birth, subject, hobby,
                              picture, state, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobby,
                picture,
                state,
                city
            ))
