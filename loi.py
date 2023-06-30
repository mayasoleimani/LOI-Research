import re
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


sia=SentimentIntensityAnalyzer()


#                   Needed:                 #
#       init with variables {EntryID,Entry,WordCount,Date,StartTime,TotalTime,Compound}
#       Store function
#Date seperator function - comes in when graphing
#Bool return function = empty entries
#Graph function

#       running main



class DiaryClassifiers():

    def __init__(self,I=[],E=[],C=[],D=[],S=[],T=[],X=[]):
        self.entry_id=I
        self.entry=E
        self.word_count=C
        self.date=D
        self.start_time=S
        self.total_time=T
        self.compound=X
        # self.diary={self.entry_id:
        #             {
        #             'entry':self.entry,
        #             'word count':self.word_count,
        #             'date':self.date,
        #             'start_time':self.start_time,
        #             'total time':self.total_time,
        #             'compound':self.compound
        #             }
        #             }   

    def DiaryAssignment(self):

        count=-1

        with open("/Users/Hp/OneDrive/UMD/Summer 2023/ENGR_492/TextCorpus/grand_diary.txt") as grandjournal:
            
            for x in grandjournal:
                
                entry=x[16:-5]
                started=x[11:15]
                wc=len(x[16:-5].split())

#               no duration recorded
                if x[11:15]!='0000' and x[len(x)-5:-1]!='0000':
                    
                    ended=x[len(x)-5:-1]
                    tot=int(ended)-int(started)
                
                else:
#                   error number for lack of total time
                    tot='5555'

                
                sentiment_score=sia.polarity_scores(entry)
                
                self.entry_id.append(count+1)
                self.entry.append(x[16:-5])
                self.word_count.append(wc)
                self.date.append(x[:11])
                self.start_time.append(started)
                self.total_time.append(int(tot))
                self.compound.append(sentiment_score['compound'])

                count=count+1

                # self.diary[self.entry_id]['entry']=x[16:-5]
                # self.diary[self.entry_id]['word count']=wc
                # self.diary[self.entry_id]['date']=x[:11]
                # self.diary[self.entry_id]['start_time']=started
                # self.diary[self.entry_id]['total_time']=tot
                # self.diary[self.entry_id]['compound']=sentiment_score['compound']


                # self.entry_id=self.entry_id+1
                # self.diary[self.entry_id]={}
        print('here')
                       
    def InvertedSearch():

        input_list=["all-time", "all time", "alltime","word count","winter","summer","spring","fall","year range", "yearrange","yearange"]
        input_check=0
        print("Welcome to the LOI Sentiment Analyzer")
        print("\n {Year range, Season {'Winter', 'Summer', 'Spring', 'Fall'}, Word Count } \n")
        while input_check == 0:

            independent=input("\nPlease choose an Independent variable from the above list\n ----> ")

            if independent.lower() not in input_list:
                print("\nMispelled entry or not in list, try again")
                input_check == 0 
            else:
                input_check=+1

        if independent.lower() == ("year range" or "yearrange" or "yearange"):
            while input_check ==1:

                
                    years=input("Please select a range of years in {2012-2022}\n ex: '2014-2016' OR '2016-2017' OR '2012-2022'\n ----> ")
                    if (int(years[:4]) or int(years[5:])) not in range(2012,2023):
                        print("\nMispelled entry or not in list, try again\n")
                        input_check == 1
                    else:
                        return years


        else:
            return independent
        
    def Visual(self):

        #### lack of data codes ####
        #  5555 in total_time = no duration
        #  0000 in start_time = no start
        #  '00'/xx/xxx in date = no season

        x_val=None
        y_val=None

        input1=DiaryClassifiers.InvertedSearch()

        print(input1)

        plt.scatter(sorted(self.word_count),self.compound)
        plt.xticks(rotation = 90) # Rotates X-Axis Ticks by 45-degrees
        plt.xticks(fontsize=10)
        plt.ylabel("Polarity")
        plt.xlabel("independent")
        plt.title("Selected Comparison: ")
        plt.legend()
        plt.show()

        pass
     
def main():

    main_run=DiaryClassifiers()

    main_run.DiaryAssignment()
    main_run.Visual()

    print("me")


if __name__=='__main__':
    main()