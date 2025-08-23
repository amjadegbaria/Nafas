from classes.Question import Question
from classes.Flow import Flow
from flows.common import stress_question, main_acknowledgement_question, grounding_questions, half_salamander, stress_question_end, sound_healing, psychological_sigh, music_healing
from utils.helpers import get_chat_id
from utils.constants import answered_questions
import i18n

translate = i18n.Translator('data').translate


questions = {
    "alt_into": Question(
        id="alt_into",
        text=translate("alt_into"),
        media="",
        media_type="",
        options={translate("alt_into_option1"): "acknowledgement_1", translate("alt_into_option2"): "task6_1"},
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
        next_question_id="half_salamander_1"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={translate('OK'): "half_salamander_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "half_salamander_9": Question(
        id="half_salamander_9",
        text=translate("half_salamander_9"),
        media="",
        media_type="",
        options={translate("yes"): "breath_exc_1", translate("no"): "breath_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath_exc_4": Question(
        id="breath_exc_4",
        text=translate("breath_exc_4"),
        media="",
        media_type="",
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
            translate('lets_continue'): "music_healing_1",
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
            translate('lets_continue'): "music_healing_1",
            translate('enough_today'): "end_question_response_no_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}
questions = {**main_acknowledgement_question, **stress_question, **grounding_questions, **half_salamander, **psychological_sigh, **sound_healing, **stress_question_end, **music_healing, **questions}

# Initialize Flow
flow = Flow("flow7", questions, "alt_into")
