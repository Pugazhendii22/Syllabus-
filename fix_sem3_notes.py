"""Apply the targeted Sem 3 and communication corrections only.
Preserves keys, entry ids and titles; safe to re-run. Do not run old generators.
"""
import json
from pathlib import Path
P = Path(__file__).with_name('prepared-notes.json')
d = json.loads(P.read_text(encoding='utf-8'))
original_keys = set(d)

def entry(key, ident):
    matches = [n for n in d[key] if n['id'] == ident]
    assert len(matches) == 1, (key, ident)
    return matches[0]

def replace(key, ident, source, text, preliminary=None):
    n = entry(key, ident)
    n['source'] = source
    n['text'] = text.strip() + '\n'
    if preliminary is True:
        n['status'] = 'preliminary'
    elif preliminary is False:
        n.pop('status', None)

def insert(key, ident, marker, content):
    n = entry(key, ident)
    old = n['text']
    block = content.strip()
    if block in old:
        old = old.replace(block+'\n\n', '', 1)
    assert old.count('## 50-minute lesson') == 1, (key, ident, marker)
    n['text'] = old.replace('## 50-minute lesson', block+'\n\n## 50-minute lesson')


replace('course-19:1','huxley-beauty','https://thephilosopher.net/huxley/tvorchestvo/the-beauty-industry/', '''# Aldous Huxley · The Beauty Industry
Functional English II · Semester 3

## Context and argument
In this essay, collected in Music at Night (1931; publication reference: https://www.jonkers.co.uk/rare-book/10870/music-at-night/aldous-huxley), Huxley combines social observation, irony and a serious argument about beauty. He claims that the American beauty industry alone has not been affected by the Depression. He reports approximately £3 million a week, or £156 million a year, spent by American women on appearance, and tentatively compares the annual sum with the revenue of India under British rule. He says he does not know the European figures but assumes they are much smaller. These are Huxley’s historical claims, not independently verified economic statistics or present-day facts; the essay does not give a specific British spending figure in the text consulted.

## Social change and partial success
Huxley associates the industry with changes in women’s social position and a less ascetic Christian attitude towards the body. He credits the campaign with partial success: he observes that more women retain a youthful appearance for longer, helped by improved health as well as cosmetic practices. His prediction that the old-fashioned image of the “old lady” will disappear is an exaggeration about appearance, not a claim that women stop ageing.

## The limitation: the porcelain jar
Huxley also calls the campaign a failure if it aims at complete human beauty. A porcelain jar can be judged by its shape, colour and surface irrespective of its contents, whereas a person is alive and has an experiencing inner life. He argues that expressions, movement and character affect how human beauty is perceived. The analogy supports his claim that outward treatment alone is insufficient; it does not mean that cosmetics are necessarily harmful or that appearance reliably reveals moral character.

## Method and critical response
The essay uses humour, irony, generalisation and comparison, but its argument is not purely satire: Huxley acknowledges benefits and makes a moral and social critique. Question his gender assumptions: he singles out women, risks judging inner lives by appearance and neglects autonomy, pleasure, work and pressures around beauty practices. Discuss the argument without endorsing ageism or judging a person’s worth by their appearance.

## 50-minute lesson
0–10: identify the historical context. 10–20: map the spending claim and its limits. 20–30: list benefits he recognises. 30–40: explain the jar analogy. 40–50: evaluate one gender assumption with evidence.

## Questions
Why does Huxley call the campaign both a success and a failure? How do a person and a jar differ in his analogy? What assumptions in his argument can be challenged?

## Reading note
The source links to an online version of the essay. Compare it with the prescribed Impressions-II selection; verify publication details and any quotation in the assigned text.''')

