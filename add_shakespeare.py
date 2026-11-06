import json
P='prepared-notes.json'
with open(P,encoding='utf-8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,pre=False):
 r={'id':id,'title':title,'source':source,'text':f'# {title}\nShakespeare · Semester 5\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Questions\n{questions}\n\nTeaching draft: compare the assigned text, edition and performance before class.'}
 if pre:r['status']='preliminary'
 return r
d['course-28:0']=[
n('theatre','Drama, theatre and stagecraft', '''## Shakespeare’s working theatre
Shakespeare wrote for the commercial English stage during the reigns of Elizabeth I and James I. His company, the Lord Chamberlain’s Men, became the King’s Men under James. In 1599 the company opened the Globe, an open-air playhouse with a stage projecting into a yard and galleries around it. Performances also occurred at court, on tour and, later, in indoor theatres such as Blackfriars; no single building describes all early modern performance.

## Staging conventions
Spectators could see one another and performers at close range. Entrances and exits, costume, props, music, words and the changing use of an adaptable stage helped establish location and action. The stage was not simply empty: its doors, upper level, pillars, tiring house and trapdoor enabled effects, though exact historical arrangements and uses are debated. Performers addressed audiences in soliloquies and asides.

In professional London playing companies, male performers played women’s roles, often with boys or young men. This matters when considering disguise in As You Like It: a boy actor could perform Rosalind, who performs Ganymede, who pretends to be Rosalind. It does not make the character’s experiences unreal.

## Performance reading
Read a scene aloud, mark entrances and exits and try two different ways of speaking an aside. Distinguish a possibility for staging from a documented historical fact.''','0–10: sketch the Globe stage. 10–22: identify entrances, props and audience position. 22–32: read a short exchange aloud. 32–42: stage an aside in two ways. 42–50: explain how performance changes interpretation.','How can words and props create a location? What is the difference between a soliloquy and an aside?','https://www.shakespearean.org.uk/a-lecture-on-elizabethan-theatre-by-thomas-larque/'),
n('contemporaries','Shakespeare and his contemporaries', '''## A shared theatrical world
Shakespeare was a working playwright and actor in a competitive and collaborative theatre culture, not an isolated writer. Companies relied on performers, managers, patrons, censors, printers and audiences. Plays could be revised, adapted and written collaboratively; individual evidence is needed before asserting collaboration on a specific work.

Christopher Marlowe’s Doctor Faustus and Tamburlaine explore ambition, knowledge and power through forceful dramatic verse. Thomas Kyd’s The Spanish Tragedy is an important revenge play with a bereaved father, investigation and a play-within-a-play; it can be compared with Hamlet without assuming the two plots are identical. Ben Jonson’s Volpone and The Alchemist are noted for satire of greed and deception. John Webster and Thomas Middleton also contributed to the rich dramatic culture around Shakespeare.

## Compare rather than rank
Take one short scene from each assigned work and compare language, performance and dramatic effect. Avoid claims that one writer invented blank verse or that every contemporary wrote in one unchanging style. Dates and authorship of early modern plays can be disputed.''','0–10: map writers and companies. 10–22: introduce Marlowe, Kyd and Jonson. 22–32: compare revenge or ambition in two passages. 32–42: discuss collaboration and competition. 42–50: support one comparison with textual detail.','How does Kyd’s revenge drama offer a comparison with Hamlet? Why study companies as well as individual writers?','https://guides.nyu.edu/shakespeare-studies/shakespeares-contemporaries'),
n('forms','Forms of Shakespearean drama', '''## Useful categories
Tragedies frequently move toward suffering and death, with serious conflicts involving individuals and wider communities. Othello, Macbeth and Hamlet differ in their causes and settings; none can be reduced to a single trait.

Comedies often use mistaken identity, disguise, verbal play and movement towards marriage or reconciliation. A happy ending need not resolve every question about consent, class or power. A Midsummer Night’s Dream and As You Like It both move away from a court into a transformative space but do so differently.

Histories dramatise political power, succession and conflict using historical material; they are crafted plays, not neutral historical records. Later plays often called romances combine loss, separation, improbable events and reunion. Genre labels help comparison but overlap: histories can be tragic, comedies can contain harm, and later editorial classifications are not rigid rules.

## Language
Blank verse is unrhymed iambic pentameter; Shakespeare also uses prose, songs and rhyme. Shifts among these forms can shape character and mood, but the choice of prose does not automatically show that a speaker is unimportant.''','0–10: identify familiar genre expectations. 10–22: contrast tragedy, comedy and history. 22–32: discuss romance and overlap. 32–42: read prose and verse aloud. 42–50: explain one complication to a genre label.','What can a genre label reveal and conceal? How do verse and prose differ?','https://www.folger.edu/blogs/shakespeare-and-beyond/shakespeare-before-he-was-famous/')]
d['course-28:1']=[
n('othello','Othello · Story by act', '''## Before reading
The play contains racist language, manipulation and intimate-partner violence. Othello is a Moor and a Venetian military commander; the meaning of racial categories in the play is historically specific, and racist claims made by characters must not be repeated as facts about him. Desdemona and Emilia have voices and decisions of their own.

## Act I — Venice: a marriage and a grievance
Iago resents Othello’s promotion of Cassio and uses Roderigo, who desires Desdemona, as an ally. They awaken Brabantio with inflammatory claims about his daughter’s marriage. Brabantio accuses Othello of using magic, but before the duke and senate Othello describes their courtship and Desdemona confirms that she chose to marry him. Ordered to Cyprus to meet a Turkish threat, Othello arranges for Desdemona to follow. Iago privately plans to use Cassio and the marriage against his general.

## Act II — Cyprus: engineered disgrace
A storm destroys the Turkish fleet. The parties arrive separately; Othello and Desdemona are joyfully reunited. During celebration Iago encourages Cassio to drink and prompts Roderigo to provoke him. A fight wounds Montano. Othello dismisses Cassio as lieutenant. Iago advises Cassio to ask Desdemona to plead his case, making a helpful gesture available for later misrepresentation.

## Act III — Suspicion and the handkerchief
Desdemona promises to help Cassio. Iago uses Cassio’s departure from her presence to insinuate that something is wrong, presenting himself as reluctant to speak and warning Othello about jealousy while provoking it. Desdemona drops a handkerchief Othello gave her; Emilia picks it up and gives it to Iago, who has asked for it. Iago places it where Cassio will find it and falsely presents its presence as evidence of an affair. Othello demands proof but accepts Iago’s invented account and vows revenge; he makes Iago lieutenant.

## Act IV — Manipulated seeing
Iago arranges for Othello to overhear only part of a conversation with Cassio. Cassio speaks of Bianca, but Othello believes he is speaking about Desdemona. Bianca appears with the handkerchief, which Cassio had given her to copy, further misleading Othello. Lodovico arrives with orders replacing Othello in Cyprus with Cassio; Othello strikes Desdemona. Later, Desdemona and Emilia discuss fidelity and the different expectations placed on women and men.

## Act V — Violence and disclosure
Iago has Roderigo attack Cassio; Cassio wounds Roderigo, and Iago wounds Cassio before killing Roderigo. Believing Cassio is dead, Othello confronts Desdemona and smothers her despite her protests of innocence. Emilia enters, exposes Iago’s lies and explains the handkerchief. Iago kills Emilia and is seized. Othello recognises the deception and kills himself. Cassio survives and authority passes to him; the play leaves Iago’s fuller explanation withheld.

## Interpretation
Iago constructs false evidence, but manipulation does not remove Othello’s responsibility for violence. Ask how racism, military reputation, trust and gender shape the play. The handkerchief is a gift, a symbol and a material object whose movement the audience can track more accurately than Othello.''','0–10: set sensitive discussion boundaries and map relationships. 10–20: trace Iago’s plans. 20–30: follow the handkerchief. 30–40: compare what audience and Othello know. 40–50: write a claim about evidence and responsibility.','How does Cassio’s request become misleading evidence? What does Emilia reveal? Why does Othello remain accountable for his actions?','https://www.folger.edu/explore/shakespeares-works/othello/read/'),
n('macbeth','Macbeth · Story by act', '''## Before reading
The play depicts murder, political violence and the killing of children. It raises questions about prophecy and responsibility without requiring an assumption that supernatural words force human actions.

## Act I — Prophecy and decision
After a battle, three witches greet Macbeth as Thane of Glamis, Thane of Cawdor and future king, and tell Banquo that his descendants will be kings. Macbeth soon learns he has indeed been made Cawdor. Duncan names Malcolm his heir and announces a visit to Macbeth’s castle. Lady Macbeth reads Macbeth’s letter about the prophecies and urges him to seize the opportunity. Macbeth hesitates, recognising Duncan’s trust and his own obligations, but he and his wife decide on murder.

## Act II — Duncan’s death
Macbeth sees an apparent dagger leading him toward Duncan’s chamber. He kills the sleeping king and returns deeply shaken, bringing the daggers with him. Lady Macbeth takes them back and smears blood on the sleeping guards. Macduff discovers Duncan’s body; Macbeth kills the guards and explains that he did so in fury. Fearing for their lives, Duncan’s sons flee—Malcolm to England and Donalbain to Ireland. Their flight raises suspicion against them; Macbeth becomes king.

## Act III — Rule through fear
Banquo suspects Macbeth but remembers the prophecy about his own descendants. Macbeth, fearing Banquo and Fleance, arranges an ambush. Banquo is killed, but Fleance escapes. At a banquet Macbeth sees Banquo’s ghost and reacts publicly, alarming the guests. Lady Macbeth tries to manage the scene. Macbeth resolves to seek out the witches again as resistance to his rule grows.

## Act IV — Ambiguous assurances and further crimes
The witches show apparitions warning Macbeth to beware Macduff, asserting that none born of woman will harm him, and promising safety until Birnam Wood comes to Dunsinane. They also show a line of kings associated with Banquo. Macbeth treats the assurances as security while arranging the murder of Macduff’s wife, children and household after learning that Macduff has fled. In England Malcolm tests Macduff’s loyalty; Ross brings news of the family’s slaughter. Malcolm and Macduff prepare to invade.

## Act V — The prophecies fulfilled
Lady Macbeth sleepwalks, speaking of blood and guilt; her death is reported later, and the play does not stage how it occurs. Malcolm’s soldiers cut branches from Birnam Wood to conceal their numbers, making the wood appear to advance on Dunsinane. Macbeth fights, but Macduff reveals that he was delivered by caesarean rather than born in the ordinary way. Macduff kills Macbeth, and Malcolm is acclaimed king.

## Interpretation
Blood, sleep and darkness recur, connecting political action to disturbed conscience. The witches’ words are equivocal: discuss how Macbeth interprets them and makes choices, rather than treating prophecy as an excuse.''','0–10: introduce characters and warning. 10–20: map the first prophecy and decision. 20–30: trace escalating violence. 30–40: explain the two misleading assurances. 40–50: write about choice and prophecy.','Why does Macbeth fear Banquo? How do Birnam Wood and Macduff challenge Macbeth’s reading of the prophecies?','https://www.folger.edu/explore/shakespeares-works/macbeth/read/'),
n('hamlet','Hamlet · Story by act', '''## Before reading
The play includes murder, suicide, grief and depictions of mental distress. Distinguish a character’s staged behaviour from a clinical diagnosis, and approach Ophelia’s death and Hamlet’s thoughts sensitively.

## Act I — A demand for revenge
At Elsinore guards and Horatio see a ghost resembling the dead king. Prince Hamlet mourns his father and is distressed by his mother Gertrude’s marriage to his uncle Claudius, now king. Laertes and Polonius warn Ophelia about Hamlet. The ghost tells Hamlet that Claudius murdered him by pouring poison into his ear, and demands revenge while instructing Hamlet to leave Gertrude to her conscience. Hamlet asks his companions to swear secrecy and suggests he may adopt an “antic” manner.

## Act II — Surveillance and a test
Polonius sends Reynaldo to gather information about Laertes. Ophelia reports Hamlet’s disturbing appearance, which Polonius interprets as lovesickness. Claudius and Gertrude enlist Rosencrantz and Guildenstern to discover what troubles Hamlet. A company of players arrives. Hamlet admires the actor’s ability to summon emotion and plans to stage a scene resembling the alleged murder so that he can observe Claudius’s response.

## Act III — Performance and killing
Hamlet reflects on living and dying and encounters Ophelia while Claudius and Polonius observe. At the play, the staged murder provokes Claudius to stop the performance and leave; Hamlet takes his reaction as confirmation. Claudius privately admits the murder and struggles to pray. Hamlet finds him kneeling but refrains from killing him, reasoning about the consequences for Claudius’s soul. In Gertrude’s chamber Polonius hides behind a tapestry; Hamlet hears him and stabs through it, killing him. The ghost appears to Hamlet again, while Gertrude cannot see it.

## Act IV — Exile, grief and another plot
Claudius sends Hamlet to England with Rosencrantz and Guildenstern and a sealed order for Hamlet’s death. Hamlet discovers and replaces the order; after an encounter with pirates he returns to Denmark. Ophelia, distressed after her father’s death, sings fragmented songs; Gertrude later reports that she has drowned. The circumstances of her death are debated in the play, not conclusively established as intentional. Laertes returns seeking revenge. Claudius and Laertes plan a fencing match with a poisoned blade and a poisoned drink as backup.

## Act V — Graveyard and catastrophe
In a graveyard Hamlet contemplates mortality with Horatio and recognises the skull of Yorick. Ophelia’s funeral arrives; Laertes and Hamlet clash in grief. Hamlet agrees to fence Laertes. Gertrude unknowingly drinks the poisoned wine. Laertes wounds Hamlet with the poisoned blade, and in the struggle the weapons are exchanged; Hamlet wounds Laertes. As they die, Laertes reveals the plot and Hamlet kills Claudius. Hamlet asks Horatio to tell his story and supports Fortinbras, who arrives and orders honours for him.

## Interpretation
Revenge, theatre, spying and uncertainty are interwoven. Hamlet’s apparent delay has many proposed explanations, including doubt, grief, ethics and political danger; no single diagnosis is required.''','0–10: map the royal family and ghost. 10–20: compare claims with evidence. 20–30: trace the play-within-the-play and Polonius’s death. 30–40: sequence the final duel. 40–50: write two competing interpretations of delay.','Why does Hamlet stage a play? What is known and not known about Ophelia’s drowning? How does the poisoned plot turn against its makers?','https://www.folger.edu/explore/shakespeares-works/hamlet/read/')]
d['course-28:2']=[
n('midsummer','A Midsummer Night’s Dream · Story by act', '''## Characters and setting
The play interweaves the Athenian court, four young lovers, a group of craftspeople rehearsing a play, and the fairies Oberon, Titania and Robin Goodfellow, also called Puck. The forest permits experiment and confusion, but magic also raises questions about consent.

## Act I — Athenian law and a plan
Theseus prepares to marry Hippolyta. Egeus demands that his daughter Hermia marry Demetrius; she loves Lysander. Theseus tells Hermia that disobedience carries severe penalties, including death or lifelong chastity. Hermia and Lysander plan to escape into the woods. They tell Helena, who loves Demetrius; hoping to win his favour, she tells him of their plan. Meanwhile, Bottom, Quince and other craftspeople choose roles in Pyramus and Thisbe for a proposed wedding entertainment.

## Act II — The forest and mistaken magic
Oberon and Titania quarrel over an Indian boy in Titania’s care. Oberon sends Puck to obtain a flower whose juice makes a sleeping person love the first creature seen on waking. Seeing Demetrius reject Helena, Oberon also directs Puck to help her. Oberon anoints Titania’s eyes. Puck mistakes sleeping Lysander for the intended Athenian and anoints him; when Helena wakes him he falls in love with her. Helena thinks she is being mocked; Hermia wakes alone and searches for Lysander.

## Act III — Confusion multiplied
The craftspeople rehearse. Puck gives Bottom an ass’s head; his frightened companions flee. Titania wakes, sees Bottom and falls in love with him. Oberon discovers Puck’s error, anoints Demetrius and brings Helena nearby. Now both men pursue Helena, who suspects a cruel trick, while Hermia believes Helena has stolen Lysander’s affection. The four quarrel. Puck leads the men apart, and once the lovers sleep he applies a remedy to Lysander’s eyes.

## Act IV — Waking and arrangements
After Titania gives Oberon the boy, he releases her from the enchantment, and Puck restores Bottom’s head. Theseus, Hippolyta and Egeus discover the sleeping lovers. Lysander again loves Hermia, while Demetrius declares love for Helena. Theseus overrules Egeus and arranges the couples’ marriages alongside his own. Bottom wakes believing his experience was an extraordinary dream and returns to the anxious craftspeople.

## Act V — A play and a blessing
The newly married couples watch the craftspeople perform Pyramus and Thisbe. Its tragic lovers and comic performance invite both laughter and reflection about theatrical illusion; the court sometimes mocks the performers. Fairies later bless the house, and Puck’s closing address suggests that if the audience has been offended it may think of the play as a dream.

## Interpretation
Compare courtly authority with fairy manipulation and theatrical play. Lysander’s enchantment is removed; the play does not show a corresponding removal of Demetrius’s love spell, a detail that complicates a simple account of freely chosen harmony.''','0–10: draw the four lovers’ initial relationships. 10–20: chart each change in the forest. 20–30: trace Titania and Bottom. 30–40: discuss performance and consent. 40–50: explain one unresolved tension in the ending.','Why does Puck enchant Lysander? What happens to Demetrius’s enchantment? How does Pyramus and Thisbe mirror or contrast with the main action?','https://www.folger.edu/explore/shakespeares-works/a-midsummer-nights-dream/read/'),
n('as-you-like-it','As You Like It · Story by act', '''## Beginning and characters
The play contrasts the court with the Forest of Arden and uses disguise, songs, debate and multiple love plots. Rosalind is the daughter of Duke Senior, who has been displaced by his brother Duke Frederick. Orlando is mistreated by his elder brother Oliver.

## Act I — Family conflict and exile
Oliver withholds Orlando’s proper upbringing and encourages the wrestler Charles to defeat him. Orlando wins; he and Rosalind are attracted to one another. Duke Frederick banishes Rosalind, and his daughter Celia chooses to go with her. For safety Rosalind adopts the disguise of a young man, Ganymede; Celia takes the name Aliena. The court fool Touchstone accompanies them.

## Act II — Arrival in Arden
Duke Senior and his followers live in the forest, reflecting on its hardships and pleasures. Adam warns Orlando of Oliver’s threat, and the two flee. Rosalind, Celia and Touchstone encounter shepherds Corin and Silvius, and arrange to obtain a cottage and flock. Orlando searches desperately for food for Adam and meets Duke Senior’s generous company. Jaques reflects on life through the famous image of the world as a stage.

## Act III — Love, role-play and pastoral argument
Orlando hangs verses about Rosalind on trees. Rosalind, still dressed as Ganymede, meets him and offers to “cure” his love by having him practise wooing Ganymede as if Ganymede were Rosalind. The audience knows what Orlando does not. Silvius loves the shepherdess Phoebe, who rejects him and becomes attracted to Ganymede. Touchstone courts Audrey, while discussions among courtiers and shepherds complicate an idealised picture of country life.

## Act IV — Rehearsal and reconciliation
In a playful mock courtship and wedding, Orlando woos Ganymede-as-Rosalind while Celia participates. Phoebe sends Ganymede a love letter. Oliver arrives with news that Orlando saved him from danger, including a lioness; Orlando was wounded. This act changes Oliver’s attitude towards his brother. Rosalind faints on hearing the account, revealing an emotion she must explain away within the disguise.

## Act V — Promises and marriages
Oliver and Celia fall in love and plan to marry. Ganymede makes a series of promises intended to resolve the tangled relationships. Rosalind reveals herself; Orlando marries Rosalind, Oliver marries Celia, Silvius marries Phoebe, and Touchstone marries Audrey. News arrives that Duke Frederick has abandoned his military plan and turned to a religious life, so Duke Senior’s position will be restored. Jaques chooses not to return with the others. Rosalind delivers the epilogue directly to the audience.

## Interpretation
Rosalind’s disguise gives her room to test Orlando’s romantic language and to direct events, while also making Phoebe’s attraction complicated. Arden is a place for reflection and change, not a hardship-free paradise.''','0–10: map the two sets of brothers. 10–20: track the journeys to Arden. 20–30: examine Ganymede’s courtship game. 30–40: compare Rosalind, Phoebe and Silvius. 40–50: explain what the ending resolves or leaves uneasy.','Why does Rosalind become Ganymede? What changes Oliver’s attitude? Why is Arden more complicated than an ideal countryside?','https://www.folger.edu/explore/shakespeares-works/as-you-like-it/read/')]
d['course-28:3']=[
n('sonnets-selection','Sonnets · Selected study — prescribed poems not specified', '''## Important: selection to confirm
The extracted syllabus says “Sonnets (A select Study)” but does not list sonnet numbers. The original text extracted from the corresponding syllabus page likewise gives no numbers. Confirm the teacher’s reading list or assigned edition before treating any particular sonnet as examinable. The example notes in this unit are practice readings, not a verified list of prescribed poems.

## Form and background
Shakespeare’s 1609 collection contains 154 numbered sonnets. Many, though not every poem, use the English sonnet pattern: fourteen lines, three quatrains and a closing couplet, often rhyming ABAB CDCD EFEF GG. Iambic pentameter is a prevailing rhythmic pattern, with expressive variations. A turn in thought may occur at the couplet or elsewhere; it is not fixed by a rule.

The form develops from earlier European traditions including Petrarchan sonnets, whose typical octave-and-sestet arrangement and love conventions were adapted by English poets. The sonnets explore beauty, time, writing, desire and other issues in varied and sometimes contradictory voices. Do not equate the speaker automatically with Shakespeare or assert the identities of the addressees as settled facts.

## Reading method
Paraphrase each quatrain, track repeated images, locate changes in argument, then explain how the couplet changes or reinforces the thought.''','0–10: confirm that the selected list is unknown. 10–22: map fourteen lines and rhyme. 22–32: compare an octave/sestet with English quatrains/couplet. 32–42: locate a turn in a sample. 42–50: write an evidence-based reading.','Why are the example sonnets not automatically prescribed? How can a couplet change the argument?','https://www.folger.edu/explore/shakespeares-works/shakespeares-sonnets/read/',True),
n('sonnet-18-example','Sonnet 18 · Practice example, not confirmed prescribed', '''## Summary
The speaker compares the beloved with a summer day but finds the beloved more lovely and more constant. Summer is short, winds can disturb its beauty, and the sun can be too hot or obscured. All beauty can decline through chance or nature’s changing course. The speaker then claims the beloved’s beauty will endure in the poem: as long as people live and can read it, the verse will keep that image alive.

## Reading
The question at the opening becomes a bold claim about poetry’s power. The couplet makes that promise dependent on future readers. The poem preserves an image in words; it does not prove that a physical person cannot die. Ask whether the confidence sounds persuasive, affectionate or self-promoting.''','0–10: paraphrase the opening question. 10–22: list summer’s imperfections. 22–32: identify the turn to verse. 32–42: discuss the promise of immortality. 42–50: explain the couplet’s condition.','Why is summer an imperfect comparison? How does the final couplet involve readers?','https://www.folger.edu/explore/shakespeares-works/shakespeares-sonnets/read/18/',True),
n('sonnet-73-example','Sonnet 73 · Practice example, not confirmed prescribed', '''## Summary
The speaker asks the beloved to see approaching age and death through three images. First, a late-autumn landscape holds few leaves on bare branches where birds once sang. Second, twilight fades toward night and sleep. Third, a fire glows on the ashes of the fuel that once sustained it. The closing couplet suggests that awareness of impending loss makes the beloved’s love stronger.

## Reading
The images move from a season to a day to a dying fire, making time seem increasingly compressed. The repeated invitation to see places the addressee in an observing role. The poem’s speaker may sound old, but that does not establish Shakespeare’s age or personal circumstances when writing it.''','0–10: name the three images. 10–22: paraphrase each quatrain. 22–32: compare their timescales. 32–42: discuss love and anticipated loss. 42–50: explain the couplet.','How do autumn, twilight and embers relate? Why does loss intensify love in the speaker’s argument?','https://www.folger.edu/explore/shakespeares-works/shakespeares-sonnets/read/73/',True),
n('sonnet-116-example','Sonnet 116 · Practice example, not confirmed prescribed', '''## Summary
The speaker argues that true love between minds does not cease merely because circumstances or a beloved change. Love is compared with a fixed navigational mark enduring storms and a guiding star whose position can be measured even if its full worth is unknown. Time damages physical beauty, but the speaker asserts that love endures beyond brief hours and weeks. The concluding couplet stakes the speaker’s writing and even the existence of love on the truth of this claim.

## Reading
The poem offers a forceful ideal, not an objective test for everyone’s relationships. Navigation imagery represents steadiness amid uncertainty; the personification of Time makes mortality an opponent. The final wager may suggest confidence, persuasion or an awareness of challenge.''','0–10: paraphrase the definition. 10–22: trace the navigational images. 22–32: compare love and Time. 32–42: debate the ideal without demanding personal disclosure. 42–50: explain the force of the wager.','Why use a star and a fixed mark? What does the final wager add?','https://www.folger.edu/explore/shakespeares-works/shakespeares-sonnets/read/116/',True),
n('sonnet-130-example','Sonnet 130 · Practice example, not confirmed prescribed', '''## Summary
The speaker denies a series of extravagant comparisons often used to praise a beloved: her eyes are not like the sun, her lips are less red than coral, and her cheeks do not display the colours of roses. He prefers some perfumes to her breath, acknowledges that music sounds sweeter than her voice, and observes that she walks on the ground rather than like an imagined goddess. The couplet nevertheless declares his love as rare as any love praised through false comparisons.

## Reading
The sonnet plays with idealising love-poetry conventions rather than simply listing insults. Its reversal can be read as affectionate realism, witty self-display, or an uncomfortable mix of praise and disparagement. Ask how standards of beauty and the beloved’s absent voice affect interpretation.''','0–10: identify the comparisons. 10–22: distinguish conventional praise from denial. 22–32: paraphrase the couplet. 32–42: discuss humour and possible discomfort. 42–50: support an interpretation with a detail.','What kind of conventional praise does the poem challenge? Does the ending erase the earlier discomfort?','https://www.folger.edu/explore/shakespeares-works/shakespeares-sonnets/read/130/',True)]
d['course-28:4']=[
n('wilson-falstaff','John Dover Wilson · The Fortunes of Falstaff — introductory approach', '''## Scope and edition check
The syllabus names the book but the extracted unit does not specify chapters. This is a short introductory approach, not a substitute for the assigned passages or a complete summary of Dover Wilson’s argument. Obtain the actual edition and reading list; verify claims and quotations there.

## Starting points
Dover Wilson studies Falstaff’s shifting fortunes in relation to Prince Hal and the Henry IV plays. Sir John Falstaff is a witty companion of Hal, associated with tavern life, appetite, verbal invention and dubious conduct. Hal moves between the tavern world and the demands of princely rule; the treatment of Falstaff becomes especially significant when the newly crowned king rejects him in Henry IV, Part 2.

One influential approach links Hal’s progress to traditions of morality drama and examines how audiences judge the tension between comic companionship and political duty. Responses to the rejection differ: readers may treat it as necessary to rule, as cruel abandonment, or as both. Do not attribute a specific detailed verdict to Wilson without checking his text.

## Apply critically
Read the rejection in its dramatic context, not merely as a plot fact. Compare the language used by Hal and Falstaff; ask how staging, prior scenes and audience sympathy affect judgment. Compare with Bradley’s character-centred approach, but do not assume every critic means the same thing by character.''','0–10: locate Falstaff and Hal in the two plays. 10–20: outline the change from prince to king. 20–30: read the rejection in an assigned edition. 30–40: debate political necessity and friendship. 40–50: identify which claims require checking in Wilson.','How does Hal’s public role complicate friendship? What must be verified before quoting or attributing a critical judgment?','https://www.rookebooks.com/1943-the-fortunes-of-falstaff',True),
n('knight-wheel','G. Wilson Knight · The Wheel of Fire — introductory approach', '''## Scope and edition check
The syllabus lists the book but gives no chapters. This note introduces an approach associated with Knight; it does not report the detailed thesis of an unspecified assigned chapter. Read the designated essay and confirm its argument and edition before examination.

## Reading for dramatic patterns
Knight is associated with attention to Shakespeare’s imagery, atmosphere, symbolism and the relationships among different elements of a dramatic work. A pattern of recurring images can help a reader think about the play as a dramatic whole rather than treating a character as if independently alive outside the text. Individual essays differ, and the meaning of a particular image must be argued from its context.

For practice, trace blood and sleep across Macbeth, or images of seeing and proof across Othello. Record who uses each image, when and to what effect; avoid assuming that a word has one unchanged symbolic meaning wherever it appears. Consider the performance as well as the printed words.

## Criticism and limits
An imagery-based reading may show connections a plot summary misses. It can also risk smoothing over conflict, history or uneven power if it treats a whole play as perfectly unified. Compare this method with an attention to character, genre or social context.''','0–10: explain that the assigned chapter is unknown. 10–22: collect an image from two scenes. 22–32: compare changes in speaker and context. 32–42: build a claim about pattern. 42–50: test the limits of that claim.','How does an image-based approach differ from a plot summary? Why should an image be interpreted in context?','https://www.literaturewise.in/mdl/mod/page/view.php?id=146',True),
n('bradley-tragedy','A. C. Bradley · Shakespearean Tragedy — introductory approach', '''## Scope and edition check
The syllabus names the book but not particular lectures. This is an introductory guide to Bradley’s approach, not a verified summary of every assigned lecture. Consult the prescribed edition and passages before attributing exact claims.

## Main orientation
Bradley’s influential lectures examine major Shakespearean tragedies, including Hamlet, Othello, King Lear and Macbeth, with sustained attention to character and action. He considers conflict within individuals and between individuals and their circumstances, as well as the role of forces such as chance. His interpretation is richer than the shorthand that every tragic protagonist simply possesses one fixed “tragic flaw.”

For Othello, a classroom can examine how trust, jealousy, manipulation, racial prejudice and military authority interact. For Macbeth, trace choices and their consequences alongside prophecy and political conditions. These examples are teaching applications, not claims that Bradley discusses each factor in the same modern terms.

## Questions for critical reading
What evidence does Bradley use when discussing a character? Does his interpretation illuminate performance, imagery, gender or historical context, or leave some of them for other approaches? Compare his emphasis with Knight’s attention to patterns of imagery without turning either critic into a caricature.''','0–10: locate the four tragedies. 10–22: distinguish character, action and circumstance. 22–32: examine a short scene. 32–42: compare character and imagery approaches. 42–50: identify one claim to verify in the assigned lecture.','Why is “one fatal flaw” an oversimplification? How might another critical method add to Bradley’s reading?','https://www.everand.com/book/322065067/Shakespearean-Tragedy-Lectures-on-Hamlet-Othello-King-Lear-Macbeth',True)]
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
