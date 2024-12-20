from classes.Question import Question
from classes.Flow import Flow
import i18n
from utils.helpers import timer
translate = i18n.Translator('data').translate

async def timer_60(update, context):
    seconds = 60
    await timer(update,seconds)
    return
async def timer_120(update, context):
    seconds = 120
    await timer(update,seconds)
    return

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
    "stress_question": Question(
        id="stress_question",
        text=translate("stress_question"),
        media="",
        media_type="",
        options={translate('stress_option1'): "stress1_1", translate('stress_option2'): "stress1_2", translate('stress_option3'): "stress1_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress1_1": Question(
        id="stress1_1",
        text=translate("stress_response_high"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="exec_transition_question"
    ),
    "stress1_2": Question(
        id="stress1_2",
        text=translate("stress_response_mid"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="exec_transition_question"
    ),
    "stress1_3": Question(
        id="stress1_3",
        text=translate("stress_response_low"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="exec_transition_question"
    ),
     "exec_transition_question": Question(
        id="exec_transition_question",
        text=translate("exec_transition_question"),
        media="",
        media_type="",
        options={translate('OK'):'grounding_question'},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_question": Question(
        id="grounding_question",
        text=translate("grounding_question"),
        media="",
        media_type="",
        options={translate('grounding_option_standing'):"grounding_standing_1", translate('grounding_option_sitting'):"grounding_sitting_1", translate('grounding_option_laying'):"grounding_laying_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_sitting_1": Question(
        id="grounding_sitting_1",
        text=translate("grounding_sitting_1"),
        media="media/grounding_sitting.png",
        media_type="image",
        options={translate("OK"): "grounding_sitting_2"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_sitting_2": Question(
        id="grounding_sitting_2",
        text=translate("grounding_sitting_2"),
        media="",
        media_type="html",
        options={},
        keyboard_type="",
        next_question_id="grounding_sitting_3"
    ),
    "grounding_sitting_3": Question(
        id="grounding_sitting_3",
        text=translate("grounding_sitting_3"),
        media="",
        media_type="",
        options={translate("done"): "grounding_result"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_standing_1": Question(
        id="grounding_standing_1",
        text=translate("grounding_standing_1"),
        media="media/grounding_standing.png",
        media_type="image",
        options={translate("OK"): "grounding_standing_2"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_standing_2": Question(
        id="grounding_standing_2",
        text=translate("grounding_standing_2"),
        media="",
        media_type="html",
        options={translate("done"):"grounding_standing_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_standing_3": Question(
        id="grounding_standing_3",
        text=translate("grounding_standing_3"),
        media="",
        media_type="",
        options={translate("done"): "grounding_result"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_laying_1": Question(
        id="grounding_laying_1",
        text=translate("grounding_laying_1"),
        media="media/grounding_laying.png",
        media_type="image",
        options={translate("OK"): "grounding_laying_2"},
        keyboard_type="inline",
        next_question_id="",
    ),
    "grounding_laying_2": Question(
        id="grounding_laying_2",
        text=translate("grounding_laying_2"),
        media="",
        media_type="",
        options={translate("OK"): "grounding_laying_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_laying_3": Question(
        id="grounding_laying_3",
        text=translate("grounding_laying_3"),
        media="",
        media_type="",
        options={translate("done"): "grounding_result"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "grounding_result": Question(
        id="grounding_result",
        text=translate("grounding_result"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="grounding_result_1"
    ),
    "grounding_result_1": Question(
        id="grounding_result_1",
        text=translate("grounding_result_1"),
        media="",
        media_type="",
        options={translate("yes"): "grounding_result_1_yes",translate("no"): "grounding_result_1_no"},
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
    "breath3_exc_1": Question(
        id="breath3_exc_1",
        text=translate("breath3_exc_1"),
        media="media/Coherence_breathing.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="breath3_exc_2"
    ),
    "breath3_exc_2": Question(
        id="breath3_exc_2",
        text=translate("breath3_exc_2"),
        media="",
        media_type="",
        options={translate("yalla"): "breath3_exc_2_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath3_exc_2_1": Question(
        id="breath3_exc_2_1",
        text=translate("breath3_exc_2_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath3_exc_2_2"
    ),
    "breath3_exc_2_2": Question(
        id="breath3_exc_2_2",
        text=translate("breath3_exc_2_2"),
        media="",
        media_type="",
        options={translate("start"): timer_60},
        keyboard_type="inline",
        next_question_id="breath3_exc_3"
    ),
    "breath3_exc_3": Question(
        id="breath3_exc_3",
        text=translate("breath3_exc_3"),
        media="",
        media_type="",
        options={
            translate("breath3_exc_3_op1"): "breath3_exc_4",
            translate("breath3_exc_3_op2"): "breath3_exc_4",
            translate("breath3_exc_3_op3"): "breath3_exc_4",
            translate("breath3_exc_3_op4"): "breath3_exc_4",

        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath3_exc_4": Question(
        id="breath3_exc_4",
        text=translate("breath3_exc_4"),
        media="",
        media_type="",
        options={translate("yalla"): "breath3_exc_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath3_exc_5": Question(
        id="breath3_exc_5",
        text=translate("breath3_exc_5"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath3_exc_6"
    ),
    "breath3_exc_6": Question(
        id="breath3_exc_6",
        text=translate("breath3_exc_6"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath3_exc_7"
    ),
    "breath3_exc_7": Question(
        id="breath3_exc_7",
        text=translate("breath3_exc_7"),
        media="",
        media_type="",
        options={translate("start"): timer_60},
        keyboard_type="inline",
        next_question_id="breath3_exc_8"
    ),
    "breath3_exc_8": Question(
        id="breath3_exc_8",
        text=translate("breath3_exc_8"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath3_exc_9"
    ),
    "breath3_exc_9": Question(
        id="breath3_exc_9",
        text=translate("breath3_exc_9"),
        media="",
        media_type="",
        options={translate("start"): timer_120},
        keyboard_type="inline",
        next_question_id="transition_1"
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

    "music_exc_1": Question(
        id="music_exc_1",
        text=translate("music_exc_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="music_exc_2"
    ),
    "music_exc_2": Question(
        id="music_exc_2",
        text=translate("music_exc_2"),
        media="",
        media_type="",
        options={translate('ready'): "music_exc_5", translate('unavailable'): "music_exc_6"},
        keyboard_type="inline",
        next_question_id=""
    ),

    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://www.youtube.com/watch?v=lt2IBf2R7fU&list=OLAK5uy_lBLi4hCNijjVXo0gQrr0WaeTNLrrczgUI&index=4",
        media_type="youtube",
        options={translate("done"): 'stress_question_end'},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_6": Question(
        id="music_exc_6",
        text=translate("music_exc_6"),
        media="",
        media_type="",
        options={translate('OK'): "music_exc_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress_question_end": Question(
        id="stress_question_end",
        text=translate("stress_question_end"),
        media="",
        media_type="",
        options={"1": "stress_low", "2": "stress_low", "3": "stress_low", "4": "stress_low", "5": "stress_still_high", "6": "stress_still_high",
                 "7": "stress_still_high", "8": "stress_still_high", "9": "stress_still_high", "10": "stress_still_high"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress_still_high": Question(
        id="stress_still_high",
        text=translate("stress_still_high"),
        media="",
        media_type="",
        options={
            translate('lets_continue'):"integration3_1",
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
            translate('lets_continue'):"integration3_1",
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
    "integration3_1": Question(
        id="integration3_1",
        text=translate("integration3_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration3_2"
    ),
    "integration3_2": Question(
        id="integration3_2",
        text=translate("integration3_2"),
        media="https://www.ddinstagram.com/reel/C8H1klNN09N/",
        media_type="youtube",
        options={translate("done"):"integration3_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration3_3": Question(
        id="integration3_3",
        text=translate("integration3_3"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration3_4"
    ),
    "integration3_4": Question(
        id="integration3_4",
        text=translate("integration3_4"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration3_5"
    ),
    "integration3_5": Question(
        id="integration3_5",
        text=translate("integration3_5"),
        media="https://www.youtube.com/shorts/DnTUaWpjiC4",
        media_type="youtube",
        options={translate("done"):"integration3_6"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration3_6": Question(
        id="integration3_6",
        text=translate("integration3_6"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration3_7"
    ),
    "integration3_7": Question(
        id="integration3_7",
        text=translate("integration3_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration3_8"
    ),
    "integration3_8": Question(
        id="integration3_8",
        text=translate("integration3_8"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration3_9"
    ),
    "integration3_9": Question(
        id="integration3_9",
        text=translate("integration3_9"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration3_10"
    ),
    "integration3_10": Question(
        id="integration3_10",
        text=translate("integration3_10"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task3_1"
    ),
    "task3_1": Question(
        id="task3_1",
        text=translate("task3_1"),
        media="https://www.ddinstagram.com/reel/C7l4wASAfrW/",
        media_type="youtube",
        options={},
        keyboard_type="",
        next_question_id="task3_2"
    ),
    "task3_2": Question(
        id="task3_2",
        text=translate("task3_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task3_3"
    ),
    "task3_3": Question(
        id="task3_3",
        text=translate("task3_3"),
        media="",
        media_type="",
        options={
            translate('task3_3_op1'):"task3_4",
            translate('task3_3_op2'): "task3_4",
            translate('task3_3_op3'): "task3_4",
            translate('task3_3_op4'): "task3_4",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task3_4": Question(
        id="task3_4",
        text=translate("task3_4"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="end_1"
    ),
    "end": Question(
        id="end",
        text=translate("end"),
        media="",
        media_type="",
        options={"1": "end_1", "2": "end_1", "3": "end_1", "4": "end_1", "5": "end_1", "6": "end_1", "7": "end_1", "8": "end_1", "9": "end_1", "10": "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "end_1": Question(
        id="end_1",
        text=translate("end_1"),
        media="media/end.webp",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id=""
    )
}




# Initialize Flow
flow = Flow("flow3", questions, "alt_into")
