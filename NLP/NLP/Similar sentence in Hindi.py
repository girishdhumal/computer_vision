from inltk.inltk import setup 
setup('hi') 
from inltk.inltk import get_similar_sentences 
# get similar sentences to the one given in hindi 
output = get_similar_sentences('मैंआज बहुत खुश हूं', 5, 'hi') 
print(output)
