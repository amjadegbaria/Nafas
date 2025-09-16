from classes.Question import Question
from classes.Flow import Flow
import i18n
from flows.common import stress_question, main_acknowledgement_question, grounding_questions, breath_exc_2, emotion_release, stress_question_end, sound_healing, rerouting_questions, integration_2, task_2, feedback


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
        next_question_id="breath2_exc_1"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={translate('OK'):"breath2_exc_1"},
        keyboard_type="inline",
        next_question_id=""
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
        options={translate('done'): "stage3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://youtu.be/FX_Qv96_x2c?si=6A4gHDP--P09UOy2",
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
            translate('ready'):"stage4",
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
            translate('OK'): "integration2"
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
                 translate("stress_response_low_transition2"): 'integration2'},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_7": Question(
        id="integration2_7",
        text=translate("integration2_7"),
        media="",
        media_type="",
        options={translate('OK'): "task2_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task2_8": Question(
        id="task2_8",
        text=translate("task2_8"),
        media="https://www.youtube.com/watch?v=qhcBjSirMss",
        media_type="youtube",
        options={},
        keyboard_type="",
        next_question_id="feedback_1"
    ),
}

questions = {**main_acknowledgement_question, **stress_question, **grounding_questions, **breath_exc_2, **rerouting_questions, **sound_healing,**emotion_release, **stress_question_end, **integration_2, **task_2, **feedback, **questions}

# Initialize Flow
flow = Flow("flow2", questions, "alt_into")




