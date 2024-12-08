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