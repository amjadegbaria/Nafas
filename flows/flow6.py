from classes.Question import Question
from classes.Flow import Flow
from flows.common import stress_question, main_acknowledgement_question, grounding_questions, rerouting_questions2, stress_question_end, sound_healing, breath_exc_478, negative_belief_stories
import i18n


translate = i18n.Translator('data').translate


questions = {
    "alt_into": Question(
        id="alt_into",
        text=translate("alt_into"),
        media="",
        media_type="",
        options={translate("alt_into_option1"): "main_acknowledgement_1", translate("alt_into_option2"): "music_healing_1"},
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
        next_question_id="rerouting_exc2"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={translate('OK'): "rerouting_exc2"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc2_7": Question(
        id="rerouting_exc2_7",
        text=translate("rerouting_exc2_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="rerouting_exc2_8"
    ),
    "rerouting_exc2_8": Question(
        id="rerouting_exc2_8",
        text=translate("grounding_result_1_yes"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath_exc_478_1"
    ),
    "breath_exc_478_5": Question(
        id="breath_exc_478_5",
        text=translate("breath_exc_478_5"),
        media="",
        media_type="",
        options={translate('done'): "music_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://www.youtube.com/watch?v=FX_Qv96_x2c&list=OLAK5uy_lBLi4hCNijjVXo0gQrr0WaeTNLrrczgUI&index=7",
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
            translate('lets_continue'): "task6_1",
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
            translate('lets_continue'): "task6_1",
            translate('enough_today'): "end_question_response_no_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}
questions = {**main_acknowledgement_question, **stress_question, **grounding_questions, **rerouting_questions2, **breath_exc_478, **sound_healing, **stress_question_end, **negative_belief_stories, **questions}

# Initialize Flow
flow = Flow("flow6", questions, "alt_into")