replace('course-19:0','assadi-ring','http://www.artarena.force9.co.uk/mina.htm', '''# Mina Assadi · A Ring to Me is Bondage
Functional English II · Semester 3

## Poet and reading note
Mina Assadi (also transliterated Asadi) is an Iranian poet who lives in exile in Sweden (biographical reference: https://prabook.com/web/mina.assadi/2080005). An online English version in Mahmud Kianush’s Modern Persian Poetry has been consulted; the precise translation and selection in Impressions-II have not been checked. This entry remains preliminary until they are compared.

## Poem summary and images
The speaker gives unexpected personal meanings to familiar things. Instead of centring a prayer mat, she imagines roads passing through gardens and associates prayer with happiness and the music of sparrows. Roads, birds and walking suggest movement and freedom. The prayer mat can be read as an image of conventional restriction in contrast to the speaker’s chosen way of praying; the poem does not simply reject prayer or all religion.

She calls solitude happiness, a desert home, and what causes sadness love. These paradoxical definitions unsettle ordinary expectations. The person who plucks a flower is described as unable to see its value; the net separates a fish from its element, suggesting violent confinement. Looking at the sea, the speaker imagines a shifting sense of smallness and vastness when it meets the ocean. A cage makes its possessor a gaoler, while unused thought becomes a wall. The closing returns to roads and gardens.

## Interpretation and form
A standard classroom reading takes the ring as a symbol of marriage experienced as bondage by women, and reads the poem as resistance to restrictive conventions and oppression. This is an interpretation: the poem does not say that every marriage or ring is oppressive. Its repeated personal definitions, contrasts and circular return give the speaker a distinctive voice. Invite different supported readings rather than treating every nature image as having only one fixed meaning.

## 50-minute lesson
0–10: introduce poet and context. 10–20: follow the roads and prayer imagery. 20–30: examine fish, net and cage. 30–40: discuss ring, sea and resistance. 40–50: write a supported interpretation and compare the ending with the opening.

## Questions
How do roads and the ring contrast? What does the fish-and-net image suggest? Why is marriage as bondage an interpretation rather than a statement about every marriage?

## Reading note
Compare the online English version with the poem and translation assigned in Impressions-II before citing line numbers or exact wording.''',True)

replace('course-19:1','raja-cow','https://xpressenglish.com/our-stories/barricades/', '''# Raja Rao · The Cow of the Barricades
Functional English II · Semester 3

## Story overview
A mysterious cow, Gauri, visits the Master on Tuesdays, accepts grain from him and disappears. People seek her, bring offerings and honour her as a sacred figure. The story separately names Mahatma Gandhi and says she has also visited him.

Against colonial rule, the Mahatma’s supporters boycott foreign cloth, government service and taxes. Mill and factory workers build barricades; the Master opposes fighting in the Mahatma’s name, but the workers insist on resistance and prepare for battle. He resigns as their President and meditates to avert bloodshed.

Gauri comes through the tense streets. Workmen lay down their arms and honour her; people help her to the top of a barricade. The soldiers’ chief shoots her in the head, and the narrative says no blood is visible. Seth Jamnalal Dwarkachand (also printed Dwarak Chand) buys two houses by the barricades, makes a loop road and erects a metal statue. Children play around it and toy Gauris circulate. The Master says she waits in the Middle Heavens to be born again when India sorrows before freedom.

## Interpretation
A common classroom interpretation reads the Master as a Gandhi-like or Gandhian figure and Gauri as Mother India, embodying compassion, sacrifice and collective hope. However, the online story distinguishes the Master from the separately named Mahatma: it says Gauri has visited one other person, Gandhi. Treat their identification as an allegorical interpretation, not a literal fact that the story never names Gandhi. Readers can also question how religious imagery represents a diverse nation and how the conflict between workers and the Master complicates a simple message.

## 50-minute lesson
0–10: identify the setting and storyteller. 10–20: trace Gauri’s visits. 20–30: map the workers, Master and soldiers. 30–40: discuss the shooting and statue. 40–50: test an allegorical reading against the text.

## Questions
Why do the workers and Master disagree? What happens when Gauri reaches the barricade? How does the statue turn death into public memory? What textual detail complicates identifying the Master literally with Gandhi?

## Reading note
The linked story is an online text; compare spelling and wording with the anthology before quoting.''')

