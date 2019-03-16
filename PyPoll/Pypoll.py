import os
import csv

Candidate_Name = []
Candidate_County = []
Candidate_VoterID = []
Unique_Candidates = []
Khan = []
Correy = []
Li = []
OTooley = []



election_data_path = os.path.join("../", "Resources", "election_data.csv")

with open(election_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csv_reader:
        Candidate_VoterID.append(row[0])
        Candidate_County.append(row[1])
        Candidate_Name.append(row[2])
        
total = len(Candidate_VoterID)
print(f'Election Results')
print(f'-------------------------')
print("Total Votes: ",total)
print(f'-------------------------')


def unique(list1): 
  

    for x in Candidate_Name: 
        # check if exists in unique_list or not 
        if x not in Unique_Candidates: 
            Unique_Candidates.append(x) 


unique(Candidate_Name)        

#print(Unique_Candidates)

#cand_Vid_Dict = dict(zip(Candidate_Name,Candidate_VoterID))
#keys = cand_Vid_Dict.keys()
#values = cand_Vid_Dict.values()

#def res_per_candidate(name):
# result = 0
# for name in cand_Vid_Dict:
     
#     result = result + 1
# print(result)
# return result


#for x in row[2]:
with open(election_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    for row in csv_reader:
        if row[2] == Unique_Candidates[0]:
           Khan.append(row[0])
        if row[2] == Unique_Candidates[1]:
           Correy.append(row[0])
        if row[2] == Unique_Candidates[2]:
           Li.append(row[0])   
        if row[2] == Unique_Candidates[3]:
           OTooley.append(row[0])

        
length_Khan = len(Khan)
length_Correy = len(Correy)
length_Li = len(Li)
length_OTooley = len(OTooley)

Vote_count = [length_Khan, length_Correy, length_Li, length_OTooley]
print(Vote_count)
Final_Dict = dict(zip(Unique_Candidates,Vote_count))
print(Final_Dict)

#calculating winner results
winner = max(Final_Dict, key=lambda x:x)
print(max(Final_Dict, key=lambda x:x))

#print(Unique_Candidates[0])
#print(length_Khan)
#print(length_Correy)
#print(length_Li)
#print(length_OTooley)

Per_Khan = (length_Khan/total) * 100
Per_Correy = (length_Correy/total) * 100
Per_Li = (length_Li/total) * 100
Per_OTooley = (length_OTooley/total) * 100





#print(round(float(Per_Correy),3))
print(f'Khan: {round(Per_Khan,3)} % ({length_Khan})')
print(f'Correy: {round(Per_Correy,3)} % ({length_Correy})')
print(f'Li: {round(Per_Li,3)} % ({length_Li})')
print(f'OTooley: {round(Per_OTooley,3)} % ({length_OTooley})')
print(f'---------------------------')
print(f'Winner : ')
print(f'---------------------------')

