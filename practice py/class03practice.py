# control structure
# topic conditional statement (if,elif,else)

# if , else
salary_pakage = float(input('Enter_your_monthly_income.'))
if salary_pakage >= 100000.00:
    print('I am joining for you..')
else:
    print("Sorry.")    

# using if , elif  , else  
WeatherCondition = input('Enter weather condition...')
if WeatherCondition == 'rainy_day':
    print('apny_tamam_outdoor_work_kr_lain')
    print('STAY_SAFE_STAY_HOME--')
elif WeatherCondition == 'low_temperature':
    print('is_OK..')
 
else:
    print('apni life normal guzarein')  

weather_condition_1 = 'rainy_day'
weather_condition_2 = 'Cool_Temperature'
if weather_condition_1 == 'rainy_day' or weather_condition_2 == 'Cool_Temperature':
    print('Happy...')             
else:
    print('Hot_Temperature')    