replace('course-19:2','ghosh-sea','https://lailalalami.com/2006/12/the-town-by-the-sea/', '''# Amitav Ghosh · The Town by the Sea
Functional English II · Semester 3

## Context and limitation
The account concerns the Indian Ocean tsunami of 26 December 2004 and its consequences in the Andaman and Nicobar Islands. Anthologies may abridge the longer account; check Impressions-II for exact selection and sequence. The subject involves bereavement and disaster and should be discussed sensitively.

## Outline and central scene
Ghosh accompanies the Director, a scientist, through the ruins of Malacca on Car Nicobar after the tsunami. The Director was away when the earthquake and waves struck; his son survived, while his wife and daughter were lost. The disaster is understood through a particular family as well as a devastated landscape.

Among the wreckage the Director picks up slides from his epidemiological research. He points out his daughter’s yellow paint box but chooses not to take it. Ghosh is struck by that choice and reflects on grief and the life of the mind. Do not turn the decision into proof that the Director values work more than his daughter: grief cannot be reliably judged from a single gesture.

## Papers, identity and planning
In the broader essay Ghosh describes survivors’ lost identity cards, certificates and other documents, showing how the loss of papers can make it harder to prove identity, property or entitlements. He also examines planning that placed settlements near the beachfront, exposing people to coastal hazards. This is a question about human decisions and unequal vulnerability, not a reason to blame victims or claim that one location explains every loss. The linked essay excerpt at https://www.barnesandnoble.com/w/incendiary-circumstances-amitav-ghosh/1111826984?ean=2940191875705 provides further context; check whether these passages appear in the assigned extract.

## Reading critically
Distinguish observed actions, reported experience and interpretation. Treat survivors respectfully and do not make assumptions about how grief should be expressed.

## 50-minute lesson
0–10: context and sensitivity note. 10–20: identify the Director, place and disaster. 20–30: compare the slides and paint box without judging grief. 30–40: discuss documents and settlement planning. 40–50: write a supported question about the account.

## Questions
What does the Director take and leave? How can lost documents affect survivors? What questions does Ghosh raise about coastal planning?

## Reading note
The linked summary discusses the central scene. The longer essay may differ from the prescribed anthology extract; check Impressions-II before quoting or assessing its scope.''',True)

n=entry('course-19:3','narayan-engine')
n['source']='https://litgram.in/engine-trouble-summary/'
n['text']=n['text'].replace('The narrator wins a road engine in a lottery at a travelling fair called Gaiety Land.', 'The story, collected in Malgudi Days (1943), is set in the fictional town of Malgudi. Its first-person narrator, the Talkative Man, wins a road engine in a lottery at the travelling fair Gaiety Land, held on the Gymkhana ground.').replace('He hires a temple elephant, labourers and Joseph, a former bus driver, to help direct the engine.', 'He hires a temple elephant, fifty labourers and Joseph, a dismissed bus driver, to help move and steer the engine.')
if '## Reading note' not in n['text']:
    n['text']=n['text'].replace('Read the assigned text and verify its wording and selection against the course anthology.','## Reading note\nThe linked summary supports the main plot; compare the story and collection details with the assigned anthology.')
