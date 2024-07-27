from Flow import Flow
from Question import Question
import i18n

translator = i18n.Translator('data')

q1 = Question("intro1", "أهلا وسهلا فيك بمساحة نَفَس. \n هيّأنا هالمحل ليكون ملجأك وبيتك بهالفترة الصعبة, اللي تلجأله لما بدك تنقطع عن هالعالم لاكم دقيقة وتوخذ نفس. \n فأستعد لتغمر نفسك بتجربة جديدة من نوعها اللي من خلال فعاليّات بسيطة راح تساعدك تخفف التوتر وتدير التحديّات القادمة بشكل انجع.", "", [])
q2 = Question("intro2", "منتمنالك تجربة ممتعة وغنيّة اللي فيها تطلع الماكسيموم وتطوّر من نفسك!", "", [])
q3 = Question("intro3", " بدك تتعامل بشكل افضل مع التوتر والتحدايّات؟ ", "", ["اه، اكيد 💪"])
q4 = Question("intro4", "زي مبتعرف, اي تغيّير وتطوّر, بحاجة لجهد ومثابرة!  مستعد تعطيه هالفرصة ؟\n اوعد نفسك عن طريق صورة لأيدك مع اشارة النصر:  ✌🏻","", ["بوعد نفسي"])
q5 = Question("intro5", "شكرا وهيك ممكن نبدا رحلتنا \n ٣ نقاط مهمات قبل لنبدأ:","", [])
q6 = Question("intro6", "هالأدوات اللي راح تشوفها مبينة على عشرات السنين من الابحاث من معاهد مرموقة. ", "", [])
q7 = Question("intro7", "مفش صح وغلط بهالتجربة!", "", [])
q8 = Question("intro8", "اعطي التغيير فرصة: خذلك نفس ل7 دقايق كل يوم ,لمدة 7 ايام \nراح تلاحظ بالايام القريبة تأثير الخطوات الصغيرة اللي كل يوم بتوخذها. \nجاهز تلتزم؟ :","", ["قول جاهز🎤"])
#q5 = Question("intro8","٣ نقاط مهمات قبل لنبدأ:","هالأدوات اللي راح تشوفها مبينة على عشرات السنين من الابحاث من معاهد مرموقة. ", [])
#q5 = Question("intro5","٣ نقاط مهمات قبل لنبدأ:","هالأدوات اللي راح تشوفها مبينة على عشرات السنين من الابحاث من معاهد مرموقة. ", [])
#q5 = Question("intro5","٣ نقاط مهمات قبل لنبدأ:","هالأدوات اللي راح تشوفها مبينة على عشرات السنين من الابحاث من معاهد مرموقة. ", [])
flow = Flow([q1, q2, q3, q4, q5, q6, q7, q8])

# q1 ([next questions])
#