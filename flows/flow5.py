from classes.Question import Question
from classes.Flow import Flow
from flows.common import stress_question,main_acknowledgement_question, grounding_questions, box_breathing, stress_question_end, sound_healing, half_salamander, task_5

import i18n


translate = i18n.Translator('data').translate

questions = {
    "alt_into": Question(
        id="alt_into",
        text=translate("alt_into"),
        media="",
        media_type="",
        options={translate("alt_into_option1"): "acknowledgement_1", translate("alt_into_option2"): "task5_1"},
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
        next_question_id="box_breathing_1"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={translate('OK'): "box_breathing_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "box_breathing_6": Question(
        id="box_breathing_6",
        text=translate("box_breathing_6"),
        media="",
        media_type="",
        options={translate("done"): "box_breathing_7"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "box_breathing_7": Question(
        id="color_breathing_7",
        text=translate("grounding_result_1_yes"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="half_salamander_1"
    ),
    "half_salamander_9": Question(
        id="half_salamander_9",
        text=translate("half_salamander_9"),
        media="",
        media_type="",
        options={translate("yes"): "music_exc_1", translate("no"): "music_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://www.youtube.com/watch?v=yLeSALiL678&list=OLAK5uy_lBLi4hCNijjVXo0gQrr0WaeTNLrrczgUI&index=6",
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
            translate('lets_continue'): "task5_1",
            translate('enough_today'): "end_question_response_no_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress_low": Question(
        id="stress_low",
        text=translate("stress_low"),
        media="",
        media_type="",
        options={
            translate('lets_continue'): "task5_1",
            translate('enough_today'): "end_question_response_no_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}
questions = {**main_acknowledgement_question, **stress_question, **grounding_questions, **box_breathing, **half_salamander, **sound_healing, **stress_question_end, **task_5, **questions}

# Initialize Flow
flow = Flow("flow5", questions, "alt_into")