insert('course-2:2','reading-skills','reading-expansion', '''## Thirty idioms and phrases in context
These are informal unless context suggests otherwise; meanings depend on use.
1. Break the ice — ease an awkward beginning. A game helped break the ice.
2. Once in a blue moon — very rarely. We eat out once in a blue moon.
3. A piece of cake — very easy. After practice, the task was a piece of cake.
4. Under the weather — feeling unwell. Ravi stayed home because he felt under the weather.
5. In the same boat — in a similar difficulty. We are all in the same boat before exams.
6. On the right track — progressing correctly. Your outline is on the right track.
7. Hit the books — study hard. I must hit the books tonight.
8. A blessing in disguise — an apparent problem that proves beneficial. Missing the bus was a blessing in disguise when the later journey met an old friend.
9. Better late than never — a late action is preferable to none. She returned the book late, but better late than never.
10. Call it a day — stop working for now. We finished the draft and called it a day.
11. Get the ball rolling — begin an activity. The chair asked a question to get the ball rolling.
12. Give a hand — help. Could you give me a hand with these chairs?
13. In hot water — in trouble. He was in hot water for missing the deadline.
14. Keep an eye on — watch or monitor. Please keep an eye on the oven.
15. Learn the ropes — learn the basic procedures. New volunteers learn the ropes from experienced members.
16. Make ends meet — manage to pay essential expenses. Rising costs made it difficult to make ends meet.
17. On cloud nine — very happy. She was on cloud nine after hearing the good news.
18. Out of the blue — unexpectedly. An old friend called out of the blue.
19. See eye to eye — agree. The committee did not see eye to eye on the plan.
20. Speak of the devil — said when a person being discussed appears. Speak of the devil: here is Meena now.
21. Spill the beans — reveal a secret. Arun spilled the beans about the surprise.
22. Take something with a pinch of salt — treat it sceptically. Take that unverified rumour with a pinch of salt.
23. The ball is in your court — it is your turn to act. I have sent the proposal; the ball is in your court.
24. Time flies — time seems to pass quickly. Time flies when we are busy.
25. Turn over a new leaf — start behaving better or differently. He decided to turn over a new leaf and arrive on time.
26. Up in the air — undecided. The venue is still up in the air.
27. By and large — generally. By and large, the session went well.
28. At short notice — with little warning. The room was changed at short notice.
29. In advance — before the event. Please book the room in advance.
30. In the long run — over a longer period. Regular practice can help in the long run.

## Thirty synonym pairs
Meanings are approximate and context-sensitive: 1. begin/start; 2. end/finish; 3. quick/rapid; 4. small/little; 5. large/big; 6. silent/quiet; 7. happy/glad; 8. sad/unhappy; 9. brave/courageous; 10. reply/answer; 11. help/assist; 12. choose/select; 13. correct/accurate; 14. difficult/hard; 15. easy/simple; 16. honest/truthful; 17. idea/notion; 18. aim/purpose; 19. error/mistake; 20. gift/present; 21. safe/secure; 22. shut/close; 23. rich/wealthy; 24. tidy/neat; 25. vacant/empty; 26. angry/cross; 27. beautiful/lovely; 28. old/aged; 29. strange/unusual; 30. careful/cautious. Check grammar and connotation before substituting.

## Thirty antonym pairs
1. early/late; 2. open/closed; 3. hot/cold; 4. high/low; 5. near/far; 6. wide/narrow; 7. large/small; 8. fast/slow; 9. clean/dirty; 10. full/empty; 11. strong/weak; 12. rich/poor; 13. kind/cruel; 14. happy/sad; 15. begin/end; 16. accept/reject; 17. arrive/depart; 18. borrow/lend; 19. buy/sell; 20. build/demolish; 21. increase/decrease; 22. include/exclude; 23. legal/illegal; 24. possible/impossible; 25. visible/invisible; 26. noisy/quiet; 27. safe/dangerous; 28. true/false; 29. generous/stingy; 30. permanent/temporary. Some contrasts depend on context.

## General comprehension: fictional passage
“The River Lane reading group started a monthly book exchange. Members place books on a table in the community hall and take another book to read. The organiser asks each person to return borrowed books at the next meeting. The group is looking for a volunteer to maintain a list of titles.”
1. How often does the exchange take place? 2. Where are books placed? 3. When are borrowed books due? 4. What help is needed? 5. Does the passage prove that every book is a novel?
Answers: 1. Monthly. 2. On a table in the community hall. 3. At the next meeting. 4. A volunteer to maintain a list of titles. 5. No; genres are not specified.

## Technical comprehension: fictional passage
“A rainwater tank has a filter at the inlet. The filter catches leaves before water enters the tank. A sensor signals when the water reaches the marked maximum level; a valve then closes the inlet. The sensor does not measure whether the water is safe to drink. The filter should be checked every month.”
1. What does the filter catch? 2. What happens at maximum level? 3. Does the sensor test drinking safety? 4. How often should the filter be checked? 5. Why must a reader not infer that the water is drinkable?
Answers: 1. Leaves. 2. The sensor signals and the valve closes the inlet. 3. No. 4. Monthly. 5. The passage explicitly says the sensor does not measure drinking safety; no safety test is described.''')

