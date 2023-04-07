## Got Stop Words

Python package that makes it easy to use **stop words** lists in Python projects. The set of lists contained within the package reflect an organization of lists collected across the Internet. Lists are available for **36 unique languages**, with multiple lists available for a number of languages including English, Spanish and Hindi. As expected, different lists for the same language have different, albeit overlapping, sets of words. Lists are divided into two banks:

1. `nltk`: These stop words lists are sourced from the [Natural Language Toolkit website](https://www.nltk.org/).
2. `other`: This is a collection of stop words lists gathered from various sources.

| Bank | # of Lists | # of Unique Languages in Bank |
| :---: | :---: | :---: |
| `nltk` | 29 | 29 |
| `other` | 27 | 25 |

As mentioned, there are lists for 36 unique languages across *both* banks.

## `nltk` Bank Available Languages

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

## `other` Bank Available Languages

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
pip install gotstopwords
```

## Usage

### Importing the Package

```python
from gotstopwords import gotstopwords
```

### `load` Method

The `load` method is used to load a stop words list with the following parameters:

* `bank`: The name of the list's bank, `nltk` or `other`.
* `lang`: The name of the language as spelled in English, e.g. `norwegian`, *or* the language's two-letter ISO 639-1 code. See below for a table of ISO 639-1 codes.
* `list_num`: The number of the desired list for those languages with more than 1 list in a bank, such as Hindi and Polish in the `other` bank. The `list_num` parameter can be omitted for those languages with only a single list.

### Examples

* Loading the stop words list for Finnish, ISO 639-1 code `fi`, from the `nltk` bank.

```python
_finnish = gotstopwords.load("nltk", "fi")

# or

_finnish = gotstopwords.load("nltk", "finnish")
```

* Loading the stop words list for Spanish, ISO 639-1 code `es`, from the `nltk` bank.

```python
_spanish = gotstopwords.load("nltk", "es")

# or

_spanish = gotstopwords.load("nltk", "spanish")
```

* Loading the stop words list for English, ISO 639-1 code `en`, from the `other` bank.

```python
_english = gotstopwords.load("other", "en")

# or

_english = gotstopwords.load("other", "english")
```

* Loading the first stop words list for Hindi, ISO 639-1 code `hi`, from the `other` bank.

```python
_hindi1 = gotstopwords.load("other", "hi", "1")

# or

_hindi1 = gotstopwords.load("other", "hindi", "1")

# or

_hindi1 = gotstopwords.load("other", "hi", 1)

# or

_hindi1 = gotstopwords.load("other", "hindi", 1)
```

Stop words lists are returned as a Python list. If there is no stop words list associated with the values that are input, an empty list will be returned.

> **Note:** Bank and language names can also be entered with capital letters if desired.  

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