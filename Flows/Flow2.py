from Flow import Flow
from Question import Question
import i18n

translator = i18n.Translator('data')

q1 = Question("intro1",
              "أهلا وسهلا فيك بمساحة نَفَس. \n هيّأنا هالمحل ليكون ملجأك وبيتك بهالفترة الصعبة, اللي تلجأله لما بدك تنقطع عن هالعالم لاكم دقيقة وتوخذ نفس. \n فأستعد لتغمر نفسك بتجربة جديدة من نوعها اللي من خلال فعاليّات بسيطة راح تساعدك تخفف التوتر وتدير التحديّات القادمة بشكل انجع.",
              "", [])
q2 = Question("intro2", "منتمنالك تجربة ممتعة وغنيّة اللي فيها تطلع الماكسيموم وتطوّر من نفسك!", "", [])
q3 = Question("intro3", " بدك تتعامل بشكل افضل مع التوتر والتحدايّات؟ ", "", ["اه، اكيد 💪"])
q4 = Question("intro4",
              "زي مبتعرف, اي تغيّير وتطوّر, بحاجة لجهد ومثابرة!  مستعد تعطيه هالفرصة ؟\n اوعد نفسك عن طريق صورة لأيدك مع اشارة النصر:  ✌🏻",
              "", ["بوعد نفسي"])
q5 = Question("intro5", "شكرا وهيك ممكن نبدا رحلتنا \n ٣ نقاط مهمات قبل لنبدأ:", "", [])
q6 = Question("intro6", "هالأدوات اللي راح تشوفها مبينة على عشرات السنين من الابحاث من معاهد مرموقة. ", "logos.jpeg", [])
q7 = Question("intro7", "مفش صح وغلط بهالتجربة!", "", [])
q8 = Question("intro8",
              "اعطي التغيير فرصة: خذلك نفس ل7 دقايق كل يوم ,لمدة 7 ايام \nراح تلاحظ بالايام القريبة تأثير الخطوات الصغيرة اللي كل يوم بتوخذها. \nجاهز تلتزم؟",
              "", ["قول جاهز🎤"])
q9 = Question("stress1", translator.translate('stress_question'), "", [translator.translate('stress_option1'),
                                                                       translator.translate('stress_option2'),
                                                                       translator.translate('stress_option3')])

q10 = Question("exc1", "[ ](https://www.youtube.com/shorts/9JhTMTksk9s)التمرين الاول", "", [])
q16 = Question("exc1_1", "جاهز نعمل التمرين مع بعض؟ ", "", ["يللا 💪🏻"])

q11 = Question("exc1_2", "1. خذ نفس عميق وسريع من أنفك. قديش اكثر يملّي رئتيك \n  2. بدون متطلع الهوا, خذ كمان واحد صغير بعديه \n 3.وبشكل بطيئ (ابطئ من وقت النفسين اللي قبل) اطلع الهوا من خلال الثم", "", ["عملتها 💪"])
q12 = Question("exc1_3", "اعمل التمرين كمان مرتين", "", [])
q13 = Question("exc1_4", "خلصت؟", "", ["اه, يللا اللي بعدو"])
q14 = Question("exc2", "تمام, لكان عد معنا بالعكس من 30 ل 1 بعقلك, او افضل بصوت منخفض اذا بزبط معك \nبس تكون جاهز اضغط الزر جاهز", "", ["جاهز"])
q15 = Question("exc2_1", "", "Countdown.mp4", [])
q16 = Question("exc2_2", "انهيت العد", "", ["اه, يللا اللي بعدو"])
q17 = Question("exc2_3", "حلو, هيك صرت جاهز للمرحلة اللي بعدها", "", [])
q18 = Question("exc2_4", "هاي الفقرة بتحتاج سماعات اذن لحتى تطلع اكبر فائده منها. \n .من فضلك وصلّ سماعات الاذن بجهازك", "", ["جاهز ✅ "])
q19 = Question("exc3", "[ ](https://www.youtube.com/watch?v=1N1vtQQ9ij0)التمرين الثالث", "", [])
q20 = Question("exc3_1", " بعد مسمعت الشرح. جاهز لتخوض التجربة؟", "", ["يللا"])
q21 = Question("exc3_2", "[ ](https://www.youtube.com/watch?v=UfcAVejslrU)شغّل الفيديو, سكّر عيونك, وركّز بالصوت", "", [])
q22 = Question("exc3_3", "انهيت التمرين", "", ["انهيته"])
q23 = Question("end", "كيف حاسس اسا؟\nمن 1-10 قديش مستوى التوتر  باللحظه الحالية", "", [])
q24 = Question("end_1", "!كل الاحترام, منهنّيك على مجهود اليوم", "end.webp", [])


flow = Flow([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24])
