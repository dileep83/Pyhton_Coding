from datetime import datetime,timedelta

if __name__ == '__main__':
    today = datetime.today()
    first = today.replace(day=1)
    lastmonth = first - timedelta(days=1)
    prev_date = datetime.now()-timedelta(days=1)

    start_date = today-timedelta(days=7)
    end_date = today-timedelta(days=1)
    
    print( today , first ,lastmonth , prev_date)
    
    print( start_date , end_date)
    
    filename = "Player_LeaderBoard_Points_"+str(prev_date.strftime('%Y-%m-%d'))+'.xlsx'
    print(filename)