insert('course-2:3','writing-skills','writing-formats', '''## Model formats and samples
All names, institutions, events and dates below are fictional classroom examples. Real documents must use verified details and any required institutional layout.

### Formal letter
Format: sender and date; recipient; subject; salutation; purpose and details; courteous request; closing and signature.
12 Lake Road, Malgudi\n12 August 2026\nThe Librarian, Malgudi College\nSubject: Request for a reading room\nDear Sir or Madam,\nOur reading group requests the use of a room on 20 August from 3 to 4 p.m. Please let us know whether it is available and how to book it.\nYours faithfully,\nAnita Rao, Group Secretary

### Informal letter
12 Lake Road, Malgudi\n12 August 2026\nDear Leela,\nOur reading group is planning a book exchange next week. I hope you can visit and tell us about the stories you enjoy. Write soon and let me know how your course is going.\nWith love,\nAnita

### Notice
MALGUDI COLLEGE READING GROUP\nNOTICE | 12 August 2026\nBook exchange: 20 August, 3 p.m., Community Hall. Members may bring a book to exchange. Contact Anita Rao, group secretary.

### Agenda
Reading group meeting, 20 August 2026, 3 p.m., Community Hall\n1. Welcome and apologies. 2. Review of previous actions. 3. Book-exchange arrangements. 4. Next meeting. 5. Closing.

### Minutes
Reading group meeting, 20 August 2026, Community Hall\nPresent: Anita Rao and Leela Das.\nDecision: Members agreed to hold a book exchange next month.\nAction: Anita will request a table by 27 August.\nNext meeting: 10 September, 3 p.m.\nRecorded by: Leela Das.\nAn agenda is prepared before a meeting; minutes record decisions afterwards.

### Report
Title: Report on the reading-group meeting\nDate: 21 August 2026\nPurpose: To record arrangements for a proposed exchange.\nSource: The meeting minutes.\nFindings: Members agreed to hold an exchange; a table still needs to be booked.\nRecommendation: Confirm table availability before announcing the venue.\nPrepared by: Leela Das.

### Paragraph
“A reading group gives people an opportunity to share ideas. Members can compare their responses and recommend books to one another. A regular meeting time can help the group continue its discussions.” The opening introduces the focus; the other sentences develop it.

### Short essay
Title: Why shared reading matters\nReading is often a private activity, but discussing a book can also be valuable. A reading group allows different interpretations to meet.\nFirst, readers can explain what they noticed and ask one another questions. Second, the group can introduce members to books they might not otherwise choose. Respectful listening matters because readers may disagree.\nShared reading therefore adds conversation to individual reading. A welcoming group can make both activities more rewarding.

## Twenty common formal-writing errors
Each correction suits the stated context; alternatives and language varieties exist.
1. She go to class. → She goes to class. (agreement)
2. The students was ready. → The students were ready. (agreement)
3. Each student have a card. → Each student has a card. (agreement)
4. He discussed about the issue. → He discussed the issue. (verb pattern)
5. She gave me an advice. → She gave me some advice. (uncountable noun)
6. I have many information. → I have much information. (uncountable noun)
7. He is a honest man. → He is an honest man. (vowel sound)
8. I saw an university. → I saw a university. (consonant sound)
9. I am here since Monday. → I have been here since Monday. (continuing situation)
10. Yesterday she go home. → Yesterday she went home. (past form)
11. I look forward to meet you. → I look forward to meeting you. (preposition + -ing)
12. She is good in drawing. → She is good at drawing. (conventional combination)
13. The news are surprising. → The news is surprising. (agreement)
14. One of the books are missing. → One of the books is missing. (head noun)
15. I did not went. → I did not go. (base verb after did)
16. He can sings. → He can sing. (base verb after modal)
17. Where you are going? → Where are you going? (direct question order)
18. The class ended, we left. → The class ended, so we left. (comma splice)
19. Its raining. → It’s raining. (it is)
20. Please return the book’s. → Please return the books. (plural, not possession).''')
insert('course-20:2','func-writing-3','application-models', '''## Model résumé: fictional example
Every detail below is invented for classroom practice; never use fictional qualifications in a real application.

ANITA RAO\nMalgudi | anita.rao@example.com | 00000 00000 (fictional contact)\nProfile: English student interested in library and reading-group work.\nEducation: B.A. English, Malgudi College, 2024–2027 (fictional).\nSkills: written communication, basic spreadsheets, organising materials.\nRelevant activity: Student reading-group volunteer, 2025–2026; arranged weekly sessions and maintained a book list.\nLanguages: English and Tamil.\nReferences: supplied if requested and with permission.

## Model covering letter: fictional example
12 Lake Road, Malgudi\n12 August 2026\nThe Coordinator, Malgudi Community Library\nSubject: Covering letter for library volunteer role\nDear Sir or Madam,\nPlease consider my enclosed résumé for the library volunteer role. My reading-group work involved organising sessions and maintaining a list of books. These activities developed my written communication and record-keeping skills.\nI would be pleased to discuss how I could support your library’s activities. Thank you for your consideration.\nYours faithfully,\nAnita Rao

## Model application letter: fictional example
12 Lake Road, Malgudi\n12 August 2026\nThe Principal, Malgudi College\nSubject: Application for permission to conduct a book exchange\nDear Sir or Madam,\nOn behalf of the reading group, I request permission to hold a book exchange in the community hall on 20 August from 3 to 4 p.m. We plan to arrange tables and return the room to its original condition. Please let us know whether the hall is available and what approval is required.\nYours faithfully,\nAnita Rao, Group Secretary

A covering letter accompanies and explains a résumé for a role; an application letter makes a formal application or request. Formats and required attachments vary.''')

