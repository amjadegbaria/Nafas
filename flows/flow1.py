import asyncio
from classes.Question import Question
from classes.Flow import Flow
from utils.helpers import timer
from flows.common import intro, main_acknowledgement_question, stress_question, grounding_questions, psychological_sigh, countdown, emotion_release, stress_question_end, sound_healing, integration_3_intro, task_1

import i18n

translate = i18n.Translator('data').translate
async def timer_30(update, context):
    seconds = 30
    asyncio.create_task(timer(update, seconds))
    return True

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
        next_question_id="breath_exc_1"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={translate("lets_continue"):"breath_exc_1", translate("repeat"): "grounding_result_repeat"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_result_repeat": Question(
        id="grounding_result_repeat",
        text=translate("grounding_result_repeat"),
        media="",
        media_type="",
        options={translate('done'):"grounding_result_1_yes"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath_exc_4": Question(
        id="breath_exc_4",
        text=translate("breath_exc_4"),
        media="",
        media_type="",
        options={translate('done'): "countdown_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "countdown_exc_4": Question(
        id="countdown_exc_4",
        text=translate("countdown_exc_4"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="stage3"
    ),
    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://www.youtube.com/watch?v=UfcAVejslrU",
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
            # translate('stress_still_high_option2'): restart_flow,
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
            translate('ready'): "stage4"
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
            translate('OK'): "integration1_1"
        },
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
    "integration1_3": Question(
        id="integration1_3",
        text=translate("integration1_3"),
        media="",
        media_type="",
        options={
            translate('integration1_3_yes'):"integration1_3_yes_answer",
            translate('integration1_3_no'): "task1_1"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration1_3_yes_answer": Question(
        id="integration1_3_yes_answer",
        text=translate("integration1_3_yes_answer"),
        media="",
        media_type="",
        options={
            translate('OK'): "task1_1"
        },
        keyboard_type="inline",
        next_question_id=""
    ),


}

questions = {**intro,**main_acknowledgement_question, **stress_question, **grounding_questions, **psychological_sigh, **countdown, **sound_healing,**emotion_release, **stress_question_end, **integration_3_intro, **task_1, **questions}

# Initialize Flow
flow = Flow("flow1", questions, "alt_into")
