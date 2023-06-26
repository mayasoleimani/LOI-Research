import re
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib as plt


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

                self.diary[self.entry_id]['entry']=x[16:-5]
                self.diary[self.entry_id]['word count']=wc
                self.diary[self.entry_id]['date']=x[:11]
                self.diary[self.entry_id]['start_time']=started
                self.diary[self.entry_id]['total_time']=tot
                self.diary[self.entry_id]['compound']=sentiment_score['compound']


                self.entry_id=self.entry_id+1
                self.diary[self.entry_id]={}



    def Visual(self):

        #If individual



        #If line graph


        pass

    def InvertedSearch(self):
        
        print("Welcome to the LOI Sentiment Analyzer")
        print("\n { All-time, Year range (2012-2022), Season, Word Count, Diary Length } \n")
        independent=input("Please choose an Independent variable from the above list: ")

        pass




            
def main():

    main_run=DiaryClassifiers()

    main_run.DiaryAssignment()
    main_run.InvertedSearch()

    print("me")


if __name__=='__main__':
    main()