from collections import abc
my_dirct = {}
print(type(my_dirct))
boolen = isinstance(my_dirct, abc.Mapping)
print(boolen)

DIAL_CODES = [                
         (86, 'China'),
         (91, 'India'),
         (1, 'United States'),
         (62, 'Indonesia'),
         (55, 'Brazil'),
         (92, 'Pakistan'),
         (880, 'Bangladesh'),
         (234, 'Nigeria'),
         (7, 'Russia'),
         (81, 'Japan'),
     ]
country_code = {country: code for code, country in DIAL_CODES}  
#print(country_code)
#change country name instead of upper 
upper_country_code = {code:country.upper() for country, code in country_code.items()}
#print(upper_country_code)
print(upper_country_code[86])