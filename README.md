# cherokee-data
Transliteration data files for the Cherokee language and syllabary (ᏣᎳᎩ)

This data maps Cherokee syllabic characters with their common/standardized transliterations, alternate transliterations, position on a syllabary chart, and a pronunciation guide (both IPA and American English equivalence).  It's meant to aid in the design of transliteration and translation scripts/software, language learning tools, or informational displays, but can be useful for anything, so please take it and use it freely!

Assembled by Natasha L. (@lupinia)

Fields
------
* **character** *(str, unicode)* - The Unicode character for the syllable.
* **transliteration** *(str)* - The syllable's main/official Latin alphabet representation.  Never more than three letters long.
* **transliteration_alt** *(str)* - Other transliterations in common use.  Generally not recommended when converting syllabic characters to Latin letters for Cherokee speakers to read, but they're sometimes used to make the language more accessible to English speakers.  For example, the name "Keetoowah" in the name of the United Keetoowah Band tribe is written in Cherokee as ᎩᏚᏩ, which transliterates as "Giduwa" (or, more commonly, "Kituwa"), but which is still pronounced "Keetoowah".
* **pronunciation_us** *(str)* - An approximate pronunciation based on American English.
* **pronunciation_notes** *(str)* - Extra notes further explaining the pronunciation.
* **startswith_vowel** *(bool)* - Indicates a syllable that doesn't start with a consonant, which can cause transliteration issues.
* **endswith_consonant** *(bool)* - Indicates a syllable that does not end in a vowel, which can cause transliterations issues.
* **chart_row** *(int)* - When displaying characters on a syllabary chart/table, this is the row in which it appears.  Values can be 1-6.  Note:  Each cell on a syllabary chart can contain up to three characters.
* **chart_col** *(int)* - When displaying characters on a syllabary chart/table, this is the column in which it appears.  Values can be 1-13.  Note:  Each cell on a syllabary chart can contain up to three characters.

Files
-----

Each file comes in CSV, JSON, and XML formats.

* "full" contains all fields.
* "transliterate" contains only the "character" and "transliteration" fields.
* "transliterate-alt" contains the "character" and "alt-transliteration" fields, meant to supplement "transliterate".  It does not contain a unique identifier per row.

Notes and Transliteration Special-Cases
---------------------------------------

* The syllable "s" (Ꮝ) is a special case, because it's only a half-syllable.  It's used to modify any other syllable to end in a consonant, and never pronounced separately.  Aside from the name of the person who invented the syllabary, Sequoyah (Ssiquoya, ᏍᏏᏉᏯ), this generally never appears at the beginning of a word.
* For syllables that start with a vowel and appear mid-word, disambiguation marks - such as an apostrophe - can be used in the Latin alphabet transliteration to indicate that the vowels are separate syllables (for example, "oli'i" instead of "olii").  There is one exception to this, which a diphthong created by the "ai" combination, pronounced like the long "i" in English; for example, in the word for "icon", ᎠᎢᎧᏂ (aikani).
* The combination of syllables ending in a consonant, and syllables beginning in a vowel, can cause serious issues when transliterating from Latin letters to  characters.  The "s" syllable (Ꮝ) further complicates this problem, because it can turn any syllable into one that ends in a consonant.
* Syllables written in the Latin alphabet are often separated with hyphens.
* Syllable emphasis in a given word is something that cannot be programmatically determined for a pronunciation guide.
* Similarly, Cherokee is a tonal language, and tonal emphasis cannot be programmatically determined.

License
-------

This data compilation is 100% public domain and free.  Use it however you wish; attribution is appreciated, but not required.
