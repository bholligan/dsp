## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> There are 8 different degrees.  
>> The degree frequencies are:  
 {'MD': 1, 'JD': 1, 'MS': 2, 'BSEd': 1, 'ScD': 6, 'PhD': 31, 'MPH': 2, 'MA': 1}

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> One title was written as 'Assistant Professor is Biostatistics'. Assuming that is the same as 'Assistant Professor of  Biostatistcs', there are 3 different titles.  
>> The title frequencies are:  
{'Assistant Professor of Biostatistics': 12, 'Professor of Biostatistics': 13, 'Associate Professor of Biostatistics': 12}


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> The list of emails is:  
>> ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']

####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> Unique domain names are:  
>> ['upenn.edu', 'mail.med.upenn.edu', 'email.chop.edu', 'cceb.med.upenn.edu']

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:
```
Bellamy: [['Sc.D.', 'bellamys@mail.med.upenn.edu', 'Associate Professor']]
Bilker: [['Ph.D.', 'warren@upenn.edu', 'Professor']]
Bryan: [['PhD', 'bryanma@upenn.edu', 'Assistant Professor']]
```
####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:
```
('A.', 'Localio'): [['JD MA MPH MS PhD', 'rlocalio@upenn.edu', 'Associate Professor']]  
('Alisa', 'Stephens'): [['Ph.D.', 'alisaste@mail.med.upenn.edu', 'Assistant Professor']]  
('Andrea', 'Troxel'): [['ScD', 'atroxel@mail.med.upenn.edu', 'Professor']]
```
####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors  
>> I did not do any special handling of faculty whose first name was a single letter and period.  
```
('Scarlett', 'Bellamy'): [['Sc.D.', 'bellamys@mail.med.upenn.edu', 'Associate Professor']]
('Warren', 'Bilker'): [['Ph.D.', 'warren@upenn.edu', 'Professor']]
('Matthew', 'Bryan'): [['PhD', 'bryanma@upenn.edu', 'Assistant Professor']]
('Jinbo', 'Chen'): [['Ph.D.', 'jinboche@upenn.edu', 'Associate Professor']]
('Jonas', 'Ellenberg'): [['Ph.D.', 'jellenbe@mail.med.upenn.edu', 'Professor']]
('Susan', 'Ellenberg'): [['Ph.D.', 'sellenbe@upenn.edu', 'Professor']]
('Rui', 'Feng'): [['Ph.D', 'ruifeng@upenn.edu', 'Assistant Professor']]
('Benjamin', 'French'): [['PhD', 'bcfrench@mail.med.upenn.edu', 'Associate Professor']]
('Phyllis', 'Gimotty'): [['Ph.D', 'pgimotty@upenn.edu', 'Professor']]
('Wensheng', 'Guo'): [['Ph.D', 'wguo@mail.med.upenn.edu', 'Professor']]
('Yenchih', 'Hsu'): [['Ph.D.', 'hsu9@mail.med.upenn.edu', 'Assistant Professor']]
('Rebecca', 'Hubbard'): [['PhD', 'rhubb@mail.med.upenn.edu', 'Associate Professor']]
('Wei-Ting', 'Hwang'): [['Ph.D.', 'whwang@mail.med.upenn.edu', 'Associate Professor']]
('Marshall', 'Joffe'): [['MD MPH Ph.D', 'mjoffe@mail.med.upenn.edu', 'Professor']]
('J.', 'Landis'): [['B.S.Ed. M.S. Ph.D.', 'jrlandis@mail.med.upenn.edu', 'Professor']]
('Mingyao', 'Li'): [['Ph.D.', 'mingyao@mail.med.upenn.edu', 'Associate Professor']]
('Yimei', 'Li'): [['Ph.D.', 'liy3@email.chop.edu', 'Assistant Professor']]
('Hongzhe', 'Li'): [['Ph.D', 'hongzhe@upenn.edu', 'Professor']]
('A.', 'Localio'): [['JD MA MPH MS PhD', 'rlocalio@upenn.edu', 'Associate Professor']]
('Nandita', 'Mitra'): [['Ph.D.', 'nanditam@mail.med.upenn.edu', 'Associate Professor']]
('Knashawn', 'Morales'): [['Sc.D.', 'knashawn@mail.med.upenn.edu', 'Associate Professor']]
('Kathleen', 'Propert'): [['Sc.D.', 'propert@mail.med.upenn.edu', 'Professor']]
('Mary', 'Putt'): [['PhD ScD', 'mputt@mail.med.upenn.edu', 'Professor']]
('Sarah', 'Ratcliffe'): [['Ph.D.', 'sratclif@upenn.edu', 'Associate Professor']]
('Michelle', 'Ross'): [['PhD', 'michross@upenn.edu', 'Assistant Professor']]
('Jason', 'Roy'): [['Ph.D.', 'jaroy@mail.med.upenn.edu', 'Associate Professor']]
('Mary', 'Sammel'): [['Sc.D.', 'msammel@cceb.med.upenn.edu', 'Professor']]
('Pamela', 'Shaw'): [['PhD', 'shawp@upenn.edu', 'Assistant Professor']]
('Russell', 'Shinohara'): [['0', 'rshi@mail.med.upenn.edu', 'Assistant Professor']]
('Haochang', 'Shou'): [['Ph.D.', 'hshou@mail.med.upenn.edu', 'Assistant Professor']]
('Justine', 'Shults'): [['Ph.D.', 'jshults@mail.med.upenn.edu', 'Professor']]
('Alisa', 'Stephens'): [['Ph.D.', 'alisaste@mail.med.upenn.edu', 'Assistant Professor']]
('Andrea', 'Troxel'): [['ScD', 'atroxel@mail.med.upenn.edu', 'Professor']]
('Rui', 'Xiao'): [['PhD', 'rxiao@mail.med.upenn.edu', 'Assistant Professor']]
('Dawei', 'Xie'): [['PhD', 'dxie@upenn.edu', 'Assistant Professor']]
('Sharon', 'Xie'): [['Ph.D.', 'sxie@mail.med.upenn.edu', 'Associate Professor']]
('Wei', 'Yang'): [['Ph.D.', 'weiyang@mail.med.upenn.edu', 'Assistant Professor']]
```
Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

