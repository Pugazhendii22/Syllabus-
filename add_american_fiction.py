import json
p='prepared-notes.json';d=json.load(open(p))
def n(id,title,body,source):
 return {'id':id,'title':title,'source':source,'text':'# '+title+'\nAmerican Literature I · Semester 4\n\n'+body+'\n\nUse the assigned text and edition alongside these teaching notes; check details and interpretations before teaching.'}
d['course-22:3']=[
n('scarlet-letter','Nathaniel Hawthorne · The Scarlet Letter — chapter guide','''## Before reading
Published in 1850 and set mainly in seventeenth-century Puritan Boston, the novel examines public shame, secrecy, revenge and moral judgment. Its narrator filters the story through a nineteenth-century imaginative reconstruction. The guide below follows the customary 24-chapter division; it is a concise chapter guide, not a substitute for the full novel.

## Introductory frame: The Custom-House
A narrator describes his work at the Salem Custom-House, his ancestors and colleagues, and the discovery of an embroidered scarlet letter with papers attributed to an earlier surveyor. The frame presents Hester’s story as a recovered account while inviting readers to consider how narrators shape history.

## Chapters 1–6: Punishment and a new life
1. **The Prison-Door.** A stern prison and an adjoining rosebush establish a contrast between institutional severity and the possibility of sympathy or beauty. The narrator offers the rose as an interpretive gesture.
2. **The Market-Place.** Hester Prynne comes from prison holding her infant and wearing a richly embroidered scarlet A, the mark of adultery. She stands on the scaffold as the crowd judges her. She remembers her earlier life but cannot escape the present humiliation.
3. **The Recognition.** Hester recognises her long-absent husband among the spectators; he signals her not to reveal him. The ministers press her to name her child’s father, but she refuses. The community sees her punishment while one participant in the affair remains unnamed.
4. **The Interview.** The man visits Hester in prison as a physician, takes the name Roger Chillingworth and asks who her lover is. She will not tell him. He asks her to conceal his identity and vows to discover the man himself; his treatment of mother and child accompanies a threat of revenge.
5. **Hester at Her Needle.** After release, Hester settles in a cottage outside town and earns a living through needlework. People use her skill yet often treat her with contempt. She also helps the poor, while the letter makes her painfully visible.
6. **Pearl.** Hester names her daughter Pearl, suggesting something precious obtained at great cost. The lively child resists easy classification; townspeople call her strange, while Hester worries about both her nature and her own capacity to guide her.

## Chapters 7–12: The minister and the physician
7. **The Governor’s Hall.** Hester takes gloves to Governor Bellingham and seeks to defend her right to keep Pearl. The richly furnished hall and a distorted reflection in armour draw attention to authority and the letter’s intrusive visibility.
8. **The Elf-Child and the Minister.** Officials question whether Pearl should remain with Hester. Pearl gives an unsettling answer to a religious question. Hester appeals to Dimmesdale, who argues that the child should stay with her mother. Pearl responds warmly to him.
9. **The Leech.** Chillingworth becomes physician to the ailing minister Dimmesdale and comes to live with him. Some see providence in this arrangement; the narrator increasingly suggests that the physician’s apparent care conceals scrutiny.
10. **The Leech and His Patient.** Chillingworth probes the relation between bodily illness and hidden guilt. Dimmesdale resists his inquiries. While the minister sleeps, Chillingworth examines his chest and reacts with intense, secret triumph; the text does not immediately provide a simple account of what he saw.
11. **The Interior of a Heart.** Chillingworth’s pursuit grows more invasive. Dimmesdale is admired by the public but tormented by private guilt; his attempts to hint at his sin only increase his congregation’s admiration. He subjects himself to severe self-punishment.
12. **The Minister’s Vigil.** At night Dimmesdale stands on the scaffold. Hester and Pearl pass after attending a deathbed and join him. Pearl asks if he will stand with them in daylight; he refuses. A meteor, open to different interpretations, illuminates the sky, and Chillingworth appears.

## Chapters 13–19: Changing meanings and the forest
13. **Another View of Hester.** Years of work and charity have changed some townspeople’s reading of the A: some associate it with ability rather than only adultery. Hester sees how secrecy has harmed Dimmesdale and resolves to act.
14. **Hester and the Physician.** Hester confronts Chillingworth about his revenge and proposes to reveal his identity to the minister. Their exchange shows how vengeance has transformed him, though he refuses to accept an easy moral correction.
15. **Hester and Pearl.** Hester reflects on her marriage and anger toward Chillingworth. Pearl makes her own green letter from plant material and questions the meaning of her mother’s A and the minister’s habit of holding his hand over his heart. Hester does not fully explain.
16. **A Forest Walk.** Hester and Pearl go into the forest to intercept Dimmesdale. The child discusses the letter and local stories about the “Black Man,” a supernatural figure in the community’s imagination. Sunlight and the brook become significant images.
17. **The Pastor and His Parishioner.** Hester reveals that Chillingworth is her husband. Dimmesdale is hurt by her concealment but eventually forgives her. They consider leaving the colony, and Hester urges him toward a new life rather than continued dependence on his tormentor.
18. **A Flood of Sunshine.** Hester and Dimmesdale plan to depart together with Pearl. Hester removes the letter and lets down her hair; the scene briefly imagines release from the social burden of the symbol. Their hope remains fragile.
19. **The Child at the Brook-Side.** Pearl will not approach her mother as expected while the letter is absent. Hester puts it back on. The encounter exposes the depth of Pearl’s connection to the sign and the difficulty of imagining a family outside the identities imposed by the past.

## Chapters 20–24: Public confession and aftermath
20. **The Minister in a Maze.** Returning to town, Dimmesdale feels strangely changed and encounters impulses at odds with his public role. He returns to work on his Election Day sermon while preparing, in secret, for the planned departure.
21. **The New England Holiday.** The town gathers for the election festivities. Hester learns from the ship’s commander that Chillingworth intends to travel on the same vessel, threatening the family’s plan.
22. **The Procession.** Officials and clergy move through the public celebration. Dimmesdale appears unusually energetic; Hester feels the distance between his public image and their forest meeting. Pearl brings another message from the ship’s commander concerning Chillingworth.
23. **The Revelation of the Scarlet Letter.** After his sermon, Dimmesdale summons Hester and Pearl to the scaffold, despite Chillingworth’s attempt to stop him. He makes a public confession, bares his chest and dies with Hester and Pearl near him. Pearl kisses him, a moment the narrator treats as significant.
24. **Conclusion.** Accounts differ over what, if anything, the crowd saw on Dimmesdale’s chest; the narrator does not settle the reports. Chillingworth dies and leaves property to Pearl. Hester and Pearl leave; years later Hester returns alone and again wears the letter. She becomes a source of counsel for women and is eventually buried near Dimmesdale beneath a shared stone bearing an A.

## Analysis and classroom plan
Compare the three scaffold scenes: Hester’s public exposure, the minister’s night vigil and his public confession. The A is not fixed in meaning; interpretations change according to wearer, community and moment. Discuss whether the novel critiques punitive institutions while still using the language of sin. In 50 minutes: 0–10 map characters; 10–20 compare scaffold scenes; 20–30 examine Pearl’s response to the letter; 30–40 debate public versus private guilt; 40–50 write a claim using one chapter as evidence.

## Questions
Why does Hester protect the father’s identity? How does revenge affect Chillingworth? Why preserve conflicting reports of Dimmesdale’s chest?''','https://www.cliffsnotes.com/literature/s/the-scarlet-letter/book-summary'),
n('huckleberry-finn','Mark Twain · Adventures of Huckleberry Finn — story overview','''## Reading notice
This novel contains slavery, racist language and violence. Establish classroom agreements that avoid requiring students to repeat racial slurs. Set before the US Civil War and published in the 1880s, it uses Huck’s first-person vernacular to expose social contradictions, while its depictions of Jim and its ending remain subjects of debate. This is an extended plot overview, not yet a chapter-by-chapter guide.

## Beginning: home and escape
Huck Finn lives with Widow Douglas and Miss Watson, who want to make him respectable. His friend Tom Sawyer invents a gang based on adventure stories. Huck’s abusive father Pap returns and tries to gain control of Huck and his money. Pap takes him to an isolated cabin and beats him. Huck stages his own murder, escapes by canoe and hides on Jackson’s Island.

There he encounters Jim, an enslaved man who has fled after learning he may be sold away from his family. Huck agrees not to reveal him. When a visit ashore alerts Huck that searchers suspect Jim is on the island, the two escape on a raft. In a floating house they find a dead man; Jim prevents Huck from looking at the face, whose identity is revealed much later.

## Down the river
Jim hopes to reach Cairo, Illinois, and travel up the Ohio toward free states. Fog separates the pair, and Huck tricks Jim by pretending that their separation was a dream. Jim’s hurt response makes Huck apologise—an important moment in which he recognises the consequences of his cruelty. They miss Cairo and continue south. Huck wrestles with a conscience shaped by a slaveholding society; when men ask about the raft, he protects Jim with a misleading story that makes them fear disease.

A steamboat collision separates the pair. Huck becomes involved with the Grangerford family and witnesses the lethal feud between them and the Shepherdsons. Jim finds and repairs the raft, and the two resume their journey. They take aboard two fugitives who pretend to be a duke and a king. The impostors exploit communities through performances and fraud, while Jim’s position becomes more dangerous.

## The Wilks fraud and Jim’s betrayal
The con men impersonate the English brothers of the recently deceased Peter Wilks and try to take the family’s inheritance. Huck sympathises with the Wilks sisters, particularly Mary Jane, and tries to protect the money. The arrival of the real brothers exposes the imposture, but the duke and king escape and return to the raft. Eventually they betray Jim for a reward, leaving him imprisoned at the Phelps farm.

Huck considers writing to Miss Watson about Jim’s whereabouts. Remembering Jim’s care and companionship, he tears up the letter and resolves to help him, even though he has been taught that doing so is morally wrong. His decision exposes the conflict between an inherited moral code and his experience of friendship.

## Phelps farm and conclusion
At the farm, Sally and Silas Phelps mistake Huck for their expected nephew Tom Sawyer. When Tom arrives, he pretends to be his brother Sid. Huck wants a straightforward rescue, but Tom devises an elaborate “evasion” modelled on romantic adventure books, involving unnecessary difficulties and delaying Jim’s release. During the escape, Tom is shot. Jim stays to help the wounded boy and is recaptured.

Tom eventually reveals that Miss Watson died and freed Jim in her will; Tom knew this while planning the dangerous game. Aunt Polly arrives and clarifies the boys’ identities. Jim tells Huck that the dead man in the floating house was Pap. Aunt Sally wants to adopt and “sivilize” Huck, who says he plans to leave for the Territory.

## Interpretive focus and lesson
Consider how Huck’s language reveals both kindness and prejudice, and how Jim’s own desire to recover his family can be overshadowed by the boys’ adventures. Critics disagree about whether the ending exposes or repeats racist assumptions. In 50 minutes: 0–10 set respectful discussion expectations; 10–20 map the journey; 20–30 examine Huck’s apology after the fog; 30–40 analyse the torn letter; 40–50 debate the ethics of Tom’s escape plan.

## Questions
Why do Jim and Huck leave the island? Why is Huck’s decision to help Jim morally complicated for him? What makes Tom’s plan troubling?''','https://www.cliffsnotes.com/literature/a/the-adventures-of-huckleberry-finn/book-summary'),
n('turn-screw','Henry James · The Turn of the Screw — story overview','''## Frame and situation
Published in 1898, this Gothic novella reaches readers through several layers of narration. At a country-house gathering, Douglas offers a manuscript written by a former governess. She had been hired by a charming uncle to care for his orphaned niece and nephew at Bly, on the condition that she handle problems without troubling him. This is a detailed overview, not yet a chapter-by-chapter guide.

## Arrival and unsettling news
At Bly, the governess meets housekeeper Mrs Grose and young Flora. A letter arrives from Miles’s school saying the boy cannot return, without giving a satisfactory explanation. When Miles arrives, the governess finds him charming and cannot reconcile his appearance with the letter’s implication. She does not immediately ask the school for details.

## Apparitions and suspicions
The governess sees an unfamiliar man on a tower and later at a window. From her descriptions, Mrs Grose identifies him as Peter Quint, a former servant who is dead. The governess later sees a woman by the lake; Mrs Grose connects her description with Miss Jessel, the former governess, also dead. Mrs Grose shares troubling memories of Quint, Miss Jessel and their closeness to the children.

The governess becomes convinced that the figures are seeking the children and that Miles and Flora know more than they admit. Yet readers see the evidence through her account: the children do not independently confirm the apparitions. Night-time incidents involving the children intensify her suspicions, and her discussions with Mrs Grose move between observation, speculation and fear.

## Crisis at Bly
Miles asks about returning to school and challenges the governess’s control. She decides to write to the uncle. While Miles plays the piano, Flora slips away; the governess and Mrs Grose find her near the lake. The governess believes Miss Jessel is present and demands that Flora acknowledge her, but Mrs Grose says she sees no one and Flora reacts with distress and anger.

Flora becomes ill, and Mrs Grose takes her away to the uncle. The governess remains with Miles, trying to learn why he was expelled and whether he has been in contact with Quint. Miles admits taking her letter and speaks vaguely about having said things at school; the exact nature and consequences remain unclear.

## Ending and interpretation
The governess sees, or believes she sees, Quint at the window while confronting Miles. Miles names Quint, and she holds him close. She says his heart has stopped: he dies in her arms. The story does not conclusively explain his death or settle whether the ghosts exist independently of her perceptions. A supernatural reading and a psychological reading both require careful attention to the language and gaps; neither should be presented as an established diagnosis.

## 50-minute lesson
0–10: draw the narrative frame. 10–20: separate the governess’s observations from her inferences. 20–30: read the lake confrontation from more than one perspective. 30–40: discuss what the ending establishes and leaves uncertain. 40–50: write two competing interpretations with textual support.

## Questions
Why does the uncle’s instruction matter? What can Mrs Grose independently verify? What is known and unknown about Miles’s death?''','https://americanliterature.com/author/henry-james/book/the-turn-of-the-screw')]
d['course-22:4']=[
n('sleepy-hollow','Washington Irving · The Legend of Sleepy Hollow','''## Setting and narrative frame
In a secluded Hudson Valley community, stories of ghosts and enchantment circulate freely. The tale is presented through the fictional historian Diedrich Knickerbocker, whose playful narrative leaves room for competing explanations. The most famous local apparition is the Headless Horseman, said to be a Hessian soldier who lost his head in the Revolutionary War.

## Story from beginning to end
Ichabod Crane, a lean schoolmaster from Connecticut, lives by teaching and by boarding with local families. He also teaches singing and enjoys listening to frightening stories. He is highly superstitious, but he is also ambitious and eager for comfort and food.

Ichabod courts Katrina Van Tassel, the daughter of a prosperous farmer. He imagines not only Katrina but the wealth and abundant produce of her family’s farm. His rival Abraham Van Brunt, known as Brom Bones, is a strong local horseman and mischievous practical joker. Brom and his companions play tricks on the schoolmaster.

At a gathering at the Van Tassel home, Ichabod enjoys a lavish feast, dancing and a circle of supernatural stories. He hopes to advance his suit with Katrina, but their private conversation is not reported; he leaves looking disappointed. Riding home on a borrowed horse through the dark, with the stories fresh in his mind, he hears and sees frightening things. A large mounted figure approaches and appears to carry its head.

Ichabod races toward the bridge by the church, hoping the horseman will vanish at the boundary. The pursuer hurls the apparent head; it strikes Ichabod and he falls. The next day his hat, saddle and a shattered pumpkin are found, but he does not return to Sleepy Hollow. Local believers say the spirit carried him off. A later report suggests he survived and made a life elsewhere. Brom marries Katrina and laughs knowingly whenever the pumpkin is mentioned, suggesting—but not proving—that he engineered the chase.

## Interpretation
The story combines comic appetite and social rivalry with Gothic suspense. Ichabod’s fear affects what he thinks he sees. The narrator’s uncertainty and the community’s attachment to legend prevent a definitive identification of the horseman. Consider how Katrina’s choices are mediated through male observers rather than simply treating her as a prize.

## 50-minute lesson
0–10: distinguish a legend from a confirmed event. 10–22: trace the rivalry and party. 22–32: reconstruct the chase using only observed details. 32–42: compare supernatural and prank explanations. 42–50: write a claim and acknowledge uncertainty.

## Questions
Why is Ichabod vulnerable to the legend? What does the pumpkin suggest? What evidence remains inconclusive?''','https://americanliterature.com/author/washington-irving/short-story/the-legend-of-sleepy-hollow'),
n('rue-morgue','Edgar Allan Poe · The Murders in the Rue Morgue','''## Opening: a method of reasoning
An unnamed narrator describes analytical thought and meets C. Auguste Dupin in Paris. Their friendship and unusual habits establish Dupin’s observational skill before the murder mystery begins. One evening Dupin reconstructs his companion’s train of thought, making reasoning itself a dramatic spectacle.

## Crime and investigation
Newspapers report the violent deaths of Madame L’Espanaye and her daughter Camille in a house on the Rue Morgue. The room appears to have been locked from within. Witnesses heard two voices, one apparently French and another so strange that they disagree about its language. Valuables remain at the scene, complicating an easy robbery theory. A bank clerk, Adolphe Le Bon, is arrested; Dupin has reason to help him and obtains permission to inspect the house.

Dupin examines the layout and evidence that others have overlooked. One window appears securely fastened, but a broken nail and a spring mechanism make a route of entry and exit possible. The force used, unusual marks and hair, and the witnesses’ failure to identify the shrill voice lead him away from the assumption of an ordinary human attacker. He reasons that an orangutan may have been involved and that a French sailor was nearby.

## Resolution
Dupin places an advertisement suggesting that an orangutan has been found. A sailor comes to claim the animal and, after initial alarm, explains what happened. He had brought the animal from Borneo. It escaped with a razor after observing him shave, climbed into the women’s room and seized Madame L’Espanaye, apparently imitating a barber. When she struggled, it turned violent; the women were killed. The sailor witnessed events from outside but could not prevent them. The animal escaped; Le Bon is released.

## Analysis and caution
Dupin’s method combines careful attention, imaginative reconstruction and testing a hypothesis through the advertisement. The apparent impossibility depends partly on assumptions about a locked window and a human voice. The narrative is also graphic and treats a captive animal as the source of danger; its nineteenth-century language about non-European places and people can be examined critically. Ratiocination is a literary representation of reasoning, not a guarantee that every real investigation works this way.

## 50-minute lesson
0–10: identify facts and assumptions in a puzzle. 10–22: chart the evidence at the crime scene. 22–32: explain the window mechanism. 32–42: evaluate Dupin’s hypothesis and the sailor’s account. 42–50: write how the narrator creates suspense.

## Questions
Why does the second voice matter? How is the apparently locked room entered? What does the advertisement allow Dupin to test?''','https://americanliterature.com/author/edgar-allan-poe/short-story/the-murders-in-the-rue-morgue'),
n('bartleby','Herman Melville · Bartleby, the Scrivener','''## Setting and narrator
An unnamed Wall Street lawyer tells the story of his employee Bartleby. The lawyer presents himself as a safe, comfortable man and introduces his copyists Turkey and Nippers and the office assistant Ginger Nut. Because the lawyer controls the account, his judgments and charitable self-image need examination.

## Story from beginning to end
The lawyer hires Bartleby to copy legal documents. At first he produces a great deal of work. When asked to help examine a document, however, he quietly replies that he would prefer not to. The phrase returns as the lawyer makes other requests. Bartleby’s calm refusal unsettles the office, and the narrator struggles to decide how to respond.

On a Sunday visit, the lawyer discovers evidence that Bartleby has been living in the office. He feels pity at the man’s isolation, but his sympathy is mixed with discomfort and concern about his own responsibilities. Bartleby declines to explain his history. Eventually he stops copying altogether. The lawyer dismisses him and offers money, but Bartleby does not leave.

Unable to resolve the situation and anxious about his business, the lawyer moves his office, leaving Bartleby behind. The new occupants complain when Bartleby remains in the building. The lawyer offers possible kinds of work and even invites him to stay at his own home, but Bartleby refuses. Other people have him removed to the prison known as the Tombs.

The lawyer visits and pays a prison attendant to provide food, but Bartleby declines to eat. On a later visit, the lawyer finds that he has died. Afterwards he reports a rumour that Bartleby once worked in a dead-letter office, handling undelivered correspondence, and had lost that post. The lawyer interprets the rumour as meaningful, but it remains unconfirmed; it does not definitively explain Bartleby’s motives.

## Interpretation
Walls, partitions and undelivered messages suggest limits on connection. Bartleby’s phrase is grammatically polite but resists the employer’s expectations. Readers differ on whether his refusal is a protest, a response to distress, an existential puzzle or something that cannot be reduced to one explanation. Avoid diagnosing him as a settled fact. Analyse the narrator’s compassion alongside the ways he seeks to escape responsibility.

## 50-minute lesson
0–10: describe the office and its work. 10–22: trace how Bartleby’s refusals change. 22–32: examine the lawyer’s competing reactions. 32–42: discuss the prison and unverified rumour. 42–50: write an interpretation with a limitation.

## Questions
How does “prefer not to” differ from a direct order or explanation? Why does the lawyer move? What can and cannot be inferred from the dead-letter rumour?''','https://www.gradesaver.com/bartleby-the-scrivener/study-guide/summary-pages-38-46'),
n('yellow-wallpaper','Charlotte Perkins Gilman · The Yellow Wallpaper','''## Context and care
Published in 1892, the story is a first-person account of a woman whose physician husband restricts her activity as treatment for a nervous condition. It invites criticism of a historical rest cure and unequal medical authority; it is not a guide to diagnosing or treating a real person. The narrator has recently had a baby, but the text does not establish a modern clinical diagnosis.

## Story from beginning to end
The narrator and her husband John rent a large house for the summer. John, a physician, dismisses her concerns and discourages work and writing. She believes activity and companionship would help her, but records her thoughts secretly. John chooses an upstairs room that she believes was once a nursery. Its barred windows, damaged floor and disturbing yellow wallpaper make her uneasy; her preferences about the room are overridden.

With little intellectual activity and much time alone, she studies the paper. Its colour and tangled design increasingly occupy her attention. She begins to discern a figure behind the outer pattern and eventually sees a woman shaking the apparent bars and creeping about. John and his sister Jennie, who helps with the household, do not share her account. The narrator hides the extent of her preoccupation and resists attempts to interfere with the paper.

As departure approaches, she becomes determined to release the woman she sees. She locks herself in the room, removes much of the wallpaper and creeps around the wall. John demands entry; she tells him where to find the key. When he enters and sees her, he faints. She declares that she has got out despite him and “Jane,” and continues creeping over his body. The identity of “Jane” is debated; the narrative does not securely explain the name.

## Interpretation
The wallpaper can be read as a figure for confinement, with the imagined woman reflecting the narrator’s experience. The ending combines a claim of escape with evident distress, so calling it simply a happy victory or simply a medical case misses its tension. Secret writing gives readers access to a perspective that other characters often discount. John’s concern for his wife does not remove the unequal authority he exercises.

## 50-minute lesson
0–10: distinguish historical medical practice from present-day care. 10–22: map whose decisions govern the room. 22–32: trace the changing wallpaper descriptions. 32–42: debate escape and confinement at the ending. 42–50: write a claim that distinguishes evidence from inference.

## Questions
Why does the narrator write secretly? How does her perception of the wallpaper change? What remains uncertain about “Jane”?''','https://americanliterature.com/author/charlotte-perkins-gilman/short-story/the-yellow-wallpaper'),
n('story-hour','Kate Chopin · The Story of an Hour','''## Opening and false report
Louise Mallard has heart trouble. Her sister Josephine and her husband’s friend Richards try to tell her gently that her husband Brently has reportedly died in a railway disaster. Richards has checked the report with a second telegram. Louise immediately weeps with her sister, then goes alone to her room.

## At the window
Sitting before an open window, Louise notices signs of spring, sounds outside and patches of blue sky among clouds. She feels something approaching her awareness and at first tries to resist it. Gradually she recognises a sense of freedom and repeats the word to herself. She imagines future years belonging to her rather than being governed by another person’s will.

Her feelings are complex. She expects to grieve when she sees Brently’s body and remembers that he looked at her with love. She acknowledges that she loved him sometimes and sometimes did not. Her joy in anticipated independence need not mean that her initial grief was false or that Brently is portrayed as deliberately cruel.

## Reversal and ending
Josephine worries outside the locked door and asks Louise to come out. Louise eventually opens it and goes downstairs with her. At that moment Brently enters: he was far from the accident and did not know about it. Josephine cries out, and Richards attempts too late to screen him from Louise’s view. The narrative then reports that Louise has died; doctors attribute her death from heart disease to “the joy that kills.”

Readers often see dramatic irony in the doctors’ conclusion: they assume joy at her husband’s return, while the preceding scene has shown Louise’s joy in the prospect of autonomy. The exact emotional and medical mechanism of her death is not described in detail; the strength of the irony comes from the contrast between public interpretation and the private feelings readers have witnessed.

## Form and teaching
The story compresses a major change in expectation into a short span. The open window and spring images can suggest possibility without reducing them to a single fixed meaning. In 50 minutes: 0–10 predict how news might be received; 10–20 sequence the reported death and private response; 20–30 analyse the window; 30–40 compare the doctors’ conclusion with Louise’s thoughts; 40–50 write about the ending’s irony.

## Questions
Why are Louise’s grief and relief not necessarily incompatible? What does she imagine at the window? Why might readers question the doctors’ diagnosis?''','https://www.owleyes.org/text/the-story-of-an-hour/read/chopins-short-story')]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added American Literature I fiction: three novels and five short stories')
