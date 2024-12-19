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
        options={translate("yalla"): "rerouting_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
"rerouting_exc_1": Question(
        id="rerouting_exc_1",
        text=translate("rerouting_exc_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="rerouting_exc_2"
    ),
    "rerouting_exc_2": Question(
        id="rerouting_exc_2",
        text=translate("rerouting_exc_2"),
        media="media/reorientation.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="rerouting_exc_3"
    ),
    "rerouting_exc_3": Question(
        id="rerouting_exc_3",
        text=translate("rerouting_exc_3"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="rerouting_exc_4"
    ),
    "rerouting_exc_4": Question(
        id="rerouting_exc_4",
        text=translate("rerouting_exc_4"),
        media="",
        media_type="",
        options={translate('OK'): "rerouting_exc_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc_5": Question(
        id="rerouting_exc_5",
        text=translate("rerouting_exc_5"),
        media="",
        media_type="html",
        options={},
        keyboard_type="",
        next_question_id="rerouting_exc_6"
    ),
    "rerouting_exc_6": Question(
        id="rerouting_exc_6",
        text=translate("rerouting_exc_6"),
        media="",
        media_type="",
        options={translate('OK'): "rerouting_exc_7"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc_7": Question(
        id="rerouting_exc_7",
        text=translate("rerouting_exc_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="rerouting_exc_8"
    ),
    "rerouting_exc_8": Question(
        id="rerouting_exc_8",
        text=translate("rerouting_exc_8"),
        media="",
        media_type="",
        options={translate('high'): "rerouting_exc_9", translate('low'): "rerouting_exc_9", translate('annoying'): "rerouting_exc_9", translate('kind'): "rerouting_exc_9", translate('other'): "rerouting_exc_9"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc_9": Question(
        id="rerouting_exc_9",
        text=translate("rerouting_exc_9"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="rerouting_exc_10"
    ),
    "rerouting_exc_10": Question(
        id="rerouting_exc_10",
        text=translate("rerouting_exc_10"),
        media="",
        media_type="html",
        options={translate('cold'): "rerouting_exc_11", translate('hot'): "rerouting_exc_11", translate('scratchy'): "rerouting_exc_11", translate('soft'): "rerouting_exc_11", translate('other'): "rerouting_exc_11"},
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
        media="https://www.youtube.com/watch?v=aS41f-yM4M8&list=OLAK5uy_lBLi4hCNijjVXo0gQrr0WaeTNLrrczgUI&index=3",
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
        media="https://www.ddinstagram.com/p/C7V7ld3s4u6/",
        media_type="youtube",
        options={
            translate('done'):"integration2_3",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_3": Question(
        id="integration2_3",
        text=translate("integration2_3"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="integration2_4"
    ),
    "integration2_4": Question(
        id="integration2_4",
        text=translate("integration2_4"),
        media="",
        media_type="",
        options={translate('nice'):"integration2_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_5": Question(
        id="integration2_5",
        text=translate("integration2_5"),
        media="",
        media_type="",
        options={translate('OK'): "integration2_6"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "integration2_6": Question(
        id="integration2_6",
        text=translate("integration2_6"),
        media="",
        media_type="",
        options={translate('why'): "integration2_7"},
        keyboard_type="inline",
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
        options={translate('yalla'):"task2_5"},
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
        options={translate("done"):"task2_7"},
        keyboard_type="inline",
        next_question_id=""
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
        options={translate('OK'):"end_1"},
        keyboard_type="inline",
        next_question_id=""
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
        keyboard_type="inline",
        next_question_id=""
    )
}

# Initialize Flow
flow = Flow("flow2", questions, "alt_into")




