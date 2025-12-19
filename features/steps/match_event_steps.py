from app.utils import delete_event
from app.stats_tagger import parse_event, get_event, get_event_rules, validate_event, get_outcome, get_player_no
from behave import given, when, then

@given('the application is running')
def step_app_running(context):
    context.result = None
    context.error = None


@when('I enter the event "{event_code}"')
def step_enter_event(context, event_code):
    try:
        # Example: adapt this to your real function
        context.result = parse_event(event_code)
    except Exception as e:
        context.error = e


@then('the event should be recorded as a shot with an outcome of goal')
def step_goal(context):
    assert context.result[0] =='shot'
    assert context.result[1] == 'goal'


@then('the event should be recorded as a shot with an outcome of point')
def step_point(context):
    assert context.result[1] == 'point'


@then('the player number should be {player:d}')
def step_player_number(context, player):
    assert context.result[2] == str(player)


@then('an error should be returned')
def step_error(context):
    assert context.result is None
