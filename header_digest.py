__author__ = 'Oranitha'
import re

master_read = open('in.txt').read().split(",")
master_write = open('out.csv',"w")
master_write.write("General Data,Total Enemies Fought,Egg,Apparel,Vista,Ambush,Eliminate,Crate,")
plain_read = master_read[::3]
for row in plain_read:
    rowlist = row.split("(")
    name = re.findall('"([^"]*)"',rowlist[0])
    master_write.write(name[0]+" Fought,"+name[0]+" Food,"+name[0]+" Material,"+name[0]+" Familiar,")

master_write.write("\n")

element_dict = {"Neutral":""};
names_read = master_read[::3]
master_read = master_read[2:]
master_read = master_read[::3]
for i in range(len(master_read)):
	row = master_read[i]
	rowlist = row.split("(")
	element_ls = re.findall('"([^"]*)"',rowlist[0])
	element = element_ls[0]
	if element not in element_dict:
		element_dict[element] = "Fest Data: "+element+",Total Enemies Fought,Egg,Apparel,Vista,Ambush,Eliminate,Crate,"

#Yes, this is necessary! Why? Because we need to populate our elemental portions before re-populating them with neutrals.
for i in range(len(master_read)):
	row = master_read[i]
	rowlist = row.split("(")
	element_ls = re.findall('"([^"]*)"',rowlist[0])
	element = element_ls[0]
	name = re.findall('"([^"]*)"',names_read[i])
	namestring = name[0]+" Fought,"+name[0]+" Currency,"+name[0]+" Chests,"
	if element == "Neutral":
		element_dict.update((entry, val+namestring) for entry, val in element_dict.items())
	else:
		element_dict[element] = element_dict[element]+namestring
with master_write as f:
    [f.write('{0}\n'.format(value[1][0:])) for value in element_dict.items() if value[0] != "Neutral"]
master_write.close()