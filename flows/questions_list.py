from classes.Question import Question
from classes.Flow import Flow
from flows.common import grounding_questions, rerouting_questions, rerouting_questions2, body_connection,\
    psychological_sigh, breath_exc_2, box_breathing, breath_exc_478, color_breathing, negative_belief_stories,\
    breath_exc_3, integration_2, integration_3, task_2, task_3, anger_exc, emotion_release, task_4, task_1, task_5,half_salamander, vagus_nerve_stim
import i18n

translate = i18n.Translator('data').translate

questions = {
    "questions_list_intro": Question(
        id="questions_list_intro",
        text=translate("questions_list_intro"),
        media="",
        media_type="",
        options={
            translate("questions_list_intro_1"): "grounding_questions",
            translate("questions_list_intro_2"):"stress_reduction_questions",
            translate("questions_list_intro_3"): "integration_questions",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_questions": Question(
        id="grounding_questions",
        text=translate("grounding_questions"),
        media="",
        media_type="",
        options={
            translate("grounding_questions_1"): "grounding_question",
            translate("stress_reduction_questions_8"): "half_salamander_1",
            translate("stress_reduction_questions_7"): "vagus_nerve_stim_1",
            translate("rerouting_exc"): "rerouting_exc_1",
            translate("rerouting_exc2_name"): "rerouting_exc2",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress_reduction_questions": Question(
        id="stress_reduction_questions",
        text=translate("stress_reduction_questions"),
        media="",
        media_type="",
        options={
            translate("tasks_questions_2"): "task2_1",
            translate("stress_reduction_questions_1"): "breath_exc_1",
            translate("stress_reduction_questions_3"): "breath3_exc_1",
            translate("stress_reduction_questions_4"): "breath_exc_478_1",
            translate("stress_reduction_questions_5"): "color_breathing_1",
            translate("stress_reduction_questions_6"): "box_breathing_1",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration_questions": Question(
        id="integration_questions",
        text=translate("integration_questions"),
        media="",
        media_type="",
        options={
            translate("emotion_release"): "emotion_release_1",
            translate("silent_anger"): "anger_exc_1",
            translate("tasks_questions_6"): "task6_1",
        },
        keyboard_type="inline",
        next_question_id="integration_questions_1"
    ),
}

questions = {**questions, **grounding_questions, **rerouting_questions, **body_connection, **psychological_sigh,
             **breath_exc_2, **breath_exc_3, **integration_2, **integration_3, **task_2, **task_3, **anger_exc,
             **emotion_release, **rerouting_questions2, **body_connection, **box_breathing,**half_salamander, **vagus_nerve_stim,
             **breath_exc_478, **color_breathing, **negative_belief_stories, **task_4, **task_1, **task_5}
# Initialize Flow
questions_list_flow = Flow("questions_list", questions, "questions_list_intro")
