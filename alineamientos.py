from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO
import pandas as pd

babosa=list(SeqIO.parse("Dlaeve_longestOrfs.good.faa", "fasta"))
humano=list(SeqIO.parse("copia.faa", "fasta"))
Genes=pd.read_csv("GenesCompartidos.csv")
def find_record_by_id(records_list, record_id):
    for record in records_list:
        if record.id == record_id:
            return record
    return None
scores=[]
for i in range(len(Genes)):
  id1_to_find = Genes.loc[i,'Dlaeve_longestOrfs.good.faa']
  id2_to_find = Genes.loc[i,'proteoma_humano.faa']

  seq1 = find_record_by_id(babosa, id1_to_find)
  seq2 = find_record_by_id(humano, id2_to_find)

  if seq1 and seq2:
      alignments = pairwise2.align.globalxx(seq1.seq, seq2.seq)
      print(f"Alignment successful between {seq1.id} and {seq2.id}!")
  else:
      if not seq1:
        print(f"Error: Sequence with ID {id1_to_find} not found in babosa.")
      if not seq2:
        print(f"Error: Sequence with ID {id2_to_find} not found in humano.")
  scores.append(alignments[0][2])
Scores=pd.DataFrame(scores)
Scores.to_csv("Scores.csv")
