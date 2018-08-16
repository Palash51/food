"""configures food with basic user groups, users and permissions"""
from init import (
    # functions
    add_group,
    add_user,
    add_user_to_group,
    add_group_permissions_for_models,
    # constants
    ADD_COOK,
    ADD_FOOD_IN_CATEGORY,
    COOK_REVIEW,
    FOOD_REVIEW,
    RESTAURANT_REVIEW,
    ORDER_FOOD,
)

if __name__ == '__main__':
    # create an restaurant admins group having full permissions
    add_group('admins', [
        ADD_COOK,
        ADD_FOOD_IN_CATEGORY,
        COOK_REVIEW,
        FOOD_REVIEW,
        RESTAURANT_REVIEW,
        ORDER_FOOD,
    ])

    add_group('restaurant_owner', [
        ADD_COOK,
        ADD_FOOD_IN_CATEGORY,
        COOK_REVIEW,
        FOOD_REVIEW,
        ORDER_FOOD,
    ])

    add_group('restaurant_manager', [
        ADD_COOK,
        ADD_FOOD_IN_CATEGORY,
        COOK_REVIEW,

    ])

    add_group('regular_users', [
        COOK_REVIEW,
        FOOD_REVIEW,
        RESTAURANT_REVIEW,
        ORDER_FOOD,
    ])

    model_names = [
        'session',
        'products',
        'category',
        'items',

        'cook',  # app name

        # model names
        'vacancy',
    ]

    add_group_permissions_for_models('admins', model_names)
    add_group_permissions_for_models('restaurant_owner', model_names)
    add_group_permissions_for_models('restaurant_manager', model_names)
    #add_group_permissions_for_models('general_managers', model_names)
    add_group_permissions_for_models('regular_users', model_names)

    # create admin
    admin_user = add_user('admin')
    add_user_to_group('admin', 'admins')

    print('configured')
