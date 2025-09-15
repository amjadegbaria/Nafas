from classes.Question import Question
from classes.Flow import Flow
from flows.common import stress_question,main_acknowledgement_question, grounding_questions, color_breathing, stress_question_end, sound_healing, vagus_nerve_stim, task_4, emotion_release, feedback

import i18n


translate = i18n.Translator('data').translate

questions = {
    "alt_into": Question(
        id="alt_into",
        text=translate("alt_into"),
        media="",
        media_type="",
        options={translate("alt_into_option1"): "stage1", translate("alt_into_option2"): "stage4"},
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
        next_question_id="color_breathing_1"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={translate('OK'): "color_breathing_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "color_breathing_6": Question(
        id="color_breathing_6",
        text=translate("color_breathing_6"),
        media="",
        media_type="",
        options={translate("done"): "color_breathing_7"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "color_breathing_7": Question(
        id="color_breathing_7",
        text=translate("grounding_result_1_yes"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="vagus_nerve_stim_1"
    ),
    "vagus_nerve_stim_7": Question(
        id="vagus_nerve_stim_7",
        text=translate("vagus_nerve_stim_7"),
        media="",
        media_type="",
        options={translate("yes"): "stage3", translate("no"): "stage3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://www.youtube.com/watch?v=XoZDqw7ahWU&list=OLAK5uy_lBLi4hCNijjVXo0gQrr0WaeTNLrrczgUI&index=4",
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
            translate('stress_still_high_option3'): "stage4",
            translate('stress_still_high_option1'): "emotion_release_1"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress_low": Question(
        id="stress_low",
        text=translate("stress_low"),
        media="",
        media_type="",
        options={
            translate('ready'): "stage4",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "stage4": Question(
        id="stage4",
        text=translate("stage4"),
        media="media/stage4.png",
        media_type="image",
        options={
            translate('OK'): "task4_1"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress1_3": Question(
        id="stress1_3",
        text=translate("stress_response_low"),
        media="",
        media_type="",
        options={translate("stress_response_low_transition1"): 'grounding_question',
                 translate("stress_response_low_transition2"): 'task4_1'},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task4_4": Question(
        id="task4_4",
        text=translate("task4_4"),
        media="",
        media_type="",
        options={
            translate('running'):"feedback_1",
            translate('walking'): "feedback_1",
            translate('dancing'): "feedback_1",
            translate('weight_lifting'): "feedback_1",
            translate('other'): "feedback_1",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
}
questions = {**main_acknowledgement_question, **stress_question, **grounding_questions, **color_breathing, **vagus_nerve_stim, **sound_healing, **stress_question_end, **task_4, **emotion_release, **feedback, **questions}

# Initialize Flow
flow = Flow("flow4", questions, "alt_into")
