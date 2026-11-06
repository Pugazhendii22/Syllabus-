import json
P='prepared-notes.json'
with open(P,encoding='utf-8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source):
 return {'id':id,'title':title,'source':source,'text':f'# {title}\nModern Fiction · Semester 6\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: read with the assigned edition. Chapter divisions, spellings and interpretations can vary; check details and quotations before class.'}
d['course-35:0']=[
n('jim-patna','Lord Jim · From youthful dreams to the Patna inquiry', '''## Opening and narrative method
Jim, the son of an English clergyman, grows up imagining adventurous acts of courage at sea. The opening moves across time: we first learn of his later work as a water-clerk, then his training and career. A storm on a training ship reveals a gap between his imagined heroism and hesitation in action. Later an injury leaves him in port; he signs on as chief mate of the ageing Patna.

## The voyage
The steamer carries hundreds of Muslim pilgrims. After an underwater collision, the officers fear that a damaged bulkhead will give way; there are too few usable boats for everyone. Jim becomes caught between a sense of duty and the panic of the other officers. He jumps into their boat, leaving the pilgrims aboard. The ship does not sink: a French gunboat finds and tows it, and the pilgrims survive. Their survival does not erase the abandonment.

## The inquiry and Marlow
Jim attends the official inquiry; the officers’ certificates are cancelled. Marlow, initially a spectator at the hearing, becomes involved in Jim’s story. Over conversation, Jim attempts to explain the jump and Marlow listens, judges and revises his understanding. Captain Brierly, a respected officer connected to the inquiry, dies by suicide, complicating any easy division between confident professional and failed man.

## How to read
The event emerges through delayed, overlapping accounts rather than a single immediately complete scene. Ask whose words we hear and whose experience is left marginal. The pilgrims are essential to the ethical issue, yet the narrative gives them much less individual attention than Jim.''','0–10: distinguish chronology from order of telling. 10–20: reconstruct the voyage. 20–30: discuss the inquiry. 30–40: examine the pilgrims’ limited perspective. 40–50: explain a narrative delay.','Did the Patna sink? Why does its survival not settle the ethical question?','https://www.sparknotes.com/lit/lordjim/section4/'),
n('jim-patusan','Lord Jim · Patusan, friendship and Jewel', '''## After the inquiry
Marlow helps Jim find work in ports, but reminders of the Patna repeatedly drive Jim away. Marlow consults the trader Stein, who reflects on romantic ideals and recommends a post in Patusan, a remote river district. Stein sends a silver ring as a token of friendship for his old associate Doramin.

## Arrival and alliances
Rajah Allang detains Jim, who escapes and reaches Doramin’s community. Doramin’s son Dain Waris becomes a close friend. Jim helps organise an attack on Sherif Ali’s stronghold, including the difficult movement of artillery. His success and subsequent conduct earn considerable trust; he becomes known as Tuan Jim.

## Jewel and the cost of a new life
Jim falls in love with Jewel, the daughter of the deceased woman associated with the trading post and stepdaughter of the resentful Cornelius. Jewel fears abandonment, drawing on what she has seen of her mother’s life. Jim promises not to leave her. Marlow visits and sees Jim’s apparent security, while also questioning whether the new role fully resolves the earlier crisis.

## Critical perspective
Patusan is not an empty stage created for a European hero: Doramin, Dain Waris, Jewel and Tamb’ Itam have interests and relationships of their own. The novel’s colonial language and unequal attention to non-European characters deserve scrutiny. Avoid treating Marlow’s judgments as neutral truth.''','0–10: locate Jim’s repeated departures. 10–20: trace the ring and alliance. 20–30: discuss Jewel’s fears. 30–40: question the colonial viewpoint. 40–50: write about trust.','What does Stein’s ring enable? Why does Jewel fear Jim will leave?','https://www.sparknotes.com/lit/lordjim/section7/'),
n('jim-end','Lord Jim · Brown’s arrival and the ending', '''## The narrative frame changes
Marlow’s spoken account ends before the full story is known. Later a selected listener receives a packet of documents, including Marlow’s written reconstruction. Marlow draws on different reports, including accounts from Tamb’ Itam, Jewel and the dying Gentleman Brown. The layered sources leave room for uncertainty and bias.

## The crisis
Brown and his armed followers arrive seeking supplies and are contained after fighting with local forces led by Dain Waris. Jim negotiates safe passage for them and accepts responsibility for the decision. Cornelius secretly guides Brown along a back channel. Tamb’ Itam delivers Jim’s message and silver ring to Dain Waris, but Brown’s men then attack the camp and kill Dain Waris. Tamb’ Itam kills Cornelius during the aftermath.

## Jim’s choice
Jewel and Tamb’ Itam urge Jim to defend himself or escape. Jim instead goes to the grieving Doramin, who shoots him. For Jim, accepting the consequences may appear to recover a sense of honour; for Jewel it breaks his promise not to abandon her. Marlow cannot close the story with a single uncontested judgment.

## Teaching focus
Compare Jim’s two decisions under pressure: abandoning the Patna and trusting Brown. Neither event is identical. Ask whether the ending places Jim’s ideal of honour above the living people who depend on him.''','0–10: identify the sources in the packet. 10–20: map the river and ambush. 20–30: compare Jim’s and Jewel’s viewpoints. 30–40: debate honour and responsibility. 40–50: write an evidence-based judgment.','How does Brown evade Dain Waris’s guard? Why might Jewel see Jim’s final action as betrayal?','https://www.sparknotes.com/lit/lordjim/section12/')]
d['course-35:1']=[
n('sons-1','Sons and Lovers · Chapters 1–6: the Morel family', '''## Publication and setting
The syllabus prints 1915, but the novel was first published in 1913; 1915 is the publication year of Lawrence’s The Rainbow. Compare the assigned edition. The novel begins in a Nottinghamshire mining community, focusing on Gertrude Morel, her miner husband Walter and their children.

## Chapters 1–3
Gertrude’s early attraction to Walter gives way to disappointment over money, drinking, deception and anger. During a violent quarrel he locks her outside while she is pregnant. Paul is born into an increasingly strained home. Walter’s illness and financial insecurity expose the family’s dependence on work and neighbours. Gertrude increasingly invests hope and affection in her eldest son William.

## Chapters 4–6
Paul grows sensitive to his mother’s moods and to conflict at home. He begins work at a Nottingham surgical-appliance firm; art and imagination remain important to him. William advances in London and becomes engaged to a fashionable woman, but dies after illness. Gertrude’s grief is overwhelming. When Paul later becomes dangerously ill with pneumonia, she nurses him and her emotional life turns increasingly toward him.

## Interpretation
A psychoanalytic reading may examine desire, rivalry and family attachment, but it is one interpretive lens, not a clinical diagnosis of fictional people. Class, industrial labour, gender and constrained choices also shape the household.''','0–10: locate the mining setting. 10–20: map Morel family relations. 20–30: trace William’s career and death. 30–40: discuss Paul’s illness and maternal attachment. 40–50: compare psychological and social explanations.','How does the family’s economic position affect Gertrude’s choices? Why should Freudian analysis not be the only lens?','https://www.coursehero.com/lit/Sons-and-Lovers/summaries/'),
n('sons-2','Sons and Lovers · Chapters 7–11: Miriam, art and conflict', '''## Chapters 7–8
During recovery and afterwards Paul spends time at the Leivers family’s Willey Farm. He and Miriam develop an intense friendship involving books, conversation, learning and the natural world. Attraction is complicated by embarrassment, religious expectations and Paul’s uncertainty. His mother feels threatened by Miriam’s influence. Family tensions continue, including conflict with Walter and concern about Arthur’s choices.

## Chapters 9–10
Paul breaks with Miriam but cannot make a clean emotional separation. She introduces him to Clara Dawes, a woman interested in women’s rights and separated from her husband Baxter. Paul gains recognition for painting and develops his work as an artist. These developments broaden the novel beyond a simple triangle of mother, son and lover.

## Chapter 11
Paul and Miriam attempt a sexual relationship, but expectations of sacrifice, guilt and mutual misunderstanding make it painful. Paul eventually breaks away again. Read Miriam as a person with ambitions, religious beliefs and decisions, not merely as an obstacle to Paul’s development; his account of what she wants is not necessarily the whole truth.

## Key question
The mother–son bond can illuminate Paul’s divided loyalties, but it does not excuse his cruelty or establish that Miriam alone is responsible for their difficulty.''','0–10: compare farm and mining town. 10–20: trace Paul and Miriam’s friendship. 20–30: identify Clara and artistic work. 30–40: examine narrative sympathy and gender. 40–50: state a non-reductive interpretation.','What draws Paul and Miriam together? What pressures make intimacy difficult?','https://www.litcharts.com/lit/sons-and-lovers/chapter-11'),
n('sons-3','Sons and Lovers · Chapters 12–15: illness and aftermath', '''## Chapters 12–13
Paul and Clara begin an affair after the break with Miriam. Clara’s independence and marriage to Baxter Dawes complicate any easy account of freedom. Paul and Baxter come into conflict, including a physical fight. Meanwhile Gertrude’s health deteriorates and a tumour is discovered. Paul’s pleasure and anxiety increasingly coexist.

## Chapter 14
Paul visits Baxter during illness and the former rivals begin to understand one another. Gertrude’s cancer advances. Paul and Annie care for her during a difficult decline. Distressed by her suffering, Paul puts a large quantity of morphia in her milk; she dies later. This ethically troubling fictional act should not be presented as a guide to real medical decisions. Clara and Baxter ultimately move toward reconciliation.

## Chapter 15
Paul and his father leave the family house for separate lodgings. Grieving, Paul struggles to work or paint and is drawn toward thoughts of death. Miriam meets him and raises marriage, but he refuses. In the final movement he turns away from darkness toward the town. This suggests a possibility of continuing, not a guarantee that he is healed or that every relationship is resolved.

## Analysis
The ending combines bereavement, dependence and uncertain survival. Treat the novel’s depictions of grief and suicidal thoughts sensitively, and allow students to question the costs of Paul’s relationships for Miriam and Clara.''','0–10: follow Paul and Clara. 10–20: trace illness and caregiving. 20–30: discuss ethical uncertainty. 30–40: examine the final image. 40–50: write a cautious interpretation.','How does Paul’s relationship with Baxter change? What does the final movement suggest without proving?','https://www.litcharts.com/lit/sons-and-lovers/chapter-15')]
d['course-35:2']=[
n('portrait-1-2','A Portrait of the Artist · Chapters 1–2', '''## Chapter 1: childhood, school and politics
The novel begins with a child’s sensory impressions and a story told by his father; language and perception develop with Stephen Dedalus. At Clongowes Wood College he experiences homesickness and school hierarchies. At Christmas dinner adults argue bitterly about Charles Stewart Parnell, nationalism and the Catholic Church, introducing political conflict through a child’s incomplete understanding.

Back at school Father Dolan strikes Stephen’s hands with a pandybat after wrongly assuming he has broken his glasses to avoid work. Encouraged by classmates, Stephen appeals to the rector, who promises to speak to Dolan. The boys celebrate Stephen, though later developments complicate the apparent triumph.

## Chapter 2: family decline and first desire
The Dedalus family’s finances worsen and they move. Stephen’s schooling continues at Belvedere, where a teacher offers him a place. He encounters Emma and later acts in a school play, experiences his father’s nostalgia during a visit to Cork, and wins prize money that he spends generously but cannot make last. Desire, isolation and guilt intensify; near the chapter’s end he seeks out a sex worker.

## Technique
The third-person narration stays close to Stephen’s changing awareness, so childhood impressions and later intellectual language feel different. Avoid reducing the novel to a straightforward account of Joyce’s own life: it is shaped fiction.''','0–10: chart childhood impressions. 10–20: map the dinner argument. 20–30: explain the pandybat episode. 30–40: track family decline. 40–50: discuss changing narrative language.','Why does Stephen appeal to the rector? How does the family’s loss of money shape his development?','https://www.gutenberg.org/ebooks/4217'),
n('portrait-3-5','A Portrait of the Artist · Chapters 3–5', '''## Chapter 3: fear and confession
After the sexual experiences closing Chapter 2, Stephen is absorbed in what he understands as sin. A religious retreat includes sermons describing death, judgment and hell in vivid detail. Frightened by the possibility of damnation, he seeks confession away from school and receives communion. The chapter shows a powerful subjective religious experience; readers need not accept its theology as medical or moral fact.

## Chapter 4: priesthood and the shore
Stephen follows strict devotional routines. A priest suggests he might have a vocation, but Stephen recognises that a clerical life would confine him. As the family’s finances continue to deteriorate, he looks toward university. Near the sea he sees a girl wading, whom he perceives through bird imagery. The experience becomes for him an awakening to beauty and artistic possibility. The girl’s own perspective is not developed.

## Chapter 5: university and departure
Stephen debates language, nationality, religion and aesthetics with fellow students including Davin, Lynch and Cranly. He explains ideas of beauty and artistic form, writes a villanelle associated with Emma, and refuses his mother’s request that he perform Easter religious duties. In conversation with Cranly, he describes a wish to pursue art through independence and exile, even at the cost of isolation. Diary entries close the novel with plans to leave Ireland and an invocation of his mythic namesake Daedalus. The departure is anticipated; the ending does not narrate a completed career abroad.

## Interpretation
Stephen’s self-definition resists family, church and nationalism, yet his claims can be self-dramatising. Examine gender, class and colonial language alongside his quest for artistic freedom.''','0–10: map fear and confession. 10–20: compare priesthood and the shore. 20–30: outline the university debates. 30–40: discuss diary form and exile. 40–50: evaluate Stephen’s claims.','Why does Stephen refuse the priestly path? What changes when the narrative ends in diary form?','https://www.gradesaver.com/portrait-of-the-artist-as-a-young-man/study-guide/summary-chapter-5')]
d['course-35:3']=[
n('dalloway-day','Mrs Dalloway · Morning, the city and memory', '''## Form and context
Woolf’s 1925 novel follows one June day in post-First World War London while moving continually into memory and between minds. It is not organised into universally agreed numbered chapters: editions divide the text differently. These guides use broad narrative sequences, not invented chapter numbers.

## Flowers and public space
Clarissa Dalloway goes out to buy flowers for the evening party. London sounds, the striking clocks and chance encounters stimulate memories of her youth at Bourton, including Peter Walsh and Sally Seton. A motorcar attracts public speculation; an aeroplane writing in the sky becomes another event through which attention passes among different observers.

## Septimus and Rezia
Among those in the city are Septimus Warren Smith, a veteran distressed by his wartime experiences and visions of his dead friend Evans, and his Italian wife Lucrezia (Rezia), who is anxious and isolated. The novel moves between their experiences rather than making Rezia merely an observer of his suffering.

## Peter’s visit
Clarissa returns home and mends her dress. Peter, recently returned from India, visits unexpectedly. Their conversation activates memories of her refusal of his proposal and her marriage to Richard. The feelings between them are unresolved and contradictory; neither character supplies an unquestionable account of the past.

## Technique
Track a clock, sound or passing object as the narration shifts viewpoint. “Stream of consciousness” is a useful term, but Woolf also uses free indirect discourse and carefully structured transitions.''','0–10: map the day. 10–20: follow the flowers and car. 20–30: compare Clarissa’s and Rezia’s viewpoints. 30–40: examine the Peter visit. 40–50: explain one transition.','How does the city connect people who do not meet? Why should edition-dependent section numbering be used cautiously?','https://www.encyclopedia.com/arts/educational-magazines/mrs-dalloway'),
n('dalloway-evening','Mrs Dalloway · Doctors, afternoon and the party', '''## The doctors and private worlds
Septimus and Rezia consult Sir William Bradshaw, who proposes rest and separation from her. The novel questions a medical authority that values conformity and control; distinguish this historical fictional critique from a general rejection of modern mental-health care. Septimus’s memories and perceptions convey both distress and a rich subjective life.

Richard lunches with Lady Bruton and Hugh Whitbread, then brings Clarissa flowers, unable easily to express his love in words. Their daughter Elizabeth spends time with her tutor Miss Kilman and later travels through London. These episodes show different relations to class, religion, work and the city.

## Septimus and the party
At home Septimus and Rezia share a brief moment over a hat she is making. When Dr Holmes comes and Septimus fears loss of control and separation, he dies by suicide. Peter later hears the ambulance without knowing whose death it marks. At Clarissa’s party, Sally returns and Sir William’s wife mentions the death of a young man. Clarissa, who never met Septimus, withdraws briefly and reflects on his death and her own life, then returns to her guests; Peter’s perception of her closes the novel.

## Interpretation and care
Clarissa’s response is complex and personal, not a model for how to interpret or respond to suicide. Compare their experiences without claiming their class, suffering or choices are identical. The party can be read as a fragile act of connection as well as a display of social privilege.''','0–10: track the doctors’ power. 10–20: compare Richard, Elizabeth and Rezia. 20–30: trace the ambulance and party news. 30–40: discuss Clarissa’s response sensitively. 40–50: write about connection and difference.','How does Clarissa learn about Septimus? What do shared public sounds achieve in the novel?','https://www.litcharts.com/lit/mrs-dalloway/summary')]
d['course-35:4']=[
n('heart-beginning','The Heart of the Matter · Colonial setting and the loan', '''## The syllabus label
The unit calls Greene and Golding an “antimodernist trend.” Treat this as a topic for inquiry rather than proof that neither writer uses modern techniques. Greene’s psychological interiority and Golding’s symbolic patterning complicate a simple opposition between modernism and antimodernism.

## The colonial community
In a British West African colony during the Second World War, police officer Major Henry Scobie has a reputation for honesty. He is passed over for promotion. His wife Louise, lonely and unhappy in the expatriate community, wants to leave for South Africa. Wilson, newly arrived and drawn to Louise, is later revealed to be investigating corruption. Colonial hierarchies shape whose experiences receive attention.

## Pressure and obligation
Scobie investigates the suicide of a young official, Pemberton, whose debts trouble him. Unable to obtain a bank loan for Louise’s passage, Scobie borrows from Yusef, a Syrian trader with interests in smuggling. This creates an obligation to a person Scobie should keep at professional distance. A Portuguese ship’s captain and a letter also test Scobie’s official duties.

## Interpretation
Pity and responsibility motivate Scobie, but they can become possessive or self-deceptive. Ask whether his decisions allow other people a real choice, and how colonial power affects Ali, his longtime servant. The novel contains suicide and religious distress; handle both with care.''','0–10: map the setting and characters. 10–20: examine promotion and Louise’s departure. 20–30: trace the loan. 30–40: question pity and power. 40–50: evaluate the unit label.','Why does Scobie borrow from Yusef? Why is “antimodernist” not a complete description of technique?','https://www.gradesaver.com/the-heart-of-the-matter/study-guide/summary'),
n('heart-ending','The Heart of the Matter · Helen, Ali and the ending', '''## The affair and blackmail
After Louise leaves, survivors of a shipwreck arrive. Scobie encounters Helen Rolt, a young widow; his sympathy develops into an affair. He feels responsible for both Helen and Louise and lies to avoid hurting them. A compromising letter falls into Yusef’s hands, enabling Yusef to pressure Scobie into assisting a transaction connected with the Portuguese ship.

## Faith and suspicion
Louise returns, aware of the affair although she does not immediately confront him. Scobie’s Catholic beliefs make him feel unable to reconcile his continuing relationship with confession and communion, yet he cannot bring himself to abandon Helen. Suspecting Ali of knowledge or disloyalty, he speaks to Yusef; Yusef arranges Ali’s death. Scobie did not knowingly order the killing, but recognises his part in exposing Ali to danger.

## Death and aftermath
Feeling trapped and believing his death will release others, Scobie plans suicide so that it will appear natural. He dies after taking accumulated medication. His belief that death solves the problem is a character’s desperate judgment, not a conclusion readers must accept. Wilson notices evidence suggesting that the death was intentional; Louise later speaks to Father Rank, who cautions against assuming human beings can judge the full extent of God’s mercy.

## Critical reading
Compare pity with responsibility and control. The book’s moral questions matter, but so do the unequal voices in its colonial setting: Ali’s life must not be treated solely as a step in Scobie’s spiritual journey.''','0–10: trace the letter. 10–20: map competing obligations. 20–30: discuss Ali and colonial power. 30–40: examine the final conversation sensitively. 40–50: write about pity.','How does Yusef gain leverage? Why is Scobie’s responsibility for Ali morally complicated?','https://www.gradesaver.com/the-heart-of-the-matter/study-guide/summary'),
n('flies-1-4','Lord of the Flies · Chapters 1–4', '''## Chapter 1: The Sound of the Shell
After an aircraft crash during wartime, British schoolboys find themselves on an island without adult supervision. Ralph and Piggy discover a conch and use it to summon others. Ralph is elected chief; Jack retains leadership of the choir, who become hunters. Ralph, Jack and Simon explore and confirm they are on an island. Jack hesitates to kill a trapped pig.

## Chapter 2: Fire on the Mountain
An assembly adopts the conch as a speaking rule. A younger boy speaks fearfully of a beast. The boys light a signal fire using Piggy’s glasses, but it spreads into the forest. Afterwards the boy with the birthmark cannot be found; the text suggests, but does not explicitly show, his death.

## Chapter 3: Huts on the Beach
Ralph and Simon work on shelters while most boys abandon the task. Jack is absorbed in hunting, producing tension between meat and protection. Simon retreats to a secluded clearing, where his sensitivity to the natural world becomes apparent.

## Chapter 4: Painted Faces and Long Hair
The littluns establish routines; Roger throws stones near one child, still held back by remembered social limits. Jack paints his face and successfully hunts. The hunters let the signal fire go out just as a ship passes. Ralph confronts Jack; in the conflict Piggy is struck and one lens of his glasses is broken.

## Teaching point
Avoid reducing each boy to a single fixed symbol: Ralph enjoys the excitement of the island too, and group behaviour changes through interaction.''','0–10: draw the island and assembly. 10–20: follow the conch and fire. 20–30: compare shelter and hunting. 30–40: discuss the missing child carefully. 40–50: analyse the missed ship.','Why is the first fire both useful and dangerous? What does the text leave uncertain about the missing boy?','https://www.pearsonschoolsandfecolleges.co.uk/asset-library/pdf/Secondary/english-literature/york-notes-gcse/samples-rapid/york-notes-for-gcse-rapid-revision-lord-of-the-flies.pdf'),
n('flies-5-8','Lord of the Flies · Chapters 5–8', '''## Chapter 5: Beast from Water
Ralph calls a meeting to address shelters, sanitation and the fire, but discussion turns to fear of a beast. Simon struggles to suggest that the danger may be connected to the boys themselves. Jack challenges the assembly’s authority; fear and excitement break up the meeting.

## Chapter 6: Beast from Air
During an aerial battle a dead parachutist comes down on the mountain. Sam and Eric, tending the fire, mistake the wind-moved figure for a beast. The boys search and discover the defensible rocky place later called Castle Rock. Ralph insists on returning to the mountain and the signal fire.

## Chapter 7: Shadows and Tall Trees
On the way Ralph wounds a boar and feels the thrill of hunting. The boys’ imitation hunt becomes frighteningly rough for Robert, who plays the pig. Ralph, Jack and Roger climb the mountain in the dark, see the parachutist’s distorted form and flee.

## Chapter 8: Gift for the Darkness
Jack unsuccessfully tries to remove Ralph as chief and forms a separate group. His hunters kill a sow and leave its head on a stake as an offering. Simon, alone nearby, experiences an imagined confrontation with the fly-covered head, the “Lord of the Flies.” Its claim that the beast cannot simply be hunted points toward violence within the group, though Simon’s experience remains presented through his consciousness.

## Critical point
The term “savage” is part of the novel’s imagery, but discuss how colonial stereotypes can shape that language. The boys are British children and the adult world around them is also at war.''','0–10: trace the beast rumours. 10–20: identify the parachutist. 20–30: examine the mock hunt. 30–40: interpret Simon’s encounter. 40–50: question colonial language.','What do the boys mistake for a beast? What does the mock hunt reveal before Simon’s death?','https://www.pearsonschoolsandfecolleges.co.uk/asset-library/pdf/Secondary/english-literature/york-notes-gcse/samples-rapid/york-notes-for-gcse-rapid-revision-lord-of-the-flies.pdf'),
n('flies-9-12','Lord of the Flies · Chapters 9–12', '''## Chapter 9: A View to a Death
Simon finds the dead parachutist and realises the boys’ mistake. At Jack’s feast, a storm gathers and the group performs a hunting dance. Simon comes from the forest trying to communicate; in the frenzy the boys attack and kill him. Ralph and Piggy are among those present. The storm and tide carry bodies away.

## Chapter 10: The Shell and the Glasses
Ralph calls Simon’s death murder, while Piggy attempts to explain it as an accident and limit their responsibility. Jack consolidates power at Castle Rock. His group raids the shelters at night and steals Piggy’s glasses, taking the means of making fire.

## Chapter 11: Castle Rock
Ralph, Piggy and Samneric go to demand the glasses back. Jack’s group seizes the twins. As Piggy tries to speak with the conch, Roger releases a boulder that kills him and shatters the shell. Ralph escapes.

## Chapter 12: Cry of the Hunters
Samneric, now under Jack’s control, warn Ralph that he is to be hunted. The hunters set fire to the island to flush him out. Ralph reaches the beach and encounters a naval officer whose ship saw the smoke. The officer’s arrival stops the pursuit; Ralph weeps for the deaths and loss he has witnessed.

## Interpretation
The rescue is ironic because a destructive hunting fire summons an officer from a world itself engaged in war. The ending does not prove that violence belongs only to children or to an imagined place outside “civilisation.”''','0–10: reconstruct Simon’s discovery. 10–20: discuss participation and denial. 20–30: track glasses and conch. 30–40: analyse the officer’s arrival. 40–50: explain the ending’s irony.','Why does Ralph call Simon’s death murder? What contradiction is created by the naval officer’s arrival?','https://www.pearsonschoolsandfecolleges.co.uk/asset-library/pdf/Secondary/english-literature/york-notes-gcse/samples-rapid/york-notes-for-gcse-rapid-revision-lord-of-the-flies.pdf')]
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Wrote',sum(len(v) for k,v in d.items() if k.startswith('course-35:')),'Modern Fiction selections across 5 units')
