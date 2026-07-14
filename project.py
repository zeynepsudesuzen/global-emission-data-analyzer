import matplotlib.pyplot as plt

# DOSYA OKUMA FONKSİYONLARI

def load_data():
    raw_data = [] #ham veri listem 
    try:
        with open("annual-co2-emissions-per-country.csv", 'r') as file:    
            file.readline()
            for line in file:
                data = line.strip().split(',')
                raw_data.append(data)
    except FileNotFoundError:
        print("\nERROR: 'annual-co2-emissions-per-country.csv' file not found!")
    return raw_data

def load_population():
    raw_data = []
    try:
        with open("population.csv", "r") as file:
            file.readline()
            for line in file:
                data = line.strip().split(',')
                raw_data.append(data)
    except FileNotFoundError:
        print("\nERROR: 'population.csv' file not found!")
    return raw_data

# CRUD MENU FONKSİYONLARI BURADAN BAŞLIYOR.

def crud_menu(country_data):
    while True:
        print("""\n1. Create Data
2. Read Data
3. Update Data
4. Delete Data
5. Back to Main Menu""")
        
        answer = input("\nSelect a database operation:")

        if answer == '1':
            create_data(country_data)
        elif answer == '2':
            read_data(country_data)
        elif answer == '3':
            update_data(country_data)
        elif answer == '4':
            delete_data(country_data)
        elif answer == '5':
            print("\nBacking to the main menu...")
            break
        else:
            print("\nPlease enter a valid number!")




