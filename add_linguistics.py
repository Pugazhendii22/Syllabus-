import json
P='prepared-notes.json'
with open(P,encoding='utf-8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source):
 return {'id':id,'title':title,'source':source,'text':f'# {title}\nIntroduction to Linguistics · Semester 6\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Questions and practice\n{questions}\n\nTeaching note: examples depend on the language, speaker and descriptive framework. Compare the assigned textbook and use the indicated variety when transcribing.'}
IPA='https://www.internationalphoneticassociation.org/IPAcharts/common_files/pdfs/pdfs_IPA_charts_E/IPA_Kiel.pdf'
EL='https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/'
d['course-32:0']=[
n('linguistics-fields','What is linguistics? Dimensions and fields', '''## Definition and method
Linguistics is the systematic study of human language: its structure, use, acquisition and change. A linguist can collect utterances, record patterns, propose a generalisation and test it against further evidence. Description asks how a language variety works; prescription recommends forms for a particular social purpose. Studying a non-standard variety descriptively does not mean denying the practical value of a formal written convention.

## Core dimensions
Phonetics studies how speech sounds are produced, transmitted and perceived. Phonology studies their organisation and contrast in a language. Morphology examines word structure; syntax examines how words form larger structures. Semantics studies conventional meaning, while pragmatics studies meaning in context, including what a speaker implies.

## Interdisciplinary work
Sociolinguistics investigates language variation, identity and social power; psycholinguistics examines processing and acquisition; neurolinguistics relates language to the nervous system; computational linguistics develops and studies computational models; applied linguistics addresses practical questions such as language teaching. Historical linguistics investigates change and relationships across time. These fields overlap.

## Language and linguistics
English, Tamil and Indian Sign Language are languages; linguistics is a discipline that studies languages. Signed languages are full human languages with their own structure, not merely gestures or copies of spoken languages. Fluency in several languages is valuable but is not a substitute for studying evidence and analysis.''','0–10: distinguish language and the discipline. 10–20: map core branches. 20–30: sort examples by field. 30–40: compare description and prescription. 40–50: propose a question and evidence.','Which branch studies word structure? Which might study accents and social identity? Answer: morphology; sociolinguistics.','https://www.britannica.com/science/linguistics'),
n('sign-symbol','Language as a symbolic system', '''## Signifier and signified
In Saussure’s model a linguistic sign joins a signifier—the associated sound pattern—and a signified, a concept. For example, the English sound pattern for “tree” is associated by speakers with a concept of a tree. The signified is a concept, not simply the physical tree itself. A written word can represent the sign, but Saussure’s original discussion distinguishes the linguistic sound-image from marks on a page.

## Convention and arbitrariness
There is generally no natural necessity connecting the sequence /triː/ to the concept: other languages use different words. This is arbitrariness of the sign. Speakers cannot individually replace words at will and expect to be understood; conventions are shared socially. Sound symbolism and onomatopoeia complicate a claim that every connection is completely arbitrary.

## Beyond vocal symbols
The syllabus emphasises vocal symbols; spoken languages do use them, but human language is not restricted to speech. Signed languages use visual-manual signs with their own linguistic systems. Some signed forms resemble what they refer to, yet conventional signs also need to be learned and can vary across languages.

## Value and relations
A sign’s value is shaped by its relationships to other signs in a system. Analyse a word in a phrase and contrast it with alternatives rather than treating words as isolated labels.''','0–10: compare a word across known languages. 10–20: identify form and concept. 20–30: test arbitrariness and exceptions. 30–40: discuss spoken and signed modalities. 40–50: write a signifier/signified example.','In the word “tree,” what is the signified? Why does arbitrariness not mean that individuals can change conventions at will?','https://www.britannica.com/science/semiotics')]
d['course-32:1']=[
n('airstream','Airstream and organs of speech', '''## Airstream mechanisms
Most English speech uses pulmonic egressive airflow: air from the lungs moves outward through the vocal tract. Airstream direction and source matter: some languages also use ejectives with glottalic egressive airflow, implosives typically with glottalic ingressive airflow, and clicks using a lingual/velaric airstream mechanism. These are not ordinary English phonemes; avoid presenting English as the measure of possible speech.

## From lungs to lips
Air passes through the trachea and larynx. Vocal folds in the larynx may vibrate, producing voicing. Above them, the pharynx, mouth and nasal cavity shape the sound. When the velum is lowered, air can pass through the nose, as in [m] and [n]; when raised, nasal airflow is blocked for typical oral sounds.

## Active and passive articulators
An active articulator moves towards another surface: the lower lip and parts of the tongue are common examples. A passive articulator is the surface approached, such as the upper teeth, alveolar ridge or hard palate. For [f], the lower lip approaches the upper teeth; for [t], the tongue approaches the alveolar region in a common English articulation. Different speakers and languages can use different contact patterns.''','0–10: draw the airway. 10–20: identify lungs, larynx and cavities. 20–30: test voicing gently with fingers at the throat. 30–40: identify active/passive articulators. 40–50: compare oral and nasal airflow.','What makes [f] labiodental? What changes when the velum is lowered?','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-2-speech-articulators/'),
n('consonants','Classifying consonants: voicing, place and manner', '''## Three labels
A consonant can be described by voicing, place of articulation and manner of articulation. For instance [p] is a voiceless bilabial plosive: the lips close, airflow is blocked then released, and the vocal folds do not vibrate during the closure. [b] is its voiced counterpart in a basic description. Actual voicing timing varies by accent and context.

## Places
Bilabial: both lips, [p b m]. Labiodental: lower lip and upper teeth, [f v]. Dental: tongue near teeth, [θ ð] in many English descriptions. Alveolar: tongue near the ridge behind upper teeth, [t d n s z l]. Postalveolar: tongue behind that ridge, [ʃ ʒ tʃ dʒ]. Palatal: tongue body near hard palate, [j] as in “yes.” Velar: tongue body near soft palate, [k ɡ ŋ]. Glottal: at the glottis, [h] in many descriptions.

## Manners
Plosive: complete closure followed by release, [p t k]. Nasal: oral closure with nasal airflow, [m n ŋ]. Fricative: narrow constriction creates turbulent noise, [f s ʃ]. Affricate: stop closure followed by a fricative release, [tʃ dʒ]. Approximant: articulators approach without the friction of a fricative, [j w ɹ]. Lateral approximant: airflow passes around the tongue’s side, [l].

## Exercise with answers
Describe [m]: voiced bilabial nasal. Describe [s]: voiceless alveolar fricative. Describe [k]: voiceless velar plosive. IPA [j] is the initial sound in “yes,” not the usual English letter j sound.''','0–10: hear a voiced/voiceless contrast. 10–20: locate places on a mouth diagram. 20–30: practise manners. 30–40: describe [m], [s] and [k]. 40–50: compare articulatory descriptions.','How do [s] and [z] differ? Answer: primarily in voicing in this basic classification.','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-4-describing-consonants-manner/'),
n('vowels-cardinal','Vowels and cardinal-vowel reference points', '''## How vowels differ
Vowels are described using approximate tongue height (close to open), tongue position (front to back), lip rounding and other properties such as duration or nasalisation. The labels describe relative tongue positions, not an exact photograph of a mouth. A diphthong involves a movement in vowel quality within a syllable; a monophthong has relatively stable quality.

## Cardinal vowels
Daniel Jones’s cardinal vowel system supplies learned reference qualities for describing vowels across languages; they are not a list of the vowels of English or of any one speaker. The eight primary reference vowels are commonly listed in order as [i e ɛ a ɑ ɔ o u], moving down the front and then up the back of the vowel space. The front set is unrounded; the back set has [ɑ] unrounded and [ɔ o u] rounded. The scheme is partly articulatory and partly auditory; trained listening is important.

## Example and caution
In many English accents, the vowel of “see” is represented broadly /iː/ and that of “sit” /ɪ/. These symbols and precise qualities depend on the transcription convention and accent. Cardinal [i] is a reference point, not an assertion that all “see” vowels are exactly identical to it. IPA vowel charts show rounded members to the right when two symbols share a cell.''','0–10: contrast vowel and consonant. 10–20: explain height, backness and rounding. 20–30: sketch the vowel quadrilateral. 30–40: locate primary reference vowels. 40–50: distinguish a reference quality from a language’s phoneme.','What are the three main articulatory dimensions? Why are cardinal vowels not simply an English vowel list?','https://assets.cambridge.org/97805217/17403/excerpt/9780521717403_excerpt.pdf'),
n('phonemes','Phonemes, allophones and minimal pairs', '''## Phonetics versus phonology
A phone is a speech sound in phonetic description, usually shown in square brackets [ ]. A phoneme is a contrastive category in a particular language or variety, conventionally shown between slashes / /. Phonemic and phonetic representations serve different analytical purposes; symbols are not letters of ordinary spelling.

## Minimal pair
Two words make a minimal pair when their forms differ in one sound in the same position and their meanings differ. In many English varieties “fan” /fæn/ and “van” /væn/ show /f/ versus /v/. The spelling change happens to match the sound change here, but sound—not the number of letters—is the test.

## Allophones and distribution
Allophones are contextually or otherwise varying realisations of one phoneme in an analysis. In many English accents, initial /p/ before a stressed vowel is aspirated [pʰ] in “pin,” while after /s/ it is typically unaspirated [p] in “spin.” This pattern is associated with complementary distribution: each variant appears in different environments. It is illustrative, not a claim that every English speaker has identical phonetics or that [pʰ] and [p] are allophones in every language. In some languages aspiration distinguishes words.

Free variation means alternatives can occur in the same environment without changing lexical meaning, though style, region or social context may influence their choice. Complementary distribution alone is not sufficient to prove that two very dissimilar sounds are allophones; phonetic similarity and the wider system also matter.''','0–10: contrast sounds and spelling. 10–20: define phone and phoneme. 20–30: test fan/van. 30–40: compare pin/spin aspiration. 40–50: distinguish complementary distribution and free variation.','What evidence does fan/van provide? Does a difference between [pʰ] and [p] necessarily signal different phonemes in every language?','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/4-3-contrastive-distribution-and-minimal-pairs/'),
n('prosody-overview','Suprasegmentals: stress, rhythm, pitch and tone', '''## Beyond individual segments
Suprasegmental features extend over or organise syllables and larger stretches of speech. Stress is prominence; pitch concerns perceived frequency; intonation is the pattern of pitch across an utterance. Length, timing and rhythm also contribute to prosody.

A stressed English syllable is often longer and clearer, and may carry a pitch movement, but prominence is not simply shouting. In some varieties “REcord” as a noun and “reCORD” as a verb differ in stress and vowel quality. Sentence prominence can shift to highlight a contrast: “I wanted TEA” may contrast tea with coffee.

Tone languages use pitch patterns to distinguish lexical or grammatical meanings; intonation can also structure utterances. Tone is not equivalent to an English question tune, and signed languages have their own non-manual and timing features. Patterns vary with language, dialect and communicative context.''','0–10: identify individual sounds. 10–20: contrast word stress. 20–30: say a sentence with different focus. 30–40: distinguish pitch, tone and intonation. 40–50: write an example.','How is word stress different from sentence prominence? Why is pitch not the same thing as tone in every language?','https://ecampusontario.pressbooks.pub/essentialsoflinguistics/chapter/3-8-suprasegmentals/')]
d['course-32:2']=[
n('ipa-transcription','Phonemic transcription: a guided method', '''## Choose a variety first
A phonemic transcription represents contrastive categories, not spelling or every detail of an individual performance. Write / / for phonemic transcription and [ ] for a phonetic transcription. The International Phonetic Alphabet provides symbols, but conventions and phoneme inventories vary by accent.

The examples below use a broad, traditional non-rhotic British teaching transcription; they are practice in that convention, not a judgment that Indian English or another accent is inferior. Dictionary notation can differ. Non-rhotic here means /r/ is normally not pronounced after a vowel unless a following vowel permits linking.

## Worked examples
• “cat” /kæt/: three phonemes, despite the three letters coincidentally matching the number of symbols.
• “ship” /ʃɪp/: three phonemes; the letters sh represent one consonant.
• “chair” /tʃeə/: two phonemes in this broad teaching analysis, /tʃ/ and /eə/. Some modern British descriptions use a different vowel symbol; phoneme counts depend on analysis.
• “teacher” /ˈtiːtʃə/: primary stress before the first syllable, and no final /r/ in this non-rhotic model.
• “about” /əˈbaʊt/: primary stress before the second syllable; the first vowel is schwa.

## Practice with answers
Transcribe “dog,” “fish” and “pen”: /dɒɡ/, /fɪʃ/, /pen/ in this model. In other accents the vowel in “dog” can differ. Compare your own pronunciation and a dictionary’s accent label, and do not mix two transcription systems in one answer without explaining it.''','0–10: identify accent and notation. 10–20: transcribe ship and cat. 20–30: practise stress marks. 30–40: transcribe the three exercise words. 40–50: compare with a dictionary and discuss variation.','Why is “ship” three phonemes rather than four letters? What does /ˈ/ mark?','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-6-the-international-phonetic-alphabet/'),
n('word-stress','Word stress: syllables and prominence', '''## Identify the syllable
A syllable normally has a nucleus, often a vowel; consonants can occur before or after it. Word stress is relative prominence assigned to a syllable. In IPA, primary stress /ˈ/ is written immediately before the stressed syllable, and secondary stress /ˌ/ before a less prominent stressed syllable where relevant.

## Examples
In the teaching convention used here, “TAble” /ˈteɪbəl/ is initially stressed, while “aBOUT” /əˈbaʊt/ has stress on the second syllable. In many English accents the noun “REcord” /ˈrekɔːd/ and verb “reCORD” /rɪˈkɔːd/ contrast in stress and vowel quality; pronunciation differs across varieties. Unstressed syllables often have reduced vowels such as schwa /ə/, but not every unstressed vowel is schwa.

## Analysis practice
1. Mark the stressed syllable in TAble, aBOUT, and TEAcher.
2. Explain why a stress mark is written before, not after, the syllable.
3. Listen to a dictionary recording in a named accent. The best evidence is the spoken form, not an invented universal rule based solely on spelling.

Do not equate stress solely with loudness: duration, vowel quality and pitch can all contribute.''','0–10: clap or mark syllables without requiring vocal participation. 10–20: listen for prominence. 20–30: mark the three examples. 30–40: compare noun and verb record. 40–50: explain schwa and variation.','Where is primary stress in /əˈbaʊt/? Answer: the second syllable. Can unstressed syllables contain vowels other than schwa? Yes.','https://ecampusontario.pressbooks.pub/essentialsoflinguistics/chapter/3-8-suprasegmentals/'),
n('sentence-stress-intonation','Sentence stress, pitch and intonation', '''## Prominence and focus
Sentence stress is the prominence given to a word or syllable in a phrase. English speakers often highlight new or contrastive information. In “AMMU brought the book,” a possible contrast is who brought it; in “Ammu brought the BOOK,” it may be what she brought. The surrounding conversation determines the interpretation; capitals here merely show prominence.

## Pitch and intonation
Pitch is perceived highness or lowness, related to vibration frequency for voiced sounds. Intonation is the changing pitch pattern across a phrase. A rise, fall or fall–rise may signal meanings such as continuation, completion, surprise or a question, but no single contour has one fixed meaning in all contexts or varieties. Yes/no questions can rise, while a question can also fall.

## Teaching practice
Give learners three short contexts before saying the same sentence with different prominence. Ask which word answers the question. Avoid stereotypes about an accent sounding “wrong” or “uneducated.” Participation may include pointing to a transcript, hearing a recording or observing a pitch display; speech production is not mandatory for every learner.''','0–10: ask a context question. 10–20: mark prominence in two answers. 20–30: compare pitch contours. 30–40: interpret the same contour in different contexts. 40–50: write a short explanation.','In answer to “Who brought the book?”, which word might receive focus in “Ammu brought the book”? Answer: Ammu.','https://iastate.pressbooks.pub/teachingpronunciation/chapter/proninence/')]
d['course-32:3']=[
n('morpheme-morph','Morpheme, morph and allomorph', '''## Definitions
A morpheme is a minimal meaningful or grammatical unit in an analysis. A morph is a form that realises a morpheme in a particular word. Allomorphs are alternative realisations of the same morpheme, often conditioned by sound or grammar. A word may contain one morpheme, as “book,” or several, as “books” = BOOK + plural.

## Free and bound
A free morpheme can occur independently as a word: “book.” A bound morpheme cannot usually stand alone in that function: plural -s or the prefix un-. Roots provide a lexical core; affixes attach to a base. Prefixes occur before, suffixes after; infixes are inserted within a base in languages that use them. A word and a morpheme are not synonymous: “unhappy” is one written word with more than one morpheme.

## Allomorphs of English plural
In a common pronunciation, “cats” ends [s] after voiceless /t/, “dogs” ends [z] after voiced /ɡ/, and “buses” ends [ɪz] after a sibilant. These are forms of the plural morpheme, not three different plural meanings. “Children” uses an irregular plural form; not every plural is formed by adding the regular suffix. Actual realisations vary by accent.

## Practice
“Unhelpful” can be analysed un- + help + -ful. “Walked” has WALK + past tense, whose suffix is typically [t] in that context. Analyses of some words are disputed; specify the evidence rather than assuming every string of letters is a morpheme.''','0–10: compare word and morpheme. 10–20: segment books and unhappy. 20–30: compare cats, dogs and buses. 30–40: classify free and bound forms. 40–50: check two answers.','What is the difference between a morpheme and an allomorph? Identify the plural allomorph in cats: [s] in the example accent.','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/5-1-what-is-morphology/'),
n('word-formation','Inflection, derivation and word formation', '''## Inflection versus derivation
Inflection marks grammatical information without usually creating a new lexeme or changing word class: “walk” → “walked” marks past tense; “book” → “books” marks plural. Derivation forms a new lexeme and may change class or meaning: “happy” → “happiness” adds a noun-forming suffix; “happy” → “unhappy” changes meaning without changing class. The distinction varies across languages and individual analyses.

## Other processes
Compounding joins bases, as “toothbrush” or “blackboard”; its meaning is not always fully predictable. Reduplication repeats all or part of a form and can mark different meanings in different languages. Conversion changes a word’s grammatical use without an overt affix, as noun “email” to verb “to email.” Blending joins parts of words, as “brunch”; clipping shortens a word, as “lab” from “laboratory.” Borrowing adopts a form from another language.

## Worked analysis
“Teachers” = teach + derivational -er + inflectional plural -s. “-er” forms a noun referring to a person associated with teaching; plural -s marks more than one. Not every English word ending in the letters er contains this suffix, so analyse meaning and structure, not letters alone.''','0–10: define inflection and derivation. 10–20: analyse walk/walked and happy/happiness. 20–30: sort compounds, blends and clippings. 30–40: segment teachers. 40–50: discuss a locally known example.','Is -s in books inflectional? Yes. Does derivation always change word class? No, as in happy/unhappy.','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/5-4-lexical-categories-and-the-split-between-derivation-and-inflection/'),
n('sandhi-categories','Sandhi and grammatical categories', '''## Sound at a boundary
Sandhi refers to sound changes conditioned at or near the meeting of forms. Internal sandhi occurs within a word; external sandhi occurs between words. Sanskrit grammatical traditions describe many such rules systematically, and analogous boundary effects can be studied in other languages. Do not assume a single rule applies to all languages or speakers.

In some English speakers’ connected speech “ten books” may have [m] before [b], as the final nasal takes on the following bilabial place. This is a possible assimilation, not a compulsory spelling change or a universal pronunciation. Sanskrit examples should be analysed using the assigned system and diacritics.

## Grammatical categories and parts of speech
Categories such as number, tense, person, aspect and case encode grammatical distinctions in different ways. English nouns commonly distinguish singular/plural; verbs can distinguish present/past. Languages do not all mark the same distinctions, and a grammatical category need not be expressed by a separate suffix.

Parts of speech classify words by grammatical behaviour: nouns, verbs, adjectives, adverbs, pronouns, determiners, prepositions and others. A word’s class is determined by distribution and use, not just by a simple meaning label. “Run” can be a verb (“they run”) or a noun (“a run”).''','0–10: locate a word boundary. 10–20: explain assimilation. 20–30: distinguish internal and external sandhi. 30–40: identify tense and number. 40–50: compare noun and verb uses of run.','What changes in a possible “ten books” pronunciation? Why is a part of speech not determined by spelling alone?','https://www.learnsanskrit.org/start/nouns/sandhi/')]
d['course-32:4']=[
n('knowledge-competence','Linguistic knowledge, competence and performance', '''## Knowledge of language
Speakers and signers know patterns they can use to understand or produce new utterances. Linguistic knowledge includes categories, combinations, sound or sign patterns and meanings. Much of it is implicit: a speaker need not be able to state a grammatical rule to use it.

## Chomsky’s distinction
In a classic formulation, competence is a speaker–hearer’s underlying linguistic knowledge, while performance is actual use in particular situations. Hesitation, memory limitations, distraction and social context may affect performance. The distinction is a theoretical tool, not a claim that a slip makes a speaker incompetent. Actual examples and judgments help researchers infer knowledge, but they are evidence to interpret, not a transparent window into it.

Communicative competence is a broader idea associated with Dell Hymes: effective language use also involves knowing what is appropriate in a social situation. Different frameworks define and investigate these concepts differently; a community’s variety must not be judged by the rules of another variety.

## Practice
A learner knows a pattern but hesitates when tired. The rule knowledge can be discussed as competence; the hesitating utterance is performance. List other possible explanations before claiming to know what a person has mentally represented.''','0–10: introduce a familiar slip. 10–20: distinguish knowledge from an utterance. 20–30: examine judgment as evidence. 30–40: compare communicative competence. 40–50: write a cautious example.','Does a hesitation prove absence of competence? No. Why should judgments be interpreted within a variety?','https://www.britannica.com/science/linguistics/Chomskys-grammar'),
n('syntax-tree','Syntax, categories and tree diagrams', '''## Words in structure
Syntax studies how words combine into phrases and sentences. Lexical categories include noun (N), verb (V), adjective (Adj) and adverb (Adv); functional categories include determiners (Det), among others. A phrase is a group of words organised around a head. “The child” is a noun phrase (NP); “reads a book” is a verb phrase (VP).

## A simple phrase marker
For “The child reads a book,” a simplified labelled bracket notation represents the same hierarchy as a tree:
[S [NP [Det The] [N child]] [VP [V reads] [NP [Det a] [N book]]]]
S stands for sentence; the first NP is the subject, and the second NP is the object of reads. Draw S at the top, branch to NP and VP, then add the labelled words and second NP as the brackets show. Other frameworks use different labels and more layers.

## Rules and tests
For this illustration, S → NP VP; NP → Det N; VP → V NP. These are simplified rules for the example, not an exhaustive account of English. A constituent is a unit within the structure. Substitution provides one clue: “The child” can be replaced by “she” in a suitable context. A single test does not always settle a disputed analysis.

## Practice
Make a matching bracket structure for “A student reads the poem.” Answer: [S [NP [Det A] [N student]] [VP [V reads] [NP [Det the] [N poem]]]].''','0–10: sort categories. 10–20: find subject and predicate. 20–30: work through the bracketed tree. 30–40: draw the practice example. 40–50: check each branch against the rules.','In the example, which NP is the object? Answer: “a book.” What does a phrase marker show? Hierarchical grouping.','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/a1-1-drawing-phrase-structure-rule-trees/'),
n('generative-grammar','Generative grammar and structural ambiguity', '''## What “generative” means
A generative grammar is a formal system intended to characterise possible structures in a language using a finite set of principles or rules. It aims to explain linguistic knowledge, not to prescribe “proper” usage or imply that people consciously recite rules. Generative approaches have changed over time; do not treat one tree or terminology as the only version.

## Hierarchy and ambiguity
“I saw the person with binoculars” can mean I used binoculars to see the person, or I saw a person who had binoculars. A structural analysis represents the phrase “with binoculars” as attaching in different places: roughly, to the verb phrase in the first reading or the noun phrase in the second. Context can favour one reading; not every listener finds both equally natural.

## Related sentence patterns
“The teacher praised the student” and “The student was praised by the teacher” share participants but differ in grammatical arrangement. Transformational analyses relate structures using formal operations; modern accounts differ about the details. Do not describe a passive as simply reversing word order: it introduces auxiliary be and a participle, and a by-phrase may be omitted.

## Practice
For “The student was praised,” identify the understood person praised: the student. Is the person who praised explicitly named? No.''','0–10: explain a grammar as a system. 10–20: use an ambiguity. 20–30: show alternative attachments. 30–40: compare active and passive. 40–50: explain why approaches differ.','Explain two readings of “I saw the person with binoculars.” Why is a passive not merely a reversal of words?','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/part/chapter-6-syntax/'),
n('semantics-change','Semantics and synchronic / diachronic variation', '''## Semantics
Semantics studies conventional linguistic meaning in words, phrases and sentences. Lexical semantics considers relations such as synonymy (similar meaning), antonymy (opposition) and polysemy (related senses of one word). Perfect interchangeability is rare: context can distinguish near-synonyms. Compositionality is the principle that the meaning of a complex expression depends on its parts and how they combine; idioms show that interpretation is not always transparently predictable.

Semantics is often distinguished from pragmatics, which considers context-dependent inference. If someone says “It is cold here,” the sentence describes temperature; in context it might also function as a request to close a window. The request is an inference, not the only meaning of the sentence.

## Two perspectives on language
A synchronic study examines a language or varieties at a particular time: for example, comparing how groups use a present-day pronunciation. A diachronic study investigates change over time: for example, comparing earlier and later English plural patterns. Both are analytical perspectives; a synchronic snapshot does not imply a language is uniform or unchanging.

Words, pronunciation and grammar change, and variation may reflect geography, social networks, context and generations. Avoid claiming that older forms are inherently better or that all speakers of a region behave alike.

## Practice
Classify “comparing present-day varieties of Tamil” as synchronic and “tracing English vowels over centuries” as diachronic. Explain why the first study can still find variation.''','0–10: define semantics. 10–20: distinguish sentence meaning from an inferred request. 20–30: compare synchronic and diachronic examples. 30–40: create one example of each. 40–50: check against definitions.','Is comparing a language across centuries synchronic or diachronic? Diachronic. Does synchronic study exclude variation? No.','https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/7-2-compositionality-why-not-just-syntax/')]
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Wrote',sum(len(v) for k,v in d.items() if k.startswith('course-32:')),'linguistics selections across 5 units')
