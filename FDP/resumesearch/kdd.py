# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:32:17 2015

@author: srini
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 20:40:16 2015

@author: srini
"""


from kdtree import KDTree

import csv
import operator
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
def find_params(entered_text):
    filtered_words = []
    tokenized_words = word_tokenize(entered_text)
    Parameters = []
    for w in tokenized_words:
        filtered_words.append(w)
    upper_tagged_nouns = [element.upper() for element in filtered_words]
    Location = "NONE"        
    Cities = ['HYDERABAD', 'PUNE', 'CHENNAI', 'BANGALORE', 'MUMBAI', 'DELHI', 'GURGAON', 'INDIA', 'USA', 'UK', 'LONDON']
    for i in upper_tagged_nouns:
        if i in Cities:
            Location = i
    Primary_Role = 'NONE'
    Roles = ['DEVELOPER', 'TECH LEAD', 'ARCHITECT', 'CONSULTANT', 'PROJECT MANAGER', 'FUNCTIONAL LEAD']     
    for i in upper_tagged_nouns:
        if i in Roles:
            Primary_Role = i
    Primary_Tech = 'NONE'
    Secondary_Tech = 'NONE'
    Techs = ['SQL/SERVER', 'SQL SERVER', 'INFORMATICA', 'SQL', 'HADOOP', 'DATA STAGE', 'TERADATA', 'BUSINESS OBJECTS', 'BUSINESSOBJECTS', 'ANDROID', 'BIG DATA', 'BIGDATA', 'ORACLE']
    Matched_Techs = []
    for i in upper_tagged_nouns:
        for l in Techs:
            if i == l:
                Matched_Techs.append(l)
    x = 0
    for i in Matched_Techs:
        x = x + 1
        if x == 1:
            Primary_Tech = Matched_Techs[0]    
        if x > 1:
            Primary_Tech = Matched_Techs[0]
            Secondary_Tech = Matched_Techs[1]
    Parameters.append(Primary_Tech)
    Parameters.append(Secondary_Tech)    
    Parameters.append(Primary_Role)
    Parameters.append(Location)
    return Parameters

# Function to filter the list
def filter_lambda(filters, tuples):
    return filter(lambda t: all(f(t) for f in filters), tuples)


    
def sorted_data_old(Primary_Technology, Role, AddSkill1):

    #Separating out the indices

    #Opening the files

    with open("C:\DataMining\IndexPredictionsOutput.csv", 'rb') as f:
        reader = csv.reader(f)
        data = map(tuple, reader)

    # Filtering the list

    if AddSkill1 == "NONE":
        def f1(t): return t[2].strip()==Primary_Technology # Primary Skill is Informatica
        def f2(t): return t[11].strip()==Role # Role
        filters = [f1,f2]
    else:
        def f1(t): return t[2].strip()==Primary_Technology # Primary Skill is Informatica
        def f2(t): return t[11].strip()==Role # Role
        def f3(t): return t[3].strip()==AddSkill1
        filters = [f1,f2,f3] 
    
    filtered_data = filter_lambda(filters, data)

    #sort the data
    sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:10]

    sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
    
    return sorted_by_distance_printed

def sorted_data(Primary_Technology, Role, AddSkill1, Location):

    with open("C:\DataMining\IndexPredictionsOutput.csv", 'rb') as f:
        reader = csv.reader(f)
        data = map(tuple, reader)
#    return "-PT-" + Primary_Technology + "-AS-" + AddSkill1 + "-LOC-" + Location + "-Role-" + Role

#1 Only Primary Skill
    if AddSkill1=="NONE" and Role=="NONE" and Location=="NONE" :
        def f1(t): return t[2].strip()==Primary_Technology
        filters = [f1]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed

#2 Only Location
    if Primary_Technology =="NONE" and AddSkill1=="NONE" and Role=="NONE" :
        def f1(t): return t[8].strip()==Location 
        filters = [f1]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed
#3 Only Role
    if Primary_Technology =="NONE" and AddSkill1=="NONE" and Location=="NONE" :
        def f1(t): return t[11].strip()==Role 
        filters = [f1]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed
#4 Role and Location 
    if  Primary_Technology =="NONE" and AddSkill1=="NONE" :
        def f1(t): return t[11].strip()==Role
        def f2(t): return t[8].strip()==Location 
        filters = [f1,f2]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed    
#5 Primary Skill and Location 
    if  AddSkill1=="NONE" and Role=="NONE" :
        def f1(t): return t[2].strip()==Primary_Technology
        def f2(t): return t[8].strip()==Location 
        filters = [f1,f2]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed
#6 Primary Skill and Role
    if  AddSkill1=="NONE" and Location=="NONE" :
        def f1(t): return t[2].strip()==Primary_Technology
        def f2(t): return t[11].strip()==Role 
        filters = [f1,f2]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed
#7 Primary Skill and Additional Skill
    if  Role=="NONE"  and Location=="NONE" :
        def f1(t): return t[2].strip()==Primary_Technology
        def f2(t): return t[3].strip()==AddSkill1
        filters = [f1,f2]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed
#8 Primary Skill,Secondary and Role   
    if  Location=="NONE"  :
        def f1(t): return t[2].strip()==Primary_Technology
        def f2(t): return t[11].strip()==Role 
        def f3(t): return t[3].strip()==AddSkill1
        filters = [f1,f2,f3]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed 

#9 Primary Skill,Secondary and Location
    if  Role=="NONE"  :
        def f1(t): return t[2].strip()==Primary_Technology
        def f2(t): return t[8].strip()==Location
        def f3(t): return t[3].strip()==AddSkill1
        filters = [f1,f2,f3]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed         
#10 Primary Skill,Role and Location   
    if  AddSkill1=="NONE"  :
        def f1(t): return t[2].strip()==Primary_Technology
        def f2(t): return t[11].strip()==Role 
        def f3(t): return t[8].strip()==Location
        filters = [f1,f2,f3]             
        filtered_data = filter_lambda(filters, data)
        sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
        sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
        return sorted_by_distance_printed     
#11 All are given
    def f1(t): return t[2].strip()==Primary_Technology
    def f2(t): return t[11].strip()==Role 
    def f3(t): return t[8].strip()==Location
    def f4(t): return t[3].strip()==AddSkill1
    
    filters = [f1,f2,f3,f4]             
    filtered_data = filter_lambda(filters, data)
    sorted_by_distance = sorted(filtered_data, key=lambda tup:tup[67])[0:50]
    sorted_by_distance_printed = map(operator.itemgetter(0,1,2,26,8,23,10), sorted_by_distance)
    return sorted_by_distance_printed     

def derived_info_old(ResumeNo):
    with open("C:\DataMining\DerivedInformation.csv", 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == ResumeNo:
                return row
        return "NoData"    
def derived_info(ResumeNo):
    with open("C:\DataMining\DerivedIndicesByTech.csv", 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == ResumeNo:
                return row
        return "NoData"    

def convert_to_int(tuples, position):
    single_list = map(lambda y:y[position], tuples)
    single_list_int = [int(x) for x in single_list]
    return single_list_int   

def summary_data(resume_num):
    
    #Opening the files
    
    with open("C:\DataMining\DerivedIndicesByTech.csv", 'rb') as f:
        reader = csv.reader(f)
        data = map(tuple, reader)

    # Filtering the data

    def f1(t): return t[1] == resume_num #Resume Number sent by the calling program.
    
    filters = [f1]
    filtered_data = filter_lambda(filters, data)    
    
    primary_tech = [tup[3] for tup in filtered_data]
    
    
    #Get all rows in the corpus with the above primary technology
    
    def f2(t): return t[3] == primary_tech[0]
        
    filters = [f2]
    tech_filtered_data = filter_lambda(filters, data)
    
    # Converting into integers and getting the max value
    
    adv_skill_int = convert_to_int(tech_filtered_data, 30)
    max_adv_skill = max(adv_skill_int)
    interval_adv_skill = abs(max_adv_skill/4)
    
    
    dev_projects_int = convert_to_int(tech_filtered_data, 32)
    max_dev_projects = max(dev_projects_int)
    interval_dev_projects = abs(max_dev_projects/4)
    
    support_projects_int = convert_to_int(tech_filtered_data, 33)
    max_support_projects = max(support_projects_int)
    interval_support_projects = abs(max_support_projects/4)
    
    maint_projects_int = convert_to_int(tech_filtered_data, 34)
    max_maint_projects = max(maint_projects_int)
    interval_maint_projects = abs(max_maint_projects/4)
    
    keyDB_int = convert_to_int(tech_filtered_data, 48)
    max_keyDB = max(keyDB_int)
    interval_keyDB = abs(max_keyDB/4)
    
    keyPL_int = convert_to_int(tech_filtered_data, 49)
    max_keyPL = max(keyPL_int)
    interval_keyPL = abs(max_keyPL/4)
    
    # Now calculating the intervals
    
    adv_skill_low = interval_adv_skill
    adv_skill_avg = adv_skill_low + interval_adv_skill
    adv_skill_high = adv_skill_avg + interval_adv_skill
    
    dev_projects_low = interval_dev_projects
    dev_projects_avg = dev_projects_low + interval_dev_projects
    dev_projects_high = dev_projects_avg + interval_dev_projects
    
    maint_projects_low = interval_maint_projects
    maint_projects_avg = maint_projects_low + interval_maint_projects
    maint_projects_high = maint_projects_avg + interval_maint_projects

    support_projects_low = interval_support_projects
    support_projects_avg = support_projects_low + interval_support_projects
    support_projects_high = support_projects_avg + interval_support_projects

    keyDB_low = interval_keyDB
    keyDB_avg = keyDB_low + interval_keyDB
    keyDB_high = keyDB_avg + interval_keyDB
    
    keyPL_low = interval_keyPL
    keyPL_avg = keyPL_low + interval_keyPL
    keyPL_high = keyPL_avg + interval_keyPL
    
    # Getting value for the original candidate
    
    num_adv_skills_t = [tup[30] for tup in filtered_data]
    num_adv_skills = int(num_adv_skills_t[0])
    
    num_dev_projects_t = [tup[32] for tup in filtered_data]
    num_dev_projects = int(num_dev_projects_t[0])
    
    num_support_projects_t = [tup[33] for tup in filtered_data]
    num_support_projects = int(num_support_projects_t[0])
    
    num_maint_projects_t = [tup[34] for tup in filtered_data]
    num_maint_projects = int(num_maint_projects_t[0])
    
    num_keyDB_t = [tup[48] for tup in filtered_data]
    num_keyDB = int(num_keyDB_t[0])
    
    num_keyPL_t = [tup[49] for tup in filtered_data]
    num_keyPL = int(num_keyPL_t[0])
    
    #Initializing the counters
    
    strength_ctr = 0
    improvement_ctr = 0
    
    #Initializing the strings
    
    strength_str1 = "..."
    strength_str2 = "..."
    strength_str3 = "..."
    
    improvement_str1 = "..."
    improvement_str2 = "..."
    improvement_str3 = "..."
    
    summary_str = "..."
    
    if (num_adv_skills > adv_skill_avg) and (num_dev_projects > dev_projects_avg) and (num_keyDB > keyDB_avg):
        strength_ctr = 3
        strength_str1 = "Excellent depth in using advanced " + primary_tech[0] + " concepts"
        strength_str2 = "Very Good development experience"
        strength_str3 = "Excellent knowledge of databases"
    elif (num_adv_skills > adv_skill_avg) and (num_dev_projects > dev_projects_avg):
        strength_ctr = 2
        strength_str1 = "Excellent depth in using advanced " + primary_tech[0] + " concepts"
        strength_str2 = "Very Good development experience"
    elif (num_adv_skills > adv_skill_avg):
        strength_ctr = 1
        strength_str1 = "Excellent depth in using advanced " + primary_tech[0] + " concepts"
    elif (num_support_projects > support_projects_avg) or (num_maint_projects > maint_projects_avg):
        strength_ctr = 1
        strength_str1 = "Very Good exeperience in Support & Maintenance projects."
        
    
    if (num_adv_skills < adv_skill_low) and (num_dev_projects < dev_projects_low) and (num_keyDB < keyDB_low):
        improvement_ctr = 3
        improvement_str1 = "Less than average experience in using advanced " + primary_tech[0] + " concepts"
        improvement_str2 = "Poor Development experience"
        improvement_str3 = "Need to spend more time working on database technologies"
    elif (num_adv_skills < adv_skill_low) and (num_dev_projects < dev_projects_low):
        improvement_ctr = 2
        improvement_str1 = "Less than average experience in using advanced " + primary_tech[0] + " concepts"
        improvement_str2 = "Poor Development experience"
    elif (num_adv_skills < adv_skill_low):
        improvement_ctr = 1
        improvement_str1 = "Less than average experience in using advanced " + primary_tech[0] + " concepts"


    if strength_ctr ==3:
        summary_str = "Excellent candidate with exceptional technical skills, can be positioned for higher roles."
    elif strength_ctr == 2:
        summary_str = "Above average candidate with sound technical skills, will be a good fit for the role"
    elif improvement_ctr ==3:
        summary_str = "The candidate is clearly below average, should not be selected."
    elif improvement_ctr ==2:
        summary_str = "Candidate may be considered after further evaluation"
    else:
        summary_str = "Average candidate can be positioned for the role"
 
    return_str = (strength_str1, strength_str2, strength_str3, improvement_str1, improvement_str2, improvement_str3, summary_str)
     
    return return_str
    

        
def get_techarea(tech):
    with open("C:\DataMining\UniqueTechs.csv", 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == tech:
                return row[1]
        return tech    
def nearest_filtered(Primary_Technology, Role):
    #Separating out the indices
    #Opening the files
    
    with open("C:\DataMining\IndexPredictionsOutput.csv", 'rb') as f:
        reader = csv.reader(f)
        data = map(tuple, reader)


    # Filtering the list
    def f1(t): return t[2].strip()==Primary_Technology # Primary Skill is Informatica
    def f2(t): return t[11].strip()==Role # Role

    filters = [f1,f2]    
    
    filtered_data = filter_lambda(filters, data)
    
    
    kd_filtered_data = map(operator.itemgetter(0,58,59,60,61,62,63,64,65,66), filtered_data)


    # Creating the tree

    tree = KDTree.construct_from_data(kd_filtered_data)
 
    # Finding the nearest neighbours, t can be varied for the number of neighbours

    nearest = tree.query(query_point=(85,10,10,10,10,10,10,10,10,10), t=10)

    # The serial number of the nearest neighbours
    nearest_index = [x[0] for x in nearest]

    # Using this to filter the original list
    kd_filtered_nearest = [tup for tup in filtered_data if tup[0] in nearest_index]

    # Preparing the dataset to be printed

    kd_filtered_nearest_printed = map(operator.itemgetter(0,1,2,26,8,23,10), kd_filtered_nearest)

    return kd_filtered_nearest_printed







