from classes.Question import Question
from classes.Flow import Flow
from flows.common import grounding_questions, rerouting_questions, body_connection_questions
import i18n

translate = i18n.Translator('data').translate

questions = {
    "questions_list_intro": Question(
        id="questions_list_intro",
        text=translate("questions_list_intro"),
        media="",
        media_type="",
        options={translate("questions_list_intro_1"): "grounding_questions"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_questions": Question(
        id="grounding_questions",
        text=translate("grounding_questions"),
        media="",
        media_type="",
        options={translate("grounding_questions_1"): "grounding_question", translate("rerouting_exc"): "rerouting_exc_1", translate("flow2_exc2"): "flow2_exc2_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

questions = {**questions, **grounding_questions, **rerouting_questions, **body_connection_questions}
# Initialize Flow
questions_list_flow = Flow("questions_list", questions, "questions_list_intro")
