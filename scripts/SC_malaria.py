#מספר הדורות עליהם נריץ את הסימולציה
Generation = int(input("enter the number of gens fot the simulation:"))
#שכיחות האלל HbS ההתחלתית
Freq_HbS = 0.06

#פתיחת קובץ להכנסת התוצאות
r_file = open("results/csv.Sickle_cell_freq_het","w")
r_file.write("Generation\tFreq_HbS\tFreq_HbA\tFreq_AA\tFreq_AS\tFreq_SS\n")



r_file.close()