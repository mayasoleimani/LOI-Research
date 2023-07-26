import datetime
from matplotlib import pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer

class DiaryClassifiers():

    def __init__(self,I=[],E=[],C=[],D=[],S=[],T=[],X=[]):
        self.entry_id=I
        self.entry=E
        self.word_count=C
        self.date=D
        self.start_time=S
        self.total_time=T
        self.compound=X

    def setDiary(self):

        sia=SentimentIntensityAnalyzer()
        count=-1
#                 [----------------------Put your own directory here---------------------]
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
                self.entry.append(x[16:-6])
                self.word_count.append(wc)
                self.date.append(x[:10])
                self.start_time.append(started)
                self.total_time.append(tot)
                self.compound.append(sentiment_score['compound'])

                count=count+1
                
    def getSearch():

        input_list=["words","started","duration","winter","summer","spring","fall","year range"]
        input_check=0
        print("\nWelcome to the LOI Sentiment Analyzer")
        print("\n {Year range, A Season {'Winter', 'Summer', 'Spring', 'Fall'}, Words, Started, Duration} \n")
        while input_check == 0:

            independent=input("Please choose an Independent variable from the above list\n ----> ")

            if independent.lower() not in input_list:
                print("\nMispelled entry or not in list, try again")
                input_check == 0 
            else:
                input_check=+1

        if independent.lower() == ("year range"):
            while input_check ==1:

                    years=input("\nPlease select a range of years in {2012-2022}\n ex: '2014-2016' OR '2017-2017' OR '2012-2022'\n ----> ")
                    firstyear=years[:4]
                    secondyear=years[5:]
                    try:
                        if (int(firstyear) and int(secondyear) not in range(2012,2023)) or len(years)!=9 or secondyear<firstyear:
                                print("\nMispelled entry or not in list, try again\n")
                                input_check == 1
                        else:
                            return years
            
                    except ValueError:
                        input_check == 1
                        print("\nRange mispelled, try again\n")

        

        else:
            return independent.lower()
        
    def setSearch(self):

        x_val=[]
        y_val=[]
        input1=DiaryClassifiers.getSearch()
        
        for x in range(0,len(self.compound)):

            if input1 == "words":
                x_val.append(self.word_count[x])
                y_val.append(self.compound[x])
             
            elif input1 == "started" and self.start_time[x] != '0000':
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
        x_label=''
        pos,neu,neg=0,0,0
        user_input=user_input.capitalize()

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
        
        
#       SPECIFY UNIQUE FACTORS FOR X'S
        if user_input in ('Winter','Spring','Fall','Summer'):
