from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
import kdd

def results1(request):   
    str1 = "Resumes170/Lakshman-Dhullipalla.txt.xml"
    str2 = "/"
    pos1 = str1.find(str2)
    finalstr = str1[str1.find("/")+1:]
    str2 = ".txt"
    pos1 = finalstr.find(str2)
    return HttpResponse(finalstr)
    #return HttpResponse(finalstr[0:pos1])

#def paramtest(request,user_id):
#    return HttpResponse(request.GET('textentered'))

def derivedInfo1(request):   
        if 'q' in request.GET:
            resumeNo = request.GET['q']
        html_DerivedInfo = []
        values = kdd.derived_info(resumeNo)
        if values =="NoData":
            return HttpResponse("Resume Number does not exist")
        i = 0
        for x in values:
            i = i+1
        # the size of the list is i-1
        index = 1
        for x in values:
            if index <= i-1:
                html_DerivedInfo.append(values[index])
                index = index+1
        Name = values[2]
        Skill = values[3]
        Exp = values[27]
        Qual = values[24]
        Employer = values[26]
        TDIdx = values[61]
        TBIdx = values[60]
        RoleIdx = values[62]
        ExpIdx = values[59]
        MBIdx = values[64]
        MDIdx = values[65]
        DIdx  = values[63]  
        TPercetile = values[71]
        MPercetile = values[72]
        DPercetile = values[73]
        Strength = "Strength to be calculated"
        Improvement = "Improvement Areas to be calculated"
        Summary = "Summary to be calculated"
        t = get_template('DerivedInfo.html')
        d = {"derivedInfo": {"name": Name, "PrSkill": Skill , "TotalExp": Exp , "Qualif": Qual ,"Employer": Employer ,"TDIdx": TDIdx , "TBIdx": TBIdx ,"RoleIdx" : RoleIdx , "ExpIdx" : ExpIdx , "MBIdx" : MBIdx , "MDIdx" : MDIdx , "DIdx" : DIdx , "TPercetile" : TPercetile ,"MPercetile" : MPercetile ,"DPercetile" : DPercetile ,"Strength" : Strength , "Improvement" : Improvement , "Summary" : Summary}}
        html = t.render(Context(d))    
        return HttpResponse(html)
def derivedInfo(request,resumeNo):   
#         if 'q' in request.GET:
#     resumeNo = request.GET['q']
        html_DerivedInfo = []
        values = kdd.derived_info(resumeNo)
        if values =="NoData":
            return HttpResponse("Resume Number does not exist")
        i = 0
        for x in values:
            i = i+1
        # the size of the list is i-1
        index = 1
        for x in values:
            if index <= i-1:
                html_DerivedInfo.append(values[index])
                index = index+1
        Name = values[2]
        Skill = values[3]
        Exp = values[27]
        Qual = values[24]
        Employer = values[26]
        TDIdx = values[61]
        TBIdx = values[60]
        RoleIdx = values[62]
        ExpIdx = values[59]
        MBIdx = values[64]
        MDIdx = values[65]
        DIdx  = values[63]  
        TPercetile = values[71]
        MPercetile = values[72]
        DPercetile = values[73]
        
        summary_Values = kdd.summary_data(resumeNo)
        Strength = summary_Values[0]+" "+ summary_Values[1] +" " + summary_Values[2]
        Improvement = summary_Values[3]+" "+ summary_Values[4] +" " + summary_Values[5]   
        Summary = summary_Values[6]    
#         return HttpResponse(summary_Values[6])
#         html_summaryValues = []
#         l = 0
#         for x in summary_Values:
#             l = l+1
#         # the size of the list is i-1
#         index = 1
#         for x in summary_Values:
#             Strength = x[0]+" "+ x[1] +" " + x[2]
#             Improvement = x[3]+" "+ x[4] +" " + x[5]   
#             Summary = x[6]    
# #             if index <= l-1:
#                 html_summaryValues.append(summary_Values[index])
#                 index = index+1
#         Strength = html_summaryValues[0]+" "+ html_summaryValues[1] +" " + html_summaryValues[2]
#         Improvement = html_summaryValues[3]+" "+ html_summaryValues[4] +" " + html_summaryValues[5]
# #        Summary = html_summaryValues[6]
#         Summary = "Test"
        t = get_template('DerivedInfo.html')
        d = {"derivedInfo": {"name": Name, "PrSkill": Skill , "TotalExp": Exp , "Qualif": Qual ,"Employer": Employer ,"TDIdx": TDIdx , "TBIdx": TBIdx ,"RoleIdx" : RoleIdx , "ExpIdx" : ExpIdx , "MBIdx" : MBIdx , "MDIdx" : MDIdx , "DIdx" : DIdx , "TPercetile" : TPercetile ,"MPercetile" : MPercetile ,"DPercetile" : DPercetile ,"Strength" : Strength , "Improvement" : Improvement , "Summary" : Summary}}
        html = t.render(Context(d))    
        return HttpResponse(html)  

