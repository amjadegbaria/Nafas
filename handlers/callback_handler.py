from telegram import Update
from telegram.ext import CallbackContext
from handlers.flow_handler import trigger_restart_flow
from database.queries import get_user_data
from handlers.flow_handler import check_user_last_interaction, process_question, is_flow_done_today
from handlers.utils import update_user_answer, is_completed, get_next_from_answer, get_user_flow
from utils.helpers import update_already_answered


async def handle_callback_query(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_data = await get_user_data(user_id)

    flow = await get_user_flow(user_id)

    # Check for inactivity and restart flow if necessary
    if flow.id != 'restart_flow' and await check_user_last_interaction(user_data):
        await trigger_restart_flow(update, context)
        return

    # Move to the next question
    question = flow.get_current_question()
    answer = update.callback_query.data

    next_question_id = get_next_from_answer(update, question)

    callback = question.get_options().get(answer)
    if callable(callback):  # If the next question is a callable, execute it
        result = await next_question_id(update, context)

        if not result:  ## if next question id is not provided, stop the flow
            return
        else:
            next_question_id = question.next_question_id

    update_already_answered(user_id, question, answer)
    # Update flow progress
    await update_user_answer(update)
    await is_completed(flow, user_id)  # Check if flow is completed

    flow.move_to_next_question(next_question_id)
    await process_question(update, context, flow)