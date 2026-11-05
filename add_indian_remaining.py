import json
p='prepared-notes.json'; d=json.load(open(p))
def n(id,title,text,source,status=None):
 x={'id':id,'title':title,'source':source,'text':'# '+title+'\nIndian Writing in English I · Semester 4\n\n'+text+'\n\nTeaching draft: compare the assigned text and edition before class.'}
 if status:x['status']=status
 return x
d['course-23:2']=[
n('intrusion','Shashi Deshpande · The Intrusion','''## Content note and approach
The story concerns sexual violence within marriage. Offer students a choice about how they engage with sensitive passages, and do not ask anyone to share personal experience. Marriage is not consent; the narrator’s reluctance and resistance matter.

## Story in sequence
A newly married couple travel through a fishing village to a secluded place overlooking the sea. The unnamed woman narrates. She and her husband barely know each other, and she is uneasy about being alone with him. He welcomes the privacy of their honeymoon, while she wants time, conversation and familiarity.

His embraces make her uncomfortable. She tries to create distance, moves toward the veranda and wishes they might become friends. When she resists his attempt to kiss her, he reacts with anger. She says they do not know each other, hoping to explain her desire to talk, but finds it difficult to continue. He turns away, and she experiences both guilt and temporary relief.

Later she wakes from a dreamlike perception of the sea to find him forcing himself on her. Frightened and unable to push him away, she experiences the act as an intrusion into her bodily and personal privacy. Afterwards he sleeps while she is left with the humiliation and loss of control. The contrast between the sea’s imagined force and her husband’s actions makes the difference between being physically hurt and being violated by another person painfully clear.

## Interpretation
First-person narration brings the reader close to the woman’s shifting sensations and limited opportunities to speak. The secluded room is “private” for the husband but does not protect her autonomy. Analyse her silence and attempts to resist without implying that a victim must say or do a particular thing for a violation to count.

## 50-minute lesson
0–10: set content-sensitive discussion boundaries. 10–22: map the couple’s different expectations. 22–32: identify moments of resistance and interruption. 32–42: discuss the sea and the meaning of privacy. 42–50: write an evidence-based response without graphic detail.

## Questions
Why does the narrator seek conversation? How does “privacy” mean different things to the two characters? How does the sea image change by the end?''','https://jdsgcollege.edu.in/wp-content/uploads/2025/07/SLM.pdf'),
n('agnostic','Khushwant Singh · The Agnostic','''## Story overview
A family’s visitor declares his scepticism about God in conversation with his hostess. She believes in God and is distressed at the thought that his arguments might influence her children. Their exchange becomes spirited: the adults appeal to contrasting beliefs and literary or religious language, while the children find the dispute entertaining. The visitor questions received faith, and the hostess defends it.

The next day, during an outing, a child’s ball becomes stuck in a tree. The visitor offers a test: if God brings the ball down and he catches it, he will believe. A breeze dislodges it and the ball comes down to him. His apparent change of position delights the hostess, bringing the dispute to a comic close.

## Interpretation and uncertainty
The event has an ordinary physical explanation as well as the meaning the participants may attach to it. A reader can ask whether the visitor’s response is sincere, playful, a concession or a comment on how people interpret coincidence. The ending need not prove that the story establishes or disproves God’s existence. Agnosticism concerns uncertainty about what can be known; it should not automatically be equated with certainty that no deity exists.

## 50-minute lesson
0–10: distinguish belief, disbelief and uncertainty. 10–20: identify the speakers’ positions. 20–30: trace the ball incident. 30–40: debate the effect of a comic coincidence. 40–50: write a response acknowledging more than one reading.

## Questions
Why is the hostess worried? What test does the visitor suggest? Why can the same event support different interpretations?''','http://rereadinglives.blogspot.com/2014/01/agnostic-by-khushwant-singh-1963-seven.html'),
n('transplanted','Rita Nath Keshari · The Transplanted Wife — unverified selection','''## Important: prescribed selection not yet identified
The syllabus lists “The Transplanted Wife” under short stories. Bibliographic information also identifies The Transplanted Wife as a collection of short stories. The particular story or stories assigned and their plots have not been verified. This is not a summary of the work, and no characters or ending should be inferred from its title.

## How to prepare once the assigned text is available
Confirm the exact story title, author, collection and edition with the course reading list. Record the narrator, setting, main characters, sequence of events and ending directly from the text. Then examine how the title relates to the story; treat ideas about marriage, movement or belonging as questions to test, not as established themes.

## Interim 50-minute lesson
0–10: identify the title and edition. 10–25: read the selected story. 25–35: create a factual event sequence. 35–45: distinguish a claim about the text from an inference. 45–50: note details requiring a second reading.

## Questions
Which story is assigned from the collection? Who tells it? What evidence supports your interpretation?''','https://www.amazon.in/Shadows-June-Rita-Nath-Keshari/dp/8172736797','preliminary'),
n('laburnum','Temsula Ao · Laburnum for My Head','''## Story in sequence
Lentina loves the yellow blossoms of the laburnum and repeatedly tries to grow one in her garden, but her efforts do not succeed. Her attachment becomes a persistent, private desire rather than a passing taste. After her husband’s death, a visit to the cemetery gives her an idea: she wants a laburnum to grow at her own grave instead of an imposing headstone.

With the help of her trusted driver Babu, Lentina explores how to secure a burial place and eventually arranges land for a new cemetery. The arrangements favour flowering trees rather than conventional headstones, linking her personal wish with a space others can use. Babu helps care for the tree. In time it blossoms; Lentina sees her wish realised before her death. Thereafter the golden tree flowers above her burial place.

## Interpretation
The recurring flowers connect individual desire, death and continuing life without requiring a single fixed symbolism. Lentina’s planning lets her express a preference about how she will be remembered. Ask how resources and social connections make her plan possible, and how Babu’s labour contributes to it. The title story is part of a collection with the same title; the course edition should be checked to confirm whether other stories are also assigned.

## 50-minute lesson
0–10: distinguish a story from a collection. 10–22: trace garden, cemetery and tree. 22–32: examine Lentina’s decisions and Babu’s role. 32–42: discuss flowers and memorials. 42–50: write how the ending changes the opening desire.

## Questions
Why does Lentina want a tree by her grave? Who helps make it possible? How can the blossoms function as a memorial?''','https://www.penguin.co.in/book/laburnum-for-my-head/')]
d['course-23:3']=[
n('village-sea','Anita Desai · The Village by the Sea','''## Setting and beginning
In the coastal village of Thul, Lila and her brother Hari help hold their family together. Their mother is seriously ill, their father drinks heavily, and their younger sisters Bela and Kamal need care. Lila takes on domestic work while Hari seeks ways to earn money. News of possible industrial development raises hopes of employment as well as questions about changes to the village.

## Two parallel journeys
The wealthy De Silva family visits its nearby holiday home. The children earn some money by helping them. Hoping to find work, Hari travels to Bombay, where the unfamiliar city is frightening and overwhelming. The De Silvas are not available when he first seeks them out, but a watchman helps him find Jagu, proprietor of the Sri Krishna Eating House. Hari works there under difficult conditions, gradually forming connections.

Nearby watch repairer Mr Panwallah teaches Hari about watches and the need to adapt to changing circumstances. Hari learns a practical skill and begins to imagine a way to earn a living at home. In Thul, meanwhile, Lila cares for her sisters and mother and receives help from the De Silvas, who assist in getting her mother hospital treatment. Hari’s father is shaken by his wife’s illness and begins to stop drinking and care for her.

## Return and ending
Hari eventually returns to Thul, bringing savings, skills and ideas, including watch repair and raising poultry. His family’s circumstances have improved, though change remains ahead. A visiting birdwatcher, Mr Ali, talks about adaptation. At a village celebration, Hari sees his recovering mother among women at the sea and calls Lila’s attention to her. The hopeful reunion is not a claim that poverty or environmental uncertainty have disappeared.

## Interpretation and lesson
The novel balances unequal access to wealth with acts of assistance and children’s resourcefulness. Discuss how Lila’s labour differs from Hari’s visible journey, and how industrialisation can create both work and disruption. In 50 minutes: 0–10 map family responsibilities; 10–22 compare Thul and Bombay; 22–32 trace Lila’s care and Hari’s learning; 32–42 examine adaptation; 42–50 write a qualified account of the ending.

## Questions
Why does Hari leave? What work does Lila do in his absence? How does the idea of adaptation connect the watchmaker and the birdwatcher?

This is a story overview, not a full chapter-by-chapter guide.''','https://www.supersummary.com/the-village-by-the-sea/summary/'),
n('rich-like-us','Nayantara Sahgal · Rich Like Us','''## Context and structure
The 1985 novel moves between the Emergency in India (1975–77) and earlier family and political histories. It centres on Sonali, an Indian civil servant, and Rose, an Englishwoman married into an Indian business family. Their different experiences allow the novel to connect public power with private relationships. Its accounts of political violence and coerced sterilisation should be situated historically and checked against independent sources.

## Narrative overview
Sonali has built a career in the civil service and is committed to professional judgment. As the Emergency changes the political climate, she faces pressure connected with commercial interests and is removed from her senior position. Her colleague Ravi Kachru adapts more successfully to the new order. Sonali reflects on what career, principle and loyalty mean in a system where proximity to power can determine outcomes.

Rose’s story reaches back to her life in England and her marriage to Ram, an Indian businessman already married to Mona. Rose must negotiate an unconventional household, cultural difference and an insecure legal and social position. Her relationship with Mona cannot be reduced to a simple rivalry; affection and tension coexist. When Ram becomes incapacitated, his son Dev’s pursuit of money and influence leaves Rose particularly vulnerable.

As the narrative returns to the Emergency, Dev becomes associated with opportunism and intimidation. Rose resists his behaviour and is eventually killed; the circumstances are made to resemble a different account. Sonali tries to understand Rose’s fate and the networks of power around it. Family documents and memories concerning the historical practice of sati also enter Sonali’s reflections, connecting violence against women across different periods without making those situations identical.

## Interpretation and lesson
The title invites scrutiny of wealth and privilege: who is protected by prosperity and who bears its costs? Compare official language about order with the experiences of those subjected to coercion. In 50 minutes: 0–10 establish the Emergency timeline; 10–22 map Rose’s household; 22–32 trace Sonali’s career; 32–42 compare public and domestic power; 42–50 write a claim about the title.

## Questions
Why is Rose’s household position precarious? How do Sonali and Ravi respond differently to political power? Why does the novel move between present and past?

This is an overview rather than a chapter-by-chapter account.''','https://www.the-criterion.com/nayantara-sahgals-rich-like-us-a-thematic-analysis/'),
n('terrible-matriarchy','Easterine Kire · A Terrible Matriarchy','''## Context and narrative focus
This 2007 coming-of-age novel follows Dielieno, often called Lieno, in an Angami Naga family. It explores gender, generations, kinship and education. Its portrayal of one family must not be treated as a complete account of all Naga communities or all traditions.

## Story overview
As a young child, Lieno notices that her grandmother Vibano gives boys preferred treatment, including better portions of food. The seemingly ordinary meal reveals an unequal hierarchy of value. Vibano takes Lieno into her household, intending to train her in the duties she believes a girl and future wife should perform. The child misses the relative warmth of her parents and brothers and struggles with her grandmother’s strict expectations.

Growing up, Lieno sees how women’s domestic labour and access to schooling are judged differently from boys’. She questions the rules while also depending on family members for support. Her mother and other relatives offer perspectives that complicate the idea that every older person or every woman holds the same view. Education becomes one important way Lieno imagines a life beyond the restrictions imposed on her.

Family conflicts, illness and losses continue as Lieno matures. The grandmother’s history helps explain the insecurity and property relations behind her preference for sons, but it does not erase the harm she does. Lieno’s later choices show care for relatives as well as resistance to unequal expectations. The family’s relationships remain complex rather than dividing neatly into wholly good and wholly bad characters.

## Interpretation and lesson
The title is ironic: an older woman has authority in the household while enforcing values that favour men. Ask how the distribution of food makes hierarchy visible and how a child narrator’s understanding changes over time. In 50 minutes: 0–10 compare what characters receive at meals; 10–22 map the household; 22–32 discuss schooling; 32–42 distinguish explanation from excuse; 42–50 write about the title’s irony.

## Questions
Why does the opening food division matter? How can a matriarch reinforce a patriarchal system? How does Lieno’s view change as she grows?

This is an introductory overview; detailed chapter and ending explanations still need preparation.''','https://www.granthaalayahpublication.org/Arts-Journal/ShodhKosh/article/download/6006/5467/31366'),
n('countdown','Amitav Ghosh · Countdown','''## Context
Published in 1999, Countdown is nonfiction responding to the nuclear tests conducted by India and Pakistan in 1998. Ghosh combines travel, observation, interviews and political reflection. Its accounts are situated in that historical moment; contemporary nuclear policy and figures must be checked separately.

## Main concerns
Ghosh speaks with people holding different positions on the tests and travels through places connected with security and its consequences. Rather than presenting nuclear weapons only as technical objects, he examines the stories nations tell about prestige, security and power. Interviews and encounters place official arguments beside anxieties about conflict and the lives of ordinary people.

The work asks how nuclear competition is understood in a region shaped by colonial history, Partition and recurrent hostility. It also questions the distance between abstract claims about national strength and the human consequences of possible nuclear war. Different interviewees’ opinions should be attributed to them; they are not automatically all Ghosh’s own conclusions or verified facts.

## Critical reading
The travel-and-interview form makes political debate concrete, but selection and arrangement still shape a reader’s response. Compare claims about deterrence and security with Ghosh’s concerns about escalation, human vulnerability and the distribution of public resources. Avoid treating either position as a substitute for independent evidence.

## 50-minute lesson
0–10: place the tests on a 1998 timeline. 10–22: identify argument and reported voices in an assigned passage. 22–32: map prestige, deterrence and risk. 32–42: assess how travel writing shapes political argument. 42–50: formulate a question requiring independent evidence.

## Questions
Why use interviews rather than a single policy statement? How can an account distinguish security claims from observed consequences? What does the 1998 context contribute?

This is an introductory guide; verify the prescribed selection and the full sequence of encounters.''','https://books.google.co.uk/books/about/Countdown.html?id=XTQriV-f1f4C&redir_esc=y'),
n('greater-common-good','Arundhati Roy · The Greater Common Good','''## Context and purpose
Roy’s 1999 essay is an advocacy intervention in debates about large dams, especially the Sardar Sarovar project in the Narmada valley. It combines personal observation, argument, reported testimony and claims about policy. It is a source for Roy’s position at that time, not a neutral or automatically current account of every project outcome.

## Main argument
Roy asks who pays for projects justified as serving a “greater common good” and who receives their benefits. She draws attention to people facing displacement, including Adivasi and other marginalised communities, and argues that loss of land, livelihood, social ties and place cannot be measured only by a compensation figure. She questions whether resettlement can provide adequate land and sustain communities.

She also disputes official estimates and promises about costs, irrigation and development. Her essay relates the issue to the Narmada Bachao Andolan and to decision-making by governments, courts and funding institutions. Her forceful comparisons and rhetorical questions are part of an attempt to make readers confront unequal power and the people hidden by aggregate benefits.

## Critical reading
Attribute numbers and allegations to their sources and dates; estimates and later project outcomes are contested and require independent verification. Supporters emphasise water, irrigation and electricity, while opponents dispute the distribution and costs of those benefits. A strong discussion can compare evidence for both without treating displacement as an abstract arithmetic problem or assuming that one passage resolves every technical question.

## 50-minute lesson
0–10: identify a development decision and its stakeholders. 10–22: map Roy’s claims about displacement and benefits. 22–32: distinguish a reported figure from its source. 32–42: compare competing arguments and missing evidence. 42–50: write a qualified response to the title.

## Questions
Who does Roy argue bears the costs? Why is resettlement more than cash compensation? How does the essay use rhetoric alongside evidence?''','https://web.cecs.pdx.edu/~sheard/course/Design&Society/Readings/Narmada/greatercommongood.pdf')]
d['course-23:4']=[
n('harvest','Manjula Padmanabhan · Harvest','''## Setting and content
This dystopian play imagines a future in which wealthy recipients acquire body parts from poorer people through a company. It includes coercive medical procedures, reproductive coercion and a character’s threat of self-harm; discuss these elements sensitively. The fictional system should not be confused with ethical, voluntary organ donation in real life.

## Action in sequence
Om, unemployed and living with his wife Jaya and mother Ma in a cramped Mumbai room, enters a contract with InterPlanta to supply organs. The company brings material comforts but also invasive rules, sanitation measures and surveillance. A screen-like contact module presents Ginni, the apparent recipient, who monitors the household and dictates how its members should live. Jaya is alarmed by the loss of autonomy; Om and Ma respond differently to the promised security.

Om’s brother Jeetu, who has a complicated relationship with Jaya and the household, returns. The guards take Jeetu rather than Om and remove his eyes. He comes back distressed and dependent on a technological device. What appears to be a mistaken substitution raises the question of how much control the family ever had. Jeetu is later taken again, and Om leaves the household in pursuit of the donor relationship. Ma increasingly retreats into a technologically mediated world of entertainment.

At the end, Jaya is alone and encounters Virgil through the contact system. He reveals that Ginni was an image and claims a relationship to Jeetu’s body; the play’s mediated presentation makes the nature of that transformation open to interpretation. Virgil wants Jaya to bear his child through a procedure arranged by the company. She refuses to surrender control on those terms, insists that he come to her in person, and threatens to take her own life if the guards force the issue. Her statement is a desperate tactic within the fictional coercive situation, not an instruction or model for real life. The confrontation ends without an assured solution to the system’s power.

## Interpretation and staging
Food, housing and entertainment arrive as inducements alongside control. The screen and the absent receiver make distance and surveillance visible onstage. Jaya’s resistance matters, yet its costs complicate any simple celebration of victory. Examine economic inequality and gender together; neither poverty nor identity alone makes exploitation inevitable.

## 50-minute lesson
0–10: distinguish fictional coercion from ethical donation. 10–22: map the contract’s benefits and costs. 22–32: trace changing control of the room. 32–42: analyse screen presence and Jaya’s final demand. 42–50: write a claim about the unresolved ending.

## Questions
How do gifts become instruments of surveillance? Why is Jeetu’s treatment significant? What does Jaya demand at the end?

This is an action overview, not a complete scene-by-scene guide.''','https://www.thebeacon.in/2022/10/22/pooja-sancheti-reading-manjula-padmanabhans-harvest-in-2022/'),
n('dreams-tipu','Girish Karnad · The Dreams of Tipu Sultan','''## Context and form
Karnad’s historical play uses Tipu Sultan’s recorded dreams and the politics of writing history to revisit the ruler of Mysore’s final years and death in 1799. The play was first produced in 1997; check the publication and language of the assigned edition rather than treating all dates as equivalent. A play based on historical documents can imaginatively reshape events and should not be used as the sole authority for historical claims.

## Dramatic framework and action
After Tipu’s defeat and death at Seringapatam, the court historian Kirmani and British scholar-officer Colin Mackenzie discuss an account of his life. Their positions differ: one has personal ties and memories, while the other is connected with the victorious colonial power and its interest in recording its opponent. Their conversation frames scenes that move back into Tipu’s political and military world.

The play interweaves conflict, diplomacy and court life with dreams attributed to Tipu. These dreams make ambitions, anxieties and images of power dramatically visible. They are not simply predictions that the audience must accept as factual prophecy. The historical conflict with the East India Company and other regional powers leads toward the fall of Seringapatam and Tipu’s death; the frame returns attention to those who will record and interpret his defeat.

## Interpretation
Ask who controls the archive, what a conqueror may want from a history of an enemy and how a remembered person differs from a figure in official accounts. The dreams add another kind of evidence, but staging, selection and interpretation remain the playwright’s choices. Tipu’s historical legacy is disputed; evaluate differing historical claims against evidence rather than turning the play into a complete verdict.

## 50-minute lesson
0–10: distinguish history from historical drama. 10–22: map the frame and shifts in time. 22–32: compare Kirmani’s and Mackenzie’s positions. 32–42: analyse one assigned dream as a theatrical device. 42–50: write what an archive can reveal and what it cannot settle.

## Questions
Why frame Tipu’s story through historians after his death? How do dreams affect the audience’s understanding? Why should a dramatic portrayal be compared with other historical sources?

This is an introductory overview, not a full scene-by-scene explanation.''','https://timesofindia.indiatimes.com/entertainment/kannada/theatre/the-dreams-of-tipu-sultan-is-now-available-online/articleshow/76492936.cms')]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added Indian Writing in English I Units III–V: 11 selections including one preliminary')