#           Insertion sort
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
            x_label="Dates in %s" % user_input
        elif len(user_input) == 9:
            x_tick_iterator=x_val[::len(x_val)//10]
            x_label="Entries in %s" % user_input
        elif user_input == 'Duration':
            x_tick_iterator=range(0,max(x_val),len(x_val)//15)
            x_label = "Duration (minutes)"
        elif user_input == 'Words':
            x_tick_iterator=range(min(x_val),max(x_val),(max(x_val)-min(x_val))//15)
            x_label="Word Count in Entries"
        elif user_input == 'Started':
            x_tick_iterator=range(0,2500,100)
            x_label="Time Started (Military)"

#PLOTTINGS
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

        DiaryClassifiers.bayes_prob(pos,neu,neg,x_val,y_val,user_input)

        plt.suptitle("          Selected Comparison: Polarity vs %s" % user_input, fontdict=font1)
        plt.title("Positive: %s , Neutral: %s , Negative: %s  " % (pos,neu,neg),fontdict=font2)
        plt.xticks(x_tick_iterator,fontsize =10,rotation = 90)
        plt.ylabel("Polarity",fontdict=font3)
        plt.xlabel("%s" % x_label,fontdict=font3)
        plt.tight_layout()
        plt.show()

    def bayes_prob(pos,neu,neg,x_val,y_val,user_input):
        
        all_scores=DiaryClassifiers().compound
        total_of_input=len(x_val)
        my_min=min(x_val)
        my_max=max(x_val)
        pos_t = sum(1 for score in all_scores if score >= 0.10)
        neu_t = sum(1 for score in all_scores if -0.10 < score < 0.10)
        neg_t = sum(1 for score in all_scores if score <= -0.10)

        print("\n*** Have you ever thought to yourself, perhaps 'What are the chances I'll feel negative given it's winter time?' ***\n") 
        print("Choose two events involving your input: %s\n " % user_input)

        if user_input in ('Words','Started','Duration'):
            print("Option 1 -> Event A  = %s { < , > } {%s - %s} and Event B = {positve, neutral, negative}" % (user_input, my_min, my_max))
            print("Option 2 -> Event A = {positve, neutral, negative} and Event B  = %s { < , > } {%s - %s}\n" % (user_input, my_min, my_max))
            print("Ex: Event A = Positive \n    Event B = %s < %s \n" % (user_input,my_max/2))
        else:
            print("Option 1 -> Event A = %s and Event B = {positve, neutral, negative}" % user_input)
            print("Option 2 -> Event A = {positve, neutral, negative} and Event B  = %s\n" % user_input)
            print("Ex: Event A = Positive\n    Event B = %s \n" % user_input)
#       Error check input #2
        user_input=user_input.lower()
        error_check=0
        while error_check==0:

            event_a=input("Event A = ").lower().strip()
            event_b=input("Event B = ").lower().strip()

            a=event_a.split()
            b=event_b.split()
            my_tuple=('positive','negative','neutral')
            other_tuple=('words','duration','started')
            if (event_a in my_tuple or event_b in my_tuple) and (a[0] == user_input or b[0] == user_input):
                if (len(a) == 1 and len(b) == 1) and (a[0] not in other_tuple and b[0] not in other_tuple):
                        error_check+=1
                elif len(a)==3 or len(b)==3:
                    if len(a) == 3:
                        if my_min < float(a[2]) < my_max+1:
                            error_check+=1
                        else:
                            print("\nEvent A out of range, try again\n")
                    else:
                        if my_min < float(b[2]) < my_max+1:
                            error_check+=1
                        else:
                            print("\nEvent B out of range, try again\n")
                else:
                    print("\nFormat incorrect, try again\n")

                        
            else:
                print("\nFormat incorrrect or not the input %s, try again\n" % user_input)

        


# SEASONS / TIME
        if user_input in ('winter','summer','spring','fall') or len(user_input) == 9:
            if event_a in ('positive','negative','neutral'):
                a_num=locals()[event_a[:3]]
                prob_a_b=a_num/total_of_input
            else:
                b_num=locals()[event_b[:3]]
                b_num_tot=locals()[(event_b[:3] + "_t")]
                prob_a_b=(b_num/b_num_tot)

# NUMERIC
        else:
            pos_temp,neu_temp,neg_temp=0,0,0
            temp_y_val=[]

            def process_event(event,pos_temp,neu_temp,neg_temp):
                #user condition
                event = event.split()
                event.pop(0)

                for i in range(len(x_val)):
                    event.insert(0, str(x_val[i]))
                    event = ' '.join(event)
                    
                    if eval(event):
                        temp_y_val.append(y_val[i])

                        if y_val[i] >= 0.10:
                            pos_temp += 1
                        elif -0.10 < y_val[i] < 0.10:
                            neu_temp += 1
                        elif y_val[i] <= -0.10:
                            neg_temp += 1
                        
                        event = event.split()
                        event.pop(0)
                    else:
                        event = event.split()
                        event.pop(0)
                return pos_temp,neu_temp,neg_temp

            if event_a not in ('positive', 'negative', 'neutral'):
                pos_temp,neu_temp,neg_temp=process_event(event_a,pos_temp,neu_temp,neg_temp)
            else:
                pos_temp,neu_temp,neg_temp=process_event(event_b,pos_temp,neu_temp,neg_temp)

            if event_a in ('positive','negative','neutral'):
                a_num=locals()[event_a[:3]+ "_temp"]
                prob_a_b=a_num/len(temp_y_val)
            
            else:
                b_num=locals()[event_b[:3] + "_temp"]
                b_num_tot=locals()[event_b[:3]]
                prob_a_b=b_num/b_num_tot

        prob_a_b*=100
        print("\n P ( %s | %s ) = %.2f %% \n" % (event_a, event_b, prob_a_b))

    def accuracy(self):

        with open('test.txt', 'r') as test_data:
            pred_score=[]
            actual_score=[]
            total=len(actual_score)
            correct=0

            for x in test_data:
                x=x.split(' ')
                polarity_label = x[0]
                rest_of_words = ' '.join(x[1:])

                for y in range(0,len(self.entry)):

                    if self.entry[y] == rest_of_words.replace("\n",''):
                        if self.compound[y] >= 0.10:
                            score="positive"
                        elif -0.10 < self.compound[y] < 0.10:
                            score="neutral"
                        elif self.compound[y] <= -0.10:
                            score ="negative"
                        pred_score.append(score)
                        actual_score.append(polarity_label)
                        break
            for x in range(len(pred_score)):
                if pred_score[x] == actual_score[x]:
                    correct+=1
            
            total=len(actual_score)
            accuracy=100 * correct/total
            print("Sentiment Accuracy: %f %%" % accuracy)

            return pred_score,actual_score

    def prec_recall(pred_score,actual_score):
                
        FP_pos,FP_neu,FP_neg=0,0,0
        FN_pos,FN_neu,FN_neg=0,0,0
        TP_pos,TP_neu,TP_neg=0,0,0

        for x in range(len(pred_score)):
            if pred_score[x] == actual_score[x]:
                if pred_score[x] =='positive':
                    TP_pos+=1
                elif pred_score[x] =='neutral':
                    TP_neu+=1
                elif pred_score[x] =='negative':
                    TP_neg+=1
            else:
                if pred_score[x] =='positive' and actual_score[x] != 'positive':
                    FN_pos+=1
                elif pred_score[x] =='neutral' and actual_score[x] != 'neutral':
                    FN_neu+=1
                elif pred_score[x] =='negative' and actual_score[x] != 'negative':
                    FN_neg+=1
                if actual_score[x] =='positive' and pred_score[x] != 'positive':
                    FP_pos+=1
                elif actual_score[x] =='neutral' and pred_score[x] != 'neutral':
                    FP_neu+=1
                elif actual_score[x] =='negative' and pred_score[x] != 'negative':
                    FP_neg+=1


                

        DiaryClassifiers.precision(TP_pos,FP_pos,label="positive")
        DiaryClassifiers.precision(TP_neu,FP_neu,label="neutral")
        DiaryClassifiers.precision(TP_neg,FP_neg,label="negative")

        DiaryClassifiers.recall(TP_pos,FN_pos,label="positive")
        DiaryClassifiers.recall(TP_neu,FN_neu,label="neutral")
        DiaryClassifiers.recall(TP_neg,FN_neg,label="negative")


    def precision(TP,FP,label):

        try:
            precision=TP/(TP+FP)
            print(label + " Precision: " + str(precision))
        except ZeroDivisionError:
            print( "Undefined Precision (0/0) for %s " % label )

    def recall(TP,FN,label):

        try:
            recall=TP/(TP+FN)
            print(label + " Recall: " + str(recall))

        except ZeroDivisionError:
            print( "Undefined Recall (0/0) for %s " % label)

def main():

    main_run=DiaryClassifiers()
    main_run.setDiary()
    main_run.setSearch()

#   evaluation
    pred_score,accuracy_score=DiaryClassifiers.accuracy(main_run)
    DiaryClassifiers.prec_recall(pred_score,accuracy_score)

if __name__=='__main__':
    main()