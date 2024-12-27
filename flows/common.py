from classes.Question import Question
import i18n


translate = i18n.Translator('data').translate

stress_question = {
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
}

stress_question_end = {
    "stress_question_end": Question(
        id="stress_question_end",
        text=translate("stress_question_end"),
        media="",
        media_type="",
        options={"1": "stress_low", "2": "stress_low", "3": "stress_low", "4": "stress_low", "5": "stress_still_high",
                 "6": "stress_still_high",
                 "7": "stress_still_high", "8": "stress_still_high", "9": "stress_still_high",
                 "10": "stress_still_high"},
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
}

grounding_questions = {
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
        next_question_id="end_1"
    ),
    "grounding_result_1_no": Question(
        id="grounding_result_1_no",
        text=translate("grounding_result_1_no"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="end_1"
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

rerouting_questions = {
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
        options={translate('done'): "end_1"},
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

rerouting_questions2 = {
    "rerouting_exc2": Question(
        id="rerouting_exc2",
        text=translate("rerouting_exc2"),
        media="media/rerouting_1_5.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="rerouting_exc2_1"
    ),
    "rerouting_exc2_1": Question(
        id="rerouting_exc2_1",
        text=translate("rerouting_exc2_1"),
        media="",
        media_type="",
        options={translate('yalla'): "rerouting_exc2_2"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc2_2": Question(
        id="rerouting_exc2_2",
        text=translate("rerouting_exc2_2"),
        media="",
        media_type="",
        options={translate('OK'): "rerouting_exc2_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc2_3": Question(
        id="rerouting_exc2_3",
        text=translate("rerouting_exc2_3"),
        media="",
        media_type="",
        options={translate('OK'): "rerouting_exc2_4"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc2_4": Question(
        id="rerouting_exc2_4",
        text=translate("rerouting_exc2_4"),
        media="",
        media_type="",
        options={translate('OK'): "rerouting_exc2_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc2_5": Question(
        id="rerouting_exc2_5",
        text=translate("rerouting_exc2_5"),
        media="",
        media_type="",
        options={translate('OK'): "rerouting_exc2_6"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc2_6": Question(
        id="rerouting_exc2_6",
        text=translate("rerouting_exc2_6"),
        media="",
        media_type="",
        options={translate('OK'): "rerouting_exc2_7"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "rerouting_exc2_7": Question(
        id="rerouting_exc2_7",
        text=translate("rerouting_exc2_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="end_1"
    ),
}

body_connection_questions = {
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
        options={translate("done"): "end_1"},
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

breath_exc_1 = {
    "breath_exc_1": Question(
        id="breath_exc_1",
        text=translate("breath_exc_1"),
        media="https://youtube.com/shorts/_rJdObUzTfQ",
        media_type="youtube",
        options={},
        keyboard_type="",
        next_question_id="breath_exc_2"
    ),
    "breath_exc_2": Question(
        id="breath_exc_2",
        text=translate("are_you_ready"),
        media="",
        media_type="",
        options={translate("ready"): "breath_exc_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath_exc_3": Question(
        id="breath_exc_3",
        text=translate('breath_exc_3'),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath_exc_4"
    ),
    "breath_exc_4": Question(
        id="breath_exc_4",
        text=translate("breath_exc_4"),
        media="",
        media_type="",
        options={translate('done'): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

breath_exc_2 = {
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
        options={translate("done"): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

breath_exc_3 = {
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
        options={translate("OK"): "breath3_exc_3"},
        keyboard_type="inline",
        next_question_id=""
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
        options={},
        keyboard_type="",
        next_question_id="breath3_exc_8"
    ),
    "breath3_exc_8": Question(
        id="breath3_exc_8",
        text=translate("breath3_exc_8"),
        media="",
        media_type="",
        options={translate("done"): "breath3_exc_9"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath3_exc_9": Question(
        id="breath3_exc_9",
        text=translate("breath3_exc_9"),
        media="",
        media_type="",
        options={translate("done"): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

breath_exc_478 = {
    "breath_exc_478_1": Question(
        id="breath_exc_478_1",
        text=translate("breath_exc_478_1"),
        media="media/478_breathing.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="breath_exc_478_2"
    ),
    "breath_exc_478_2": Question(
        id="breath_exc_478_2",
        text=translate("breath_exc_478_2"),
        media="",
        media_type="",
        options={translate('OK'): "breath_exc_478_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath_exc_478_3": Question(
        id="breath_exc_478_3",
        text=translate("breath_exc_478_3"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="breath_exc_478_4"
    ),
    "breath_exc_478_4": Question(
        id="breath_exc_478_4",
        text=translate("breath_exc_478_4"),
        media="",
        media_type="",
        options={translate('done'): "breath_exc_478_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath_exc_478_5": Question(
        id="breath_exc_478_5",
        text=translate("breath_exc_478_5"),
        media="",
        media_type="",
        options={translate('done'): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

color_breathing = {
    "color_breathing_1": Question(
        id="color_breathing_1",
        text=translate("color_breathing_1"),
        media="media/color_breathing.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="color_breathing_2"
    ),
    "color_breathing_2": Question(
        id="color_breathing_2",
        text=translate("color_breathing_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="color_breathing_3"
    ),
    "color_breathing_3": Question(
        id="color_breathing_3",
        text=translate("color_breathing_3"),
        media="",
        media_type="",
        options={
            translate("OK"): "color_breathing_4"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "color_breathing_4": Question(
        id="color_breathing_4",
        text=translate("color_breathing_4"),
        media="",
        media_type="",
        options={
            translate("green"): "color_breathing_5",
            translate("blue"): "color_breathing_5",
            translate("purple"): "color_breathing_5",
            translate("pink"): "color_breathing_5",
            translate("yellow"): "color_breathing_5",
            translate("grey"): "color_breathing_5",
            translate("white"): "color_breathing_5",
            translate("other"): "color_breathing_5"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "color_breathing_5": Question(
        id="color_breathing_5",
        text=translate("color_breathing_5"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="color_breathing_6"
    ),
    "color_breathing_6": Question(
        id="color_breathing_6",
        text=translate("color_breathing_6"),
        media="",
        media_type="",
        options={translate("done"): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

box_breathing = {
    "box_breathing_1": Question(
        id="box_breathing_1",
        text=translate("box_breathing_1"),
        media="media/box_breathing_2.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="box_breathing_2"
    ),
    "box_breathing_2": Question(
        id="box_breathing_2",
        text=translate("box_breathing_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="box_breathing_3"
    ),
    "box_breathing_3": Question(
        id="box_breathing_3",
        text=translate("box_breathing_3"),
        media="",
        media_type="",
        options={
            translate("OK"): "box_breathing_4"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "box_breathing_4": Question(
        id="box_breathing_4",
        text=translate("box_breathing_4"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="box_breathing_5"
    ),
    "box_breathing_5": Question(
        id="box_breathing_5",
        text=translate("box_breathing_5"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="box_breathing_6"
    ),
    "box_breathing_6": Question(
        id="box_breathing_6",
        text=translate("box_breathing_6"),
        media="",
        media_type="",
        options={translate("done"): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

vagus_nerve_stim = {
    "vagus_nerve_stim_1": Question(
        id="vagus_nerve_stim_1",
        text=translate("vagus_nerve_stim_1"),
        media="media/vagus_nerve_stim.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="vagus_nerve_stim_2"
    ),
    "vagus_nerve_stim_2": Question(
        id="vagus_nerve_stim_2",
        text=translate("vagus_nerve_stim_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="vagus_nerve_stim_3"
    ),
    "vagus_nerve_stim_3": Question(
        id="vagus_nerve_stim_3",
        text=translate("vagus_nerve_stim_3"),
        media="",
        media_type="",
        options={
            translate("ready"): "vagus_nerve_stim_4"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "vagus_nerve_stim_4": Question(
        id="vagus_nerve_stim_4",
        text=translate("vagus_nerve_stim_4"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="vagus_nerve_stim_5"
    ),
    "vagus_nerve_stim_5": Question(
        id="vagus_nerve_stim_5",
        text=translate("vagus_nerve_stim_5"),
        media="",
        media_type="",
        options={
            translate("OK"): "vagus_nerve_stim_6"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "vagus_nerve_stim_6": Question(
        id="vagus_nerve_stim_6",
        text=translate("vagus_nerve_stim_6"),
        media="https://www.ddinstagram.com/p/DBcbG-RyHrw/",
        media_type="youtube",
        options={translate("done"): "vagus_nerve_stim_7"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "vagus_nerve_stim_7": Question(
        id="vagus_nerve_stim_7",
        text=translate("vagus_nerve_stim_7"),
        media="",
        media_type="",
        options={translate("yes"): "end_1", translate("no"): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

half_salamander = {
    "half_salamander_1": Question(
        id="half_salamander_1",
        text=translate("half_salamander_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="half_salamander_2"
    ),
    "half_salamander_2": Question(
        id="half_salamander_2",
        text=translate("half_salamander_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="half_salamander_3"
    ),
    "half_salamander_3": Question(
        id="half_salamander_3",
        text=translate("half_salamander_3"),
        media="",
        media_type="",
        options={
            translate("yalla"): "half_salamander_4"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "half_salamander_4": Question(
        id="half_salamander_4",
        text=translate("half_salamander_4"),
        media="",
        media_type="",
        options={translate("OK"): "half_salamander_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "half_salamander_5": Question(
        id="half_salamander_5",
        text=translate("half_salamander_5"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="half_salamander_6"
    ),
    "half_salamander_6": Question(
        id="half_salamander_6",
        text=translate("half_salamander_6"),
        media="",
        media_type="",
        options={translate("OK"): "half_salamander_7"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "half_salamander_7": Question(
        id="half_salamander_7",
        text=translate("half_salamander_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="half_salamander_8"
    ),
    "half_salamander_8": Question(
        id="half_salamander_8",
        text=translate("half_salamander_8"),
        media="",
        media_type="",
        options={translate("OK"): "half_salamander_9"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "half_salamander_9": Question(
        id="half_salamander_9",
        text=translate("half_salamander_9"),
        media="",
        media_type="",
        options={translate("yes"): "end_1", translate("no"): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
}

integration_1 = {
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
        next_question_id="end_1"
    ),
}

integration_2 = {
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
        next_question_id="end_1"
    ),
}

task_1 = {
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
        options={},
        keyboard_type="",
        next_question_id="end_1"
    ),
}

task_2 = {
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
}

task_4 = {
    "task4_1": Question(
        id="task4_1",
        text=translate("task4_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task4_2"
    ),
    "task4_2": Question(
        id="task4_2",
        text=translate("task4_2"),
        media="https://youtube.com/shorts/sMmLmpF9vQY?feature=share",
        media_type="youtube",
        options={translate('done'): "task4_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task4_3": Question(
        id="task4_3",
        text=translate("task4_3"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task4_4"
    ),
    "task4_4": Question(
        id="task4_4",
        text=translate("task4_4"),
        media="",
        media_type="",
        options={
            translate('running'):"end_1",
            translate('walking'): "end_1",
            translate('dancing'): "end_1",
            translate('weight_lifting'): "end_1",
            translate('other'): "end_1",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
}

task_5 = {
    "task5_1": Question(
        id="task5_1",
        text=translate("task5_1"),
        media="media/anger1.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="task5_2"
    ),
    "task5_2": Question(
        id="task5_2",
        text=translate("task5_2"),
        media="media/anger2.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="task5_3"
    ),
    "task5_3": Question(
        id="task5_3",
        text=translate("task5_3"),
        media="media/anger3.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="task5_4"
    ),
    "task5_4": Question(
        id="task5_4",
        text=translate("task5_4"),
        media="media/anger4.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="task5_5"
    ),
    "task5_5": Question(
        id="task5_5",
        text=translate("task5_5"),
        media="media/anger5.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="task5_6"
    ),
    "task5_6": Question(
        id="task5_6",
        text=translate("task5_6"),
        media="media/anger6.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="task5_7"
    ),
    "task5_7": Question(
        id="task5_7",
        text=translate("task5_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="end_1"
    ),
}

anger_exc = {
    "anger_exc_1": Question(
        id="anger_exc_1",
        text=translate("anger_exc_1"),
        media="media/anger_exc.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="anger_exc_2"
    ),
    "anger_exc_2": Question(
        id="anger_exc_2",
        text=translate("anger_exc_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="anger_exc_3"
    ),
    "anger_exc_3": Question(
        id="anger_exc_3",
        text=translate("anger_exc_3"),
        media="",
        media_type="",
        options={
            translate('room'):"anger_exc_4",
            translate('bathroom'): "anger_exc_4",
            translate('nature'): "anger_exc_4",
            translate('car'): "anger_exc_4",
            translate('special_place'): "anger_exc_4",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "anger_exc_4": Question(
        id="anger_exc_4",
        text=translate("anger_exc_4"),
        media="",
        media_type="",
        options={
            translate('head'): "anger_exc_5",
            translate('throat'): "anger_exc_5",
            translate('chest'): "anger_exc_5",
            translate('belly'): "anger_exc_5",
            translate('legs'): "anger_exc_5",
            translate('other'): "anger_exc_5",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "anger_exc_5": Question(
        id="anger_exc_5",
        text=translate("anger_exc_5"),
        media="",
        media_type="",
        options={
            translate('yes'): "anger_exc_6",
            translate('no'): "anger_exc_11",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "anger_exc_6": Question(
        id="anger_exc_6",
        text=translate("anger_exc_6"),
        media="",
        media_type="",
        options={
            translate('OK'): "anger_exc_7",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "anger_exc_7": Question(
        id="anger_exc_7",
        text=translate("anger_exc_7"),
        media="",
        media_type="",
        options={
            translate('done'): "anger_exc_8",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "anger_exc_8": Question(
        id="anger_exc_8",
        text=translate("anger_exc_8"),
        media="",
        media_type="",
        options={
            translate('feeling_better'): "anger_exc_9",
            translate('feeling_same'): "anger_exc_10",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "anger_exc_9": Question(
        id="anger_exc_9",
        text=translate("anger_exc_9"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="end_1"
    ),
    "anger_exc_10": Question(
        id="anger_exc_10",
        text=translate("anger_exc_10"),
        media="",
        media_type="",
        options={
            translate('yes'): "end_1",
            translate('no'): "end_1",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "anger_exc_11": Question(
        id="anger_exc_11",
        text=translate("anger_exc_11"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="anger_exc_6"
    ),
}

negative_belief_stories = {
    "task6_1": Question(
        id="task6_1",
        text=translate("task6_1"),
        media="media/negative_belief_stories.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="task6_2"
    ),
    "task6_2": Question(
        id="task6_2",
        text=translate("task6_2"),
        media="https://www.ddinstagram.com/p/C_OVoksuLtU/",
        media_type="youtube",
        options={translate('done'): "task6_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_3": Question(
        id="task6_3",
        text=translate("task6_3"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task6_4"
    ),
    "task6_4": Question(
        id="task6_4",
        text=translate("task6_4"),
        media="media/beliefs.png",
        media_type="image",
        options={},
        keyboard_type="",
        next_question_id="task6_5"
    ),
    "task6_5": Question(
        id="task6_5",
        text=translate("task6_5"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task6_6"
    ),
    "task6_6": Question(
        id="task6_6",
        text=translate("task6_6"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task6_7"
    ),
    "task6_7": Question(
        id="task6_7",
        text=translate("task6_7"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task6_8"
    ),
    "task6_8": Question(
        id="task6_8",
        text=translate("task6_8"),
        media="",
        media_type="",
        options={translate("yalla"): "task6_9"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_9": Question(
        id="task6_9",
        text=translate("task6_9"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task6_10"
    ),
    "task6_10": Question(
        id="task6_10",
        text=translate("task6_10"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task6_11"
    ),
    "task6_11": Question(
        id="task6_11",
        text=translate("task6_11"),
        media="",
        media_type="",
        options={translate("OK"): "task6_12"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_12": Question(
        id="task6_12",
        text=translate("task6_12"),
        media="",
        media_type="",
        options={
            translate("unlovable"): "task6_13",
            translate("incapable"): "task6_13",
            translate("weak"): "task6_13",
            translate("loser"): "task6_13",
            translate("stupid"): "task6_13",
            translate("ugly"): "task6_13",
            translate("lazy"): "task6_13",
            translate("unimportant"): "task6_13",
            translate("not_enough"): "task6_13",
            translate("not_talented"): "task6_13",
            translate("worthless"): "task6_13",
            translate("hopeless"): "task6_13",
            translate("boring"): "task6_13",
            translate("scared"): "task6_13",
            translate("unaccepted"): "task6_13",
            translate("lier"): "task6_13",
            translate("incompetent"): "task6_13",
            translate("helpless"): "task6_13",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_13": Question(
        id="task6_13",
        text=translate("task6_13"),
        media="",
        media_type="",
        options={
            translate("burden"): "task6_14",
            translate("embarrassing"): "task6_14",
            translate("selfish"): "task6_14",
            translate("incompetent"): "task6_14",
            translate("unimportant"): "task6_14",
            translate("untrustworthy"): "task6_14",
            translate("clingy"): "task6_14",
            translate("fake"): "task6_14",
            translate("critical"): "task6_14",
            translate("arrogant"): "task6_14",
            translate("narrow-minded"): "task6_14",
            translate("ridiculous"): "task6_14",
            translate("not funny"): "task6_14",
            translate("immature"): "task6_14",
            translate("ignorant"): "task6_14",
            translate("annoying"): "task6_14",
            translate("distracting"): "task6_14",
            translate("uninteresting"): "task6_14",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_14": Question(
        id="task6_14",
        text=translate("task6_14"),
        media="",
        media_type="",
        options={
            translate("failing"): "task6_15",
            translate("struggling"): "task6_15",
            translate("late"): "task6_15",
            translate("worried"): "task6_15",
            translate("broken"): "task6_15",
            translate("lost"): "task6_15",
            translate("lonely"): "task6_15",
            translate("broke"): "task6_15",
            translate("not ready"): "task6_15",
            translate("wrong"): "task6_15",
            translate("hesitant"): "task6_15",
            translate("stressed"): "task6_15",
            translate("scared"): "task6_15",
            translate("confused"): "task6_15",
            translate("neglected"): "task6_15",
            translate("walking for others"): "task6_15",
            translate("irresponsible"): "task6_15",
            translate("not focused"): "task6_15",
            translate("ignoring"): "task6_15",
            translate("disappointing"): "task6_15"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_15": Question(
        id="task6_15",
        text=translate("task6_15"),
        media="",
        media_type="",
        options={
            translate("successful"): "task6_16",
            translate("happy"): "task6_16",
            translate("find_love"): "task6_16",
            translate("enjoy_life"): "task6_16"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_16": Question(
        id="task6_16",
        text=translate("task6_16"),
        media="",
        media_type="",
        options={
            translate("OK"): "task6_17",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_17": Question(
        id="task6_17",
        text=translate("task6_17"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task6_18"
    ),
    "task6_18": Question(
        id="task6_18",
        text=translate("task6_18"),
        media="",
        media_type="",
        options={
            translate("yalla"): "task6_19"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_19": Question(
        id="task6_19",
        text=translate("task6_19"),
        media="",
        media_type="",
        options={
            translate("OK"): "task6_20"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_20": Question(
        id="task6_20",
        text=translate("task6_20"),
        media="",
        media_type="",
        options={
            translate("rip"): "task6_21"
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task6_21": Question(
        id="task6_21",
        text=translate("task6_21"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task6_22"
    ),
    "task6_22": Question(
        id="task6_22",
        text=translate("task6_22"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="end_1"
    ),
}

acknowledgement_question = {
    "acknowledgement_1": Question(
        id="acknowledgement_1",
        text=translate("acknowledgement_1"),
        media="",
        media_type="",
        options={
            translate('happy'):"acknowledgement_happy",
            translate('disgusted'): "acknowledgement_disgusted",
            translate('sad'): "acknowledgement_sad",
            translate('scared'): "acknowledgement_scared",
            translate('angry'): "acknowledgement_angry",
            translate('surprised'): "acknowledgement_surprised",
        },
        keyboard_type="",
        next_question_id=""
    ),
    "acknowledgement_happy": Question(
        id="acknowledgement_happy",
        text=translate("acknowledgement_happy"),
        media="",
        media_type="",
        options={
            translate('proud'): "acknowledgement_2",
            translate('optimistic'): "acknowledgement_2",
            translate('acceptable'): "acknowledgement_2",
            translate('cheerful'): "acknowledgement_2",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "acknowledgement_disgusted": Question(
        id="acknowledgement_disgusted",
        text=translate("acknowledgement_disgusted"),
        media="",
        media_type="",
        options={
            translate('disappointed'): "acknowledgement_2",
            translate('aversion'): "acknowledgement_2",
            translate('unaccepted'): "acknowledgement_2",
            translate('avoidant'): "acknowledgement_2",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "acknowledgement_sad": Question(
        id="acknowledgement_sad",
        text=translate("acknowledgement_sad"),
        media="",
        media_type="",
        options={
            translate('guilty'): "acknowledgement_2",
            translate('feeling_low'): "acknowledgement_2",
            translate('lonely'): "acknowledgement_2",
            translate('bored'): "acknowledgement_2",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "acknowledgement_scared": Question(
        id="acknowledgement_scared",
        text=translate("acknowledgement_scared"),
        media="",
        media_type="",
        options={
            translate('freaking'): "acknowledgement_2",
            translate('anxious'): "acknowledgement_2",
            translate('rejected'): "acknowledgement_2",
            translate('unsafe'): "acknowledgement_2",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "acknowledgement_angry": Question(
        id="acknowledgement_angry",
        text=translate("acknowledgement_angry"),
        media="",
        media_type="",
        options={
            translate('very_angry'): "acknowledgement_2",
            translate('hurt'): "acknowledgement_2",
            translate('threatened'): "acknowledgement_2",
            translate('separated'): "acknowledgement_2",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "acknowledgement_surprised": Question(
        id="acknowledgement_happy",
        text=translate("acknowledgement_happy"),
        media="",
        media_type="",
        options={
            translate('shocked'): "acknowledgement_2",
            translate('confused'): "acknowledgement_2",
            translate('amazed'): "acknowledgement_2",
            translate('terrified'): "acknowledgement_2",
        },
        keyboard_type="inline",
        next_question_id=""
    ),
    "acknowledgement_2": Question(
        id="acknowledgement_2",
        text=translate("acknowledgement_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id=""
    ),
}

sound_healing = {
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
        options={translate('ready'): "music_exc_3", translate('unavailable'): "music_exc_6"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_3": Question(
        id="music_exc_3",
        text=translate("music_exc_3"),
        media="https://www.youtube.com/watch?v=1N1vtQQ9ij0",
        media_type="youtube",
        options={},
        keyboard_type="",
        next_question_id="music_exc_4"
    ),
    "music_exc_4": Question(
        id="music_exc_4",
        text=translate("music_exc_4"),
        media="",
        media_type="",
        options={translate('ready'): "music_exc_5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_5": Question(
        id="music_exc_5",
        text=translate("music_exc_5"),
        media="https://www.youtube.com/watch?v=UfcAVejslrU",
        media_type="youtube",
        options={translate('done'): "end_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "music_exc_6": Question(
        id="music_exc_6",
        text=translate("music_exc_6"),
        media="",
        media_type="",
        options={translate('OK'): "music_exc_3"},
        keyboard_type="inline",
        next_question_id=""
    ),
}