def results2(request):   
    if 'q' in request.GET:
        y = 0
        rank = 1
        PrimaryTech = "NONE"
        PrimaryRole = "NONE"
        AddSkill1   = "NONE"
        inputs = request.GET['q'].split()
        for x in inputs:
            y = y+1
        if y == 0: 
            return HttpResponse("NO SEARCH CRITERIA PROVIDED")
        if y == 2:    
            PrimaryTech = inputs[0] 
            PrimaryRole = inputs[1]
            AddSkill1   = "NONE"    
        if y == 4:    
            PrimaryTech = inputs[0] 
            PrimaryRole = inputs[1]
            AddSkill1   = inputs[3]
        html_candidates = []
        values = kdd.sorted_data(PrimaryTech.upper(),PrimaryRole.upper(),AddSkill1.upper())
        for x in values[0:]:
            html_candidates.append((rank,x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
            rank = rank+1
        t = get_template('results.html')
#       html = t.render(Context({'html_candidates':html_candidates}))
        html = t.render(Context({'html_candidates':html_candidates}))    
        return HttpResponse(html)

def results(request):   
    if 'q' in request.GET:
        y = 0
        rank = 1
        PrimaryTech = "NONE"
        PrimaryRole = "NONE"
        AddSkill1   = "NONE"
        Location = "INDIA"
        parameters = []
        inputs = request.GET['q'].split()
        for x in inputs:
            y = y+1
        if y == 0: 
            return HttpResponse("NO SEARCH CRITERIA PROVIDED")
        parameters = kdd.find_params(request.GET['q'])
        PrimaryTech = parameters[0]
        AddSkill1   = parameters[1]
        PrimaryRole = parameters[2]
        Location    = parameters[3]
        html_candidates = []
#        resume_numbers = []
        values = kdd.sorted_data(PrimaryTech.upper(),PrimaryRole.upper(),AddSkill1.upper(),Location.upper())
        for x in values[0:]:
            html_candidates.append((rank,x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
#            resume_numbers.append(x[0])
            rank = rank+1
        t = get_template('results.html')
        html = t.render(Context({'html_candidates':html_candidates}))    
        return HttpResponse(html)     

def ResultsByProfile(request):   
    rank = 1
    Profile="NONE"
    if request.GET['q'] == "KoteswarN.docx":
        Profile="Android"
    if request.GET['q'] == "VijayP.docx":    
        Profile="BI"
    PrimaryTech = "NONE"
    PrimaryRole = "NONE"
    AddSkill1   = "NONE"    
    if 'q' in request.GET:
        y = 0
    if Profile=="Android":
        PrimaryTech = "Android"
        PrimaryRole = "Developer"
        AddSkill1   = "NONE"
    if Profile=="BI":
        PrimaryTech = "BI"
        PrimaryRole = "Developer"
        AddSkill1   = "NONE"    
    html_candidates = []
    values = kdd.sorted_data(PrimaryTech,PrimaryRole,AddSkill1)
    for x in values[0:]:
        html_candidates.append((rank,x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        rank = rank+1
        t = get_template('results.html')
        html = t.render(Context({'html_candidates':html_candidates}))    
        return HttpResponse(html)     

def ResultsByJD(request):   
    rank = 1
    JD="NONE"
    if request.GET['q'] == "Job Description for DataBase Architect.doc":
        JD="DB2"
    if request.GET['q'] == "Job Description for Teradata Developer.docx":    
        JD="TD"
    PrimaryTech = "NONE"
    PrimaryRole = "NONE"
    AddSkill1   = "NONE"    
    if 'q' in request.GET:
        y = 0
    if JD=="TD":
        PrimaryTech = "Teradata"
        PrimaryRole = "Developer"
        AddSkill1   = "NONE"
    if JD=="DB2":
        PrimaryTech = "DB2"
        PrimaryRole = "Architect"
        AddSkill1   = "NONE"    
    if JD=="NONE":
        PrimaryTech = "NONE"
        PrimaryRole = "NONE"
        AddSkill1   = "NONE"    
    html_candidates = []
    values = kdd.sorted_data(PrimaryTech,PrimaryRole,AddSkill1)
    for x in values[0:]:
        html_candidates.append((rank,x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        #html_candidates.append((rank,x[0][x[0].find("/")+1:],x[1],x[2],x[3],x[4],x[5],x[6]))
        rank=rank+1
    t = get_template('results.html')
    html = t.render(Context({'html_candidates':html_candidates}))    
    return HttpResponse(html)     
    

def home(request):
    return render(request, "HomePage.html")

def search_resume(request):
    return render(request, 'search_resume.html')

def JDInterface(request):
    return render(request, 'JDInterface.html')

def ResumeInterface(request):
    return render(request, 'ResumeInterface.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
        
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
