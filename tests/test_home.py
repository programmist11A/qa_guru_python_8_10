from home_8_10.page.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_student_registration_form():
    # GIVEN
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Anton')
    registration_page.fill_last_name('Fomin')
    registration_page.fill_email('catman@mail.ru')
    registration_page.choose_a_gender()
    registration_page.fill_telephone_number('9694840725')
    registration_page.choose_date_of_birth(month='2', year='90', day='019')
    registration_page.choose_a_subject('Computer Science')
    registration_page.choose_a_hobby()
    registration_page.add_picture('sun.jpg')
    registration_page.type_current_address('Krasnodar')
    registration_page.choose_state('NCR')
    registration_page.choose_city('Delhi')
    registration_page.submit_form()

    # THEN
    registration_page.student_should_by_reg(
        'Anton Fomin',
        'catman@mail.ru',
        'Other',
        '9694840725',
        '19 February,1989',
        'Computer Science',
        'Sports, Reading',
        'sun.jpg',
        'Krasnodar',
        'NCR Delhi')