def create_data(country_data):
    country = input("\nEnter country name:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return 

    code = input("Enter country code:").strip().upper()
    if not code.replace('_','').isalpha(): 
        print("\nERROR: Invalid input! Code must be letters.")
        return

    try:
        year = int(input("Enter a year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    try:
        emission = float(input("Enter emissions:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Emission must be numbers.")
        return

    country = country[0].upper() + country[1:]
    new_record = [country, code, str(year), str(emission)]

    record_control = False
    for line in country_data:
        if line[0].lower() == country.lower() and line[2] == str(year):
            print("\nThe record already exists!")
            record_control = True
            break

    if not record_control:   
        country_data.append(new_record)

        with open("annual-co2-emissions-per-country.csv", 'a') as file:
            file.write(f"{country},{code},{year},{emission}\n")

        print("\nData successfully added!")

    


def read_data(country_data):
    while True:
        print ("""\n---Read Data Menu---
1. Displaying all records for a selected year 
2. Displaying all available records for a selected country 
3. Displaying records whose CO₂ emission values fall within a user-defined range
4. Back to main menu""")
        
        question = input("\nSelect the number of one of the operation:").strip()

        header = f"{'Country':<25} | {'Code':<6} | {'Year':<6} | {'Emission':<15}"
        separator = ("-" * 62)

        if question == '1':
            try:
                year = int(input("\nEnter a year:").strip())
            except ValueError:
                print("\nERROR: Invalid input! Year must be numbers.")
                continue

            record_control = False
            for line in country_data:
                if year == int(line[2]):
                    if not record_control:
                        print("\n" + header)
                        print(separator)
                    print(f"{line[0]:<25} | {line[1]:<6} | {line[2]:<6} | {line[3]:<15}")
                    record_control = True
            if not record_control:
                print("\nNo matching record is found!")

        elif question == '2':
            country = input("\nEnter country:").strip().lower()
            if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
                print("\nERROR: Invalid input! Country must be letters.")
                continue
                
            record_control = False
            for line in country_data:
                if country == line[0].lower():
                    if not record_control:
                        print("\n" + header)
                        print(separator)
                    print(f"{line[0]:<25} | {line[1]:<6} | {line[2]:<6} | {line[3]:<15}")
                    record_control = True
            if not record_control:
                print("\nNo matching record is found!")

        elif question == '3':              
            try:
                emission1 = float(input("\nEnter min emission:").strip())
            except ValueError:
                print("\nERROR: Invalid input! Min emission must be numbers.")
                continue

            try:
                emission2 = float(input("Enter max emission:").strip())
            except ValueError:
                print("\nERROR: Invalid input! Max emission must be numbers.")
                continue

            min_e = min(emission1, emission2)
            max_e = max(emission1, emission2)

            record_control = False
            for line in country_data:
                if min_e <= float(line[3]) <= max_e:
                    if not record_control:
                        print("\n" + header)
                        print(separator)
                    print(f"{line[0]:<25} | {line[1]:<6} | {line[2]:<6} | {line[3]:<15}")
                    record_control = True
            if not record_control:
                print("\nNo matching record is found!")
                
        elif question == '4':
            print("\nBacking to the main menu...")
            break
        else:
            print("\nPlease enter a valid number!")




def update_data(country_data):
    country = input("\nEnter country name:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        year = int(input("Enter a year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    record_control = False
    for line in country_data:
        if country == line[0].lower() and year == int(line[2]):
            try:
                emission = float(input("Enter new emission value:").strip())
                line[3] = str(emission)
                record_control = True 
                
                with open("annual-co2-emissions-per-country.csv", 'w') as file:
                    file.write("Entity,Code,Year,Annual CO2 emissions\n")
                    for row in country_data:
                        file.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")

                print("\nData successfully updated!")
                break
            except ValueError:
                print("\nERROR: Invalid input! Emission must be numbers.")
                return

    if not record_control:
        print("\nNo matching record is found!")
    



def delete_data(country_data):
    country = input("\nEnter country name:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        year = int(input("Enter a year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    record_control = False
    for line in country_data:
        if line[0].lower() == country and int(line[2]) == year:
            country_data.remove(line)
            record_control = True

            with open("annual-co2-emissions-per-country.csv", 'w') as file:
                file.write(f"Entity,Code,Year,Annual CO2 emissions\n")
                for row in country_data:
                    file.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")

            print("\nData successfully deleted.")
            break
            
    if not record_control:
        print("\nNo matching record is found!")




# ANALYSİS MENU FONKSİYONLARI BURADAN BAŞLIYOR.



def analysis_menu(country_data,population_data):
    while True:
        print("""\n1. Countries Above Threshold
2. Country Comparison
3. Year-to-Year Comparison
4. Average Emission
5. Emission Intensity
6. Trend Analysis over Time
7. Sorting Emission Data
8. Back to main menu""")
        
        answer = input("\nSelect an analysis task:")

        if answer == '1':
            countries_above_threshold(country_data)
        elif answer == '2':
            country_comparison(country_data)
        elif answer == '3':
            year_to_year_comparison(country_data)
        elif answer == '4':
            average_emission(country_data)
        elif answer == '5':
            emission_intensity(country_data,population_data)
        elif answer == '6':
            trend_analysis_over_time(country_data)
        elif answer == '7':
            sorting_emission_data(country_data)
        elif answer == '8':
            print("\nBacking to the main menu...")
            break
        else:
            print("\nPlease enter a valid number!")




def countries_above_threshold(country_data):
    try:
        year = int(input("\nEnter a year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    try:
        emission = float(input("Enter the emission threshold value:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Emission must be numbers.")
        return

    record_control = False
    for line in country_data:
        if year == int(line[2]):
            if float(line[3]) > emission:
                if not record_control:
                    print(f"\n---Countries exceeding {emission} in {year}---")
                    print("-" * 40)
                print(f"{line[0]}: {line[3]}")
                record_control = True
                
    if not record_control:
        print("No matching record is found for this year or threshold!")
   



def country_comparison(country_data):
    try:
        year = int(input("\nEnter a year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    country1 = input("Enter the first country:").strip().lower()
    if not country1.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    country2 = input("Enter the second country:").strip().lower()
    if not country2.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    emission1 = None
    emission2 = None

    for line in country_data:
        if year == int(line[2]):
            if country1 == line[0].lower():
                emission1 = float(line[3])
            if country2 == line[0].lower():
                emission2 = float(line[3])
                
    if emission1 is not None and emission2 is not None:
        c1 = country1[0].upper() + country1[1:]
        c2 = country2[0].upper() + country2[1:]
        print(f"\n--- Comparison Results for {year} ---")
        print("-" * 40)
        print(f"{c1} : {emission1}")
        print(f"{c2} : {emission2}")
        print("-" * 40)

        if emission1 > emission2:
            print(f"RESULT: {c1} has higher emissions.")
        elif emission2 > emission1:
            print(f"RESULT: {c2} has higher emissions.")
        else:
            print("RESULT: Both countries are equal.")
    else:
        print("One or both countries could not be found for this year!")




def year_to_year_comparison(country_data):
    country = input("\nEnter the country:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        year1 = int(input("Enter the first year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    try:
        year2 = int(input("Enter the second year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    emission1 = None
    emission2 = None
    for line in country_data:
        if country == line[0].lower():
            if year1 == int(line[2]):
                emission1 = float(line[3])
            if year2 == int(line[2]):
                emission2 = float(line[3])

    if emission1 is not None and emission2 is not None:
        emission_difference = emission1 - emission2
        if emission1 != 0:
            percentage_change = (emission_difference * 100) / emission1
            p_text = f"{percentage_change:.2f}%"
        else:
            p_text = "Undefined (Division by zero)"
            
        print(f"\n--- Analysis Results for {country[0].upper() + country[1:]} ---")
        print("-" * 40)
        print(f"Year {year1} Emission : {emission1}")
        print(f"Year {year2} Emission : {emission2}")
        print(f"Difference : {emission_difference:.2f}")
        print(f"Percentage Change : {p_text}")
        print("-" * 40)
    else:
        print("No matching record is found for this country or the selected years!!")




def average_emission(country_data):
    country = input("\nEnter country:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        year1 = int(input("Enter the start year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    try:
        year2 = int(input("Enter the end year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    start_year = min(year1, year2)
    end_year = max(year1, year2)
    total_emission = 0
    counter = 0
    
    for line in country_data:
        if country == line[0].lower():
            row_year = int(line[2])
            if start_year <= row_year <= end_year:
                emission = float(line[3])
                total_emission += emission
                counter += 1   
                
    if counter > 0:
        average = total_emission / counter
        print(f"\n--- Average Emission Results for {country[0].upper() + country[1:]} ---")
        print("-" * 40)
        print(f"Period : {start_year} - {end_year}")
        print(f"Total Records : {counter}")
        print(f"Average : {average:.2f}")
        print("-" * 40)
    else:
        print("\nNo matching record is found for this country or the selected years!!")





def emission_intensity(country_data,population_data):
    country = input("\nEnter the country:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        year = int(input("Enter a year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    emission = None
    population = None
    intensity = 0
    
    for line in country_data:
        if country == line[0].lower() and year == int(line[2]):
            emission = float(line[3])
            break

    for line in population_data:
        if country == line[0].lower() and year == int(line[2]):
            population = int(line[3])
            break
    
    if emission is not None and population is not None:
        if population > 0:
            intensity = emission / population

            print(f"\n--- Emission Intensity Results for {country[0].upper() + country[1:]} ---")
            print("-" * 40)
            print(f"Year : {year}")
            print(f"Total Emission : {emission}")
            print(f"Total Population : {population}")
            print(f"Per-capita CO2 : {intensity:.6f}") 
            print("-" * 40)
        else:
            print("\nERROR: Population cannot be zero for calculation!")
    else:
        print("\nNo matching record is found for this country or the selected years!!")
        




def trend_analysis_over_time(country_data):
    country = input("\nEnter the country:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        year = int(input("Enter ending year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    year1 = year - 1 
    year2 = year - 2 
    emission, emission1, emission2 = None, None, None

    for line in country_data:
        if country == line[0].lower():
            if year == int(line[2]):
                emission = float(line[3])
            elif year1 == int(line[2]):
                emission1 = float(line[3])
            elif year2 == int(line[2]):
                emission2 = float(line[3])

    if emission is not None and emission1 is not None and emission2 is not None:  
        print(f"\n--- Trend Analysis for {country[0].upper() + country[1:]} ---")
        print("-" * 40)
        print(f"{year2}: {emission2}")
        print(f"{year1}: {emission1}")
        print(f"{year} : {emission}")
        print("-" * 40)
        if emission < emission1 < emission2:
            print("RESULT: Consistent DECREASE in emissions.")
        elif emission > emission1 > emission2:
            print("RESULT: Consistent INCREASE in emissions.")
        else:
            print("RESULT: No consistent trend found.")
    else:
        print("\nNo matching record is found for the last 3 years of this country!!")
            


            

def sorting_emission_data(country_data):
    country = input("\nEnter country:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        year1 = int(input("Enter the start year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    try:
        year2 = int(input("Enter the end year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    choose = input("""To choose ascending order : enter '1' 
To choose descending order : enter '2'.""").strip()

    start_year = min(year1, year2)
    end_year = max(year1, year2)
    total = []

    for line in country_data:
        if country == line[0].lower():
            if start_year <= int(line[2]) <= end_year:
                emission = float(line[3])
                year = int(line[2])
                total.append([emission , year])
                
    if len(total) > 0:
        if choose == '1':
            total.sort()
            print(f"\n--- Sorted Emissions for {country[0].upper() + country[1:]} ({start_year}-{end_year}) ---")
            for i in total:       
                print(f"Year : {i[1]:<6} | Emission : {i[0]:<15}" )
        elif choose == '2':
            total.sort()
            total.reverse()
            print(f"\n--- Sorted Emissions for {country[0].upper() + country[1:]} ({start_year}-{end_year}) ---")
            for i in total:
                print(f"Year : {i[1]:<6} | Emission : {i[0]:<15}" )
        else:
            print("\nERROR: Invalid sorting choice!")
    else:
        print("\nNo matching record is found!")


# REPORTİNG PLOTTİNG MENU BURADAN BAŞLIYOR.

def report_plotting(country_data,population_data):
    while True:
        print("""\n1. Report Generation
2. Plotting
3. Back to main menu""")
        
        answer = input("\nSelect a reporting task:")

        if answer == '1':
            report_generation(country_data,population_data)
        elif answer == '2':
            plotting(country_data)
        elif answer == '3':
            print("Backing to the main menu...")
            break
        else:
            print("Please enter a valid number!")


def report_generation(country_data,population_data):
    country = input("\nEnter country:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        n = int(input("Enter the value of n (for the last n years): ").strip())
    except ValueError:
        print("\nERROR: Invalid input! n must be numbers.")
        return

    country_records = []
    for line in country_data: 
        if country == line[0].lower():
            year = int(line[2])
            emission = float(line[3])
            country_records.append([year,emission])

    if len(country_records) > 0:    
        min_y, max_y = country_records[0][0], country_records[0][0]
        min_e, max_e = country_records[0][1], country_records[0][1]

        for i in country_records:
            if i[1] < min_e:
                min_e = i[1]
                min_y = i[0]
            if i[1] > max_e:
                max_e = i[1]
                max_y = i[0]
        
        latest_year = country_records[0][0]
        for i in country_records:
            if i[0] > latest_year:
                latest_year = i[0]
        
        start_year = (latest_year - n) + 1
        last_n_emissions = []

        for i in country_records:
            if start_year <= i[0] <= latest_year:
                last_n_emissions.append(i[1])

        if len(last_n_emissions) > 0:
            total_sum = 0
            for i in last_n_emissions:
                total_sum += i
            average = total_sum / len(last_n_emissions)

            # STANDART SAPMA Formül: Kök içinde ( (değer - ortalama)^2 toplamı / eleman sayısı )
            sum_e = 0
            for i in last_n_emissions:
                sum_e += (i - average) ** 2

            standart_sapma = (sum_e / len(last_n_emissions)) ** 0.5
        else:
            average = 0
            standart_sapma = 0

        c_name = country[0].upper() + country[1:]
        print(f"\n--- Summary Report for {c_name} ---")
        print('-' * 40)
        print(f"Historical MIN Emission : {min_e} (Year: {min_y})")
        print(f"Historical MAX Emission : {max_e} (Year: {max_y})")
        print(f"Average Emission (Last {n} Years) : {average:.2f}")
        print(f"Standard Deviation (Last {n} Years) : {standart_sapma:.2f}")
        print("-" * 40)
    else:
        print("\nNo matching record is found for this country!")




def plotting(country_data):
    country = input("\nEnter country:").strip().lower()
    if not country.replace(' ', '').replace('-', '').replace("'", "").isalpha():
        print("\nERROR: Invalid input! Country must be letters.")
        return

    try:
        year1 = int(input("Enter the start year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    try:
        year2 = int(input("Enter the end year:").strip())
    except ValueError:
        print("\nERROR: Invalid input! Year must be numbers.")
        return

    start_year = min(year1, year2)
    end_year = max(year1, year2)

    years = []
    emissions = []

    for line in country_data:
        if country == line[0].lower():
            row_year = int(line[2])
            if start_year <= row_year <= end_year:
                years.append(str(row_year))
                emissions.append(float(line[3]))
    
    if len(emissions) > 0:
        c_name = country[0].upper() + country[1:]
        plt.bar(years, emissions) 
        plt.title(f"CO2 Emissions of {c_name} ({start_year} - {end_year})")
        plt.xlabel("Year")
        plt.ylabel("Emissions (tonnes)")
        plt.show()
        
    else:
        print("\nNo matching record is found for this country in the selected years!")


def main():
    country_data = load_data()
    population_data = load_population()

    if not country_data or not population_data:
        print("\nWARNING: One or both datasets could not be loaded. Please check your files.")
        
    print("\nProgram is starting...")
    while True:
        print("""\n1. CRUD Operations
2. Data Analysis
3. Report & Plotting
4. Exit the program""")
        choose = input("\nSelect a category:")

        if choose == '1':
            crud_menu(country_data)
        elif choose == '2':
            analysis_menu(country_data,population_data)
        elif choose == '3':
            report_plotting(country_data,population_data)
        elif choose == '4':
            print("\nThe program was stopped.")
            break
        else:
            print("\nPlease enter a valid number!")

main()