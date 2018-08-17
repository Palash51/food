"""configures cook app with development sample data"""


from init import (
    add_user,
    add_user_to_group,
)
from account.models import BusinessUnit, Employee, Employment, Position
from cook.models import Vacancy, Cook


if __name__ == '__main__':
    # create managers
    sarvana_bhavan_owner_user = add_user('sb_owner')
    add_user_to_group('sb_owner', 'restaurant_owner')
    sarvana_bhavan_manager_user = add_user('sb_manager')
    add_user_to_group('sb_manager', 'restaurant_manager')
    sarvana_bhavan_marketer_user = add_user('sb_marketer')
    add_user_to_group('sb_marketer', 'restaurant_manager')
    saravana_bhavan_user = add_user('sb_user')
    add_user_to_group('sb_user', 'regular_users')

    sarvana = BusinessUnit.objects.create(name='sarvana')
    sarvana_chennai = BusinessUnit.objects.create(name='sarvana_chennai', parent=sarvana)
    sarvana_mumbai = BusinessUnit.objects.create(name='sarvana_mumbai', parent=sarvana)

    sarvana_owner_position = Position.objects.create(name='restaurant_owner')
    sarvana_manager_position = Position.objects.create(name='restaurant_manager')

    
    accountant_position = Position.objects.create(name='accountant')
    delivery_position = Position.objects.create(name='delivery_boy')
    marketing_position = Position.objects.create(name='marketing_position')
    receptionist_position = Position.objects.create(name='receptionist')

    
    Cook.objects.create(name='John', email='jhon@gmail.com', information='')
    Cook.objects.create(name='moglee', email='moglee@gmail.com', information='')
    Cook.objects.create(name='sherkhan', email='sherkhan@gmail.com', information='')
    Cook.objects.create(name='Ustaad', email='Ustaad@gmail.com', information='')
    Cook.objects.create(name='khatri', email='khatri@gmail.com', information='')
    Cook.objects.create(name='sekhar', email='sekharCook@gmail.com', information='')
    Cook.objects.create(name='Jay', email='Jay@gmail.com', information='')
    Cook.objects.create(name='Jennifer', email='Jennifer@gmail.com', information='')

    sarvana_bhavan_owner_employee = Employee.objects.create(name='sb_owner', email='g@x.com', user=sarvana_bhavan_owner_user)
    sarvana_bhavan_manager_employee = Employee.objects.create(name='sb_manager', email='ghr1@x.com', user=sarvana_bhavan_manager_user)
    sarvana_bhavan_marketer_employee = Employee.objects.create(name='sb_marketer', email='g@x.com', user=sarvana_bhavan_marketer_user)

    sarvana_bhavan_owner_employment = Employment.objects.create(businessunit=sarvana, employee=sarvana_bhavan_owner_employee, position=sarvana_owner_position)
    sarvana_bhavan_manager_employment = Employment.objects.create(businessunit=sarvana, employee=sarvana_bhavan_manager_employee, position=sarvana_manager_position, parent=sarvana_bhavan_owner_employment)
    sarvana_bhavan_marketer_employment = Employment.objects.create(businessunit=sarvana, employee=sarvana_bhavan_marketer_employee, position=sarvana_manager_position, parent=sarvana_bhavan_owner_employment)

    print('sample data added')