insert('course-20:3','func-writing-4','news-models', '''## Three fictional classroom models
The names, events and observations below are invented for practice, not real reporting. Verify all facts and obtain permission before publishing a real account.

### News article
Reading group plans book exchange\nBy Staff Reporter | Malgudi, 21 August 2026\nThe Malgudi College reading group plans to hold a book exchange next month, according to minutes from its meeting on 20 August.\nThe minutes record that members agreed to request a table for the event. The group has not yet confirmed the venue. Organisers intend to share further details after the arrangements are complete.\nThe lead gives the main development and attributes it to a source; the second paragraph adds context and makes the unconfirmed venue clear.

### Letter to the editor
12 Lake Road, Malgudi\n22 August 2026\nThe Editor, The Malgudi Gazette\nSubject: Access to reading spaces\nSir or Madam,\nShared reading spaces can give students and local residents a place to study and exchange ideas. I suggest that local institutions consult users about opening times before planning future activities. A brief, accessible consultation could help identify different needs without assuming that all readers want the same facilities.\nYours faithfully,\nAnita Rao

### Report
Report on reading-group meeting\nTo: Group Coordinator | From: Leela Das | Date: 21 August 2026\nPurpose: Record decisions about a proposed book exchange.\nSource: Minutes of the meeting on 20 August.\nFindings: Members agreed to plan an exchange and request a table. The venue remains unconfirmed.\nRecommendation: Confirm the venue and table before circulating a notice.\nIn a real report, record the method, dates, findings and limitations accurately. A recommendation is a proposed action, not an established fact.''')

