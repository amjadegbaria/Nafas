from classes.Question import Question
from classes.Flow import Flow
# from handlers.command_handler import restart_flow
import i18n


translate = i18n.Translator('data').translate

questions = {
    "restart": Question(
        id="restart",
        text=translate("restart_message"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="restart2"
    ),
    "restart2": Question(
        id="restart2",
        text=translate("restart_message"),
        media="",
        media_type="",
        options={'button': 'restart'},
        keyboard_type="inline",
        next_question_id=""
    )
}

RESTART_FLOW = Flow('restart_flow', questions, "restart")