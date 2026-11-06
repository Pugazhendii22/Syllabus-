import json
P='prepared-notes.json'
with open(P,encoding='utf-8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source):
 return {'id':id,'title':title,'source':source,'text':f'# {title}\nModern Drama · Semester 6\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: check the assigned edition, translation and stage directions; performance choices and interpretations may differ.'}
d['course-34:0']=[
n('theatre-context','Modern and postwar theatre: a working map', '''## The syllabus spans several periods
Modern British, Irish, European and American drama includes works before as well as after the Second World War. Wilde’s The Importance of Being Earnest and Shaw’s Arms and the Man belong to the 1890s; Eliot’s Murder in the Cathedral is from the 1930s. Do not call all the prescribed plays postwar simply because the unit asks about postwar theatre.

Realist and naturalist drama developed domestic settings, social pressures and psychologically motivated conflict; symbolism and verse drama explored other ways of presenting inner or spiritual experience. After 1945, theatre responded in diverse ways to war, reconstruction, class, empire and social change. British “kitchen-sink” drama is often linked with Osborne’s Look Back in Anger; American theatre includes Miller’s critique of success and family life. These labels identify tendencies, not total national styles.

## Epic theatre
Brecht developed epic theatre before and after the war. Narration, songs, visible theatrical devices, episodic scenes and direct address can encourage critical distance, often called the alienation or defamiliarisation effect. The aim is not to prevent all feeling, but to invite audiences to question social arrangements and imagine alternatives. The Caucasian Chalk Circle links a custody story with a land dispute through this theatrical method.

## Theatre of the Absurd
Critic Martin Esslin used the term for diverse plays that challenge conventional plot, stable meaning and communication. It was not a formally unified group speaking with one voice. In Beckett’s Waiting for Godot, repetition, pauses and contradictory memories coexist with physical comedy and companionship; uncertainty need not mean that “nothing matters.”

## Performance lens
For any play ask: what can an audience see and hear, who controls space, how do pauses or props matter, and what effect might a different staging produce?''','0–10: place the plays on a timeline. 10–20: distinguish realism, verse drama and epic theatre. 20–30: compare a narrator and direct address. 30–40: explore repetition in absurd drama. 40–50: state one limit of a label.','Why are not all these plays postwar? How does Brechtian distance differ from simply removing emotion?','https://www.britannica.com/art/Western-theatre/Post-World-War-II-theatre')]
d['course-34:1']=[
n('murder-cathedral','T. S. Eliot · Murder in the Cathedral', '''## Setting and structure
Eliot’s verse drama reimagines the 1170 murder of Archbishop Thomas Becket in Canterbury. It has two parts separated by an interlude. The women of Canterbury form a chorus, giving collective voice to fear and, later, witness. The play is an interpretation of history, not a substitute for independent historical evidence.

## Part I: return and temptation
After exile, Thomas returns amid tension with King Henry II. Priests and the chorus debate what his return will bring. Four tempters offer pleasure, political office, an alliance with barons and finally the glory of martyrdom. The fourth is hardest: Thomas must reject the desire to die for personal pride or fame while remaining faithful to what he understands as his duty.

## Interlude and Part II
In a Christmas sermon Thomas reflects on celebration, sacrifice and the nature of martyrdom. On 29 December four knights confront him. Priests urge him to escape and eventually bring him into the cathedral. He refuses to turn it into a fortress; the doors are opened, and the knights kill him. The knights then directly address the audience with arguments justifying their act. Their defence is a dramatic perspective to examine, not an objective verdict. Priests and chorus respond to the death.

## Performance and themes
Verse, chant, chorus and sudden prose addresses connect spiritual conflict to public theatre. Discuss church and state, motive versus outward action, and the ordinary people who bear the consequences of political violence.''','0–10: map the historical conflict. 10–20: compare the four temptations. 20–30: discuss the sermon. 30–40: stage the knights’ audience address. 40–50: assess its effect.','Why is the fourth temptation distinct? What does the chorus contribute that Thomas’s speeches do not?','https://www.gradesaver.com/murder-in-the-cathedral/study-guide/summary'),
n('godot','Samuel Beckett · Waiting for Godot', '''## Act I
Vladimir and Estragon meet by a tree and wait for Godot. They talk, quarrel, consider leaving or hanging themselves, and pass time with routines involving boots and hats. Pozzo arrives leading Lucky by a rope, demonstrates his authority and orders Lucky to dance and then think; Lucky’s long fragmented speech ends when the others stop him. After Pozzo and Lucky depart, a boy reports that Godot will not come today but will come tomorrow. The pair say they will leave, but the stage direction has them remain.

## Act II
The pattern recurs with differences: the tree has leaves; the men’s memories are uncertain. Pozzo returns blind, accompanied by Lucky, now mute. After they fall, helping becomes a confused collective struggle. Pozzo denies or cannot recall meeting the pair earlier. A boy again brings a postponement; whether he is the same boy is not firmly established by the play. The pair contemplate departure and again do not move.

## How to read and stage it
Repetition is not identical: changing bodies, a tree and uncertain memory matter. The rope makes unequal power visible, while dependence complicates the relationship. Humour, affection, suffering and philosophical uncertainty coexist. Godot’s identity is never definitively explained; it is not correct to say the play proves he is God. Consider how silence, timing and physical action create meaning beyond the words.''','0–10: reconstruct Act I. 10–20: list differences in Act II. 20–30: stage a short silent waiting exercise. 30–40: discuss power and dependence. 40–50: defend an interpretation without fixing Godot’s identity.','What changes between the acts? Why is “Godot is definitely God” not a settled answer?','https://interestingliterature.com/2021/06/beckett-waiting-for-godot-summary-analysis/')]
d['course-34:2']=[
n('arms-man','George Bernard Shaw · Arms and the Man', '''## Act I
During the Serbo-Bulgarian War, Raina admires her fiancé Sergius’s apparently heroic cavalry charge. A fleeing Swiss professional soldier fighting for Serbia, Captain Bluntschli, climbs into her room. He carries chocolate rather than extra cartridges and offers a practical view of war. Raina hides him from pursuers; with Catherine’s help he eventually escapes wearing Major Petkoff’s old coat.

## Act II
The war has ended. Petkoff and Sergius return; Sergius is frustrated with military advancement. His and Raina’s highly romantic exchange contrasts with his flirtation with Louka, the servant. Bluntschli returns to give back the coat, risking exposure of the earlier secret. The men welcome his help with military logistics, while Raina’s feelings grow more complicated.

## Act III
Bluntschli handles practical orders; Raina reveals that she had placed an inscribed photograph in the coat. Louka tells Sergius about the hidden soldier, and a proposed duel dissolves as the romantic misunderstandings unravel. Petkoff finds the photograph, although Raina briefly removes it from the coat. Nicola relinquishes his claim to Louka; Sergius and Louka become engaged. Bluntschli and Raina also agree to marry after his age and inherited wealth are clarified.

## Interpretation
Shaw contrasts glamorous heroic poses with survival, logistics and social reality. Yet practical Bluntschli’s wealth also helps make the marriage acceptable, which complicates a simple victory over class. Examine Louka’s agency and the limits imposed by service.''','0–10: contrast heroic and practical descriptions. 10–20: reconstruct the coat’s journey. 20–30: examine Louka and class. 30–40: stage a confrontation. 40–50: discuss comedy and war.','Why is chocolate important? Does the ending fully escape class and money?','https://www.cliffsnotes.com/literature/a/arms-and-the-man/summary-and-analysis/act-iii'),
n('chalk-circle','Bertolt Brecht · The Caucasian Chalk Circle', '''## Prologue and frame
Two groups dispute use of a valley after wartime displacement. Their debate about who should work the land introduces a sung story that tests possession against socially useful care. Editions and productions may vary in their treatment of the prologue and names.

## Governor’s child and Grusha’s flight
After a coup, Governor Georgi Abashwili is killed and his wife Natella flees, leaving the child Michael behind amid the chaos. The servant Grusha, initially hesitant and aware of the danger, takes the child and carries him through a dangerous journey, including a precarious bridge. She seeks shelter with her brother and later enters a marriage of convenience to provide the child with a household. Her fiancé Simon’s return complicates their relationship when he sees her with a child and husband.

## Azdak and the test
A parallel strand follows village scribe Azdak, unexpectedly made judge during political turmoil. His decisions are irregular and often favour poor people, though his methods are also open to criticism. When Natella seeks Michael, partly to secure his inheritance, a custody case brings the stories together. Azdak orders the child placed in a chalk circle and tells both women to pull. Natella pulls; Grusha lets go rather than hurt Michael. Azdak awards the child to Grusha, disposes of the estate for public use, and in the same proceeding signs a divorce that frees her from her marriage. Azdak later disappears.

## Epic method
The singer, songs and episodic structure make the action openly theatrical. The closing principle favours those who care for or productively use things, but ask whether the play’s stylised test is a sufficient model for real custody decisions. Its relation to earlier Chinese and biblical stories can be explored without treating the plots as identical.''','0–10: map the land dispute. 10–20: follow Grusha’s choices. 20–30: introduce Azdak. 30–40: stage and question the chalk test. 40–50: connect form and social argument.','How do the valley and child disputes correspond? What makes Azdak’s justice both attractive and problematic?','https://www.gradesaver.com/the-caucasian-chalk-circle/study-guide/summary-act-five')]
d['course-34:3']=[
n('look-back-anger','John Osborne · Look Back in Anger', '''## Act I
Jimmy Porter, his wife Alison and their friend Cliff share a cramped room. Jimmy’s verbal attacks on class, politics and Alison punctuate an ordinary Sunday. Rough play between Jimmy and Cliff upsets the ironing board and Alison burns her arm. Alison privately tells Cliff she is pregnant but has not told Jimmy. Jimmy and Alison’s affectionate bear-and-squirrel game offers a temporary refuge from conflict. News that Alison’s friend Helena will visit provokes Jimmy’s hostility; he cruelly imagines Alison suffering the loss of a child.

## Act II
Helena learns more about the marriage and contacts Alison’s father, Colonel Redfern. Jimmy recalls watching his father die from wounds connected with the Spanish Civil War. When Hugh’s mother, who helped him financially, is dying, Jimmy asks Alison to accompany him; she goes to church with Helena instead. Alison leaves with her father. Helena remains, tells Jimmy about the pregnancy, and after an angry exchange they begin a relationship.

## Act III
Helena has taken Alison’s place in the household. Cliff plans to leave. Alison returns, having suffered a miscarriage. Helena decides that her relationship with Jimmy is wrong and leaves. Jimmy and Alison confront her loss and their pain, then return to their bear-and-squirrel game.

## Interpretation
The play’s postwar class anger and domestic realism are central, but Jimmy’s intelligence and frustration do not excuse his emotional cruelty. The final tenderness can be staged as reconciliation, retreat or an uncertain combination; the play does not prove the relationship’s problems are solved. Discuss miscarriage without presenting it as a deserved punishment.''','0–10: map the household. 10–20: follow shifts in relationships. 20–30: discuss class and verbal power. 30–40: stage the animal game in two ways. 40–50: assess the ending.','What does the bear-and-squirrel game provide? Why might the ending be both tender and troubling?','https://www.litcharts.com/lit/look-back-in-anger/summary'),
n('salesman','Arthur Miller · Death of a Salesman', '''## Act I: home and memory
Willy Loman returns early from a sales trip, too exhausted and distracted to drive safely. Linda urges him to ask for local work. Their adult sons Biff and Happy are visiting. Willy slips between present conversations and memories of Biff’s school football promise, the neighbour Bernard, and his successful brother Ben. Charley offers Willy work, which he refuses, though he accepts financial help. Linda tells the sons that Willy’s difficulties include attempts to take his own life. Biff proposes seeking business support from his former employer Bill Oliver.

## Act II: the failed hopes
Willy asks Howard for a local position and is fired. Bernard, now successful, and Charley offer contrasts to Willy’s values. Biff waits for Oliver, who does not remember him as he hoped; he steals Oliver’s pen and recognises the gap between his former position and his fantasies. At a restaurant the sons struggle to tell Willy the truth and leave him behind. Willy’s memories reveal that young Biff discovered him with another woman in a Boston hotel, shattering Biff’s faith in his father.

Willy buys seeds and attempts to plant them at night. In conversation with an imagined Ben he considers the life-insurance payment as a legacy. Biff confronts him and weeps; Willy understands his son’s love but still clings to the idea that his death can help him. Willy drives away and dies by suicide.

## Requiem
At the sparsely attended funeral Linda, Biff, Happy, Charley and Bernard respond differently. Biff questions Willy’s dreams; Happy intends to pursue them; Charley defends the vulnerability of a salesman’s life. Linda’s final words about paying off the house are painfully double-edged.

## Form and care
The play’s fluid transitions stage memory, not a simple chronological sequence. Discuss the pressure of economic insecurity and ideals of success without treating suicide as a solution or romantic sacrifice.''','0–10: distinguish present from memory. 10–20: track Biff and Willy’s hopes. 20–30: discuss the Boston revelation. 30–40: analyse seeds and the funeral. 40–50: compare characters’ readings of success.','Why does Biff’s meeting with Oliver matter? What does the small funeral challenge?','https://www.litcharts.com/lit/death-of-a-salesman/summary')]
d['course-34:4']=[
n('earnest','Oscar Wilde · The Importance of Being Earnest', '''## Act I: London identities
In London, Jack Worthing uses the name Ernest and invents a troublesome brother as an excuse to leave his country responsibilities. His friend Algernon invents an invalid named Bunbury for similar escapes. Jack proposes to Gwendolen, who is attracted to the name Ernest. Her mother Lady Bracknell refuses consent after learning that Jack was found as a baby in a handbag at Victoria Station.

## Act II: the country house
Algernon arrives at Jack’s country home pretending to be the fictional brother Ernest and courts Jack’s ward Cecily. She has already imagined a romance with that name. Jack arrives intending to announce his brother’s death, only to find Algernon impersonating him. Gwendolen visits; she and Cecily first clash when each believes herself engaged to Ernest, then discover both men have deceived them. The men arrange to be christened Ernest.

## Act III: the handbag
The women seek explanations. Lady Bracknell initially approves Cecily’s fortune but Jack withholds consent to her engagement while his own is blocked. The mention of Miss Prism prompts a revelation: years earlier she accidentally put a manuscript in a pram and a baby in her handbag, leaving the bag at the station. The bag identifies Jack as Lady Bracknell’s sister’s son and Algernon’s older brother. Military records reveal his father’s name was Ernest, the name Jack was given. The couples reunite and the title’s pun returns.

## Analysis
Epigram, reversals and implausible coincidence satirise respectability, class, marriage and the gap between appearance and conduct. The ending rewards aristocratic ancestry as well as mocking its importance: this tension is part of the comedy.''','0–10: draw the invented identities. 10–20: follow who loves which “Ernest.” 20–30: stage the tea scene. 30–40: analyse the handbag revelation. 40–50: discuss satire and its limits.','What is Bunburying? Why is Jack’s final identity both a resolution and a joke?','https://www.gutenberg.org/ebooks/844'),
n('riders-sea','J. M. Synge · Riders to the Sea', '''## Opening: a family waiting
In a cottage on the Aran Islands, Cathleen and Nora receive clothing taken from a drowned man found far north. Their brother Michael is missing. They hide the bundle from their mother Maurya until they can check whether it belongs to him. Maurya has already lost her husband and other sons to the sea and fears for Bartley, her remaining son.

## The journey and recognition
Bartley plans to take horses to a fair despite dangerous conditions. Maurya tries to stop him and does not give him a blessing as he leaves. The sisters send her after him with bread. While she is away they identify Michael’s clothing through its stitching, confirming his death.

## Vision and ending
Maurya returns saying she saw Bartley on the red mare and Michael, in fine clothes, riding behind on the grey pony; her distress prevented her giving Bartley the bread and blessing. The vision is a dramatic experience of the supernatural, not something the audience can independently verify. Neighbours bring Bartley’s body: the grey pony knocked him into the sea. Maurya blesses the dead and, in grief, acknowledges that no one lives forever.

## Reading and staging
This one-act tragedy combines domestic work, economic necessity, religious practice and mourning. The sea sustains the island community while threatening life; it is more than a simple villain. Maurya’s final composure need not mean that grief has disappeared. Notice how offstage events, clothing, the loaf and sound bring the wider world into a small room.''','0–10: identify each family member. 10–20: follow the clothing and bread. 20–30: discuss vision and offstage action. 30–40: examine the sea as livelihood and threat. 40–50: interpret Maurya’s final response.','How do the sisters identify Michael’s clothes? Why does Bartley’s decision involve both danger and livelihood?','https://www.gutenberg.org/ebooks/994')]
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Wrote',sum(len(v) for k,v in d.items() if k.startswith('course-34:')),'Modern Drama selections across 5 units')
