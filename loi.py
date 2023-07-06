import numpy as np
import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


sia=SentimentIntensityAnalyzer()


#                   Needed:                 #
# Graph
#   fix scale for graph
#   need legend for pos,neu,neg



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

    def setDiary(self):

        count=-1

        with open("/Users/Hp/OneDrive/UMD/Summer 2023/ENGR_492/TextCorpus/grand_diary.txt") as grandjournal:
            
            for x in grandjournal:
                
                entry=x[16:-5]
                started=x[11:15]
                wc=len(x[16:-5].split())
                ended=x[len(x)-5:-1]

#               duration condition
                if started !='0000' and ended!='0000':
                    if started < ended:
                        starttime = datetime.datetime.strptime(started, '%H%M')
                        endtime = datetime.datetime.strptime(ended, '%H%M')
                        tot=(endtime-starttime).total_seconds()/60
                    else:
                        started=int(started)
                        ended=int(ended)
                        ended+=2360
                        tot=int(ended)-int(started)
                else:
                    tot='5555'

                
                sentiment_score=sia.polarity_scores(entry)
                
                self.entry_id.append(count+1)
                self.entry.append(x[16:-5])
                self.word_count.append(wc)
                self.date.append(x[:10])
                self.start_time.append(started)
                self.total_time.append(tot)
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
                
    def getSearch():

        input_list=["word count","start time","duration","winter","summer","spring","fall","year range"]
        input_check=0
        print("Welcome to the LOI Sentiment Analyzer")
        print("\n {Year range, Season {'Winter', 'Summer', 'Spring', 'Fall'}, Word Count, Start Time, Duration} \n")
        while input_check == 0:

            independent=input("\nPlease choose an Independent variable from the above list\n ----> ")

            if independent.lower() not in input_list:
                print("\nMispelled entry or not in list, try again")
                input_check == 0 
            else:
                input_check=+1

        if independent.lower() == ("year range"):
            while input_check ==1:
                
                    years=input("Please select a range of years in {2012-2022}\n ex: '2014-2016' OR '2016-2017' OR '2012-2022'\n ----> ")
                    if (int(years[:4]) or int(years[5:])) not in range(2012,2023):
                        print("\nMispelled entry or not in list, try again\n")
                        input_check == 1
                    else:
                        return years


        else:
            return independent
        
    def setSearch(self):

        x_val=[]
        y_val=[]
        input1=DiaryClassifiers.getSearch()
        
        for x in range(0,len(self.compound)):

            if input1 == "word count":
                x_val.append(self.word_count[x])
                y_val.append(self.compound[x])
             
            elif input1 == "start time" and self.start_time[x] != '0000':
                x_val.append(int(self.start_time[x]))
                y_val.append(self.compound[x])

            elif input1 == "duration" and self.total_time[x] != '5555':
                x_val.append(self.total_time[x])
                y_val.append(self.compound[x])

            elif input1 in ('winter','spring','summer','fall'):

                my_month=self.date[x][:2]

                if input1 == 'winter' and my_month in ('12','01','02'):
                    x_val.append(self.date[x])
                    y_val.append(self.compound[x])
                elif input1 == 'spring' and my_month in ('03','04','05'):
                    x_val.append(self.date[x])
                    y_val.append(self.compound[x])
                elif input1 == 'summer' and my_month in ('06','07','08'):
                    x_val.append(self.date[x])
                    y_val.append(self.compound[x])
                elif input1 == 'fall' and my_month in ('09','10','11'):
                    x_val.append(self.date[x])
                    y_val.append(self.compound[x])

                
            elif len(input1) == 9:
                first_year=int(input1[:4])
                second_year=int(input1[5:])

                if int(self.date[x][6:10]) in range(first_year,second_year+1):
                    x_val.append(self.date[x])
                    y_val.append(self.compound[x])

        return DiaryClassifiers.visual(x_val,y_val,input1)
        
    def visual(x_val,y_val,user_input):

        x_tick_iterator=None

        pos,neu,neg=0,0,0
        for i in range(0,len(y_val)):
            if y_val[i] >= .05:
                pos+=1
                plt.scatter(x_val[i],y_val[i],c='#15F500', s=35,edgecolors='b')

            elif y_val[i] < .05 and y_val[i] > -.05:
                neu+=1
                plt.scatter(x_val[i],y_val[i], c='#F5F300',  s=35,edgecolors='b')

            elif y_val[i] <= -.05:
                neg+=1
                plt.scatter(x_val[i],y_val[i], c='#F52900', s=35,edgecolors='b')

        #x tick marking
        if user_input in ('word count', 'start time', 'duration'):
            x_tick_iterator=range(min(x_val),max(x_val),(max(x_val)-min(x_val))//15)
        elif user_input in ('winter','spring','fall','summer'):
            pass
        
        plt.xticks(x_tick_iterator,fontsize =10,rotation = 90) # Rotates X-Axis Ticks by 45-degrees
        plt.ylabel("Polarity")
        plt.xlabel("%s" % user_input.capitalize())
        plt.title("Selected Comparison: Polarity vs %s" % user_input)
        plt.legend(loc="best")
        plt.show()
        pass

def main():

    main_run=DiaryClassifiers()

    main_run.setDiary()
    main_run.setSearch()

    print("me")


if __name__=='__main__':
    main()