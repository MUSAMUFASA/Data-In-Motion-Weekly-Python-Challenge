def oldest_person(persons):
    # STEP 1 - Extracting Names and Date of Births into two separate lists, names and dobs.
    names = [each_person["name"] for each_person in persons]
    dobs = [each_person["date_of_birth"] for each_person in persons]
    # STEP 2 - Checking for the least year in the list, [dobs]. This represents the oldest date in the dictionary.
    years = [int (each_date[0:4]) for each_date in dobs]
    oldest_year = min (years)
    # STEP 3a - Checking for the number of times the oldest years appear in the list; An edge case could be that
    # different people have the same of years of birth.
    number_oldest_y = years.count (oldest_year)
    # STEP 4 - If the oldest year appears only once, then the person with that year should definitely be the oldest.
    # The block of code below matches the index of the year to the person, from the [names] list.
    if number_oldest_y == 1:
        index_name_oldest_person = years.index (oldest_year)
        name_oldest_person = names[index_name_oldest_person]
        dob_oldest_person = dobs[index_name_oldest_person]
        print (f"The oldest person is {name_oldest_person}, with a Date of Birth: {dob_oldest_person}.")
    # STEP 5 - Else, the months for the multiple persons having the same years are checked. The block of code below
    # extracts the month from the [doba] list and puts them in a list called [months].
    else:
        months = [int (each_date[5:7]) for each_date in dobs]
        oldest_month = min (months)
        number_oldest_m = months.count (oldest_month)
        # STEP 5a - If the oldest month appears only once, the person with that is the oldest.The block of code below
        # matches the index of the month to the person, from the [names] list.
        if number_oldest_m == 1:
            index_name_oldest_person = months.index (oldest_month)
            name_oldest_person = names[index_name_oldest_person]
            dob_oldest_person = dobs[index_name_oldest_person]
            print (f"The oldest person is {name_oldest_person}, with a Date of Birth: {dob_oldest_person}.")
        else:
            # STEP 5b - It could also be that multiple persons were born in the same month and same year. The block
            # of code below extracts the day and appends it to a [days] list.
            days = [int (each_date[-2:]) for each_date in dobs]
            # STEP 5c - The code below checks for the oldest day.
            oldest_day = min (days)
            # STEP 5d - The block of code below matches the oldest day with the person in the [names] list.
            index_name_oldest_person = days.index (oldest_day)
            name_oldest_person = names[index_name_oldest_person]
            dob_oldest_person = dobs[index_name_oldest_person]
            print (f"The oldest person is {name_oldest_person}, with a Date of Birth: {dob_oldest_person}.")


persons = [
{"name": "Kedeisha", "date_of_birth": "1994-05-20"},
{"name": "Homer", "date_of_birth": "1956-05-12"},
{"name": "Bruce", "date_of_birth": "1915-04-07"},
]


oldest_person (persons)

