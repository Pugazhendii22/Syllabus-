import re,json
s=open('syllabus.txt').read(); s=s[s.index('--- PAGE 7 ---'):]
pat=re.compile(r'(?im)^[ \t]*Course Title[ \t]*:[ \t]*([^\n]*)')
ms=list(pat.finditer(s)); sem=1; courses=[]
for i,m in enumerate(ms):
    before=s[:m.start()]; sems=re.findall(r'(?im)^\s*SEMESTER\s+([1-8])\s*$',before)
    if sems: sem=int(sems[-1])
    title=m.group(1).strip(); end=ms[i+1].start() if i+1<len(ms) else len(s)
    part=s[m.end():end]; part=re.split(r'(?im)^\s*SEMESTER\s+[1-8]\s*$',part)[0]
    if not title:
        title='Modern Indian Languages'
    page=re.findall(r'--- PAGE (\d+) ---',before); page=int(page[-1]) if page else 7
    # Keep unit segments only up to references/exam. Some PDFs omit details; do not invent them.
    marks=list(re.finditer(r'(?im)^[ \t]*unit[ \t]*[–-]?[ \t]*(IV|III|II|I|V|[1-5])\b([^\n]*)',part))
    units=[]
    for j,u in enumerate(marks):
        if j and u.group(1).upper()==marks[j-1].group(1).upper(): continue
        a=u.start(); b=marks[j+1].start() if j+1<len(marks) else len(part)
        body=part[u.end():b]; body=re.split(r'(?im)^\s*(?:References|Recommended (?:Books|Readings?)|Suggested (?:Readings?)|Bibliography|End Semester Examination|Course Outcomes|Scheme of Examination|Testing and evaluation|Evaluation|CLO/PO)\s*[:\n]',body)[0]
        body=re.split(r'(?im)^\s*CLO[1-5]\b',body)[0]
        body=re.sub(r'--- PAGE \d+ ---\s*\n\s*\d+\s*\n','\n',body)
        body=re.sub(r'(?m)^\s*\d+\s*$','',body); body=re.sub(r'\n\s*\n+', '\n',body).strip()
        header=u.group(2).strip(' –—:-\t')
        if len(body)>2500: body=body[:2500].rsplit(' ',1)[0]+'…'
        units.append({'title':'Unit '+u.group(1)+(' · '+header if header else ''),'content':body})
    # remove spurious units appearing after end-of-course exam
    courses.append({'id':f'course-{len(courses)+1}','semester':sem,'title':title.title() if title.isupper() else title,'page':page,'units':units})
open('courses.json','w').write(json.dumps(courses,ensure_ascii=False,indent=2))
print('courses',len(courses),'units',sum(len(c['units']) for c in courses))
for c in courses: print(c['semester'],c['title'],len(c['units']),c['page'])
