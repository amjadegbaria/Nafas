import asyncio
from classes.Question import Question
from classes.Flow import Flow
from utils.helpers import timer
from flows.common import intro, stress_question, grounding_questions, psychological_sigh, countdown, stress_question_end, sound_healing, integration_3_intro, task_1

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
        next_question_id="music_exc_1"
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
            translate('lets_continue'): "integration1_1",
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
            translate('lets_continue'): "integration1_1",
            translate('enough_today'): "end_question_response_no_1"},
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
    "integration1_2": Question(
        id="integration1_2",
        text=translate("integration1_2"),
        media="https://www.youtube.com/shorts/oyl4H8lyTvE",
        media_type="youtube",
        options={translate('done'):"task1_1"},
        keyboard_type="inline",
        next_question_id=""
    ),

}

questions = {**intro, **stress_question, **grounding_questions, **psychological_sigh, **countdown, **sound_healing, **stress_question_end, **integration_3_intro, **task_1, **questions}

# Initialize Flow
flow = Flow("flow1", questions, "alt_into")
