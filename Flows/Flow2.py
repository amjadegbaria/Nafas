from classes.Question import Question
from classes.Flow import Flow
import i18n

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
    "breath2_exc_1": Question(
        id="breath2_exc_1",
        text=translate("breath2_exc_1"),
        media="media/Box_breathing.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="breath2_exc_2"
    ),
    "breath2_exc_2": Question(
        id="breath2_exc_2",
        text=translate("breath2_exc_2"),
        media="",
        media_type="",
        options={translate("OK"): "breath2_exc_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath2_exc_3": Question(
        id="breath2_exc_3",
        text=translate("breath2_exc_3"),
        media="",
        media_type="",
        options={translate("OK"): "breath2_exc_4"},
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
        options={translate("yalla"): "flow2_exc2_1"},
        keyboard_type="inline",
        next_question_id=""
    ),

    "flow2_exc2_1": Question(
        id="flow2_exc2_1",
        text=translate("flow2_exc2_1"),
        media="media/rubbing_exc.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="flow2_exc2_2"
    ),
    "flow2_exc2_2": Question(
        id="flow2_exc2_2",
        text=translate("flow2_exc2_2"),
        media="",
        media_type="",
        options={translate('OK'): "flow2_exc2_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "flow2_exc2_3": Question(
        id="flow2_exc2_3",
        text=translate("flow2_exc2_3"),
        media="",
        media_type="",
        options={translate('OK'): "flow2_exc2_4"},
        keyboard_type="inline",
        next_question_id="flow2_exc2_4"
    ),
    "flow2_exc2_4": Question(
        id="flow2_exc2_4",
        text=translate("flow2_exc2_4"),
        media="",
        media_type="",
        options={translate("done"): "music_exc_1"},
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
        media="https://www.youtube.com/watch?v=kgBjvXcHvS8",
        media_type="youtube",
        options={translate("done"):'stress_question_end'},
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
        keyboard_type="reply",
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
    "integration2": Question(
        id="integration2",
        text=translate("integration2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_1"
    ),
    "integration2_1": Question(
        id="integration2_1",
        text=translate("integration2_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_2"
    ),
    "integration2_2": Question(
        id="integration2_2",
        text=translate("integration2_2"),
        media="",
        media_type="",
        options={
            translate('integration2_2_op1'):"integration2_3",
            translate('integration2_2_op2'):"integration2_3",
            translate('integration2_2_op3'):"integration2_3",
            translate('integration2_2_op4'):"integration2_3"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_3": Question(
        id="integration2_3",
        text=translate("integration2_3"),
        media="media/hefty-smurf-stubbed-toe.gif",
        media_type="image",
        options={translate("right"):"integration2_4"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_4": Question(
        id="integration2_4",
        text=translate("integration2_4"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_5"
    ),
    "integration2_5": Question(
        id="integration2_5",
        text=translate("integration2_5"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_6"
    ),
    "integration2_6": Question(
        id="integration2_6",
        text=translate("integration2_6"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_7"
    ),
    "integration2_7": Question(
        id="integration2_7",
        text=translate("integration2_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_8"
    ),
    "integration2_8": Question(
        id="integration2_8",
        text=translate("integration2_8"),
        media="",
        media_type="",
        options={translate("integration2_8_op1"):"integration2_9"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_9": Question(
        id="integration2_9",
        text=translate("integration2_9"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_10"
    ),
    "integration2_10": Question(
        id="integration2_10",
        text=translate("integration2_10"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_11"
    ),
    "integration2_11": Question(
        id="integration2_11",
        text=translate("integration2_11"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_12"
    ),
    "integration2_12": Question(
        id="integration2_12",
        text=translate("integration2_12"),
        media="",
        media_type="",
        options={translate("yalla"):"integration2_13"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_13": Question(
        id="integration2_13",
        text=translate("integration2_13"),
        media="",
        media_type="",
        options={
            translate("integration2_13_op1"):"integration2_13_op1_response",
            translate("integration2_13_op2"): "integration2_13_op2_response",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_13_op1_response": Question(
        id="integration2_13_op1_response",
        text=translate("integration2_13_op1_response"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_14"
    ),
    "integration2_13_op2_response": Question(
        id="integration2_13_op2_response",
        text=translate("integration2_13_op2_response"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_14"
    ),
    "integration2_14": Question(
        id="integration2_14",
        text=translate("integration2_14"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_15"
    ),
    "integration2_15": Question(
        id="integration2_15",
        text=translate("integration2_15"),
        media="",
        media_type="",
        options={translate('integration2_15_op1'):"integration2_16"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_16": Question(
        id="integration2_16",
        text=translate("integration2_16"),
        media="",
        media_type="",
        options={translate('integration2_16_op1'):"integration2_17"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_17": Question(
        id="integration2_17",
        text=translate("integration2_17"),
        media="",
        media_type="",
        options={translate('integration2_17_op1'):"integration2_18"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_18": Question(
        id="integration2_18",
        text=translate("integration2_18"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_19"
    ),
    "integration2_19": Question(
        id="integration2_19",
        text=translate("integration2_19"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_20"
    ),
    "integration2_20": Question(
        id="integration2_20",
        text=translate("integration2_20"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_21"
    ),
    "integration2_21": Question(
        id="integration2_21",
        text=translate("integration2_21"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_22"
    ),
    "integration2_22": Question(
        id="integration2_22",
        text=translate("integration2_22"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_23"
    ),
    "integration2_23": Question(
        id="integration2_23",
        text=translate("integration2_23"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task2_1"
    ),
    "task2_1": Question(
        id="task2_1",
        text=translate("task2_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task2_2"
    ),
    "task2_2": Question(
        id="task2_2",
        text=translate("task2_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task2_3"
    ),
    "task2_3": Question(
        id="task2_3",
        text=translate("task2_3"),
        media="",
        media_type="",
        options={translate('yalla'):"task2_4"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task2_4": Question(
        id="task2_4",
        text=translate("task2_4"),
        media="",
        media_type="",
        options={translate('exp_chest_1'):"task2_5", translate('exp_belly_1'):"task2_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task2_5": Question(
        id="task2_5",
        text=translate("task2_5"),
        media="",
        media_type="",
        options={translate('exp_chest_2'):"task2_6",translate("exp_belly_2"):"task2_6"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task2_6": Question(
        id="task2_6",
        text=translate("task2_6"),
        media="https://www.youtube.com/watch?v=Y8w8lxMv8mw",
        media_type="youtube",
        options={},
        keyboard_type="",
        next_question_id="task2_7"
    ),
    "task2_7": Question(
        id="task2_7",
        text=translate("task2_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task2_8"
    ),
    "task2_8": Question(
        id="task2_8",
        text=translate("task2_8"),
        media="https://www.youtube.com/watch?v=qhcBjSirMss",
        media_type="youtube",
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
        keyboard_type="reply",
        next_question_id=""
    ),
    "end_1": Question(
        id="end_1",
        text=translate("end_1"),
        media="end.webp",
        media_type="image",
        options={},
        keyboard_type="reply",
        next_question_id=""
    )
}

# Initialize Flow
flow = Flow("flow3", questions)