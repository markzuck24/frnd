# coding=utf-8

from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu

# candidate = "Mursí wrote Friday in a symbolic oath in Tahrir Square, where the revolution began, that ended Mubarak 's authoritarian rule last year, and vowed that he grasps the presidential powers of his office by the military council, which took over from the exiled leader."
# reference1 = "Morsi took a symbolic oath on Friday in Tahrir Square, birthplace of the uprising that ended Mubarak's authoritarian rule last year, and vowed to reclaim presidential powers stripped from his office by the military council that took over from the ousted leader."
# reference2 = "On Friday, Morsi took a symbolic oath on Tahrir Square, the birthplace of the uprising that ended Mubarak's authoritarian rule last year, and vowed to reclaim presidential powers stripped of his office by the military council which took over from the ousted leader."
# reference3 = "On Friday, Morsi took a symbolic oath on Tahrir Square, the birthplace of the uprising that ended Mubarak's authoritarian rule last year, and vowed to reclaim presidential powers stripped of his office by the military council which took over from the ousted leader."
# reference4 = "On Friday, Morsi took a symbolic oath on Tahrir Square, the birthplace of the uprising that ended Mubarak's authoritarian rule last year, and vowed to reclaim presidential powers stripped of his office by the military council which took over from the ousted leader."
# reference5 = "On Friday, Morsi took a symbolic oath on Tahrir Square, the birthplace of the uprising that ended Mubarak's authoritarian rule last year, and vowed to reclaim presidential powers stripped of his office by the military council which took over from the ousted leader."
# reference6 = "On Friday, Morsi took a symbolic oath on Tahrir Square, the birthplace of the uprising that ended Mubarak's authoritarian rule last year, and vowed to restore presidential powers stripped of his office by the military council which took over the ousted leader."


# # Using readlines() 
# file1 = open('de-enR.txt', 'r') 
# Lines = file1.readlines() 
  
# # count = 0
# # Strips the newline character 
# for line in Lines: 
#     c= word_tokenize(line)



# r1= word_tokenize(reference1)
# r2= word_tokenize(reference2)
# r3= word_tokenize(reference3)
# r4= word_tokenize(reference4)
# r5= word_tokenize(reference5)
# r6= word_tokenize(reference6)

c=
weights = (0.2,0.3,0.4,0.1)

r=[r1,r2,r3,r4,r5,r6]
ref=[r1]

score1 = sentence_bleu(r,c,weights)
score2 = sentence_bleu(ref,c,weights)

print "\nBLEU score with single Reference sentence = ", score2*100
print "BLEU score with Multiple Reference sentences = ", score1*100
print "\n"
