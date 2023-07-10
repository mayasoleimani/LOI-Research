import numpy as np
import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


sia=SentimentIntensityAnalyzer()


#                   Needed:                 #
# Graph
#   fix scale for graph
#   need legend for pos,neu,neg
#   add a byes statistic function



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
                
    def getSearch():

        input_list=["word count","start time","duration","winter","summer","spring","fall","year range"]
        input_check=0
        print("\nWelcome to the LOI Sentiment Analyzer")
        print("\n {Year range, Season {'Winter', 'Summer', 'Spring', 'Fall'}, Word Count, Start Time, Duration} \n")
        while input_check == 0:

            independent=input("Please choose an Independent variable from the above list\n ----> ")

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
            return independent.lower()
        
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
                    x_val.append(self.date[x][:5])
                    y_val.append(self.compound[x])
                elif input1 == 'spring' and my_month in ('03','04','05'):
                    x_val.append(self.date[x][:5])
                    y_val.append(self.compound[x])
                elif input1 == 'summer' and my_month in ('06','07','08'):
                    x_val.append(self.date[x][:5])
                    y_val.append(self.compound[x])
                elif input1 == 'fall' and my_month in ('09','10','11'):
                    x_val.append(self.date[x][:5])
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
        #user_input=user_input.lower()

        font1 = {'family': 'serif',
                'color':  '#810000',
                'weight': 'bold',
                'size': 18,
                }
        font2 = {'family': 'serif',
                'color':  '#540000',
                'weight': 'normal',
                'size': 12,
                }
        font3 = {'family': 'serif',
                'color':  'k',
                'weight': 'bold',
                'size': 12,
                }
#each request's specified parameters

        if user_input in ('winter','spring','fall','summer'):

            for i in range(1,len(x_val)):
                key = x_val[i]
                key_y=y_val[i]
                j = i - 1
                while j >= 0 and x_val[j] > key :
                    x_val[j + 1] = x_val[j]
                    y_val[j+1] = y_val[j]
                    j -= 1
                x_val[j + 1] = key
                y_val[j+ 1] = key_y
            
            x_tick_iterator=x_val[::len(x_val)//15]

        elif len(user_input) == 9:

            x_tick_iterator=x_val[::len(x_val)//15]

        elif user_input == 'duration':
            x_tick_iterator=range(0,max(x_val),len(x_val)//15)
            user_input = "Duration (minutes)"

        elif user_input == 'word count':
            x_tick_iterator=range(min(x_val),max(x_val),(max(x_val)-min(x_val))//15)

        elif user_input == 'start time':
            x_tick_iterator=range(0,2500,100)



#Plottings

        for entry in range(0,len(y_val)):
            if y_val[entry] >= .10:
                pos+=1
                plt.scatter(x_val[entry],y_val[entry], c='#11C600', s=35,edgecolors='k')
            elif y_val[entry] < .10 and y_val[entry] > -.10:
                neu+=1
                plt.scatter(x_val[entry],y_val[entry], c='#EDEB22', s=35,edgecolors='k')
            elif y_val[entry] <= -.10:
                neg+=1
                plt.scatter(x_val[entry],y_val[entry], c='#3A60FF', s=35,edgecolors='k')

        
        plt.suptitle("          Selected Comparison: Polarity vs %s" % user_input.capitalize(), fontdict=font1)
        plt.title("Positive: %s , Neutral: %s , Negative: %s  " % (pos,neu,neg),fontdict=font2)
        plt.xticks(x_tick_iterator,fontsize =10,rotation = 90)
        plt.ylabel("Polarity",fontdict=font3)
        plt.xlabel("%s" % user_input.capitalize(),fontdict=font3)
        plt.tight_layout()
        plt.show()

def main():

    main_run=DiaryClassifiers()

    main_run.setDiary()
    main_run.setSearch()

if __name__=='__main__':
    main()