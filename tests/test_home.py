from home_8_10.page.registration_page import RegistrationPage
from home_8_10.data.users import User

registration_page = RegistrationPage()


def test_student_registration_form():
    # GIVEN
    student = User(first_name='Anton', last_name='Fomin', email='catman@mail.ru', gender='Other',
                   phone_number='9694840725',
                   month_of_brith='2', year_of_brith='89', day_of_brith='019', subject='Computer Science',
                   hobby='Sports, Reading', picture='sun.jpg',
                   current_address='Krasnodar', state='NCR',
                   city='Delhi')
    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.student_should_by_registred(student)
