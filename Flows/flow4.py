from classes.Question import Question
from classes.Flow import Flow

import i18n


translate = i18n.Translator('data').translate

questions = {
    "intro1": Question(
        id="intro1",
        text=translate("intro1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="intro2"
    ),
    "intro2": Question(
        id="intro2",
        text=translate("intro2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="intro3"
    ),
    "intro3": Question(
        id="intro3",
        text=translate("intro3"),
        media="",
        media_type="",
        options={translate("yes_sure"): "intro4"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "intro4": Question(
        id="intro4",
        text=translate("intro4"),
        media="",
        media_type="",
        options={translate("promise"): "intro5"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "intro5": Question(
        id="intro5",
        text=translate("intro5"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="intro6"
    ),
    "intro6": Question(
        id="intro6",
        text=translate("intro6"),
        media="media/logos.jpeg",
        media_type="image",
        options={},
        keyboard_type="inline",
        next_question_id="intro7"
    ),
    "intro7": Question(
        id="intro7",
        text=translate("intro7"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="intro8"
    ),
    "intro8": Question(
        id="intro8",
        text=translate("intro8"),
        media="",
        media_type="",
        options={translate('ready'): "stress1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "stress1": Question(
        id="stress1",
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
        next_question_id="stress1_4"
    ),
    "stress1_2": Question(
        id="stress1_2",
        text=translate("stress_response_mid"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="stress1_4"
    ),
    "stress1_3": Question(
        id="stress1_3",
        text=translate("stress_response_low"),
        media="",
        media_type="",
        options={},
        keyboard_type="inline",
        next_question_id="stress1_4"
    ),
    "stress1_4": Question(
        id="stress1_4",
        text=translate("exec_transition_question"),
        media="",
        media_type="",
        options={translate("yalla"): "grounding_sitting_1"},
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
        options={translate("done"): "breath_exc_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "breath_exc_1": Question(
        id="breath_exc_1",
        text=translate("breath_exc_1"),
        media="https://www.ddinstagram.com/reel/C7m4nqpOa3y/",
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
        options={translate('done'): "rerouting_exc_1"},
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
        media="",
        media_type="",
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
        options={},
        keyboard_type="",
        next_question_id="stress_question_end"
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
    "stress_question_end": Question(
        id="stress_question_end",
        text=translate("stress_question_end"),
        media="",
        media_type="",
        options={"1": "em_reg_1", "2": "em_reg_1", "3": "em_reg_1", "4": "em_reg_1", "5": "em_reg_1", "6": "em_reg_1", "7": "em_reg_1", "8": "em_reg_1", "9": "em_reg_1", "10": "em_reg_1"},
        keyboard_type="inline",
        next_question_id=""
    ),
    "em_reg_1": Question(
        id="em_reg_1",
        text=translate("em_reg_1"),
        media="https://www.ddinstagram.com/reel/C5qVMNRI3E0/",
        media_type="youtube",
        options={},
        keyboard_type="",
        next_question_id="task1_1"
    ),
    "task1_1": Question(
        id="task1_1",
        text=translate("task1_1"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task1_2"
    ),
    "task1_2": Question(
        id="task1_2",
        text=translate("task1_2"),
        media="",
        media_type="",
        options={},
        keyboard_type="",
        next_question_id="task1_3"
    ),
    "task1_3": Question(
        id="task1_3",
        text=translate("task1_3"),
        media="",
        media_type="",
        options={translate("task1_3_1"): "task1_4",
                 translate("task1_3_2"): "task1_4",
                 translate("task1_3_3"): "task1_4",
                 translate("task1_3_4"): "task1_4",
                 translate("task1_3_5"): "task1_4",
                 translate("task1_3_6"): "task1_4",
                 },
        keyboard_type="inline",
        next_question_id=""
    ),
    "task1_4": Question(
        id="task1_4",
        text=translate("task1_4"),
        media="",
        media_type="",
        options={translate("important-1"): "end_1", translate("important-2"): "end_1", translate("important-3"): "end_1",},
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
flow = Flow("flow4", questions, "alt_into")
