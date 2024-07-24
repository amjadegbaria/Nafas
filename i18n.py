from babel.plural import PluralRule
import json
from string import Template
import glob
import os
import yaml
from datetime import datetime
from babel.dates import format_datetime

supported_format = ['json', 'yaml']


class Translator():
    def __init__(self, translations_folder, file_format='json', default_locale='ar'):
        # initialization
        self.data = {}
        self.locale = 'ar'
        self.plural_rule = PluralRule({'one': 'n is 1'})

        # check if format is supported
        if file_format in supported_format:
            # get list of files with specific extensions
            files = glob.glob(os.path.join(translations_folder, f'*.{file_format}'))
            for fil in files:
                # get the name of the file without extension, will be used as locale name
                loc = os.path.splitext(os.path.basename(fil))[0]
                with open(fil, 'r', encoding='utf8') as f:
                    if file_format == 'json':
                        self.data[loc] = json.load(f)
                    elif file_format == 'yaml':
                        self.data[loc] = yaml.safe_load(f)

    def set_locale(self, loc):
        if loc in self.data:
            self.locale = loc
        else:
            print('Invalid locale')

    def get_locale(self):
        return self.locale

    def set_plural_rule(self, rule):
        try:
            self.plural_rule = PluralRule(rule)
        except Exception:
            print('Invalid plural rule')

    def get_plural_rule(self):
        return self.plural_rule

    def translate(self, key, **kwargs):
        # return the key instead of translation text if locale is not supported
        if self.locale not in self.data:
            return key

        text = self.data[self.locale].get(key, key)
        # type dict represents key with plural form
        if type(text) == dict:
            count = kwargs.get('count', 1)
            # parse count to int
            try:
                count = int(count)
            except Exception:
                print('Invalid count')
                return key
            text = text.get(self.plural_rule(count), key)
        return Template(text).safe_substitute(**kwargs)


def parse_datetime(dt, input_format='%Y-%m-%d', output_format='MMMM dd, yyyy', output_locale='en'):
    dt = datetime.strptime(dt, input_format)
    return format_datetime(dt, format=output_format, locale=output_locale)