import os

from selene import browser, have


def test_web():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Anton')
    browser.element('#lastName').type('Fomin')
    browser.element('#userEmail').type('catman@mail.ru')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('9694840725')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select").click().element('option[value="1"]').click()
    browser.element(".react-datepicker__year-select").click().element('[value="1989"]').click()
    browser.element(".react-datepicker__day--019").click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/sun.jpg'))
    browser.element('#currentAddress').type('Krasnodar')
    browser.element('#react-select-3-input').type('NCR').click().press_enter()
    browser.element('#react-select-4-input').type('Delhi').click().press_enter()
    browser.element("#submit").press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks for submitting the form"))
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
        'Anton Fomin',
        'catman@mail.ru',
        'Other',
        '9694840725',
        '19 February,1989',
        'Computer Science',
        'Sports, Reading',
        'sun.jpg',
        'Krasnodar',
        'NCR Delhi'))

