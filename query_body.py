import math

# Utsav Mandal

def load_docs():
    docs = []
    with open('docs.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        docs.append(line.strip().split())
    print("Doc size: ",len(docs))
    print("Sample doc: ",docs[216])
    return docs

def load_inv_index():
    inv_index = {}
    with open('inv-index.txt', 'r') as f:
        lines = f.readlines()
    for i in range(0, len(lines), 2):
        inv_index[lines[i].strip()] = lines[i+1].strip().split()
    print("Inv index size: ",len(inv_index))
    return inv_index

docs=[]
inv_index={}
docs = load_docs()
inv_index = load_inv_index()

def get_tf(term):
    tf = {}
    if term in inv_index:
        for ii in inv_index[term]:
            if ii not in tf:
                tf[ii] = 1
            else:
                tf[ii] += 1

    for key in tf:
        tf[key]/=len(docs[int(key)])
    return tf

def get_idf(term):
    if term in inv_index:
        return math.log(len(docs)/len(set(inv_index[term])))
    else:
        return 0
    
def get_potential_docs(query):
    potential_docs = {}
    for term in query:
        if term not in inv_index:
            continue
        tf_val=get_tf(term)
        idf_val=get_idf(term)
        print(term, tf_val, idf_val)
        for key in tf_val:
            if key not in potential_docs:
                potential_docs[key]=tf_val[key]*idf_val
            else:
                potential_docs[key]+=tf_val[key]*idf_val
    
    for key in potential_docs:
        potential_docs[key]/=len(query)

    potential_docs = dict(sorted(potential_docs.items(), key=lambda item: item[1], reverse=True))

    return potential_docs

query_term=input('Enter the query term: ')
query=[term.lower() for term in query_term.strip().split()]
print(query)

links=[]
with open('Qdata/q_index.txt','r') as f:
    links=f.readlines()
# print(len(links))

title=[]
with open('Qdata/output_headings.txt','r') as f:
    title=f.readlines()
# print(len(title))

potential_docs = get_potential_docs(query)
for key in potential_docs:
    print("Document: ",int(key)+1,title[int(key)],links[int(key)],"Score: ", potential_docs[key])