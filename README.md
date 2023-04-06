# Got Stop Words

## Introduction

This Python package makes it easy to use **stop words** lists in Python projects. The set of lists contained within the package reflect an organization of lists collected across the Internet. Lists are available for **36 unique languages**, with multiple lists available for a number of languages including English, Spanish and Hindi. As expected, different lists for the same language have different, albeit overlapping, sets of words. Lists are divided into two banks:

1. `nltk`: These stop words lists are sourced from the [Natural Language Toolkit website](https://www.nltk.org/).
2. `other`: This is a collection of stop words lists gathered from various sources.

| Bank | # of Lists | # of Unique Languages in Bank |
| :---: | :---: | :---: |
| `nltk` | 29 | 29 |
| `other` | 27 | 25 |

As mentioned above, there are stop words lists available for 35 unique languages across both banks.

## `nltk` Available Languages

29 stop words lists for 29 unique languages are available in the `nltk` bank.

* Arabic
* Azerbaijani
* Basque
* Bengali
* Catalan
* Chinese
* Danish
* Dutch
* English
* Finnish
* French
* German
* Greek
* Hebrew
* [Hinglish](https://en.wikipedia.org/wiki/Hinglish)
* Hungarian
* Indonesian
* Italian
* Kazakh
* Nepali
* Norwegian
* Portuguese
* Romanian
* Russian
* Slovene
* Spanish
* Swedish
* Tajik
* Turkish

## `other` Available Languages

27 stop words lists for 25 unique languages are available in the `other` bank.

* Arabic
* Armenian
* Bulgarian
* Chinese
* Danish
* Dutch
* English
* Finnish
* French
* German
* Greek
* Hindi 1
* Hindi 2
* Indonesian
* Italian
* Japanese
* Latvian
* Norwegian
* Persian
* Polish 1
* Polish 2
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkish

## Installation

```
pip install got-stop-words
```

```python
from got-stop-words import got-stop-words
```

## Usage

The `load` method is used to load a stop words list with the following parameters:

* `bank`: The name of the list's bank, `nltk` or `other`.
* `lang`: The name of the language as spelled in English, e.g. `norwegian`, *or* the language's two-letter ISO 639-1 code. See below for a table of ISO-639-1 codes.
* `list_num`: The number of the desired list for those languages with more than 1 list in a bank, such as Hindi and Polish in the `other` bank. The `list_num` parameter can be omitted for those languages with only a single list. If the `list_num` parameter is omitted for those languages with multiple lists, the first list is returned.

**Example:** Loading the stop words list for Finnish from the `nltk` bank.

```python
fi-stop-words = got-stop-words.load("nltk", "fi")

# or

fi-stop-words = got-stop-words.load("nltk", "finnish")
```

**Example:** Loading the stop words list for Hindi from the `other` bank.

```python
hi-stop-words = got-stop-words.load("other", "hi", "1")

# or

hi-stop-words = got-stop-words.load("other", "hindi", "1")
```

Stop words lists are returned as a Python list.


## ISO 639-1 Language Codes

> **Note:** There is no ISO 639-1 code for Hinglish. However, the package permits specification of the Hinglish stop words list using the 2-character code `hn`.

| ISO 639-1 Code | Language |
| :---: | :--- |
| ar | arabic |
| az | azerbaijani |
| bg | bulgarian |
| bn | bengali |
| ca | catalan |
| da | danish |
| de | german |
| el | greek |
| en | english |
| es | spanish |
| eu | basque |
| fa | persian |
| fi | finnish |
| fr | french |
| he | hebrew |
| hi | hindi |
| hu | hungarian |
| hy | armenian |
| id | indonesian |
| it | italian |
| ja | japanese |
| kk | kazakh |
| lv | latvian |
| ne | nepali |
| nl | dutch |
| no | norwegian |
| pl | polish |
| pt | portuguese |
| ro | romanian |
| ru | russian |
| sl | sloveve |
| sv | swedish |
| tg | tajik |
| tr | turkish |
| zh | chinese |

## Sources

NLTK word lists are obtained from: http://anoncvs.postgresql.org/cvsweb.cgi/pgsql/src/backend/snowball/stopwords/

## License

This project is licensed under the terms of the **MIT** license.