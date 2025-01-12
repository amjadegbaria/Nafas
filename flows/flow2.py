from classes.Question import Question
from classes.Flow import Flow
import i18n
from flows.common import stress_question, grounding_questions, breath_exc_2, stress_question_end, sound_healing, rerouting_questions, integration_2, task_2


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
        next_question_id="breath2_exc_1"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath2_exc_1"
    ),
    "breath2_exc_4": Question(
        id="breath2_exc_4",
        text=translate("breath2_exc_4"),
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
        options={translate("yalla"): "rerouting_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc_11": Question(
        id="rerouting_exc_11",
        text=translate("rerouting_exc_11"),
        media="",
        media_type="",
        options={translate('done'): "music_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://www.youtube.com/watch?v=aS41f-yM4M8&list=OLAK5uy_lBLi4hCNijjVXo0gQrr0WaeTNLrrczgUI&index=3",
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
            translate('lets_continue'):"integration2",
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
            translate('lets_continue'):"integration2",
            translate('enough_today'):"end_question_response_no_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "end_question_response_no_1": Question(
        id="end_question_response_no_1",
        text=translate("end_question_response_no_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="end_question_response_no_2"
    ),
    "end_question_response_no_2": Question(
        id="end_question_response_no_2",
        text=translate("end_question_response_no_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id=""
    ),
    "integration2_7": Question(
        id="integration2_7",
        text=translate("integration2_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task2_1"
    )
}

questions = {**stress_question, **grounding_questions, **breath_exc_2, **rerouting_questions, **sound_healing, **stress_question_end, **integration_2, **task_2, **questions}

# Initialize Flow
flow = Flow("flow2", questions, "alt_into")




