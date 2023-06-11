import re

# Utsav Mandal

with open('Qdata/output_headings.txt','r') as f:
    lines=f.readlines()

# for ind,line in enumerate(lines):
#     print(ind,line)

def preprocess(document_text):
    # remove the leading numbers from the string, remove not alpha numeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

docs=[]

def extract_words_from_document(add):
    # Remove all non-alphabetic characters except whitespaces
    with open(add,'r') as f:
        document=f.read()
    clean_text = re.sub(r'[^a-zA-Z\s]', '', document)
    
    # Split the text into individual words
    words =  [term.lower() for term in clean_text.split()]
    
    return words

for ind,line in enumerate(lines):
    doc = preprocess(line)
    words = extract_words_from_document('Qdata/q'+str(ind+1)+"/"+str(ind+1)+'.txt')
    doc.extend(words)
    docs.append(doc)

inv_index={}

for ind,doc in enumerate(docs):
    for term in doc:
        if term not in inv_index:
            inv_index[term]=[ind]
        else:
            inv_index[term].append(ind)

print(len(docs))
print(len(inv_index))
# print(len(set(inv_index['the'])))
# print(len(inv_index['the']))
# print(len(set(inv_index['of'])))
# print(len(inv_index['of']))

with open ('docs.txt','w') as f:
    for doc in docs:
        for term in doc:
            f.write(term+' ')
        f.write('\n')

with open ('inv-index.txt','w') as f:
    for key in inv_index:
        f.write(key+'\n')
        for value in inv_index[key]:
            f.write(str(value)+' ')
        f.write('\n')