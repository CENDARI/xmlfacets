#!/usr/bin/env python
# -*- coding: utf-8 -*- 

ISO639 = {
    "aar": u"Afar", "aa": u"Afar",
    "abk": u"Abkhazian", "ab": u"Abkhazian",
    "ace": u"Achinese", 
    "ach": u"Acoli", 
    "ada": u"Adangme", 
    "ady": u"Adyghe; Adygei", 
    "afa": u"Afro-Asiatic languages", 
    "afh": u"Afrihili", 
    "afr": u"Afrikaans", "af": u"Afrikaans",
    "ain": u"Ainu", 
    "aka": u"Akan", "ak": u"Akan",
    "akk": u"Akkadian", 
    "alb": u"Albanian", "sqi": u"Albanian", "sq": u"Albanian",
    "ale": u"Aleut", 
    "alg": u"Algonquian languages", 
    "alt": u"Southern Altai", 
    "amh": u"Amharic", "am": u"Amharic",
    "ang": u"English, Old (ca.450-1100)", 
    "anp": u"Angika", 
    "apa": u"Apache languages", 
    "ara": u"Arabic", "ar": u"Arabic",
    "arc": u"Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)", 
    "arg": u"Aragonese", "an": u"Aragonese",
    "arm": u"Armenian", "hye": u"Armenian", "hy": u"Armenian",
    "arn": u"Mapudungun; Mapuche", 
    "arp": u"Arapaho", 
    "art": u"Artificial languages", 
    "arw": u"Arawak", 
    "asm": u"Assamese", "as": u"Assamese",
    "ast": u"Asturian; Bable; Leonese; Asturleonese", 
    "ath": u"Athapascan languages", 
    "aus": u"Australian languages", 
    "ava": u"Avaric", "av": u"Avaric",
    "ave": u"Avestan", "ae": u"Avestan",
    "awa": u"Awadhi", 
    "aym": u"Aymara", "ay": u"Aymara",
    "aze": u"Azerbaijani", "az": u"Azerbaijani",
    "bad": u"Banda languages", 
    "bai": u"Bamileke languages", 
    "bak": u"Bashkir", "ba": u"Bashkir",
    "bal": u"Baluchi", 
    "bam": u"Bambara", "bm": u"Bambara",
    "ban": u"Balinese", 
    "baq": u"Basque", "eus": u"Basque", "eu": u"Basque",
    "bas": u"Basa", 
    "bat": u"Baltic languages", 
    "bej": u"Beja; Bedawiyet", 
    "bel": u"Belarusian", "be": u"Belarusian",
    "bem": u"Bemba", 
    "ben": u"Bengali",
    "bn": u"Bengali",
    "ber": u"Berber languages", 
    "bho": u"Bhojpuri", 
    "bih": u"Bihari languages",
    "bh": u"Bihari languages",
    "bik": u"Bikol", 
    "bin": u"Bini; Edo", 
    "bis": u"Bislama",
    "bi": u"Bislama",
    "bla": u"Siksika", 
    "bnt": u"Bantu (Other)", 
    "bos": u"Bosnian",
    "bs": u"Bosnian",
    "bra": u"Braj", 
    "bre": u"Breton",
    "br": u"Breton",
    "btk": u"Batak languages", 
    "bua": u"Buriat", 
    "bug": u"Buginese", 
    "bul": u"Bulgarian",
    "bg": u"Bulgarian",
    "bur": u"Burmese", "mya": u"Burmese","my": u"Burmese",
    "byn": u"Blin; Bilin", 
    "cad": u"Caddo", 
    "cai": u"Central American Indian languages", 
    "car": u"Galibi Carib", 
    "cat": u"Catalan; Valencian",
    "ca": u"Catalan; Valencian",
    "cau": u"Caucasian languages", 
    "ceb": u"Cebuano", 
    "cel": u"Celtic languages", 
    "cha": u"Chamorro",
    "ch": u"Chamorro",
    "chb": u"Chibcha", 
    "che": u"Chechen",
    "ce": u"Chechen",
    "chg": u"Chagatai", 
    "chi": u"Chinese", "zho": u"Chinese","zh": u"Chinese",
    "chk": u"Chuukese", 
    "chm": u"Mari", 
    "chn": u"Chinook jargon", 
    "cho": u"Choctaw", 
    "chp": u"Chipewyan; Dene Suline", 
    "chr": u"Cherokee", 
    "chu": u"Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic",
    "cu": u"Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic",
    "chv": u"Chuvash",
    "cv": u"Chuvash",
    "chy": u"Cheyenne", 
    "cmc": u"Chamic languages", 
    "cop": u"Coptic", 
    "cor": u"Cornish",
    "kw": u"Cornish",
    "cos": u"Corsican",
    "co": u"Corsican",
    "cpe": u"Creoles and pidgins, English based", 
    "cpf": u"Creoles and pidgins, French-based ", 
    "cpp": u"Creoles and pidgins, Portuguese-based ", 
    "cre": u"Cree",
    "cr": u"Cree",
    "crh": u"Crimean Tatar; Crimean Turkish", 
    "crp": u"Creoles and pidgins ", 
    "csb": u"Kashubian", 
    "cus": u"Cushitic languages", 
    "cze": u"Czech", "ces": u"Czech","cs": u"Czech",
    "dak": u"Dakota", 
    "dan": u"Danish",
    "da": u"Danish",
    "dar": u"Dargwa", 
    "day": u"Land Dayak languages", 
    "del": u"Delaware", 
    "den": u"Slave (Athapascan)", 
    "dgr": u"Dogrib", 
    "din": u"Dinka", 
    "div": u"Divehi; Dhivehi; Maldivian",
    "dv": u"Divehi; Dhivehi; Maldivian",
    "doi": u"Dogri", 
    "dra": u"Dravidian languages", 
    "dsb": u"Lower Sorbian", 
    "dua": u"Duala", 
    "dum": u"Dutch, Middle (ca.1050-1350)", 
    "dut": u"Dutch; Flemish", "nld": u"Dutch; Flemish","nl": u"Dutch; Flemish",
    "dyu": u"Dyula", 
    "dzo": u"Dzongkha",
    "dz": u"Dzongkha",
    "efi": u"Efik", 
    "egy": u"Egyptian (Ancient)", 
    "eka": u"Ekajuk", 
    "elx": u"Elamite", 
    "eng": u"English",
    "en": u"English",
    "enm": u"English, Middle (1100-1500)", 
    "epo": u"Esperanto",
    "eo": u"Esperanto",
    "est": u"Estonian",
    "et": u"Estonian",
    "ewe": u"Ewe",
    "ee": u"Ewe",
    "ewo": u"Ewondo", 
    "fan": u"Fang", 
    "fao": u"Faroese",
    "fo": u"Faroese",
    "fat": u"Fanti", 
    "fij": u"Fijian",
    "fj": u"Fijian",
    "fil": u"Filipino; Pilipino", 
    "fin": u"Finnish",
    "fi": u"Finnish",
    "fiu": u"Finno-Ugrian languages", 
    "fon": u"Fon", 
    "fre": u"French", "fra": u"French","fr": u"French",
    "frm": u"French, Middle (ca.1400-1600)", 
    "fro": u"French, Old (842-ca.1400)", 
    "frr": u"Northern Frisian", 
    "frs": u"Eastern Frisian", 
    "fry": u"Western Frisian",
    "fy": u"Western Frisian",
    "ful": u"Fulah",
    "ff": u"Fulah",
    "fur": u"Friulian", 
    "gaa": u"Ga", 
    "gay": u"Gayo", 
    "gba": u"Gbaya", 
    "gem": u"Germanic languages", 
    "geo": u"Georgian", "kat": u"Georgian","ka": u"Georgian",
    "ger": u"German", "deu": u"German","de": u"German",
    "gez": u"Geez", 
    "gil": u"Gilbertese", 
    "gla": u"Gaelic; Scottish Gaelic",
    "gd": u"Gaelic; Scottish Gaelic",
    "gle": u"Irish",
    "ga": u"Irish",
    "glg": u"Galician",
    "gl": u"Galician",
    "glv": u"Manx",
    "gv": u"Manx",
    "gmh": u"German, Middle High (ca.1050-1500)", 
    "goh": u"German, Old High (ca.750-1050)", 
    "gon": u"Gondi", 
    "gor": u"Gorontalo", 
    "got": u"Gothic", 
    "grb": u"Grebo", 
    "grc": u"Greek, Ancient (to 1453)", 
    "gre": u"Greek, Modern (1453-)", "ell": u"Greek, Modern (1453-)","el": u"Greek, Modern (1453-)",
    "grn": u"Guarani",
    "gn": u"Guarani",
    "gsw": u"Swiss German; Alemannic; Alsatian", 
    "guj": u"Gujarati",
    "gu": u"Gujarati",
    "gwi": u"Gwich'in", 
    "hai": u"Haida", 
    "hat": u"Haitian; Haitian Creole",
    "ht": u"Haitian; Haitian Creole",
    "hau": u"Hausa",
    "ha": u"Hausa",
    "haw": u"Hawaiian", 
    "heb": u"Hebrew",
    "he": u"Hebrew",
    "her": u"Herero",
    "hz": u"Herero",
    "hil": u"Hiligaynon", 
    "him": u"Himachali languages; Western Pahari languages", 
    "hin": u"Hindi",
    "hi": u"Hindi",
    "hit": u"Hittite", 
    "hmn": u"Hmong; Mong", 
    "hmo": u"Hiri Motu",
    "ho": u"Hiri Motu",
    "hrv": u"Croatian",
    "hr": u"Croatian",
    "hsb": u"Upper Sorbian", 
    "hun": u"Hungarian",
    "hu": u"Hungarian",
    "hup": u"Hupa", 
    "iba": u"Iban", 
    "ibo": u"Igbo",
    "ig": u"Igbo",
    "ice": u"Icelandic", "isl": u"Icelandic","is": u"Icelandic",
    "ido": u"Ido",
    "io": u"Ido",
    "iii": u"Sichuan Yi; Nuosu",
    "ii": u"Sichuan Yi; Nuosu",
    "ijo": u"Ijo languages", 
    "iku": u"Inuktitut",
    "iu": u"Inuktitut",
    "ile": u"Interlingue; Occidental",
    "ie": u"Interlingue; Occidental",
    "ilo": u"Iloko", 
    "ina": u"Interlingua (International Auxiliary Language Association)",
    "ia": u"Interlingua (International Auxiliary Language Association)",
    "inc": u"Indic languages", 
    "ind": u"Indonesian",
    "id": u"Indonesian",
    "ine": u"Indo-European languages", 
    "inh": u"Ingush", 
    "ipk": u"Inupiaq",
    "ik": u"Inupiaq",
    "ira": u"Iranian languages", 
    "iro": u"Iroquoian languages", 
    "ita": u"Italian",
    "it": u"Italian",
    "jav": u"Javanese",
    "jv": u"Javanese",
    "jbo": u"Lojban", 
    "jpn": u"Japanese",
    "ja": u"Japanese",
    "jpr": u"Judeo-Persian", 
    "jrb": u"Judeo-Arabic", 
    "kaa": u"Kara-Kalpak", 
    "kab": u"Kabyle", 
    "kac": u"Kachin; Jingpho", 
    "kal": u"Kalaallisut; Greenlandic",
    "kl": u"Kalaallisut; Greenlandic",
    "kam": u"Kamba", 
    "kan": u"Kannada",
    "kn": u"Kannada",
    "kar": u"Karen languages", 
    "kas": u"Kashmiri",
    "ks": u"Kashmiri",
    "kau": u"Kanuri",
    "kr": u"Kanuri",
    "kaw": u"Kawi", 
    "kaz": u"Kazakh",
    "kk": u"Kazakh",
    "kbd": u"Kabardian", 
    "kha": u"Khasi", 
    "khi": u"Khoisan languages", 
    "khm": u"Central Khmer",
    "km": u"Central Khmer",
    "kho": u"Khotanese; Sakan", 
    "kik": u"Kikuyu; Gikuyu",
    "ki": u"Kikuyu; Gikuyu",
    "kin": u"Kinyarwanda",
    "rw": u"Kinyarwanda",
    "kir": u"Kirghiz; Kyrgyz",
    "ky": u"Kirghiz; Kyrgyz",
    "kmb": u"Kimbundu", 
    "kok": u"Konkani", 
    "kom": u"Komi",
    "kv": u"Komi",
    "kon": u"Kongo",
    "kg": u"Kongo",
    "kor": u"Korean",
    "ko": u"Korean",
    "kos": u"Kosraean", 
    "kpe": u"Kpelle", 
    "krc": u"Karachay-Balkar", 
    "krl": u"Karelian", 
    "kro": u"Kru languages", 
    "kru": u"Kurukh", 
    "kua": u"Kuanyama; Kwanyama",
    "kj": u"Kuanyama; Kwanyama",
    "kum": u"Kumyk", 
    "kur": u"Kurdish",
    "ku": u"Kurdish",
    "kut": u"Kutenai", 
    "lad": u"Ladino", 
    "lah": u"Lahnda", 
    "lam": u"Lamba", 
    "lao": u"Lao",
    "lo": u"Lao",
    "lat": u"Latin",
    "la": u"Latin",
    "lav": u"Latvian",
    "lv": u"Latvian",
    "lez": u"Lezghian", 
    "lim": u"Limburgan; Limburger; Limburgish",
    "li": u"Limburgan; Limburger; Limburgish",
    "lin": u"Lingala",
    "ln": u"Lingala",
    "lit": u"Lithuanian",
    "lt": u"Lithuanian",
    "lol": u"Mongo", 
    "loz": u"Lozi", 
    "ltz": u"Luxembourgish; Letzeburgesch",
    "lb": u"Luxembourgish; Letzeburgesch",
    "lua": u"Luba-Lulua", 
    "lub": u"Luba-Katanga",
    "lu": u"Luba-Katanga",
    "lug": u"Ganda",
    "lg": u"Ganda",
    "lui": u"Luiseno", 
    "lun": u"Lunda", 
    "luo": u"Luo (Kenya and Tanzania)", 
    "lus": u"Lushai", 
    "mac": u"Macedonian", "mkd": u"Macedonian","mk": u"Macedonian",
    "mad": u"Madurese", 
    "mag": u"Magahi", 
    "mah": u"Marshallese",
    "mh": u"Marshallese",
    "mai": u"Maithili", 
    "mak": u"Makasar", 
    "mal": u"Malayalam",
    "ml": u"Malayalam",
    "man": u"Mandingo", 
    "mao": u"Maori", "mri": u"Maori","mi": u"Maori",
    "map": u"Austronesian languages", 
    "mar": u"Marathi",
    "mr": u"Marathi",
    "mas": u"Masai", 
    "may": u"Malay", "msa": u"Malay","ms": u"Malay",
    "mdf": u"Moksha", 
    "mdr": u"Mandar", 
    "men": u"Mende", 
    "mga": u"Irish, Middle (900-1200)", 
    "mic": u"Mi'kmaq; Micmac", 
    "min": u"Minangkabau", 
    "mis": u"Uncoded languages", 
    "mkh": u"Mon-Khmer languages", 
    "mlg": u"Malagasy",
    "mg": u"Malagasy",
    "mlt": u"Maltese",
    "mt": u"Maltese",
    "mnc": u"Manchu", 
    "mni": u"Manipuri", 
    "mno": u"Manobo languages", 
    "moh": u"Mohawk", 
    "mon": u"Mongolian",
    "mn": u"Mongolian",
    "mos": u"Mossi", 
    "mul": u"Multiple languages", 
    "mun": u"Munda languages", 
    "mus": u"Creek", 
    "mwl": u"Mirandese", 
    "mwr": u"Marwari", 
    "myn": u"Mayan languages", 
    "myv": u"Erzya", 
    "nah": u"Nahuatl languages", 
    "nai": u"North American Indian languages", 
    "nap": u"Neapolitan", 
    "nau": u"Nauru",
    "na": u"Nauru",
    "nav": u"Navajo; Navaho",
    "nv": u"Navajo; Navaho",
    "nbl": u"Ndebele, South; South Ndebele",
    "nr": u"Ndebele, South; South Ndebele",
    "nde": u"Ndebele, North; North Ndebele",
    "nd": u"Ndebele, North; North Ndebele",
    "ndo": u"Ndonga",
    "ng": u"Ndonga",
    "nds": u"Low German; Low Saxon; German, Low; Saxon, Low", 
    "nep": u"Nepali",
    "ne": u"Nepali",
    "new": u"Nepal Bhasa; Newari", 
    "nia": u"Nias", 
    "nic": u"Niger-Kordofanian languages", 
    "niu": u"Niuean", 
    "nno": u"Norwegian Nynorsk; Nynorsk, Norwegian",
    "nn": u"Norwegian Nynorsk; Nynorsk, Norwegian",
    "nob": u"Bokmål, Norwegian; Norwegian Bokmål",
    "nb": u"Bokmål, Norwegian; Norwegian Bokmål",
    "nog": u"Nogai", 
    "non": u"Norse, Old", 
    "nor": u"Norwegian",
    "no": u"Norwegian",
    "nqo": u"N'Ko", 
    "nso": u"Pedi; Sepedi; Northern Sotho", 
    "nub": u"Nubian languages", 
    "nwc": u"Classical Newari; Old Newari; Classical Nepal Bhasa", 
    "nya": u"Chichewa; Chewa; Nyanja",
    "ny": u"Chichewa; Chewa; Nyanja",
    "nym": u"Nyamwezi", 
    "nyn": u"Nyankole", 
    "nyo": u"Nyoro", 
    "nzi": u"Nzima", 
    "oci": u"Occitan (post 1500); Provençal",
    "oc": u"Occitan (post 1500); Provençal",
    "oji": u"Ojibwa",
    "oj": u"Ojibwa",
    "ori": u"Oriya",
    "or": u"Oriya",
    "orm": u"Oromo",
    "om": u"Oromo",
    "osa": u"Osage", 
    "oss": u"Ossetian; Ossetic",
    "os": u"Ossetian; Ossetic",
    "ota": u"Turkish, Ottoman (1500-1928)", 
    "oto": u"Otomian languages", 
    "paa": u"Papuan languages", 
    "pag": u"Pangasinan", 
    "pal": u"Pahlavi", 
    "pam": u"Pampanga; Kapampangan", 
    "pan": u"Panjabi; Punjabi",
    "pa": u"Panjabi; Punjabi",
    "pap": u"Papiamento", 
    "pau": u"Palauan", 
    "peo": u"Persian, Old (ca.600-400 B.C.)", 
    "per": u"Persian", "fas": u"Persian","fa": u"Persian",
    "phi": u"Philippine languages", 
    "phn": u"Phoenician", 
    "pli": u"Pali",
    "pi": u"Pali",
    "pol": u"Polish",
    "pl": u"Polish",
    "pon": u"Pohnpeian", 
    "por": u"Portuguese",
    "pt": u"Portuguese",
    "pra": u"Prakrit languages", 
    "pro": u"Provençal, Old (to 1500)", 
    "pus": u"Pushto; Pashto",
    "ps": u"Pushto; Pashto",
    "qaa": u"Reserved for local use", 
    "qtz": u"Reserved for local use", 
    "que": u"Quechua",
    "qu": u"Quechua",
    "raj": u"Rajasthani", 
    "rap": u"Rapanui", 
    "rar": u"Rarotongan; Cook Islands Maori", 
    "roa": u"Romance languages", 
    "roh": u"Romansh",
    "rm": u"Romansh",
    "rom": u"Romany", 
    "rum": u"Romanian; Moldavian; Moldovan", "ron": u"Romanian; Moldavian; Moldovan","ro": u"Romanian; Moldavian; Moldovan",
    "run": u"Rundi",
    "rn": u"Rundi",
    "rup": u"Aromanian; Arumanian; Macedo-Romanian", 
    "rus": u"Russian",
    "ru": u"Russian",
    "sad": u"Sandawe", 
    "sag": u"Sango",
    "sg": u"Sango",
    "sah": u"Yakut", 
    "sai": u"South American Indian (Other)", 
    "sal": u"Salishan languages", 
    "sam": u"Samaritan Aramaic", 
    "san": u"Sanskrit",
    "sa": u"Sanskrit",
    "sas": u"Sasak", 
    "sat": u"Santali", 
    "scn": u"Sicilian", 
    "sco": u"Scots", 
    "sel": u"Selkup", 
    "sem": u"Semitic languages", 
    "sga": u"Irish, Old (to 900)", 
    "sgn": u"Sign Languages", 
    "shn": u"Shan", 
    "sid": u"Sidamo", 
    "sin": u"Sinhala; Sinhalese",
    "si": u"Sinhala; Sinhalese",
    "sio": u"Siouan languages", 
    "sit": u"Sino-Tibetan languages", 
    "sla": u"Slavic languages", 
    "slo": u"Slovak", "slk": u"Slovak","sk": u"Slovak",
    "slv": u"Slovenian",
    "sl": u"Slovenian",
    "sma": u"Southern Sami", 
    "sme": u"Northern Sami",
    "se": u"Northern Sami",
    "smi": u"Sami languages", 
    "smj": u"Lule Sami", 
    "smn": u"Inari Sami", 
    "smo": u"Samoan",
    "sm": u"Samoan",
    "sms": u"Skolt Sami", 
    "sna": u"Shona",
    "sn": u"Shona",
    "snd": u"Sindhi",
    "sd": u"Sindhi",
    "snk": u"Soninke", 
    "sog": u"Sogdian", 
    "som": u"Somali",
    "so": u"Somali",
    "son": u"Songhai languages", 
    "sot": u"Sotho, Southern",
    "st": u"Sotho, Southern",
    "spa": u"Spanish; Castilian",
    "es": u"Spanish; Castilian",
    "srd": u"Sardinian",
    "sc": u"Sardinian",
    "srn": u"Sranan Tongo", 
    "srp": u"Serbian",
    "sr": u"Serbian",
    "srr": u"Serer", 
    "ssa": u"Nilo-Saharan languages", 
    "ssw": u"Swati",
    "ss": u"Swati",
    "suk": u"Sukuma", 
    "sun": u"Sundanese",
    "su": u"Sundanese",
    "sus": u"Susu", 
    "sux": u"Sumerian", 
    "swa": u"Swahili",
    "sw": u"Swahili",
    "swe": u"Swedish",
    "sv": u"Swedish",
    "syc": u"Classical Syriac", 
    "syr": u"Syriac", 
    "tah": u"Tahitian",
    "ty": u"Tahitian",
    "tai": u"Tai languages", 
    "tam": u"Tamil",
    "ta": u"Tamil",
    "tat": u"Tatar",
    "tt": u"Tatar",
    "tel": u"Telugu",
    "te": u"Telugu",
    "tem": u"Timne", 
    "ter": u"Tereno", 
    "tet": u"Tetum", 
    "tgk": u"Tajik",
    "tg": u"Tajik",
    "tgl": u"Tagalog",
    "tl": u"Tagalog",
    "tha": u"Thai",
    "th": u"Thai",
    "tib": u"Tibetan", "bod": u"Tibetan","bo": u"Tibetan",
    "tig": u"Tigre", 
    "tir": u"Tigrinya",
    "ti": u"Tigrinya",
    "tiv": u"Tiv", 
    "tkl": u"Tokelau", 
    "tlh": u"Klingon; tlhIngan-Hol", 
    "tli": u"Tlingit", 
    "tmh": u"Tamashek", 
    "tog": u"Tonga (Nyasa)", 
    "ton": u"Tonga (Tonga Islands)",
    "to": u"Tonga (Tonga Islands)",
    "tpi": u"Tok Pisin", 
    "tsi": u"Tsimshian", 
    "tsn": u"Tswana",
    "tn": u"Tswana",
    "tso": u"Tsonga",
    "ts": u"Tsonga",
    "tuk": u"Turkmen",
    "tk": u"Turkmen",
    "tum": u"Tumbuka", 
    "tup": u"Tupi languages", 
    "tur": u"Turkish",
    "tr": u"Turkish",
    "tut": u"Altaic languages", 
    "tvl": u"Tuvalu", 
    "twi": u"Twi",
    "tw": u"Twi",
    "tyv": u"Tuvinian", 
    "udm": u"Udmurt", 
    "uga": u"Ugaritic", 
    "uig": u"Uighur; Uyghur",
    "ug": u"Uighur; Uyghur",
    "ukr": u"Ukrainian",
    "uk": u"Ukrainian",
    "umb": u"Umbundu", 
    "und": u"Undetermined", 
    "urd": u"Urdu",
    "ur": u"Urdu",
    "uzb": u"Uzbek",
    "uz": u"Uzbek",
    "vai": u"Vai", 
    "ven": u"Venda",
    "ve": u"Venda",
    "vie": u"Vietnamese",
    "vi": u"Vietnamese",
    "vol": u"Volapük",
    "vo": u"Volapük",
    "vot": u"Votic", 
    "wak": u"Wakashan languages", 
    "wal": u"Walamo", 
    "war": u"Waray", 
    "was": u"Washo", 
    "wel": u"Welsh", "cym": u"Welsh","cy": u"Welsh",
    "wen": u"Sorbian languages", 
    "wln": u"Walloon",
    "wa": u"Walloon",
    "wol": u"Wolof",
    "wo": u"Wolof",
    "xal": u"Kalmyk; Oirat", 
    "xho": u"Xhosa",
    "xh": u"Xhosa",
    "yao": u"Yao", 
    "yap": u"Yapese", 
    "yid": u"Yiddish",
    "yi": u"Yiddish",
    "yor": u"Yoruba",
    "yo": u"Yoruba",
    "ypk": u"Yupik languages", 
    "zap": u"Zapotec", 
    "zbl": u"Blissymbols; Blissymbolics; Bliss", 
    "zen": u"Zenaga", 
    "zgh": u"Standard Moroccan Tamazight", 
    "zha": u"Zhuang; Chuang",
    "za": u"Zhuang; Chuang",
    "znd": u"Zande languages", 
    "zul": u"Zulu",
    "zu": u"Zulu",
    "zun": u"Zuni", 
    "zxx": u"No linguistic content; Not applicable", 
    "zza": u"Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki", 
}
