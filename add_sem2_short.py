import json
p='prepared-notes.json';d=json.load(open(p))
def n(id,title,source,text,status=None):
 x=dict(id=id,title=title,source=source,text=text)
 if status:x['status']=status
 return x
d['course-8:4']=[
n('wells-ants','H. G. Wells · The Empire of the Ants','https://standardebooks.org/ebooks/h-g-wells/short-fiction/text/the-empire-of-the-ants','''# The Empire of the Ants
H. G. Wells · English Literature II · Semester 2, Unit 5

## Introduction
First published in 1905, Wells’s short story imagines an organised species of ants threatening human settlement in the Amazon region. Its speculative premise questions the assumption that human dominance over nature is permanent. Do not confuse the story with later films that use its title but change the plot.

## Detailed story
1. Captain Gerilleau commands the Brazilian gunboat Benjamin Constant and has orders to travel upriver to help the settlement of Badama against an alarming outbreak of ants. The English engineer Holroyd accompanies the expedition. Gerilleau is initially inclined to think of ant incursions as natural troubles that eventually pass; reports suggest this outbreak is different.
2. The journey through the forest makes human settlements seem isolated within a vast environment. Holroyd reflects on the relative fragility of human occupation. Reports describe ants that remain in places they have occupied, attack effectively and appear organised. The crew’s apprehension grows as rumours and observation meet.
3. They encounter a vessel, a cuberta, apparently abandoned on the river. A boarding party investigates and finds the consequences of an attack. Lieutenant da Cunha is bitten or stung by the ants; he becomes seriously ill and dies, apparently from their poison. The scene transforms an alarming report into an immediate danger for the crew.
4. The crew destroys the abandoned craft and reaches Badama. The settlement is deserted and shows signs of the ants’ occupation. The crew is unwilling to land and face the threat directly. Gerilleau fires the gunboat’s large gun at the settlement, but the action offers no convincing solution. He withdraws downstream to seek further instructions.
5. The concluding frame presents Holroyd’s continuing concern that the ants may spread and challenge human control. It is a warning and speculation, not a completed account of ants conquering the whole world. The expedition ends without clearly defeating the threat.

## Themes and technique
The ants are a speculative rival whose apparent organisation and possible tool use disturb easy distinctions between human and animal intelligence. The story questions confidence in technology: a gunboat’s cannon cannot easily solve the problem. The Amazon setting is filtered through European and colonial perspectives; discuss how people and landscape are represented rather than accepting those assumptions uncritically. Narrative distance and an open future make the threat larger than the witnessed events.

## Characters and questions
Gerilleau confronts a threat for which familiar habits offer no clear plan; Holroyd becomes increasingly alert to the implications. Ask: How does the upriver journey alter the crew’s understanding? What does the abandoned boat establish? Why is the cannon inadequate? What does the unresolved ending suggest about human control?

## 50-minute lesson
0–10: discuss an assumption about human superiority. 10–25: map the expedition and its encounters. 25–35: compare Gerilleau’s and Holroyd’s responses. 35–45: analyse the ending as warning rather than completed conquest. 45–50: exit ticket on one piece of evidence.

## Reading note
The linked Standard Ebooks edition provides the complete story. Check the spelling of names and sequence against the course edition.'''),
n('greene-party','Graham Greene · The End of the Party','https://www.enotes.com/topics/graham-greene/questions/please-submit-an-analysis-end-party-by-graham-1279790','''# The End of the Party
Graham Greene · English Literature II · Semester 2, Unit 5

## Overview and content note
Greene’s psychological short story follows twins Peter and Francis Morton as they face a children’s party. Francis is intensely afraid of darkness, and the anticipated game of hide-and-seek becomes a source of mounting dread. The story ends with a child’s death; its treatment of fear deserves sensitivity.

## Detailed story
1. Francis wakes from a frightening dream and dreads the party to be held by Mrs Henne-Falcon. The twins are unusually close, and Peter understands that Francis’s fear is more serious than ordinary reluctance. Francis remembers the discomfort and humiliation of the previous party, especially the game played in the dark.
2. Francis tries to avoid attending, and Peter attempts to help him. The adults do not appreciate the full intensity of his fear and the boys are sent to the event. The approaching evening makes ordinary surroundings threatening from Francis’s perspective.
3. At the party the children play various games. The approaching hide-and-seek remains in Francis’s mind even while other activities continue. Peter tries to protect him and to prevent or change the game, but other children insist. The contrast between the party’s cheerful social purpose and Francis’s terror creates dramatic tension.
4. For hide-and-seek, the lights are extinguished. Francis hides alone, overwhelmed by the darkness. Peter seeks his brother and, because of their close connection, finds him. Peter reaches out and touches him in an attempt to offer comfort; in the darkness Francis cannot experience the gesture in the reassuring way Peter intends.
5. When the lights return, Francis is found dead. Peter remains beside his brother, struggling to understand a loss that is both emotional and bound up with their sense of being twins. The story presents an extreme fictional outcome; do not treat it as a general medical claim that fear routinely causes death, or claim a medically confirmed diagnosis not established by the text.

## Characters, form and themes
Francis’s perspective makes fear vivid and shows how an adult may underestimate a child’s experience. Peter’s protectiveness is sincere but cannot remove the danger. The twins’ resemblance and emotional closeness create a double or mirror motif. Darkness, dreams and foreshadowing give the story Gothic elements. The gap between intended comfort and experienced terror makes the ending especially painful.

## Classroom discussion
How does Greene build anticipation before the game begins? Why do the twins’ different responses matter? How do party games become frightening rather than harmless? What do adults and other children fail to notice? Why should the final touch be interpreted in context rather than as deliberate harm?

## 50-minute lesson
0–10: distinguish a character’s fear from an outside observer’s judgement. 10–25: trace the sequence from dream to party. 25–35: examine darkness and foreshadowing. 35–45: discuss Peter’s intentions and the twins’ bond. 45–50: students write a brief evidence-based interpretation.

## Reading note
Read the complete story in a licensed course edition. The linked critical discussion is a secondary interpretation; check details and wording against the prescribed text.'''),
n('amis-heavy','Martin Amis · Heavy Water — preliminary outline','https://mg.co.za/article/1999-01-08-gimmicky-amis-not-at-his-best/','''# Heavy Water — preliminary outline, not yet a full story summary
Martin Amis · English Literature II · Semester 2, Unit 5

## Important limitation
This is an initial teaching outline only. The full sequence and ending have not yet been checked against the assigned edition, so they are deliberately not supplied. Read the story in the authorised collection before teaching or relying on a plot summary. The title story was revised for the later collection, so edition differences may matter.

## Verified starting point
The story concerns an ageing working-class mother and her adult son John on a cruise. The confined holiday setting brings their caring relationship into contact with other passengers and their reactions. A review of the revised story describes changes between versions, including the background of John’s father. Avoid transferring details from one version to another without checking.

## Questions to guide reading
1. How is the mother’s perspective represented, and what does it reveal and conceal about John’s own experience?
2. How do other passengers respond to the pair? What assumptions shape their reactions?
3. How do care, fatigue, social exclusion and control interact?
4. What does the cruise setting contribute to the story’s social criticism?
5. Which details and ending appear in the edition assigned by the department?

## Teaching caution
Use respectful, current language when discussing disability. Distinguish a character’s attitudes from the author’s narrative choices and do not assume that disability makes a person’s thoughts or agency inaccessible. The linked review supplies background, not a substitute for the story.''','preliminary')]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
