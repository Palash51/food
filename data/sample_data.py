"""configures cook app with development sample data"""
# flake8: noqa E501

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

    # vacant positions (do not fill by employees)
    accountant_position = Position.objects.create(name='accountant')
    delivery_position = Position.objects.create(name='delivery_boy')
    marketing_position = Position.objects.create(name='marketing_position')
    receptionist_position = Position.objects.create(name='receptionist')

    
    Cook.objects.create(name='Nicole Jackson', email='NicoleJackson@gmail.com', information='')
    Cook.objects.create(name='Stephanie Wong', email='StephanieWong@gmail.com', information='')
    Cook.objects.create(name='Tamara Johnson', email='TamaraJohnson@gmail.com', information='')
    Cook.objects.create(name='Luke Meyer', email='LukeMeyer@gmail.com', information='')
    Cook.objects.create(name='Ruby Valdez', email='RubyValdez@gmail.com', information='')
    Cook.objects.create(name='Sonia Gill', email='SoniaGill@gmail.com', information='')
    Cook.objects.create(name='Randal Mccarthy', email='RandalMccarthy@gmail.com', information='')
    Cook.objects.create(name='Lela Mckenzie', email='LelaMckenzie@gmail.com', information='')
    Cook.objects.create(name='Tomas Cox', email='TomasCox@gmail.com', information='')
    Cook.objects.create(name='Lucy Harrison', email='LucyHarrison@gmail.com', information='')
    Cook.objects.create(name='Jack Cook', email='JackCook@gmail.com', information='')
    Cook.objects.create(name='Charlotte Hardy', email='CharlotteHardy@gmail.com', information='')
    Cook.objects.create(name='Clay Parsons', email='ClayParsons@gmail.com', information='')
    Cook.objects.create(name='Kevin Wheeler', email='KevinWheeler@gmail.com', information='')
    Cook.objects.create(name='Angelo Crawford', email='AngeloCrawford@gmail.com', information='')
    Cook.objects.create(name='Marion Bass', email='MarionBass@gmail.com', information='')
    Cook.objects.create(name='Jennifer Rose', email='JenniferRose@gmail.com', information='')
    Cook.objects.create(name='Natasha Harvey', email='NatashaHarvey@gmail.com', information='')
    Cook.objects.create(name='Grant Nguyen', email='GrantNguyen@gmail.com', information='')
    Cook.objects.create(name='Abel Palmer', email='AbelPalmer@gmail.com', information='')

    sarvana_bhavan_owner_employee = Employee.objects.create(name='sb_owner', email='g@x.com', user=sarvana_bhavan_owner_user)
    sarvana_bhavan_manager_employee = Employee.objects.create(name='sb_manager', email='ghr1@x.com', user=sarvana_bhavan_manager_user)
    sarvana_bhavan_marketer_employee = Employee.objects.create(name='sb_marketer', email='g@x.com', user=sarvana_bhavan_marketer_user)

    sarvana_bhavan_owner_employment = Employment.objects.create(businessunit=sarvana, employee=sarvana_bhavan_owner_employee, position=sarvana_owner_position)
    sarvana_bhavan_manager_employment = Employment.objects.create(businessunit=sarvana, employee=sarvana_bhavan_manager_employee, position=sarvana_manager_position, parent=sarvana_bhavan_owner_employment)
    sarvana_bhavan_marketer_employment = Employment.objects.create(businessunit=sarvana, employee=sarvana_bhavan_marketer_employee, position=sarvana_manager_position, parent=sarvana_bhavan_owner_employment)

    print('sample data added')
