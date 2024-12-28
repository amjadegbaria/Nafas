from classes.Question import Question
from classes.Flow import Flow
from flows.common import grounding_questions, rerouting_questions, body_connection_questions, psychological_sigh, breath_exc_2, breath_exc_3, integration_2, integration_3, task_2, task_3, anger_exc
import i18n

translate = i18n.Translator('data').translate

questions = {
    "questions_list_intro": Question(
        id="questions_list_intro",
        text=translate("questions_list_intro"),
        media="",
        media_type="",
        options={translate("questions_list_intro_1"): "grounding_questions",
                 translate("questions_list_intro_2"):"stress_reduction_questions",
                 translate("questions_list_intro_3"): "integration_questions",
                 translate("questions_list_intro_4"): "tasks_questions"},
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
    "stress_reduction_questions": Question(
        id="stress_reduction_questions",
        text=translate("stress_reduction_questions"),
        media="",
        media_type="",
        options={translate("stress_reduction_questions_1"): "breath_exc_1", translate("stress_reduction_questions_2"): "breath2_exc_1", translate("stress_reduction_questions_3"): "breath3_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration_questions": Question(
        id="integration_questions",
        text=translate("integration1_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration_questions_1"
    ),
    "integration_questions_1": Question(
        id="integration_questions_1",
        text=translate("integration1_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration_questions_2"
    ),
    "integration_questions_2": Question(
        id="integration_questions_2",
        text=translate("integration_questions_2"),
        media="",
        media_type="",
        options={
            translate("integration_questions_3"): "integration2",
            translate("integration_questions_4"): "integration3_1",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "tasks_questions": Question(
        id="tasks_questions",
        text=translate("tasks_questions"),
        media="",
        media_type="",
        options={
            translate("tasks_questions_1"): "task2_1",
            translate("tasks_questions_2"): "task3_1",
            translate("silent_anger"): "anger_exc_1"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
}

questions = {**questions, **grounding_questions, **rerouting_questions, **body_connection_questions, **psychological_sigh,
             **breath_exc_2, **breath_exc_3, **integration_2, **integration_3, **task_2, **task_3, **anger_exc}
# Initialize Flow
questions_list_flow = Flow("questions_list", questions, "questions_list_intro")
