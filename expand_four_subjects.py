"""Add detailed classroom material for Ammu's four selected subjects.

Append by stable ID without disturbing existing notes or bookmarks.
"""
import json
P='prepared-notes.json'
with open(P,encoding='utf8') as f:d=json.load(f)
def add(key,id,title,body,source,preliminary=False):
 item={'id':id,'title':title,'source':source,'text':f'# {title}\n\n{body}\n\nTeaching draft: consult the prescribed edition and verify quotations, text divisions and historical details before class.'}
 if preliminary:item['status']='preliminary'
 d[key]=[x for x in d.get(key,[]) if x['id']!=id]+[item]

add('course-1:3','faustus-sequence','Doctor Faustus · detailed story and teaching sequence', '''## Before teaching
The 1604 A-text and 1616 B-text differ in length, scenes and wording; modern act divisions also vary. This guide follows the major shared sequence rather than claiming fixed scene numbers. Warn students that the drama contains threats of eternal punishment.

## Learning goals
Reconstruct the bargain; analyse Faustus’s ambition, fear and use of power; relate comic scenes to the tragedy; distinguish the play’s theological perspectives from a single certain answer.

## Beginning: a scholar’s choice
The Chorus introduces Faustus, a scholar of humble origins whose rise invites comparison with Icarus. In his study Faustus rejects the limits he sees in logic, medicine, law and theology. His reading of theology is selective: he dwells on sin and death while overlooking passages about forgiveness. Valdes and Cornelius encourage him to practise magic. The good and evil angels stage competing pressures on him. Two scholars worry about his new company; Wagner’s wordplay produces a comic contrast to scholarly seriousness.

## The bargain
Faustus conjures Mephistopheles, who speaks of hell as separation from God and warns of suffering. Faustus nevertheless demands service and proposes a pact with Lucifer. He will receive 24 years of service and then forfeit his soul. His blood congeals while he tries to sign, and a warning appears on his arm. He treats warnings as obstacles, signs of fear or matters to interpret, not as reasons for a settled change of course. Mephistopheles supplies distractions and promised knowledge.

## Doubt and performance
Faustus asks questions about the heavens and repeatedly considers repentance. Devils divert or threaten him; a pageant of the Seven Deadly Sins offers spectacle. The distinction between genuine choice and coercive influence becomes increasingly difficult. He travels and plays tricks at the Pope’s court; later he entertains the Emperor by conjuring figures associated with Alexander. At other points he deceives a horse-courser. Comic scenes involving servants and magicians echo, rather than simply interrupt, the desire to acquire power.

## Final hours
Scholars ask to see Helen of Troy. An Old Man urges Faustus toward repentance, but fear and temptation continue. Faustus asks for Helen again. He tells scholars about the pact as the final night approaches; they offer prayer. Alone, he imagines time slowing, celestial bodies moving and his own body changing, but midnight arrives and devils claim him. How the aftermath is staged and whether scholars find remains depends on the version.

## Interpretive questions
Is Faustus condemned by a freely chosen act, by repeated despair, by forces controlling him, or by a combination? How do grand promises of knowledge compare with later practical tricks? Avoid describing any single religious tradition as speaking with one voice.

## 50-minute plan
0–8: establish versions and dramatic frame. 8–18: analyse Faustus’s opening choices. 18–28: map the bargain and warnings. 28–38: compare an ambitious promise with a comic episode. 38–46: read the final soliloquy sensitively. 46–50: exit answer—one possible interpretation supported by a scene.

## Revision answers
1. Length of the pact? Twenty-four years. 2. What does Mephistopheles say hell involves? Separation from God and suffering. 3. Why compare A and B texts? Their scenes and details differ; the assigned edition determines the wording.''','https://marloweshakespeare.info/farey/faustus.html')
add('course-1:3','shoemakers-sequence','The Shoemaker’s Holiday · detailed story and teaching sequence', '''## Plot strands
The comedy connects the courtship of Rowland Lacy and Rose with the working lives of Simon Eyre’s London shoemakers and the marriage of Ralph and Jane. Scene divisions differ in editions, so follow the printed text when assigning exact numbers.

## 1. Families, class and war
Rose’s father, the Lord Mayor, and Lacy’s uncle, the Earl of Lincoln, oppose the match. Lacy is ordered to serve in the war in France. Eyre and his men ask that newly married Ralph be spared conscription, but Lacy refuses. Ralph leaves Jane for military service; the unequal freedom of Lacy and Ralph matters throughout the comedy.

## 2. Disguise and the workshop
Instead of accompanying the army, Lacy arranges for another to go and stays in London disguised as a Dutch shoemaker, Hans. Eyre employs him. Lacy’s skill and imitation of foreign speech make his disguise theatrically entertaining, but also invite discussion of stereotypes. Rose, kept apart by her father, continues to pursue a meeting with him.

## 3. Eyre’s rise and Rose’s plan
Lacy alerts Eyre to an opportunity to buy goods from a ship and sell them profitably. Eyre’s fortunes rise; he becomes sheriff and then Lord Mayor. Rose and Lacy recognise each other despite the disguise and use helpers to arrange their marriage. Eyre’s prosperity allows him to support them and promise a feast for the craft.

## 4. Ralph and Jane
Ralph returns from war injured. A pair of shoes sent to the workshop helps him recognise that Jane is about to marry Hammon, who has led her to believe Ralph is dead. The shoemakers interrupt the wedding preparations. Jane recognises and chooses her husband; Hammon withdraws. Jane’s mistaken belief is not disloyalty: she was misinformed about Ralph’s fate.

## 5. Reconciliation and holiday
Rose and Lacy marry with Eyre’s help. Their relatives object and appeal to the king, who pardons Lacy’s military offence and approves the union. The play ends with Eyre’s festive hospitality and recognition of the shoemaking trade. Read the celebration alongside the fact that Ralph bears the physical cost of a war Lacy escapes.

## 50-minute plan
0–10: make a character map. 10–20: compare Lacy’s and Ralph’s military situations. 20–30: trace the shoe and Jane’s choice. 30–40: discuss Eyre’s rise and the king’s decision. 40–50: write whether the ending dissolves class difference or merely manages it.

## Check
Who is Hans? Lacy in disguise. How does Ralph learn about Jane? He recognises a shoe associated with her. Why does the feast matter? It makes the craft’s communal identity visible.''','https://www.litcharts.com/lit/the-shoemakers-holiday/summary')
add('course-1:3','lear-acts-one-two','King Lear · Acts I–II: division and betrayal', '''## Before reading
The play includes family abuse and extreme violence. Quarto and Folio versions differ in wording and some scene divisions; use the class edition. Lear’s three daughters are Goneril, Regan and Cordelia. Gloucester’s sons are Edgar and Edmund.

## Act I
Lear decides to divide his kingdom and asks his daughters to express their love. Goneril and Regan give elaborate assurances; Cordelia refuses to add flattery to sincere affection. Lear disinherits her and banishes Kent for speaking in her defence. France accepts Cordelia as a bride without the promised dowry; Burgundy withdraws.

In the parallel plot, Edmund resents his status as Gloucester’s illegitimate son and forges a letter suggesting that Edgar plans to attack their father. Lear stays first with Goneril. She complains about his knights and reduces his authority. Kent, disguised, returns to serve Lear, and the Fool uses jokes and songs to criticise Lear’s mistake. Lear leaves for Regan, believing she will treat him better.

## Act II
Edmund deepens the deception, arranging an encounter that makes Edgar appear dangerous. Edgar escapes and adopts the disguise of “Poor Tom.” Kent is placed in the stocks after conflict with Oswald; Lear sees this as an insult to his authority. Goneril and Regan refuse his demands for a large retinue and compete to reduce the number of knights he may keep. He goes out into the storm rather than accept their terms.

## Analysis
Lear’s ceremonial demand turns love into a public performance; Cordelia’s refusal raises the question of whether saying less can mean feeling more. Edmund’s resentment has a social cause, but does not excuse his manipulation. Compare how both fathers misread their children.

## 50-minute plan
0–10: draw two family trees. 10–20: examine the love test. 20–30: track Edmund’s forged evidence. 30–40: compare Kent and Edgar’s disguises. 40–50: explain why Lear goes into the storm.

## Check
Who forges the letter? Edmund. Who disguises himself as Poor Tom? Edgar. Why does France marry Cordelia? He values her despite the loss of her dowry.''','https://www.folger.edu/explore/shakespeares-works/king-lear/read/')
add('course-1:3','lear-acts-three-five','King Lear · Acts III–V: storm, recognition and tragedy', '''## Act III: storm and cruelty
Lear, the Fool and Kent face the storm; Edgar, disguised as Poor Tom, joins them. Lear begins to think of poor and exposed people whom he had neglected while powerful. Gloucester helps Lear, but Edmund reports his father’s actions to Cornwall. At Gloucester’s home Cornwall and Regan interrogate and blind Gloucester. A servant intervenes and wounds Cornwall, who later dies. Gloucester learns that Edmund betrayed him.

## Act IV: seeing and reunion
The blind Gloucester is led by Edgar, whom he does not recognise. Edgar stages an imagined cliff at Dover to prevent his father’s suicide, then stays with him. The play does not require students to treat deception as a general substitute for mental-health care. Cordelia arrives with French forces and seeks her father; Lear and Cordelia are reunited. Their reconciliation does not reverse all the damage already done. Goneril and Regan both desire Edmund, creating further conflict.

## Act V: battle and deaths
The British forces defeat the French. Edmund orders that Lear and Cordelia, now prisoners, be killed. Edgar challenges and mortally wounds Edmund and reveals his identity. Goneril poisons Regan and then kills herself. Edgar reports that Gloucester died after learning who he was. Edmund attempts to countermand the order, but too late: Cordelia has been hanged. Lear enters carrying her body and dies. The final survivors face the task of responding to the ruined kingdom; the final speaker differs between Quarto and Folio traditions.

## Key themes
Sight and blindness complicate knowledge: physical sight does not ensure moral insight, and disability must not be reduced to a metaphor for ignorance. The storm externalises disorder but also exposes vulnerable bodies. Reconciliation is real without guaranteeing a happy ending.

## 50-minute plan
0–10: recap the two plots. 10–20: compare storm and shelter. 20–30: discuss the blinding without re-enactment. 30–40: reconstruct battle and delayed order. 40–50: debate justice and the unresolved ending.

## Check
Who tries to prevent Gloucester’s suicide? Edgar. Does Edmund’s attempted reversal save Cordelia? No. Why compare editions? The texts and final lines differ.''','https://www.folger.edu/explore/shakespeares-works/king-lear/read/')
add('course-1:4','crusoe-start','Robinson Crusoe · voyages and survival: detailed sequence', '''## Scope and content warning
This guide follows the 1719 novel’s narrative sequence; chapter numbering differs across editions and abridgements. It includes enslavement, colonial violence and language that dehumanises Indigenous people. Do not repeat that language as an objective description.

## 1. Leaving home
Crusoe’s father urges him to accept a secure middle station in life. Crusoe instead goes to sea, experiences storms and danger, and interprets events retrospectively as warnings. His wish for adventure is also a desire for commercial gain.

## 2. Captivity, escape and Brazil
On a later voyage a North African vessel captures him and he is enslaved at Salé. He escapes by boat with the boy Xury. A Portuguese captain rescues them and takes them toward Brazil. Crusoe sells Xury’s service to the captain, who promises eventual freedom on conditions. Crusoe’s own experience of enslavement does not stop him participating in another person’s exploitation.

In Brazil Crusoe becomes a plantation owner. Seeking more labour and profit, he joins a voyage intended to acquire enslaved Africans. A storm and shipwreck leave him stranded on an island near South America. Other crew members are lost.

## 3. Making a life
Crusoe salvages food, tools, weapons and other supplies from the ship. He builds shelter and fortifications, keeps a calendar and journal, and learns to cultivate grain, make pottery and manage goats. He repeatedly adapts after failure: a large canoe, for instance, is too difficult to move to the water. The wreck and later labour are both essential to his survival; he is not self-sufficient from nothing.

## 4. Illness and religion
Ill and frightened, Crusoe reads the Bible and interprets recovery as providential. His spiritual account develops alongside anxiety, fear and hope. Readers can ask whether his religious interpretation changes his view of other people as well as of himself.

## 50-minute plan
0–10: establish voyage and commercial setting. 10–20: trace capture and escape. 20–30: discuss Xury and the slave-trading voyage. 30–40: map practical survival. 40–50: connect illness and religious interpretation.

## Check
Why is the ship sailing when it wrecks? To obtain enslaved labour for Brazilian plantations. What resources aid survival? Materials salvaged from the wreck, his labour and the island’s ecology.''','https://www.gutenberg.org/ebooks/521')
add('course-1:4','crusoe-end','Robinson Crusoe · footprint, Friday and return', '''## 1. The footprint
After years on the island, Crusoe finds a single human footprint. He is terrified and imagines danger. His fear reveals that the island is not isolated from other people simply because he has not seen them. Evidence of visitors and human remains later intensifies his anxiety.

## 2. Friday
Crusoe rescues a captive pursued by others and names him Friday after the day of their meeting. He teaches him English and Christianity and expects him to call him master. Friday brings knowledge, action and relationships of his own; read his speech through Crusoe’s first-person account rather than assuming the narrator gives him equal control over the story. The friendship and the hierarchy coexist.

## 3. Further rescues
Crusoe and Friday help rescue a Spaniard and Friday’s father from another group of visitors. Friday’s joyful recognition of his father interrupts any idea that he lacks family or a history outside Crusoe’s service. Plans to bring other Europeans to the island remain in motion when an English ship appears.

## 4. Mutiny and departure
The ship’s captain has been overpowered by mutineers. Crusoe and Friday help him regain control; some mutineers remain on the island. Crusoe leaves after about 28 years. In Europe he learns that his Brazilian plantation has produced wealth during his absence. The ending brings the narrative back to property and commerce, not merely individual endurance.

## Critical discussion
Crusoe’s inventories, journal and practical detail create an effect of realism. At the same time, his claims to ownership, naming of Friday and links to slavery invite postcolonial and ethical readings. A critical reading need not deny the narrative’s interest in survival or faith.

## 50-minute plan
0–10: reread the footprint episode. 10–20: reconstruct Friday’s rescue. 20–30: analyse names and authority. 30–40: follow the mutiny and return. 40–50: debate survival and colonial possession.

## Check
Who is rescued with the Spaniard? Friday’s father. What allows Crusoe to leave? Helping a captain recover his ship from mutineers.''','https://www.gutenberg.org/ebooks/521')
add('course-1:4','pamela-part1','Pamela · letters, confinement and resistance', '''## Content warning and scope
The novel depicts harassment, attempted sexual assault and coercive control. This follows Pamela; or, Virtue Rewarded (1740), rather than assuming details of every later sequel or adaptation. Letter divisions and page numbers vary by edition.

## 1. A servant writes home
Pamela Andrews, a young servant, writes to her parents after the death of her employer. Her employer’s son, Mr B, initially gives her gifts and then makes unwanted sexual advances. Her parents urge her to protect herself and come home. The letters combine affection, fear and the practical problem of employment and money.

## 2. Surveillance and removal
Pamela tries to leave. Mr B controls transport and correspondence; she is taken to his Lincolnshire estate rather than safely home. Mrs Jewkes supervises her closely. Because her letters may be intercepted, Pamela records events in a journal intended for her parents. The form lets readers observe her uncertainty while also showing how the powerful may read her private words.

## 3. Attempts to escape
The clergyman Mr Williams tries to help by exchanging messages and seeking assistance. Local people hesitate to challenge Mr B’s social power. Pamela’s attempt to escape fails, and Williams is punished through legal action. Mr B and Mrs Jewkes use disguise and access to Pamela’s room in an attempted assault. Pamela’s resistance must not be treated as the cause of that violence.

## 4. A changed proposal
Mr B reads Pamela’s account and later offers marriage. Pamela is suspicious of deception and wants freedom to return to her parents. On her journey she receives further messages and returns, believing his proposal and professed reform. The novel stages her choice within a profoundly unequal situation; readers can debate its moral framing without assuming that marriage erases coercion.

## 50-minute plan
0–10: discuss letters and content warning. 10–20: trace Pamela’s attempts to leave. 20–30: map who controls transport and correspondence. 30–40: discuss Mr Williams and local authority. 40–50: evaluate the marriage proposal through textual evidence.

## Check
Why does Pamela keep a journal? Her letters and movement are controlled. Who oversees her confinement? Mrs Jewkes on Mr B’s behalf.''','https://www.ebsco.com/research-starters/literature-and-writing/pamela-samuel-richardson/')
add('course-1:4','pamela-part2','Pamela · marriage, class and interpretation', '''## Marriage and household
Pamela and Mr B marry after his proposal. Her father learns that the marriage is intended to be genuine. The narrative then turns to Pamela’s new position as the wife of a wealthy man and to the reactions of people who think her birth and former employment make the marriage improper.

## Lady Davers
Mr B’s sister Lady Davers challenges and insults Pamela, doubting that the marriage is respectable or valid. Pamela experiences further restriction and intimidation. Eventually the family moves toward reconciliation, though a discussion of class conflict should not imply that social inequality disappears.

## Mr B’s past and Pamela’s authority
Pamela learns about a child from Mr B’s earlier relationship and takes an interest in the child’s care. She also negotiates relationships with servants, family and neighbours from her altered social position. The story asks what power she gains and what constraints remain in marriage.

## Reading the title critically
“Virtue rewarded” is the novel’s own framing, not an instruction to present a marriage with a former abuser as a reward in real life. Compare Pamela’s expressed feelings with her limited options, the unequal wealth of the characters and the social authority of marriage. Students may differ on whether they find Mr B’s reform convincing.

## Epistolary method
Letters and journal entries create immediacy and access to Pamela’s reasoning, but a letter is also addressed to particular readers and can be intercepted. Ask how the intended audience shapes what is written. The printed novel itself is a crafted work, not a discovered set of historical documents.

## 50-minute plan
0–10: recap events before marriage. 10–20: analyse Lady Davers and rank. 20–30: identify changes in Pamela’s position. 30–40: debate reform and coercion with care. 40–50: write about the title and epistolary form.

## Check
Who challenges the marriage on grounds of class? Lady Davers. Does marriage retroactively make Mr B’s earlier conduct consensual? No.''','https://www.ebsco.com/research-starters/literature-and-writing/pamela-samuel-richardson/')
add('course-1:4','tom-jones-beginning','Tom Jones · books 1–6: the foundling and the family', '''## Structure
Fielding’s novel has 18 books, each containing chapters; this is a guide to groups of books, not a claim that every episode occurs in the same chapter across editions. Introductory chapters feature a narrator who discusses storytelling and invites readers to judge.

## Foundling and household
Squire Allworthy returns to find a baby in his bed and adopts him as Tom Jones. Suspicion falls on Jenny Jones and the schoolmaster Partridge, but the real parentage remains unresolved until late in the novel. Allworthy’s sister Bridget marries Captain Blifil; their son, Master Blifil, grows up with Tom. Their tutors, Thwackum and Square, represent competing forms of moral authority, each open to satire.

## Tom and Sophia
Tom is generous but impulsive and sexually reckless. He becomes attached to Sophia Western, the neighbouring squire’s daughter. Sophia’s father values hunting and property; her aunt Mrs Western imagines a socially advantageous match. Tom’s encounter with Molly Seagrim and gossip about him complicate his relationship with Sophia. Neither Tom nor Blifil should be judged only by outward reputation.

## Illness and expulsion
When Allworthy becomes ill and later recovers, Tom’s actions are reported and interpreted against him. Bridget dies, and Blifil uses others’ mistakes and selective information to turn Allworthy against Tom. Allworthy sends Tom away. Sophia is pressured to marry Blifil and decides to flee rather than submit.

## Reading focus
The narrator distinguishes hypocrisy from imperfect conduct but also exposes Tom’s errors. Ask how class, inheritance and incomplete information shape the difference between moral judgment and social reputation.

## 50-minute plan
0–10: draw the household. 10–20: track the foundling mystery. 20–30: compare Tom and Blifil with evidence. 30–40: discuss Sophia’s choices. 40–50: explain the expulsion.

## Check
Who finds Tom? Allworthy. What remains uncertain in the opening books? Tom’s parentage.''','https://www.coursehero.com/lit/Tom-Jones/plot-summary/')
add('course-1:4','tom-jones-road','Tom Jones · books 7–12: road, encounters and pursuit', '''## Departure and pursuit
Tom travels away from Allworthy’s estate. Sophia also leaves home to escape a forced marriage to Blifil. Their journeys proceed along different routes and repeatedly intersect without a simple reunion. Partridge joins Tom; his talk and mistaken assumptions create comic misunderstandings.

## Inns and encounters
Tom meets soldiers, travellers and a variety of hosts. He helps a woman known as Mrs Waters, and they become sexually involved. Sophia arrives at the inn, learns of their encounter and leaves her muff on Tom’s bed as a sign for him; she departs hurt and angry. The incident matters because Tom’s declared love and his behaviour are in tension, and because objects carry information across separate plots.

## Sophia’s journey
Sophia travels with her maid Honour and confronts the vulnerability of a woman moving without her father’s protection. She meets relatives and seeks a safe place in London. Her refusal to marry Blifil is an exercise of agency within constraints, not proof that travel is equally safe for men and women.

## Narrator and structure
The narrator offers comic introductions and commentary while controlling what readers know about mistaken identities and timings. When teaching an assigned chapter, check the local sequence in the edition: these paragraphs compress several encounters rather than replacing the book.

## 50-minute plan
0–10: put the two journeys on a map. 10–20: discuss Partridge’s role. 20–30: track the inn and muff. 30–40: compare risks facing Tom and Sophia. 40–50: analyse narrative suspense.

## Check
Why does Sophia leave home? To resist an unwanted marriage. What does the muff help reveal? Tom’s involvement with Mrs Waters at the inn.''','https://www.coursehero.com/lit/Tom-Jones/plot-summary/')
add('course-1:4','tom-jones-end','Tom Jones · books 13–18: London and recognition', '''## London complications
Tom lodges with Mrs Miller and meets Nightingale. Lady Bellaston becomes involved with Tom, while Sophia comes under pressure from relatives. Lord Fellamar attempts to force himself on Sophia; her lack of consent is central, regardless of the social plans made around her. Sophia learns of Tom’s proposal to Lady Bellaston and is distressed. Tom and Sophia’s relationship is repeatedly affected by incomplete or misleading information.

## Violence and imprisonment
A confrontation with Mr Fitzpatrick leads to Fitzpatrick being wounded and Tom being imprisoned. The danger of a criminal charge brings the narrative’s misunderstandings to a crisis. Reports about Mrs Waters create a further fear that Tom has unknowingly been intimate with his own mother.

## The parentage mystery
Mrs Waters is connected to Jenny Jones but reveals that Tom’s mother is Bridget, Allworthy’s sister. Blifil had withheld a letter explaining Tom’s birth; other information exposes his manipulation. Allworthy recognises Tom as his nephew and reconciles with him. The revelation resolves the feared maternal relationship with Mrs Waters, while also showing how status and inheritance affect people’s judgments.

## Ending
Sophia hears accounts that put some of Tom’s actions in a different light but retains reason to question his faithfulness. With consent and family reconciliation, Tom and Sophia marry. Tom and Sophia show generosity toward Blifil despite his conduct. Western’s swift approval after learning of Tom’s inheritance invites a critical reading of a supposedly happy settlement.

## 50-minute plan
0–10: map the London characters. 10–20: trace Sophia’s vulnerability. 20–30: order the prison and parentage revelations. 30–40: evaluate Allworthy’s change of view. 40–50: debate the marriage and status.

## Check
Who is Tom’s mother? Bridget Allworthy. Who concealed the letter? Blifil. Why does Western change his attitude? Tom’s newly established status and inheritance make the match attractive to him.''','https://www.gradesaver.com/the-history-of-tom-jones-a-foundling/study-guide/summary-book-18')
add('course-2:0','comm-practice-1','Communication basics · activities with answers', '''## Goals and teaching
Students identify purpose, sender, receiver, message, channel, feedback and noise; they practise adjusting a message for an audience. Noise can be physical, semantic, emotional or technological. Feedback can be delayed or absent, so communication is not always a neat two-way loop.

## Model
A teacher emails students that a room has changed. Sender: teacher; message: new room and time; channel: email; receivers: students; feedback: replies or confirmation. If the time is unclear, that is a message-design barrier. If a student has no internet, access is a channel barrier. A quiet student is not automatically inattentive.

## Practice
1. A speaker gives directions while traffic makes the words hard to hear. Identify one barrier and one response. 2. Rewrite “Meet me there later” for a class group without inventing a venue: provide placeholders for place and time. 3. Give one example of non-verbal communication and two possible meanings. 4. What could confirm that the receiver understood?

## Suggested answers
1. Physical noise; move somewhere quieter or write the directions. 2. “Please meet at [place] at [time].” 3. Folded arms might indicate discomfort, cold or habit; context is needed. 4. Ask the person to summarise the instruction in their own words; do not assume a nod proves comprehension.

## 50-minute lesson
0–10: discuss a misunderstood message. 10–20: map the email example. 20–30: rewrite vague instructions. 30–42: pairs practise accessible channels and feedback. 42–50: exit ticket names one barrier and a remedy.''','https://open.lib.umn.edu/communication/chapter/1-2-the-communication-process/')
add('course-2:1','comm-practice-2','Listening and speaking · practice and answer guide', '''## Key distinction
Hearing is perceiving sound; active listening includes attention, checking meaning and responding. Listening purposes include understanding instructions, appreciating a performance and evaluating a claim. Do not equate a single posture or eye-contact pattern with good listening: disability and culture affect communication.

## Listening task
Read aloud: “The reading club meets on Thursday at 4 p.m. in Room 12. Bring a notebook. If Room 12 is unavailable, meet outside the library.” Ask: day? time? room? contingency? Replay once and invite students to ask for clarification.

## Answers
Thursday; 4 p.m.; Room 12; outside the library if that room is unavailable. The passage does not say a fee or name a book; avoid guessing.

## Speaking tasks
Pairs: greet each other, ask for a repeat and summarise a message. Group discussion: “Should a college library stay open later?” Assign facilitator, timekeeper and note-taker; support claims with reasons rather than invented statistics. Extempore: allow one minute to plan and one minute to speak on “A useful learning habit,” with an opening, one example and closing.

## Feedback rubric
Give one point each for relevant content, understandable organisation, respectful turn-taking, a clarification strategy and a response to the listener. Accent is not a measure of intelligence. Allow alternatives to oral performance when needed.

## 50-minute lesson
0–8: discuss listening. 8–18: read and check the task. 18–28: pair conversation. 28–40: group discussion. 40–50: short extempore and supportive feedback.''','https://open.lib.umn.edu/communication/chapter/5-1-understanding-how-and-why-we-listen/')
add('course-2:2','comm-practice-3','Reading, vocabulary and comprehension · worked exercises', '''## Mini-passage
“The college garden collects rainwater in a small tank. Volunteers water the young plants in the morning. The club hopes to add more shade next year, but it has not yet chosen a design.”

## Questions
1. What does the tank collect? 2. When do volunteers water plants? 3. Has a shade design been selected? 4. Skim: state the passage’s topic in one sentence. 5. Scan: locate the time word. 6. Can we conclude every college student volunteers? 7. In “a clear explanation,” suggest a context-appropriate synonym for clear; give an antonym for “early” in a time context.

## Answers
1. Rainwater. 2. In the morning. 3. No. 4. A college garden’s present work and plans. 5. “Morning.” 6. No: the passage says only “volunteers.” 7. “Understandable”; “late.” Other appropriate answers are possible.

## Skills
Skimming establishes overall meaning; scanning searches for a specific detail. Intensive reading studies wording and reasoning closely; extensive reading builds experience through larger quantities of reading. A technical text may require attention to definitions, diagrams, units and claims. An idiom’s meaning is conventional and may not be literal; always consider context.

## 50-minute lesson
0–10: distinguish skim and scan. 10–20: read the mini-passage. 20–30: answer and justify. 30–40: infer cautiously and compare synonyms. 40–50: write one factual and one inferential question.''','https://learnenglish.britishcouncil.org/skills/reading')
add('course-2:3','comm-practice-4','Writing skills · models and editing practice', '''## Formal email model
Subject: Request to use the library room
Dear Librarian,
I am writing on behalf of the reading club to ask whether a room is available on [date] from [time] to [time]. Please let us know the booking procedure and any conditions.
Thank you for your help.
[Name]

The placeholders prevent invention of facts. Add an attachment only if it actually exists.

## Notice and minutes
Notice: “Reading Club Meeting | [Date and time] | [Room] | Members are invited to discuss the next reading selection. Contact: [name].” Minutes record what happened: “Members agreed to request a room. Action: the secretary will email the librarian by [date].” An agenda is a plan before a meeting; minutes are a record after it.

## Edit these
1. “The students is preparing a report.” 2. “Me and my friend has sent the email.” 3. “The meeting was held, we discussed books.”

## Suggested answers
1. “The students are preparing a report.” 2. “My friend and I have sent the email.” 3. “The meeting was held, and we discussed books,” or use two sentences. Follow institutional style and do not mark valid language varieties as inherently wrong.

## 50-minute lesson
0–10: identify email purpose and audience. 10–20: write a subject and request. 20–30: compare agenda and minutes. 30–40: edit the sentences with reasons. 40–50: peer-check completeness and tone.''','https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/email_etiquette.html')
add('course-2:4','comm-practice-5','Personality development · reflection and ethical practice', '''## Learning aims
Practise self-assessment, constructive feedback, emotional awareness, teamwork, time planning and professional ethics. Personality is not a fixed checklist of ideal behaviour. A student should not be graded on disclosing personal feelings or conforming to one culturally preferred style.

## Scenarios
1. A group member misses a deadline. Draft a respectful check-in and a plan. 2. You notice a classmate interrupted repeatedly. What can a facilitator do? 3. You are offered an impressive statistic but cannot verify it before a presentation. What do you do? 4. List an urgent task, an important non-urgent task and a realistic rest break.

## Possible responses
1. Ask privately whether support or a revised timeline is needed, then agree on responsibilities. 2. Invite the interrupted person to continue without forcing them to speak. 3. Omit the claim or label it unverified and seek a source. 4. Answers vary; allocate specific time rather than treating busyness as success.

## Emotional awareness
Name a feeling privately if useful, pause and choose an appropriate response. Emotional intelligence is not a diagnosis or a promise of success; avoid inferring emotion from a single gesture. Leadership includes listening, shared responsibility and ethical decisions, not just speaking loudly.

## 50-minute lesson
0–10: private self-reflection. 10–20: discuss a neutral teamwork scenario. 20–30: practise a check-in. 30–40: prioritise tasks. 40–50: write a realistic improvement goal.''','https://open.lib.umn.edu/communication/chapter/9-3-communication-in-groups/')
add('course-19:0','grammar-64–74','Grammar 64–74 · articles and nouns (edition check needed)', '''## Edition warning
The syllabus gives “Essential English Grammar” (Murphy, 2012) and units 64–74, but the assigned book’s contents page has not been checked. The sequence below follows the publicly available second edition of Essential Grammar in Use, a possible but not confirmed match. Use the headings in Ammu’s book as the authority; different editions have different numbering.

## Possession: useful review
Use apostrophe + s for one owner: “Rina’s book.” With a regular plural ending in s, use an apostrophe after s: “the students’ room.” “Its” shows possession; “it’s” means “it is” or “it has.”

## A/an and plural nouns
Use a before a consonant sound and an before a vowel sound: “a university” begins with a /y/ sound; “an hour” begins with a vowel sound. Many plurals add -s or -es; irregular forms include child/children and person/people.

## Countable and uncountable
Countable nouns can have a number: one idea, two ideas. Uncountable uses generally do not take a/an or ordinary plural -s: “some information,” “much advice.” Meaning can change: “a coffee” can mean a cup of coffee.

## A/an and the
Use a/an for a non-specific singular countable item and the when the intended referent is identifiable: “I saw a dog. The dog was sleeping.” Shared context, unique reference and conventional usage affect the choice.

## Institutional expressions, general meanings and names
Compare “go to work,” “go home” and “go to the cinema.” General plurals or mass nouns often omit the: “Books are useful”; “Water is essential.” Geographical names vary: India and Lake Victoria ordinarily have no article; the Indian Ocean and the Himalayas take the. Check examples rather than memorising an absolute rule.

## This, that, these, those and one/ones
This/that are singular; these/those plural. “This chair is near me; those chairs are across the room.” They can also stand without a following noun: “This is mine.” “One” and “ones” can replace a repeated noun: “the blue one”; “the red ones.”

## Practice
1. Correct: “The students book is new” when one student owns it. 2. Choose a/an: ___ hour, ___ uniform. 3. Correct: “She gave me an advice.” 4. Complete: “I saw a film. ___ film was funny.” 5. Choose: “___ books here are mine” (plural, near).

## Answers
1. “The student’s book is new.” 2. an hour; a uniform. 3. “She gave me some advice” or “a piece of advice.” 4. The. 5. These.

## 50-minute plan
0–10: check the actual contents page. 10–20: model articles and ownership. 20–30: sort countable and uncountable uses. 30–40: pair practice. 40–50: review answers and a self-written example.''','https://www.hasanboy.uz/wp-content/uploads/2017/11/Essential-Grammar-in-Use.pdf',True)
add('course-19:1','grammar-75–83','Grammar 75–83 · pronouns and quantity (edition check needed)', '''## Edition warning
These topic-to-unit numbers follow a possible second-edition comparison, not a verified contents page for the prescribed 2012 book. Confirm each unit heading before teaching.

## One and ones: useful review
“One” avoids repeating a singular countable noun; “ones” replaces a plural: “I like the blue pen. Which one?” / “The blue ones.”

## Some, any and negative forms
Some commonly appears in affirmative statements and offers: “some tea,” “Would you like some tea?” Any commonly appears in negatives and questions: “I don’t have any”; “Do you have any?” “No” precedes a noun: “no money.” “None” can replace a noun: “How many? None.” Nobody/anybody and nothing/anything express people and things; use one grammatical negative in standard formal examples: “I don’t know anybody” or “I know nobody.”

## Every, all, most, both, either and neither
“Every student has a card” uses a singular verb; “all students have cards” uses plural agreement. “Most students” is general; “most of the students in this class” identifies a group. Both means the two together; either can mean one or the other; neither means not one and not the other. Agreement with neither can vary by construction and register.

## Quantity
Use “many books” with countable plurals and “much time” with uncountable nouns; “a lot of” works with either. In ordinary affirmative speech, “a lot of” is often more natural than “much.” Compare “a few books” (some) with “few books” (not many), and “a little time” (some) with “little time” (not much).

## Practice
1. I have two pens. The blue ___ is mine. 2. Do you have ___ questions? 3. Rewrite “I don’t have any money” using no. 4. Every student ___ (has/have) a card. 5. ___ books / ___ time (many or much).

## Answers
1. one. 2. any. 3. I have no money. 4. has. 5. many books; much time. Context may permit alternatives in other constructions.

## 50-minute plan
0–10: verify assigned headings. 10–20: model substitution and negatives. 20–30: practise quantities. 30–40: pairs explain agreement. 40–50: answer review.''','https://www.hasanboy.uz/wp-content/uploads/2017/11/Essential-Grammar-in-Use.pdf',True)
add('course-19:2','grammar-84–95','Grammar 84–95 · description and word order (edition check needed)', '''## Edition warning
The following is based on a possible second edition, not the confirmed 2012 prescribed copy. Match headings with the book before teaching.

## 84–85: adjectives and adverbs
Adjectives describe nouns or follow linking verbs: “a careful student”; “The student is careful.” Adverbs often describe actions: “She reads carefully.” Not all adverbs end in -ly; “fast” can be an adjective or adverb.

## 86–89: comparisons and superlatives
Short adjectives often add -er/-est: small, smaller, smallest. Longer ones commonly use more/most: more interesting, most interesting. Compare two things with than: “This path is shorter than that one.” “Not as long as” expresses an unequal comparison. Irregular forms include good, better, best.

## 90–91: enough and too
“Enough” follows an adjective (“warm enough”) but normally precedes a noun (“enough time”). “Too” often means more than desirable: “too hot to touch,” not simply “very hot.”

## 92–95: position and objects
A common pattern is subject + verb + object + place/time: “She reads a book at home every evening.” Frequency adverbs normally precede ordinary verbs but follow be: “He usually walks”; “He is usually early.” “Already,” “yet” and “still” signal timing in context. Give can take two objects (“Give me the book”) or a prepositional phrase (“Give the book to me”); pronouns favour “Give it to me.”

## Practice
1. The child spoke ___ (quiet/quietly). 2. A bus is ___ (large) than a car. 3. There is not ___ time (enough/too). 4. Place usually: “She is early.” 5. Rewrite “Give me it” in a common formal pattern.

## Answers
1. quietly. 2. larger. 3. enough. 4. She is usually early. 5. Give it to me.

## 50-minute plan
0–10: check headings. 10–20: adjectives and adverbs. 20–30: comparisons. 30–40: word-order cards. 40–50: practise and correct.''','https://www.hasanboy.uz/wp-content/uploads/2017/11/Essential-Grammar-in-Use.pdf',True)
add('course-19:3','grammar-96–106','Grammar 96–106 · time, place and prepositions (edition check needed)', '''## Edition warning
Topic numbers below come from a possible second-edition comparison; confirm the assigned book before claiming an exact unit mapping.

## 96–98: time expressions
“At” commonly marks clock times (“at 5”), “on” days and dates (“on Monday”), and “in” months, years and longer periods (“in June”). “From … to” specifies a range; “until” an endpoint. “Since” marks a starting point and “for” a duration: “since 2020,” “for three years.” “During” precedes a noun phrase (“during the film”); “while” commonly introduces a clause (“while we watched”).

## 99–104: place and movement
In often places something within an area, at identifies a point or venue, and on indicates a surface, route or conventional usage: “in the room,” “at the station,” “on the table.” Context changes the best choice: “at the school” and “in the school” can focus on different things. Under, behind, opposite, over and through express spatial relations. “Go to college” but “go home.” “By bus,” “with a pen” and “about a book” are conventional combinations.

## 105–106: combinations
Many adjectives select a preposition: “good at,” “interested in,” “afraid of.” After a preposition, an -ing form can follow: “good at drawing.” Verbs also combine conventionally: “listen to music,” “look at a picture,” “wait for a friend.” Learn combinations with a meaningful sentence, not by translating one word at a time.

## Practice
1. Meet ___ Monday ___ 3 p.m. 2. She has lived here ___ 2020. 3. He is good ___ drawing. 4. We walked ___ the tunnel. 5. Listen ___ the instructions.

## Answers
1. on; at. 2. since. 3. at. 4. through. 5. to. Other prepositions can work in different contexts.

## 50-minute plan
0–10: check actual headings. 10–20: create a time line. 20–30: describe a room and movement. 30–40: practise adjective/verb combinations. 40–50: corrections and exit ticket.''','https://www.hasanboy.uz/wp-content/uploads/2017/11/Essential-Grammar-in-Use.pdf',True)
add('course-19:4','grammar-107–114','Grammar 107–114 · phrasal verbs and clauses (edition check needed)', '''## Edition warning
The syllabus assigns these numbers but does not reproduce their topics. This sequence follows a possible second edition only; confirm the contents of the prescribed 2012 copy before treating the mapping as certain.

## 107–108: phrasal verbs
A phrasal verb combines a verb and particle: “go out,” “take off,” “turn on.” Meanings can be literal or idiomatic. Some object-taking combinations allow a noun on either side of the particle: “turn on the light” / “turn the light on.” With a pronoun, say “turn it on,” not “turn on it.” Not all verb–particle combinations are separable; learn each in context.

## 109–110: connectors and when
“And” adds; “but” contrasts; “or” offers alternatives; “so” expresses a result; “because” introduces a reason. In a future time clause, use present form with future meaning: “When she arrives, we will begin,” rather than normally “when she will arrive.”

## 111–112: if clauses
A real future possibility can use “If it rains, we will stay inside.” A hypothetical present or future can use “If I had more time, I would read more.” These patterns express different meanings, not different degrees of intelligence; “were” is often preferred in formal hypothetical “if I were.”

## 113–114: relative clauses
“Who” commonly refers to people; “which” to things; “that” may refer to either in many defining clauses. “The teacher who helped us is here.” When the relative word is the object, it can often be omitted: “The book (that) I borrowed is here.” Compare the subject: “The book that fell” cannot normally omit that.

## Practice
1. Turn ___ the light; turn it ___. 2. Complete: “When she ___ (arrive), we will begin.” 3. “If I had a bicycle, I ___ (ride) to college.” 4. Combine: “The student is here. She helped me.” 5. Can the word that be omitted in “the book that I read”?

## Answers
1. on; on. 2. arrives. 3. would ride. 4. “The student who helped me is here.” 5. Yes: “the book I read.”

## 50-minute plan
0–10: verify headings. 10–20: act out phrasal verbs. 20–30: compare real and hypothetical conditions. 30–40: combine relative clauses. 40–50: review and exit ticket.''','https://www.hasanboy.uz/wp-content/uploads/2017/11/Essential-Grammar-in-Use.pdf',True)
add('course-20:0','writing-workshop-types','Types of writing · models and classroom exercises', '''## Four purposes
Descriptive writing creates a sensory impression; narrative writing relates events; expository writing explains; persuasive writing offers a position and reasons. A text can combine purposes.

## Four original models
Description: “The blue reading room held three long tables. Afternoon light fell across the books.”
Narrative: “When the rain began, Meena carried the books inside. She returned to find the courtyard empty.”
Exposition: “A library catalogue helps readers find a book by title, author or subject.”
Persuasion: “The college should provide quiet study hours because students need a predictable place to concentrate.” A real proposal should also consider evidence, costs and other users’ needs.

## Message model
“Hi Arun, the reading group is meeting at [place] on [date] at [time]. Please let me know if you can attend. —Meena.” Do not invent logistics when writing for an actual event.

## Practice and feedback
1. Identify each model’s main purpose. 2. Add one observation to the description without claiming a person’s feelings as visible fact. 3. Add an event and consequence to the narrative. 4. Give a reason and a possible objection to the proposal.

Answers: description, narrative, exposition, persuasion. For 2–4, multiple answers are possible; check relevance, clarity and whether invented details suit the task.

## 50-minute lesson
0–10: compare purposes. 10–20: analyse four models. 20–30: write a description. 30–40: revise it into a narrative or explanation. 40–50: peer feedback.''','https://owl.purdue.edu/owl/general_writing/academic_writing/essay_writing/index.html')
add('course-20:1','writing-workshop-precis','Paragraphs and précis · worked model and practice', '''## Original source passage
“The college planted a small garden beside the library. Volunteers water it every morning using collected rainwater. The garden gives students a quiet place to sit, though the group still needs a plan for maintaining it during holidays.”

## Paragraph structure
A topic sentence states a focus; supporting sentences develop it with reasons or examples; a concluding sentence can relate back to the main point. Paragraphs need unity and coherence, not a fixed number of sentences.

## Model précis
“Library volunteers maintain a rainwater-fed garden that offers quiet space, but holiday care remains unresolved.” It retains the main situation and qualification without adding a personal opinion. Actual précis length and attribution should follow the teacher’s instructions.

## Blog and picture task
Turn the topic into a blog plan: title, reader, opening, two headings, verified evidence and a closing invitation. For a picture, divide a page into “visible” and “possible inference”; a person holding an umbrella does not by itself prove it is raining. Creative tasks may invent details if presented as fiction.

## Practice
1. Identify the unresolved problem. 2. Write a shorter précis without claiming that all students use the garden. 3. Draft a topic sentence about a useful campus facility. 4. List one observable detail and one possible inference from an assigned picture.

## Answers and rubric
1. Holiday maintenance. 2–4: responses vary; check accuracy, concision, logical order and source fidelity. Avoid copying long phrases without attribution.

## 50-minute lesson
0–10: read and annotate. 10–20: identify central and supporting ideas. 20–30: draft précis. 30–40: plan a blog. 40–50: compare observation and inference.''','https://owl.purdue.edu/owl/general_writing/the_writing_process/paragraphs_and_paragraphing/index.html')
add('course-20:2','writing-workshop-applications','Applications and résumé · guided models', '''## Email application
Subject: Application for [role]
Dear [name or selection committee],
I am writing to apply for [role], advertised on [source/date]. My experience in [real task] helped me develop [relevant skill]. I have attached my résumé as requested and would welcome an opportunity to discuss my application.
Thank you for your consideration.
[Name] | [contact]

Only include a source, attachment or experience if it is real. Adjust salutation and format to the instructions.

## Résumé structure
Name and professional contact; education; relevant skills; genuine projects, activities or experience; optional additional sections if useful. Use accurate dates and descriptions. Example, if true: “Organised weekly reading sessions for a student group and maintained attendance records.” Do not invent grades, employers, results or references.

## Covering letter
Connect one or two requirements to concrete evidence. Avoid merely repeating the résumé. Close with thanks and a suitable next step. An application form may require different fields; follow it rather than forcing a letter format.

## Practice
1. Write a subject line for a volunteer application. 2. Replace “I am perfect at everything” with one factual skill and supporting task. 3. Find two things to check before sending. 4. Explain how a cover letter differs from a résumé.

## Possible answers
1. “Application for Library Volunteer Role.” 2. Answers vary and must be truthful. 3. Recipient address, correct role, spelling, requested attachment and deadline. 4. The résumé summarises qualifications; the letter relates selected evidence to the role.

## 50-minute lesson
0–10: identify audience. 10–20: write a subject and opening. 20–30: draft one truthful résumé entry. 30–40: write a supporting paragraph. 40–50: use an application checklist.''','https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/job_search_writing/index.html')
add('course-20:3','writing-workshop-news','News and reports · attribution and worked practice', '''## Fictional classroom facts
A college reading club met on 12 July in Room 4. Twelve members attended, according to the club secretary. They agreed to collect suggestions for the next book. These facts are invented only for this exercise; never present them as a real event.

## Sample news lead
“Twelve members attended the college reading club’s meeting in Room 4 on 12 July, according to the club secretary.” A report could then explain the decision and attribute further information. Do not add a quotation, impact or statistic that has not been supplied.

## Letter to the editor
“Sir/Madam, The question of access to quiet study spaces deserves attention. A consultation with students and staff could identify when space is most needed. Yours faithfully, [name].” A genuine letter should identify any article it refers to and provide evidence for factual claims.

## Report structure
Title; purpose; method or source; findings; recommendations where requested. “Twelve attended” is a reported finding if reliably recorded. “Consider asking members for suggestions” is a recommendation. A small attendance count does not prove what the whole college believes.

## Practice
1. Name the source for the attendance figure. 2. Write a headline without exaggeration. 3. Separate the finding and recommendation above. 4. Is “All students want the club” supported?

## Suggested answers
1. The club secretary. 2. “Reading club meets to discuss its next book.” 3. Attendance is a finding; a suggestion-gathering step is a recommendation. 4. No.

## 50-minute lesson
0–10: discuss verification. 10–20: write a lead from the facts. 20–30: draft a letter. 30–40: organise a report. 40–50: identify unsupported claims.''','https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/index.html')
add('course-20:4','writing-workshop-grammar','Grammar and vocabulary · exercises with answers', '''## Punctuation practice
1. Correct the comma splice: “The lecture ended, the students left.” 2. Add punctuation to a direct question: “Where is the library” 3. Show the book belongs to one student: “the students book.”

Suggested answers: “The lecture ended, and the students left” or two sentences; “Where is the library?”; “the student’s book.” If several students own it: “the students’ book.”

## Vocabulary in context
4. Give a synonym for “bright” in “bright sunlight” and one in “a bright student.” 5. Give an antonym for “early” in “an early train.”

Possible answers: strong or vivid sunlight; intelligent or quick student; late. Synonyms are not automatically interchangeable in every sentence.

## Reported speech
6. On Monday, Priya says, “I will call tomorrow.” Report it on Tuesday. 7. The teacher said, “Please close the door.” Report the request. 8. Arun said, “Water boils at 100°C at standard atmospheric pressure.” Can the present tense remain?

Suggested answers: “On Monday, Priya said that she would call on Tuesday.” “The teacher asked us to close the door.” Yes; present tense can remain when reporting a continuing general truth. Backshift depends on context rather than one mechanical rule.

## Common errors
9. Correct “Each student have a card.” 10. Correct “She gave me an information.” Answers: “Each student has a card”; “She gave me some information” or “a piece of information.” Respect legitimate varieties of English and explain a chosen formal convention.

## 50-minute lesson
0–10: punctuation. 10–20: context-sensitive vocabulary. 20–30: reported speech. 30–40: agreement and nouns. 40–50: peer explanations and exit ticket.''','https://owl.purdue.edu/owl/general_writing/punctuation/index.html')
with open(P,'w',encoding='utf8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Four-subject additions completed; original notes retained except for five expanded grammar entries with the same stable IDs.')
