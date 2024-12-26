from classes.Question import Question
import i18n


translate = i18n.Translator('data').translate

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
        media_type="",
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
        options={translate("yes"): "end_1",translate("no"): "end_1"},
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