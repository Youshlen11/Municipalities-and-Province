import requests

get_request_api = requests.post("https://sfrs-j75dy.ondigitalocean.app/api/listDistricts")
#print(get_request_api.status_code)
#print(get_request_api.json())

count_array = 0
number_of_Districts = 1

print('|-----------------------------------------|-------------------------------|')
print ("{:<10} {:<30} {:<10} {:<20} {:<10}".format('|','Municipalities','|','Province','|'))
print('|-----------------------------------------|-------------------------------|')

for count_array in range(0,11):
    get_district_municipalities = get_request_api.json()['data'][int(count_array)]['name']
    get_province = get_request_api.json()['data'][int(count_array)]['province']['name']
    get_district_municipalities = str(number_of_Districts) + ") "+ get_district_municipalities + " District"
    number_of_Districts += 1

    print ("{:<10} {:<30} {:<10} {:<20} {:<10}".format('|',get_district_municipalities,'|',get_province,'|'))
    
    count_array += 1                                                                                                                                                                                                             
    get_district_municipalities = ""

print('|-----------------------------------------|-------------------------------|')
print(r"""\

                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /


            """)