insert('course-20:4','func-writing-5','speech-and-vocabulary', '''## Direct and indirect speech: rules table
Changes depend on who reports, when and whether the statement still holds. Backshift is common after a past reporting verb, not an unconditional rule.

| Type | Direct speech | Possible indirect form |
| --- | --- | --- |
| Statement | Meena said, “I am tired.” | Meena said that she was tired. |
| Yes/no question | Ravi asked, “Are you ready?” | Ravi asked whether I was ready. |
| Wh-question | Ravi asked, “Where do you live?” | Ravi asked where I lived. |
| Command | The teacher said, “Close the door.” | The teacher told us to close the door. |
| Negative command | The teacher said, “Do not run.” | The teacher told us not to run. |
| Request | She said, “Please help me.” | She asked me to help her. |
| Exclamation | She said, “What a beautiful garden!” | She exclaimed that the garden was beautiful. |

Indirect questions normally use statement word order, without the question mark of a direct question. Choose a reporting verb that matches the function; do not invent an addressee if the context does not supply one.

### Typical tense changes after a past reporting verb
| Direct | Possible backshift |
| --- | --- |
| present simple: works | past simple: worked |
| present continuous: is working | past continuous: was working |
| past simple: worked | past perfect: had worked |
| present perfect: has worked | past perfect: had worked |
| will | would |
| can | could |

Present tense can remain when the information is still true, and past simple can remain when the timing is clear or the situation is still relevant. “Must” changes according to meaning; obligation may be reported with “had to,” but logical necessity need not change mechanically.

### Time and place words
When the reporting viewpoint changes, today may become that day, yesterday the previous day, tomorrow the next day, now then, here there, and this that. Adjust to actual context: a speaker’s “tomorrow” on Monday may be reported on Tuesday as “today” or “Tuesday,” not automatically “the next day.”

### Practice with answers
1. Report: She asked, “Where is the key?” → She asked where the key was. 2. Report: The teacher said, “Do not write on the desk.” → The teacher told us not to write on the desk. 3. Report on Tuesday: On Monday he said, “I will return tomorrow.” → On Monday he said he would return on Tuesday. 4. Report: The guide said, “The Earth moves around the Sun.” → The guide said that the Earth moves around the Sun; present can remain for a continuing general truth.

## Thirty synonym pairs
These are approximate and context-sensitive: 1. begin/start; 2. end/finish; 3. quick/rapid; 4. small/little; 5. large/big; 6. silent/quiet; 7. happy/glad; 8. sad/unhappy; 9. brave/courageous; 10. reply/answer; 11. help/assist; 12. choose/select; 13. correct/accurate; 14. difficult/hard; 15. easy/simple; 16. honest/truthful; 17. idea/notion; 18. aim/purpose; 19. error/mistake; 20. gift/present; 21. safe/secure; 22. shut/close; 23. rich/wealthy; 24. tidy/neat; 25. vacant/empty; 26. angry/cross; 27. beautiful/lovely; 28. old/aged; 29. strange/unusual; 30. careful/cautious.

## Thirty antonym pairs
1. early/late; 2. open/closed; 3. hot/cold; 4. high/low; 5. near/far; 6. wide/narrow; 7. large/small; 8. fast/slow; 9. clean/dirty; 10. full/empty; 11. strong/weak; 12. rich/poor; 13. kind/cruel; 14. happy/sad; 15. begin/end; 16. accept/reject; 17. arrive/depart; 18. borrow/lend; 19. buy/sell; 20. build/demolish; 21. increase/decrease; 22. include/exclude; 23. legal/illegal; 24. possible/impossible; 25. visible/invisible; 26. noisy/quiet; 27. safe/dangerous; 28. true/false; 29. generous/stingy; 30. permanent/temporary.

## Twenty common formal-writing errors
1. She go. → She goes. (agreement)
2. They was ready. → They were ready. (agreement)
3. Each student have a card. → Each student has a card. (agreement)
4. He discussed about the plan. → He discussed the plan. (verb pattern)
5. She gave an advice. → She gave some advice. (uncountable noun)
6. I have many information. → I have much information. (uncountable noun)
7. A honest person. → An honest person. (vowel sound)
8. An university. → A university. (consonant sound)
9. I am here since Monday. → I have been here since Monday. (continuing situation)
10. Yesterday she go home. → Yesterday she went home. (past form)
11. I look forward to meet you. → I look forward to meeting you. (preposition + -ing)
12. She is good in drawing. → She is good at drawing. (conventional combination)
13. The news are surprising. → The news is surprising. (agreement)
14. One of the books are missing. → One of the books is missing. (head noun)
15. I did not went. → I did not go. (base verb after did)
16. He can sings. → He can sing. (base verb after modal)
17. Where you are going? → Where are you going? (direct question order)
18. The class ended, we left. → The class ended, so we left. (comma splice)
19. Its raining. → It’s raining. (it is)
20. Please return the book’s. → Please return the books. (plural, not possession)
These model formal conventions; other valid varieties and context-appropriate alternatives exist.''')

for key, ident, note in [
 ('course-20:2','func-writing-3','The linked Purdue guide provides job-search writing guidance. Adapt layouts to the recipient and institutional instructions.'),
 ('course-20:3','func-writing-4','The linked Purdue journalism guide introduces reporting practices. The models above are fictional and should not be presented as real events.'),
 ('course-20:4','func-writing-5','The linked Purdue guide covers punctuation. Consult a suitable grammar reference for reported speech and usage in context.')]:
    n = entry(key, ident)
    if '## Reading note' not in n['text']:
        n['text'] = n['text'].rstrip()+'\n\n## Reading note\n'+note+'\n'

assert set(d) == original_keys
P.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('Updated 10 targeted entries; all other entries and keys preserved.')
