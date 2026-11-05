import json
p='prepared-notes.json';d=json.load(open(p))
def n(id,title,source,text):return dict(id=id,title=title,source=source,text=text)
source='https://owl.purdue.edu/owl/general_writing/index.html'
d['course-3:0']=[n('exam-reading','Unit 1 · Reading Comprehension','https://uniskills.library.curtin.edu.au/academic-writing/reading-and-note-taking/reading-strategies/','''# Unit 1: Reading Comprehension
English for Competitive Exams · Semester 1

## Objectives
Identify main ideas and details; infer meaning using evidence; assess tone, style and rhetorical choices; use skimming, scanning, intensive and extensive reading purposefully.

## Main idea and supporting detail
The topic is what a passage is about; the main idea is what it says about that topic. Supporting details give reasons, examples or evidence. For each paragraph, ask: What is its function? Does it introduce a claim, explain, qualify or conclude? A good title captures the whole passage rather than a single example.

## Inference and critical evaluation
An inference is a conclusion reasonably supported by stated evidence, not a free guess. Notice words such as “some”, “may” and “often”: replacing them with “all”, “must” or “always” may make an answer too strong. Critical reading asks who makes the claim, what evidence is supplied, what assumptions are necessary and whether alternative explanations exist. A claim and proof are different.

## Strategies
Skim for the general direction and structure. Scan for a particular name, figure or term. Read intensively when the exact logic or wording matters. Extensive reading means reading larger quantities, often for broad understanding and vocabulary development. In an exam, preview the questions, read for overall sense and return to the relevant lines; strategy can vary with the test.

## Tone, style and devices
Tone is the writer’s attitude, for example cautious, critical or enthusiastic; support the answer with language from the passage. Style concerns how the writer uses language. Rhetorical devices include contrast, repetition, analogy, rhetorical question and irony. An analogy explains one thing by comparing it with another; it can clarify an argument but does not by itself prove it. Irony depends on context: do not call every humorous sentence ironic.

## Worked exercise
Passage: “The town library extended its weekend hours. Attendance increased, but staff observed that many visitors still had difficulty reaching the building because buses were infrequent. The council is considering a later bus service.”
1. Main idea: the library’s longer hours increased use, while transport remained a problem.
2. Detail: buses were infrequent.
3. Inference: transport may affect some people’s ability to use the library. We cannot infer that all non-users lack transport.
4. Has the council introduced a later bus? No; it is considering one.
5. Tone: informative and measured; the text reports changes and qualifications without exaggerated language.

## 50-minute class
0–10 min: explain topic, main idea and detail. 10–20: skim and title the passage. 20–30: scan for facts and justify an inference. 30–40: evaluate a stronger but unsupported claim. 40–47: identify tone and one rhetorical device in a second passage. 47–50: exit ticket: explain how to test an inference.

## Practice and revision
1. A passage reports one successful trial. Can we conclude a method always works? No; one trial does not establish universal success.
2. Which strategy locates an examination date? Scanning, followed by checking context.
3. Explain how a contrast contributes to an argument using a passage of your choice.

## Reading note
Practise with passages from different genres, including academic prose, reports and opinion writing. Do not assume every exam uses the same pattern or marking scheme.''')]
d['course-3:1']=[n('exam-grammar','Unit 2 · Functional Grammar','https://owl.purdue.edu/owl/general_writing/grammar/index.html','''# Unit 2: Functional Grammar
English for Competitive Exams · Semester 1

## Parts of speech
A noun names a person, place, thing or idea; a pronoun stands for a noun phrase; a verb expresses an action, state or relation; an adjective modifies a noun; an adverb often modifies a verb, adjective, clause or another adverb; a preposition links a noun phrase to another element; a conjunction connects words or clauses; an interjection expresses an immediate reaction. A word’s function depends on context: “book” is a noun in “a book” and a verb in “book a room.”

## Articles and prepositions
Use “a” before a consonant sound (“a university”) and “an” before a vowel sound (“an hour”); “the” usually identifies a specific or already understood referent. Some nouns in general statements take no article: “Books can help.” Prepositions express relationships, but usage is often conventional: “interested in”, “depend on”, “arrive at the station” and “arrive in Chennai.” Learn phrases in context, not as isolated lists.

## Subject–verb agreement
A singular subject generally takes a singular present-tense verb: “The student reads.” Plural: “The students read.” Find the actual subject, not just the nearest noun: “The list of books is on the table.” With “each”, agreement is normally singular: “Each student has a card.” Some collective nouns vary by dialect and meaning.

## Active and passive
Active: “The committee approved the plan.” Passive: “The plan was approved by the committee.” The object of the active sentence becomes the subject of the passive; a form of “be” and a past participle are used. Retain tense when transforming. Passive is useful when the action or recipient matters more than the actor, but should not hide responsibility when the actor matters.

## Clauses, reported speech and phrasal verbs
A clause has a subject and predicate: “because it rained” is dependent; “the match stopped” can stand independently. “The match stopped because it rained” combines them. In reported speech, pronouns, time expressions and tense may change according to context: She said, “I am tired” → She said that she was tired. Backshift is common after a past reporting verb but is not automatic when a fact still holds. A phrasal verb combines a verb and particle: “look up a word”; “give up” means stop trying. Their meanings depend on context.

## Vocabulary relationships
An idiom is an expression whose meaning may not be predictable from its separate words; “once in a blue moon” means rarely. Synonyms are similar in a given context, not always interchangeable; antonyms express contrast. Use context to select the best answer.

## Practice with answers
1. “She is ___ honest person.” → an (initial vowel sound).
2. “The box of pencils ___ on the table.” → is (subject: box).
3. Change “They built the bridge in 2000” to passive. → “The bridge was built in 2000.”
4. “Because it rained” is a dependent clause; it needs an independent clause to complete that sentence.
5. Report “I am ready,” said Mira. → Mira said that she was ready, in an ordinary past-reporting context.
6. “Look up” in “look up the meaning” means search for information.

## 50-minute lesson
0–10: identify parts of speech in context. 10–20: articles and agreement. 20–30: transform active/passive sentences. 30–40: clauses and reported speech. 40–47: contextual vocabulary. 47–50: one corrected sentence with explanation.

## Exam reminder
Read the complete sentence, identify its meaning and structure, and check agreement and tense after choosing an answer. Explanations above are introductory; context and accepted varieties matter.''')]
d['course-3:2']=[n('exam-written','Unit 3 · Written Communication',source,'''# Unit 3: Written Communication
English for Competitive Exams · Semester 1

## Paragraphs and essays
A paragraph develops one central point with explanation and support. An essay typically introduces its topic and thesis, develops connected arguments in body paragraphs, and concludes by synthesising the response. For exam writing, interpret the instruction: “discuss” may require several perspectives, while “evaluate” requires reasoned judgement. Plan before writing.

## Description, narration and argument
Description presents features of a person, place or situation through selected details. Narration relates events in a meaningful sequence, using time markers where helpful. Argument makes a claim and supports it with reasons and evidence; acknowledge a relevant counterargument rather than misrepresenting it. Example: Claim: the college should extend library hours. Reason: students need access after class. Evidence should be a verified survey or usage record, not an invented statistic.

## Reports, letters and notes
A report’s headings depend on the question but may include purpose, method, findings and recommendations. A formal letter gives recipient and date as required, a clear purpose, supporting details and a courteous closing; an informal letter uses a tone appropriate to a personal relationship. Note-making selects main points and subpoints, using consistent abbreviations and a clear title or key when required.

## Summary, paraphrase and précis
A summary condenses the central ideas in fresh language. A paraphrase restates a selected passage in different words and structure while preserving its meaning and usually similar scope. A précis is a concise, coherent restatement of a longer passage’s essential argument; follow the exam’s word limit and format. In academic work, credit the original for summaries and paraphrases as well as quotations. Do not insert your own unsupported opinion into a neutral summary.

## Notice and poster
A notice conveys a specific announcement: organisation, heading, date, event or instruction, time, place, relevant audience and contact/signature as required. A poster combines brief text with visual hierarchy for an audience and purpose. Its format depends on the exam; include essential information rather than assuming decoration earns more marks than clarity.

## Worked example
Original: “The college opened a reading room in the evening. Students who worked during the day could use it after their shifts. The library plans to monitor attendance before deciding whether to continue.”
Possible summary: “The college is testing evening reading-room access to help working students and will review attendance before continuing.” This preserves the purpose and conditional future decision without claiming the service is permanent.

## 50-minute class
0–10: identify the purpose and audience of an essay. 10–20: draft a supported paragraph. 20–30: distinguish summary from paraphrase. 30–40: produce a notice with all key facts. 40–47: peer-review for omissions and invented details. 47–50: revise one sentence.

## Review
1. Difference between summary and paraphrase? A summary condenses central ideas; a paraphrase restates a selected passage with its meaning intact.
2. A notice must identify the event, time and place, among other required details.
3. Which claim is stronger: “The change is useful” or a claim with verifiable supporting evidence? The supported claim, assuming the evidence is relevant.

## Examination note
Follow the particular examination’s current word limits and marking instructions; the syllabus itself does not establish one universal format for all competitive exams.''')]
d['course-3:3']=[n('exam-listening','Unit 4 · Listening and Speaking Skills','https://www.open.edu/openlearn/mod/oucontent/view.php?id=65974&section=3.2','''# Unit 4: Listening and Speaking Skills
English for Competitive Exams · Semester 1

## Listening and hearing
Hearing is the perception of sound; listening includes attending, interpreting and responding. Listening helps candidates follow instructions, answer relevantly and understand other viewpoints. A useful routine is to focus, note key words, listen to the complete question, ask for clarification where permitted, and check the interpretation before responding.

## Effective speech
A clear speech suits the audience and purpose. Organise a central message, a few logically ordered points and a conclusion. Speak audibly at a comfortable pace, articulate key terms, and use examples accurately. Fluency does not require one accent or uninterrupted speech: effective communication is intelligible, appropriate and responsive. Avoid inventing facts or forcing unfamiliar vocabulary.

## Social exchanges and dialogue
Examples: greeting—“Good morning. How are you?”; request—“Could you please explain the next step?”; clarification—“Do you mean that the form is due on Monday?”; polite disagreement—“I see your point, but I think another factor matters.” Adapt formality to situation. A dialogue requires turn-taking as well as asking and answering questions.

## Persuasive arguments
A persuasive argument makes a specific claim and supplies reasons and appropriate support. Model: “The library should open later on two weekdays because many students have classes during the day. The college could pilot the change and review actual attendance.” Acknowledge limits: longer hours also need staffing and funding. A proposal does not become true merely because it is confidently delivered.

## Elocution
Elocution is the practice of clear and effective spoken delivery. In a short speech, mark pauses at meaningful boundaries, vary emphasis appropriately and rehearse for time. Interpret the speech’s purpose and audience. Volume, speed, stress and intonation can affect clarity; performance should not be judged by an arbitrary claim that only one accent is correct.

## Class practice
Pairs: one student gives three instructions for a campus event; the other paraphrases them before acting. Groups: give a one-minute persuasive proposal, followed by one question and a respectful answer. Elocution: read a short passage twice, first for meaning and then with deliberate pauses.

## Sample questions and responses
1. What is the difference between hearing and listening? Hearing is sound perception; listening actively attends to and interprets it.
2. Give an appropriate clarification. “Could you repeat the last date for submitting the form?”
3. Name two qualities of effective speech. Clear organisation and suitable pacing; other supported answers are possible.

## 50-minute lesson
0–10: hearing and listening. 10–20: listening-and-paraphrase exercise. 20–30: social dialogue. 30–40: develop a claim and reason. 40–47: short delivery practice. 47–50: feedback on one specific behaviour.

## Exam reminder
Check the specific test’s interview or speaking instructions. Prepared scripts should not replace listening to the question actually asked.''')]
d['course-3:4']=[n('exam-study','Unit 5 · Study Skills','https://owl.purdue.edu/owl/research_and_citation/using_research/index.html','''# Unit 5: Study Skills
English for Competitive Exams · Semester 1

## Building vocabulary
Learn words in meaningful sentences. Record definition, part of speech, pronunciation, collocations and an example. Review across several sessions and use the word in your own writing. Check a dictionary when a meaning inferred from context is uncertain. Similar words may differ in register or collocation: accuracy matters more than using difficult words.

## Research and library tools
Begin with a focused question and useful keywords; add synonyms. A catalogue identifies items in a library’s collection. Books can offer sustained treatment; periodicals include journals and magazines, whose purposes vary. A bibliography lists works relevant to or used in a topic. An index helps locate a subject within a book or collection. Evaluate authorship, date, evidence and relevance before trusting a source. Search results are starting points, not automatic proof.

## Note-making and source use
Separate your own ideas from a source’s claims. Record author, title, publication details and page numbers as you read so you can return to the source. Use headings and concise points. Summarising condenses central ideas; paraphrasing restates a passage’s meaning in your own words and structure; quoting reproduces exact wording with quotation marks and an appropriate citation. All three require acknowledgement when using another person’s work. Follow the requested citation style rather than mixing systems.

## References list
A reference list gives readers enough information to locate cited material. Its exact order, punctuation and treatment of authors vary by style, such as MLA or APA. Check the edition of the relevant style guide and your teacher’s instructions. Do not fabricate missing publication information.

## Answering an exam question
1. Read the whole question and underline the task, topic and limits.
2. Allocate time in proportion to marks, while following the exam’s rules.
3. Draft a brief plan: direct answer, relevant points, examples and conclusion where needed.
4. Write legibly and stay within the requested scope; avoid memorised material that does not answer the question.
5. Reserve time to check meaning, omissions, calculations where relevant and grammar.
6. Evaluate your answer against the question and marking guidance, not merely its length.

## Worked example
Question: “Explain two barriers to listening and suggest a response to each.” A relevant plan has two barrier–response pairs: noise → move to a quieter space; unfamiliar terminology → ask for definitions and an example. A generic essay about communication that omits responses does not fully answer the task.

## 50-minute lesson
0–10: vocabulary log. 10–20: catalogue, index and bibliography. 20–30: summary versus paraphrase and quote. 30–40: plan an answer to the example. 40–47: peer-check for both required responses. 47–50: self-assessment.

## Questions
Why do paraphrases need citation? What is the difference between a library catalogue and a book index? How can a student use a question’s command words when planning?

## Reading note
The Purdue research guide explains source use. Citation requirements depend on the assignment or exam.''')]
d['course-4:0']=[n('spoken-grammar','Unit I · Working with Grammar','https://owl.purdue.edu/owl/general_writing/grammar/index.html','''# Unit I: Working with Grammar
Spoken English · Semester 1

## Sentence construction and types
A basic complete sentence has a subject and a finite verb and expresses a complete thought: “The students are discussing the poem.” Sentences can make statements, ask questions, issue requests or commands, and express strong feeling. They may be simple (one independent clause), compound (independent clauses joined) or complex (an independent clause with a dependent clause). In conversation, shorter fragments can also be meaningful in context.

## Parts of speech and auxiliaries
Nouns, pronouns, verbs, adjectives, adverbs, prepositions, conjunctions and interjections perform different roles. Auxiliary verbs help form questions, negatives, tense, aspect or modality: “Do you read?”, “She is speaking”, “They have arrived”, “We can try.” Match the auxiliary to the intended meaning; “can” often expresses ability or possibility, while “must” can express strong obligation or inference depending on context.

## Number, agreement and determiners
Singular: “A student is ready.” Plural: “Students are ready.” The subject determines verb agreement: “The quality of the answers is important.” Determiners specify or quantify nouns: a/an, the, this, these, some, many and each. “A university” and “an hour” show that a/an depends on initial sound, not spelling. Context matters when choosing “some” or “any.”

## Active and passive; comparison
Active: “The teacher asked a question.” Passive: “A question was asked by the teacher.” Preserve tense and meaning when changing voice. Comparison: “clear, clearer, clearest”; “important, more important, most important.” Irregular forms include good, better, best. Avoid doubling the comparative: “more better” is not standard edited English.

## Punctuation and common usage
Written speech transcripts still need appropriate capitals, full stops, question marks and commas. Speech itself uses pauses and intonation, not visible punctuation. Compare “She speaks clearly” with “Does she speak clearly?” Common standard-form corrections: “He go” → “He goes”; “She is senior than me” → “She is senior to me.” Do not equate a regional accent with a grammatical error.

## Practice with answers
1. Form a question: “You are ready.” → “Are you ready?”
2. Agree: “Each student ___ a notebook.” → has.
3. Passive: “They completed the task.” → “The task was completed.”
4. Compare: “This road is ___ than that road.” → longer, or another suitable comparative adjective.
5. Identify the auxiliary in “She has finished.” → has.

## 50-minute lesson
0–10: construct sentences from word cards. 10–20: auxiliaries and question formation. 20–30: agreement in a dialogue. 30–40: active and passive role-play. 40–47: comparison and corrections. 47–50: exit ticket with one explanation.

## Review
How does an auxiliary help form a question? Why does “list” rather than “books” control agreement in “the list of books is”? When is passive voice useful?''')]
d['course-4:1']=[n('spoken-vocab','Unit II · Vocabulary Building and Pronunciation','https://www.teachingenglish.org.uk/professional-development/teachers/knowing-subject/d-h/phoneme','''# Unit II: Vocabulary Building and Pronunciation
Spoken English · Semester 1

## Word formation
Prefixes attach before a base (un + clear → unclear); suffixes attach after it (teach + er → teacher). Some word classes change through suffixes: decide (verb), decision (noun), decisive (adjective). Form and meaning are not always predictable, so check a dictionary. A compound joins elements, as in “classroom”; spelling conventions differ.

## Word relationships and use
Synonyms are similar in context (begin/start); antonyms contrast (possible/impossible). Homonyms are words with the same spelling or sound but different meanings; terminology varies between dictionaries. For example “bank” can mean a financial institution or the side of a river. One-word substitutes condense a definition: a person who writes poems is a poet. For odd-one-out questions, identify a defensible shared feature: rose, jasmine, lotus, carrot → carrot is a vegetable while the others are commonly classified as flowers.

Idioms may have non-literal meanings: “break the ice” means ease an awkward beginning. Practise joining sentences with appropriate relationships: “It rained. We stayed indoors.” → “Because it rained, we stayed indoors.” Do not join clauses in a way that changes the original meaning.

## Vowels and consonants
Speech sounds are made by the vocal organs; spelling and sound do not correspond one-to-one in English. Vowels generally involve relatively open airflow, while consonants involve some obstruction or narrowing. A phoneme is a sound category that can distinguish meaning in a language or variety. Pronunciation varies legitimately across Englishes, so use a suitable model and seek intelligibility rather than erasing a speaker’s accent.

## Word stress, sentence stress and intonation
Word stress makes one syllable more prominent: in a common pronunciation, REcord is a noun and reCORD is a verb. Check the dictionary for the variety being taught. Sentence stress highlights information relevant to meaning: “I wanted the RED book” contrasts colour. Intonation is the movement of pitch across an utterance; a question may rise or fall depending on its form, meaning and context. Do not present one pitch pattern as universal for every question.

## Practice with answers
1. Change “happy” to a noun: happiness.
2. Antonym of “accept” in many contexts: reject.
3. Join: “She was tired. She completed the work.” → “Although she was tired, she completed the work.”
4. Explain “bank” in “river bank”: land alongside a river.
5. Say “I asked for the RED pen” and then “I asked for the red PEN”; discuss which contrast each emphasis suggests.

## 50-minute lesson
0–10: form word families. 10–20: synonyms, antonyms and idioms in context. 20–30: listen and identify prominent syllables. 30–40: practise sentence emphasis and intonation in pairs. 40–47: join sentences with logical connectors. 47–50: record one new word and example.

## Review
Why does spelling not always predict pronunciation? How can sentence stress change the information highlighted? Why should students hear more than one intelligible variety of English?''')]
d['course-4:2']=[n('spoken-conversation','Unit III · Conversational Skills','https://pressbooks.bccampus.ca/uvicpeopleteamsandorganizations/chapter/chapter-4-communication-and-perception/','''# Unit III: Conversational Skills
Spoken English · Semester 1

## Beginning and sustaining conversation
A conversation involves listening, responding and taking turns. In a new setting, greet the person, introduce yourself and ask a relevant open or closed question. Example: “Good morning. I’m Meena from the English department. How did you find the workshop?” Follow up using what the person actually says. Respect the other person’s willingness to talk; a conversation is not a list of memorised questions.

## Asking and answering questions
Closed questions often invite a short answer: “Is the library open?” Open questions invite explanation: “What did you find useful about the session?” Use “Could you repeat that?” or “Do you mean…?” to clarify. Answer directly first, then add a relevant detail. Politeness depends on relationship and context, not a fixed formula alone.

## Description
For a person, choose relevant details such as role, interests or observed behaviour; avoid unnecessary assumptions about appearance or identity. For a place, orient the listener and select significant features. For an event, identify what happened, where, when and why it mattered. Example: “The seminar was held in the library on Tuesday. Students discussed how to evaluate online sources.”

## Extempore, persuasive and descriptive speaking
Extempore speaking uses limited preparation; take a moment to organise an opening, two points and a closing. A persuasive talk makes a claim and supports it with reasons and evidence. A descriptive talk helps the listener visualise a subject through purposeful detail. In all cases, adapt your voice, vocabulary and length to the audience; neither loudness nor an unfamiliar accent is a measure of the quality of ideas.

## Narration and character
A narrative usually establishes setting and characters, presents a sequence or problem and describes an outcome. Use time markers such as “first,” “later” and “finally” where useful. To describe a character, distinguish a stated fact from an interpretation: “She returns the lost book” is an action; “she is considerate” is an interpretation supported by that action. Explain situations without presenting an assumption as a fact.

## Model activity
Tell a one-minute account: “On Monday, our class planned a reading event. At first, the room was unavailable. We spoke to the librarian, found another space and held the event on Friday. The experience showed us the value of planning alternatives.” Listeners identify setting, problem, action and outcome; then ask one clarification question.

## 50-minute lesson
0–10: introductions in pairs. 10–20: open and closed questions. 20–30: describe a place without naming it; partner asks questions. 30–40: one-minute narration. 40–47: brief persuasive speech with one reason. 47–50: constructive peer feedback.

## Questions
What makes a follow-up question effective? How does a descriptive speech differ from a persuasive one? What evidence supports a claim about a fictional character?''')]
d['course-4:3']=[n('spoken-group','Unit IV · Group Communication','https://pressbooks.bccampus.ca/uvicpeopleteamsandorganizations/chapter/chapter-4-communication-and-perception/','''# Unit IV: Group Communication
Spoken English · Semester 1

## Group discussion
A group discussion is a structured exchange in which participants contribute to a shared purpose. It is not a competition to speak most. Begin by identifying the question and time available. Participants offer relevant points, listen, support claims with examples, respond to others and help the group summarise its position. If disagreement occurs, address the idea rather than attacking the person.

Useful expressions: “Could we define the problem first?” “I would like to add…” “What evidence supports that?” “We seem to agree on two points, but differ on the third.” A facilitator can invite a quieter member without forcing anyone to disclose personal information.

## Assigning tasks and leadership
Divide a task into manageable roles: facilitator, researcher, timekeeper, note-taker and presenter are possible examples. Explain each role, expected output and deadline. Rotate responsibilities so all students practise speaking and coordination. A leader checks progress, clarifies uncertainty and shares decisions; leadership need not mean doing all the work.

## Task completion and cohesion
Example task: plan a college reading event. Agree on audience, venue, budget assumptions, responsibilities and deadline. Each participant reports progress, identifies obstacles and asks for help where needed. Summarise decisions in writing. Group cohesion means a sense of shared purpose and respectful cooperation, not an obligation to agree on everything. Clear goals, fair participation and constructive conflict resolution can support it.

## Group presentations and slides
Organise the presentation with an introduction, coordinated sections and a conclusion. Rehearse transitions between speakers and keep to the allotted time. Slides should support, not replace, speech: use readable text, clear headings and relevant visuals, and credit sources. Do not overload slides or read every word aloud. Check accessibility, including contrast and descriptions of important visuals; provide materials in accessible formats when needed. Slide software is one possible tool, not a prerequisite for every presentation.

## 50-minute lesson
0–8: explain discussion purpose and roles. 8–15: assign roles for the reading-event task. 15–30: groups plan and record decisions. 30–42: each group presents for three minutes. 42–47: peers provide one strength and one improvement. 47–50: members reflect on whether everyone had an opportunity to contribute.

## Assessment checklist
Was the response relevant? Did the student listen and build on a point? Were reasons understandable? Was speaking time shared? Did the group report decisions accurately? Feedback should focus on observable actions, not assumptions about personality or accent.

## Questions
What is the difference between leadership and domination? How can roles improve accountability? What makes a slide useful? How can a group disagree respectfully?''')]
d['course-4:4']=[n('spoken-listening','Unit V · Listening Skills and Non-verbal Communication','https://openbooks.macewan.ca/professionalcommunication/chapter/5-4-barriers-to-effective-listening/','''# Unit V: Listening Skills and Non-verbal Communication
Spoken English · Semester 1

## Why listening matters
Listening supports comprehension, cooperation and accurate responses. Hearing sound is not the same as understanding it. Active listening includes paying attention, recognising the speaker’s purpose, paraphrasing a key point and requesting clarification. It does not require agreement with everything said.

## Basics and barriers
Listen first for the situation and general message; then note important details, distinctions and the speaker’s purpose. Noise, a poor audio connection, unfamiliar vocabulary, fatigue, stress, prejudice and rehearsing a reply can interfere. Reduce distractions, request repetition or accessible formats, take selective notes and check interpretation. Treat listening as a learnable practice rather than a personality label.

## Listening for gist, style and tone
Gist is the overall point: “The speaker wants the meeting postponed.” Style refers to features of expression, such as formal or conversational wording. Tone is the attitude conveyed—perhaps concerned, enthusiastic or uncertain. Base tone judgements on words and delivery together, and recognise that accent, cultural differences or vocal disability can affect interpretation. If a message is ambiguous, ask rather than declaring what the speaker feels.

## Voice recording exercises
With participants’ permission, record a short speech or dialogue and listen back. First check whether the central point is clear; then review pace, audible volume, pauses and transitions. Identify one strength and one manageable next step. Recording must be optional or accommodated when necessary; do not share recordings without consent. The aim is intelligibility and confidence, not eliminating a regional accent.

## Non-verbal communication and etiquette
Gesture, posture, personal space, facial expression and eye behaviour can support or complicate spoken meaning. A listener may indicate attention by a verbal response, a nod, a question or another culturally and personally appropriate behaviour. Avoid diagnosing honesty or interest from a single gesture. Expectations differ by context, culture, neurodiversity and disability. Etiquette means respectful behaviour suited to the situation: wait for a turn, ask before recording, respect personal space and use a courteous form of address.

## Practice
A speaker says: “The event is moving to Friday because the hall is unavailable on Thursday.” Gist: the event has moved to Friday. Key reason: the hall is unavailable Thursday. A listener should not infer the event has been cancelled.
Pair activity: one student describes a route for thirty seconds; the other paraphrases and asks a clarification. Compare the original and paraphrase without penalising harmless differences in wording.

## 50-minute lesson
0–10: distinguish hearing, gist and detail. 10–20: route-listening exercise. 20–30: identify barriers and solutions. 30–40: optional recording and self-review. 40–47: discuss different interpretations of a gesture. 47–50: exit ticket: give one respectful clarification question.

## Questions
What is listening for gist? Name two barriers and solutions. Why is one gesture not conclusive evidence of a person’s feelings? What makes feedback on a recording constructive?''')]
with open(p,'w') as f:json.dump(d,f,ensure_ascii=False,indent=2)
