import re
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
sia=SentimentIntensityAnalyzer()

#                   Needed:                 #
#init with variables {EntryID,Entry,WordCount,Date,StartTime,TotalTime,Compound}
#Store function
#Date seperator function - comes in when graphing
#Bool return function = empty entries
#Graph function

#running main



class DiaryClassifiers(object):

    def __init__(self,I=0,E=0,C=0,D=0,S=0,T=0,X=0):
        self.entry_id=I
        self.entry=E
        self.word_count=C
        self.date=D
        self.start_time=S
        self.total_time=T
        self.compound=X
        self.diary={self.entry_id:
                    {
                    'entry':self.entry,
                    'word count':self.word_count,
                    'date':self.date,
                    'start_time':self.start_time,
                    'total time':self.total_time,
                    'compound':self.compound
                    }
                    }   

    def DiaryAssignment(self):


        with open("/Users/Hp/OneDrive/UMD/Summer 2023/ENGR_492/TextCorpus/grand_diary.txt") as grandjournal:
            
            for x in grandjournal:
                
                sent=sia.polarity_scores(x)

                self.diary[self.entry_id]['entry']=x[16:-5]
                self.diary[self.entry_id]['word count']=0
                self.diary[self.entry_id]['date']=x[:11]
                self.diary[self.entry_id]['start_time']=x[11:15]
                self.diary[self.entry_id]['total_time']=0
                self.diary[self.entry_id]['compound']=sent['compound']


                self.entry_id=self.entry_id+1
                self.diary[self.entry_id]={}



    def Visual(self):

        #If individual



        #If line graph


        pass


            
def main():

    main_run=DiaryClassifiers()

    main_run.DiaryAssignment()

if __name__=='__main__':
    main()