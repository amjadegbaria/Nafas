from classes.Question import Question
from classes.Flow import Flow
import i18n
from flows.common import stress_question, grounding_questions, breath_exc_3, stress_question_end, sound_healing, emotions, task_3

translate = i18n.Translator('data').translate

questions = {
    "alt_into": Question(
        id="alt_into",
        text=translate("alt_into"),
        media="",
        media_type="",
        options={translate("yes_sure"): "stress_question"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_result_1": Question(
        id="grounding_result_1",
        text=translate("grounding_result_1"),
        media="",
        media_type="",
        options={translate("yes"): "grounding_result_1_yes", translate("no"): "grounding_result_1_no"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_result_1_yes": Question(
        id="grounding_result_1_yes",
        text=translate("grounding_result_1_yes"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath3_exc_1"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath3_exc_1"
    ),
    "breath3_exc_9_1": Question(
        id="breath3_exc_9_1",
        text=translate("breath3_exc_2_3"),
        media="",
        media_type="",
        options={translate("done"): "transition_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
     "transition_1": Question(
        id="transition_1",
        text=translate("transition_1"),
        media="",
        media_type="",
        options={translate("yalla"): "music_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://www.youtube.com/watch?v=lt2IBf2R7fU&list=OLAK5uy_lBLi4hCNijjVXo0gQrr0WaeTNLrrczgUI&index=4",
        media_type="youtube",
        options={translate('done'): "stress_question_end"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress_still_high": Question(
        id="stress_still_high",
        text=translate("stress_still_high"),
        media="",
        media_type="",
        options={
            translate('lets_continue'):"emotions_1",
            translate('enough_today'):"end_question_response_no_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress_low": Question(
        id="stress_low",
        text=translate("stress_low"),
        media="",
        media_type="",
        options={
            translate('lets_continue'):"emotions_1",
            translate('enough_today'):"end_question_response_no_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "emotions_12": Question(
        id="emotions_12",
        text=translate("emotions_12"),
        media="",
        media_type="",
        options={translate("done"): "task3_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}


questions = {**stress_question, **grounding_questions, **breath_exc_3, **sound_healing, **stress_question_end, **emotions, **task_3, **questions}


# Initialize Flow
flow = Flow("flow3", questions, "alt_into")
