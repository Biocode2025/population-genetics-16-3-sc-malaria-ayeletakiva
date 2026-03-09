#מספר הדורות עליהם נריץ את הסימולציה
Generation = int(input("enter the number of gens fot the simulation:"))
#שכיחות האלל HbS ההתחלתית
Freq_HbS = 0.06

#פתיחת קובץ להכנסת התוצאות
r_file = open("results/csv.Sickle_cell_freq_het","w")
r_file.write("Generation\tFreq_HbS\tFreq_HbA\tFreq_AA\tFreq_AS\tFreq_SS\n")

#סימולציה לחישוב התפלגות הגנוטיפים ושכיחות האלל לאורך הדורות
for gen in range(Generation + 1):
    q = Freq_HbS
    p = 1-q
    #כמות הגנוטיפים לאחר הסלקציה
    Amount_SS = 0*(q**2)
    Amount_AA = 0.98*(p**2)
    Amount_AS = 1*(2*q*p)
    #חישוב כמות יחסית
    tot_amount = Amount_SS + Amount_AS + Amount_AA
    
    Freq_SS = Amount_SS/tot_amount
    Freq_AS = Amount_AS/tot_amount
    Freq_AA = Amount_AA/tot_amount
    r_file.write("%d\t%f\t%f\t%f\t%f\t%f\n"%(gen,Freq_HbS,p,Freq_AA,Freq_AS,Freq_SS))
    Freq_HbS = q/(0.98*p +2*q)

r_file.close()