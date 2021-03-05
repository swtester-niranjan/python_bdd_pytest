from behave import *

use_step_matcher("re")
basket = 0


def addbasket(count: int):
    """

    :type count: object
    """
    global basket
    if count != 0:
        basket = basket + count
        return basket


@given("the basket has 2 cucumbers")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    addbasket(count = 2)


@when("4 cucumbers are added to the basket")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    addbasket(count = 4)


@then("the basket contains 6 cucumbers")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global basket
    print('cucumbers at present in the basket is ', + basket)
    assert (basket == 6)


@then("i finish")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('i am finished. the total count is ', + basket)
