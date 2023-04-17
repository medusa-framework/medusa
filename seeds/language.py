from flask_seeder import Seeder
from modules.app.base.seeders.base import BaseSeeder
from config.app import db
from modules.app.language.models.language import Language


class LanguageSeeder(BaseSeeder, Seeder):
    def __init__(self):
        self.priority = 10
        self._class = Language
        super().__init__(db=db)

    def seeds(self):
        return [
            {
                "iso_639_1": "xx",
                "english_name": "No Language",
                "name": "No Language",
            },
            {
                "iso_639_1": "aa",
                "english_name": "Afar"
            },
            {
                "iso_639_1": "af",
                "english_name": "Afrikaans",
                "name": "Afrikaans",
            },
            {
                "iso_639_1": "ak",
                "english_name": "Akan"
            },
            {
                "iso_639_1": "an",
                "english_name": "Aragonese"
            },
            {
                "iso_639_1": "as",
                "english_name": "Assamese"
            },
            {
                "iso_639_1": "av",
                "english_name": "Avaric"
            },
            {
                "iso_639_1": "ae",
                "english_name": "Avestan"
            },
            {
                "iso_639_1": "ay",
                "english_name": "Aymara"
            },
            {
                "iso_639_1": "az",
                "english_name": "Azerbaijani",
                "name": "Azərbaycan",
            },
            {
                "iso_639_1": "ba",
                "english_name": "Bashkir"
            },
            {
                "iso_639_1": "bm",
                "english_name": "Bambara",
                "name": "Bamanankan",
            },
            {
                "iso_639_1": "bi",
                "english_name": "Bislama"
            },
            {
                "iso_639_1": "bo",
                "english_name": "Tibetan"
            },
            {
                "iso_639_1": "br",
                "english_name": "Breton"
            },
            {
                "iso_639_1": "ca",
                "english_name": "Catalan",
                "name": "Català",
            },
            {
                "iso_639_1": "cs",
                "english_name": "Czech",
                "name": "Český",
            },
            {
                "iso_639_1": "ce",
                "english_name": "Chechen"
            },
            {
                "iso_639_1": "cu",
                "english_name": "Slavic"
            },
            {
                "iso_639_1": "cv",
                "english_name": "Chuvash"
            },
            {
                "iso_639_1": "kw",
                "english_name": "Cornish"
            },
            {
                "iso_639_1": "co",
                "english_name": "Corsican"
            },
            {
                "iso_639_1": "cr",
                "english_name": "Cree"
            },
            {
                "iso_639_1": "cy",
                "english_name": "Welsh",
                "name": "Cymraeg",
            },
            {
                "iso_639_1": "da",
                "english_name": "Danish",
                "name": "Dansk",
            },
            {
                "iso_639_1": "de",
                "english_name": "German",
                "name": "Deutsch",
            },
            {
                "iso_639_1": "dv",
                "english_name": "Divehi"
            },
            {
                "iso_639_1": "dz",
                "english_name": "Dzongkha"
            },
            {
                "iso_639_1": "eo",
                "english_name": "Esperanto",
                "name": "Esperanto",
            },
            {
                "iso_639_1": "et",
                "english_name": "Estonian",
                "name": "Eesti",
            },
            {
                "iso_639_1": "eu",
                "english_name": "Basque",
                "name": "euskera",
            },
            {
                "iso_639_1": "fo",
                "english_name": "Faroese"
            },
            {
                "iso_639_1": "fj",
                "english_name": "Fijian"
            },
            {
                "iso_639_1": "fi",
                "english_name": "Finnish",
                "name": "suomi",
            },
            {
                "iso_639_1": "fr",
                "english_name": "French",
                "name": "Français",
            },
            {
                "iso_639_1": "fy",
                "english_name": "Frisian"
            },
            {
                "iso_639_1": "ff",
                "english_name": "Fulah",
                "name": "Fulfulde",
            },
            {
                "iso_639_1": "gd",
                "english_name": "Gaelic"
            },
            {
                "iso_639_1": "ga",
                "english_name": "Irish",
                "name": "Gaeilge",
            },
            {
                "iso_639_1": "gl",
                "english_name": "Galician",
                "name": "Galego",
            },
            {
                "iso_639_1": "gv",
                "english_name": "Manx"
            },
            {
                "iso_639_1": "gn",
                "english_name": "Guarani"
            },
            {
                "iso_639_1": "gu",
                "english_name": "Gujarati"
            },
            {
                "iso_639_1": "ht",
                "english_name": "Haitian; Haitian Creole"
            },
            {
                "iso_639_1": "ha",
                "english_name": "Hausa",
                "name": "Hausa",
            },
            {
                "iso_639_1": "sh",
                "english_name": "Serbo-Croatian"
            },
            {
                "iso_639_1": "hz",
                "english_name": "Herero"
            },
            {
                "iso_639_1": "ho",
                "english_name": "Hiri Motu"
            },
            {
                "iso_639_1": "hr",
                "english_name": "Croatian",
                "name": "Hrvatski",
            },
            {
                "iso_639_1": "hu",
                "english_name": "Hungarian",
                "name": "Magyar",
            },
            {
                "iso_639_1": "ig",
                "english_name": "Igbo"
            },
            {
                "iso_639_1": "io",
                "english_name": "Ido"
            },
            {
                "iso_639_1": "ii",
                "english_name": "Yi"
            },
            {
                "iso_639_1": "iu",
                "english_name": "Inuktitut"
            },
            {
                "iso_639_1": "ie",
                "english_name": "Interlingue"
            },
            {
                "iso_639_1": "ia",
                "english_name": "Interlingua"
            },
            {
                "iso_639_1": "id",
                "english_name": "Indonesian",
                "name": "Bahasa indonesia",
            },
            {
                "iso_639_1": "ik",
                "english_name": "Inupiaq"
            },
            {
                "iso_639_1": "is",
                "english_name": "Icelandic",
                "name": "Íslenska",
            },
            {
                "iso_639_1": "it",
                "english_name": "Italian",
                "name": "Italiano",
            },
            {
                "iso_639_1": "jv",
                "english_name": "Javanese"
            },
            {
                "iso_639_1": "ja",
                "english_name": "Japanese",
                "name": "日本語",
            },
            {
                "iso_639_1": "kl",
                "english_name": "Kalaallisut"
            },
            {
                "iso_639_1": "kn",
                "english_name": "Kannada",
                "name": "?????",
            },
            {
                "iso_639_1": "ks",
                "english_name": "Kashmiri"
            },
            {
                "iso_639_1": "kr",
                "english_name": "Kanuri"
            },
            {
                "iso_639_1": "kk",
                "english_name": "Kazakh",
                "name": "қазақ",
            },
            {
                "iso_639_1": "km",
                "english_name": "Khmer"
            },
            {
                "iso_639_1": "ki",
                "english_name": "Kikuyu"
            },
            {
                "iso_639_1": "rw",
                "english_name": "Kinyarwanda",
                "name": "Kinyarwanda",
            },
            {
                "iso_639_1": "ky",
                "english_name": "Kirghiz",
                "name": "??????",
            },
            {
                "iso_639_1": "kv",
                "english_name": "Komi"
            },
            {
                "iso_639_1": "kg",
                "english_name": "Kongo"
            },
            {
                "iso_639_1": "ko",
                "english_name": "Korean",
                "name": "한국어/조선말",
            },
            {
                "iso_639_1": "kj",
                "english_name": "Kuanyama"
            },
            {
                "iso_639_1": "ku",
                "english_name": "Kurdish"
            },
            {
                "iso_639_1": "lo",
                "english_name": "Lao"
            },
            {
                "iso_639_1": "la",
                "english_name": "Latin",
                "name": "Latin",
            },
            {
                "iso_639_1": "lv",
                "english_name": "Latvian",
                "name": "Latviešu",
            },
            {
                "iso_639_1": "li",
                "english_name": "Limburgish"
            },
            {
                "iso_639_1": "ln",
                "english_name": "Lingala"
            },
            {
                "iso_639_1": "lt",
                "english_name": "Lithuanian",
                "name": "Lietuvių",
            },
            {
                "iso_639_1": "lb",
                "english_name": "Letzeburgesch"
            },
            {
                "iso_639_1": "lu",
                "english_name": "Luba-Katanga"
            },
            {
                "iso_639_1": "lg",
                "english_name": "Ganda"
            },
            {
                "iso_639_1": "mh",
                "english_name": "Marshall"
            },
            {
                "iso_639_1": "ml",
                "english_name": "Malayalam"
            },
            {
                "iso_639_1": "mr",
                "english_name": "Marathi"
            },
            {
                "iso_639_1": "mg",
                "english_name": "Malagasy"
            },
            {
                "iso_639_1": "mt",
                "english_name": "Maltese",
                "name": "Malti",
            },
            {
                "iso_639_1": "mo",
                "english_name": "Moldavian"
            },
            {
                "iso_639_1": "mn",
                "english_name": "Mongolian"
            },
            {
                "iso_639_1": "mi",
                "english_name": "Maori"
            },
            {
                "iso_639_1": "ms",
                "english_name": "Malay",
                "name": "Bahasa melayu",
            },
            {
                "iso_639_1": "my",
                "english_name": "Burmese"
            },
            {
                "iso_639_1": "na",
                "english_name": "Nauru"
            },
            {
                "iso_639_1": "nv",
                "english_name": "Navajo"
            },
            {
                "iso_639_1": "nr",
                "english_name": "Ndebele"
            },
            {
                "iso_639_1": "nd",
                "english_name": "Ndebele"
            },
            {
                "iso_639_1": "ng",
                "english_name": "Ndonga"
            },
            {
                "iso_639_1": "ne",
                "english_name": "Nepali"
            },
            {
                "iso_639_1": "nl",
                "english_name": "Dutch",
                "name": "Nederlands",
            },
            {
                "iso_639_1": "nn",
                "english_name": "Norwegian Nynorsk"
            },
            {
                "iso_639_1": "nb",
                "english_name": "Norwegian Bokmål",
                "name": "Bokmål",
            },
            {
                "iso_639_1": "no",
                "english_name": "Norwegian",
                "name": "Norsk",
            },
            {
                "iso_639_1": "ny",
                "english_name": "Chichewa; Nyanja"
            },
            {
                "iso_639_1": "oc",
                "english_name": "Occitan"
            },
            {
                "iso_639_1": "oj",
                "english_name": "Ojibwa"
            },
            {
                "iso_639_1": "or",
                "english_name": "Oriya"
            },
            {
                "iso_639_1": "om",
                "english_name": "Oromo"
            },
            {
                "iso_639_1": "os",
                "english_name": "Ossetian; Ossetic"
            },
            {
                "iso_639_1": "pi",
                "english_name": "Pali"
            },
            {
                "iso_639_1": "pl",
                "english_name": "Polish",
                "name": "Polski",
            },
            {
                "iso_639_1": "pt",
                "english_name": "Portuguese",
                "name": "Português",
            },
            {
                "iso_639_1": "qu",
                "english_name": "Quechua"
            },
            {
                "iso_639_1": "rm",
                "english_name": "Raeto-Romance"
            },
            {
                "iso_639_1": "ro",
                "english_name": "Romanian",
                "name": "Română",
            },
            {
                "iso_639_1": "rn",
                "english_name": "Rundi",
                "name": "Kirundi",
            },
            {
                "iso_639_1": "ru",
                "english_name": "Russian",
                "name": "Pусский",
            },
            {
                "iso_639_1": "sg",
                "english_name": "Sango"
            },
            {
                "iso_639_1": "sa",
                "english_name": "Sanskrit"
            },
            {
                "iso_639_1": "si",
                "english_name": "Sinhalese",
                "name": "සිංහල",
            },
            {
                "iso_639_1": "sk",
                "english_name": "Slovak",
                "name": "Slovenčina",
            },
            {
                "iso_639_1": "sl",
                "english_name": "Slovenian",
                "name": "Slovenščina",
            },
            {
                "iso_639_1": "se",
                "english_name": "Northern Sami"
            },
            {
                "iso_639_1": "sm",
                "english_name": "Samoan"
            },
            {
                "iso_639_1": "sn",
                "english_name": "Shona"
            },
            {
                "iso_639_1": "sd",
                "english_name": "Sindhi"
            },
            {
                "iso_639_1": "so",
                "english_name": "Somali",
                "name": "Somali",
            },
            {
                "iso_639_1": "st",
                "english_name": "Sotho"
            },
            {
                "iso_639_1": "es",
                "english_name": "Spanish",
                "name": "Español",
            },
            {
                "iso_639_1": "sq",
                "english_name": "Albanian",
                "name": "shqip",
            },
            {
                "iso_639_1": "sc",
                "english_name": "Sardinian"
            },
            {
                "iso_639_1": "sr",
                "english_name": "Serbian",
                "name": "Srpski",
            },
            {
                "iso_639_1": "ss",
                "english_name": "Swati"
            },
            {
                "iso_639_1": "su",
                "english_name": "Sundanese"
            },
            {
                "iso_639_1": "sw",
                "english_name": "Swahili",
                "name": "Kiswahili",
            },
            {
                "iso_639_1": "sv",
                "english_name": "Swedish",
                "name": "svenska",
            },
            {
                "iso_639_1": "ty",
                "english_name": "Tahitian"
            },
            {
                "iso_639_1": "ta",
                "english_name": "Tamil",
                "name": "தமிழ்",
            },
            {
                "iso_639_1": "tt",
                "english_name": "Tatar"
            },
            {
                "iso_639_1": "te",
                "english_name": "Telugu",
                "name": "తెలుగు",
            },
            {
                "iso_639_1": "tg",
                "english_name": "Tajik"
            },
            {
                "iso_639_1": "tl",
                "english_name": "Tagalog"
            },
            {
                "iso_639_1": "th",
                "english_name": "Thai",
                "name": "ภาษาไทย",
            },
            {
                "iso_639_1": "ti",
                "english_name": "Tigrinya"
            },
            {
                "iso_639_1": "to",
                "english_name": "Tonga"
            },
            {
                "iso_639_1": "tn",
                "english_name": "Tswana"
            },
            {
                "iso_639_1": "ts",
                "english_name": "Tsonga"
            },
            {
                "iso_639_1": "tk",
                "english_name": "Turkmen"
            },
            {
                "iso_639_1": "tr",
                "english_name": "Turkish",
                "name": "Türkçe",
            },
            {
                "iso_639_1": "tw",
                "english_name": "Twi"
            },
            {
                "iso_639_1": "ug",
                "english_name": "Uighur"
            },
            {
                "iso_639_1": "uk",
                "english_name": "Ukrainian",
                "name": "Український",
            },
            {
                "iso_639_1": "ur",
                "english_name": "Urdu",
                "name": "اردو",
            },
            {
                "iso_639_1": "uz",
                "english_name": "Uzbek",
                "name": "ozbek",
            },
            {
                "iso_639_1": "ve",
                "english_name": "Venda"
            },
            {
                "iso_639_1": "vi",
                "english_name": "Vietnamese",
                "name": "Tiếng Việt",
            },
            {
                "iso_639_1": "vo",
                "english_name": "Volapük"
            },
            {
                "iso_639_1": "wa",
                "english_name": "Walloon"
            },
            {
                "iso_639_1": "wo",
                "english_name": "Wolof",
                "name": "Wolof",
            },
            {
                "iso_639_1": "xh",
                "english_name": "Xhosa"
            },
            {
                "iso_639_1": "yi",
                "english_name": "Yiddish"
            },
            {
                "iso_639_1": "za",
                "english_name": "Zhuang"
            },
            {
                "iso_639_1": "zu",
                "english_name": "Zulu",
                "name": "isiZulu",
            },
            {
                "iso_639_1": "ab",
                "english_name": "Abkhazian"
            },
            {
                "iso_639_1": "zh",
                "english_name": "Mandarin",
                "name": "普通话",
            },
            {
                "iso_639_1": "ps",
                "english_name": "Pushto",
                "name": "پښتو",
            },
            {
                "iso_639_1": "am",
                "english_name": "Amharic"
            },
            {
                "iso_639_1": "ar",
                "english_name": "Arabic",
                "name": "العربية",
            },
            {
                "iso_639_1": "bg",
                "english_name": "Bulgarian",
                "name": "български език",
            },
            {
                "iso_639_1": "cn",
                "english_name": "Cantonese",
                "name": "广州话 / 廣州話",
            },
            {
                "iso_639_1": "mk",
                "english_name": "Macedonian"
            },
            {
                "iso_639_1": "el",
                "english_name": "Greek",
                "name": "ελληνικά",
            },
            {
                "iso_639_1": "fa",
                "english_name": "Persian",
                "name": "فارسی",
            },
            {
                "iso_639_1": "he",
                "english_name": "Hebrew",
                "name": "עִבְרִית",
            },
            {
                "iso_639_1": "hi",
                "english_name": "Hindi",
                "name": "हिन्दी",
            },
            {
                "iso_639_1": "hy",
                "english_name": "Armenian"
            },
            {
                "iso_639_1": "en",
                "english_name": "English",
                "name": "English",
            },
            {
                "iso_639_1": "ee",
                "english_name": "Ewe",
                "name": "Èʋegbe",
            },
            {
                "iso_639_1": "ka",
                "english_name": "Georgian",
                "name": "ქართული",
            },
            {
                "iso_639_1": "pa",
                "english_name": "Punjabi",
                "name": "ਪੰਜਾਬੀ",
            },
            {
                "iso_639_1": "bn",
                "english_name": "Bengali",
                "name": "বাংলা",
            },
            {
                "iso_639_1": "bs",
                "english_name": "Bosnian",
                "name": "Bosanski",
            },
            {
                "iso_639_1": "ch",
                "english_name": "Chamorro",
                "name": "Finu' Chamorro",
            },
            {
                "iso_639_1": "be",
                "english_name": "Belarusian",
                "name": "беларуская мова",
            },
            {
                "iso_639_1": "yo",
                "english_name": "Yoruba",
                "name": "Èdè Yorùbá",
            }
        ]
