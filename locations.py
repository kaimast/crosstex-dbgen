#! /usr/bin/python3

# Countries, alphabetically sorted by "name"
# These are translated into @country definitions for CrossTeX
COUNTRIES = [('USA', {'name': ''})
            ,('Oz', {'name': 'Australia'})
            ,('Austria', {'name': 'Austria'})
            ,('Australia', {'name': 'Australia'})
            ,('Belgium', {'name': 'Belgium'})
            ,('Brazil', {'name': 'Brazil'})
            ,('Barbados', {'name': 'Barbados'})
            ,('Canada', {'name': 'Canada'})
            ,('CzechRepublic', {'name': 'Czechia'})
            ,('China', {'name': 'China'})
            ,('Curacao', {'name': 'Curaçao'})
            ,('Domnicia', {'name': 'Domninica'})
            ,('Denmark', {'name': 'Denmark'})
            ,('Finland', {'name': 'Finland'})
            ,('France', {'name': 'France'})
            ,('Germany', {'name': 'Germany'})
            ,('Greece', {'name': 'Greece'})
            ,('Hungary', {'name': 'Hungary'})
            ,('India', {'name': 'India'})
            ,('Ireland', {'name': 'Ireland'})
            ,('Israel', {'name': 'Israel'})
            ,('Italy', {'name': 'Italy'})
            ,('Japan', {'name': 'Japan'})
            ,('Korea', {'name': 'Korea'})
            ,('Malaysia', {'name': 'Malaysia'})
            ,('Mexico', {'name': 'Mexico'})
            ,('Norway', {'name': 'Norway'})
            ,('Poland', {'name': 'Poland'})
            ,('Portugal', {'name': 'Portugal'})
            ,('SaintLucia', {'name': 'Saint Lucia'})
            ,('Scotland', {'name': 'Scotland'})
            ,('Slovakia', {'name': 'Slovakia'})
            ,('Spain', {'name': 'Spain'})
            ,('Sweden', {'name': 'Sweden'})
            ,('Switzerland', {'name': 'Switzerland'})
            ,('SaintKitts', {'name': 'Saint Kitts'})
            ,('Taiwan', {'name': 'Taiwan'})
            ,('Turkey', {'name': 'Turkey'})
            ,('TrinidadAndTobago', {'name': 'Trinidad and Tobago'})
            ,('UK', {'name': 'United Kingdom', 'shortname': 'UK'})
            ,('NewZealand', {'name': 'New Zealand'})
            ,('PuertoRico', {'name': 'Puerto Rico'})
            ,('Netherlands', {'name': 'The Netherlands'})
            ,('Anywhere', {'name': 'Anywhere'})
            ]

US_STATES = [('AL', {'longname': 'Alabama', 'shortname': 'AL'})
            ,('AK', {'longname': 'Alaska', 'shortname': 'AK'})
            ,('AZ', {'longname': 'Arizona', 'shortname': 'AZ'})
            ,('AR', {'longname': 'Arkansas', 'shortname': 'AR'})
            ,('CA', {'longname': 'California', 'shortname': 'CA'})
            ,('CO', {'longname': 'Colorado', 'shortname': 'CO'})
            ,('CT', {'longname': 'Connecticut', 'shortname': 'CT'})
            ,('DE', {'longname': 'Delaware', 'shortname': 'DE'})
            ,('FL', {'longname': 'Florida', 'shortname': 'FL'})
            ,('GA', {'longname': 'Georgia', 'shortname': 'GA'})
            ,('HI', {'longname': 'Hawaii', 'shortname': 'HI'})
            ,('ID', {'longname': 'Idaho', 'shortname': 'ID'})
            ,('IL', {'longname': 'Illinois', 'shortname': 'IL'})
            ,('IN', {'longname': 'Indiana', 'shortname': 'IN'})
            ,('IA', {'longname': 'Iowa', 'shortname': 'IA'})
            ,('KS', {'longname': 'Kansas', 'shortname': 'KS'})
            ,('KY', {'longname': 'Kentucky', 'shortname': 'KY'})
            ,('LA', {'longname': 'Louisiana', 'shortname': 'LA'})
            ,('ME', {'longname': 'Maine', 'shortname': 'ME'})
            ,('MD', {'longname': 'Maryland', 'shortname': 'MD'})
            ,('MA', {'longname': 'Massachusetts', 'shortname': 'MA'})
            ,('MI', {'longname': 'Michigan', 'shortname': 'MI'})
            ,('MN', {'longname': 'Minnesota', 'shortname': 'MN'})
            ,('MS', {'longname': 'Mississippi', 'shortname': 'MS'})
            ,('MO', {'longname': 'Missouri', 'shortname': 'MO'})
            ,('MT', {'longname': 'Montana', 'shortname': 'MT'})
            ,('NE', {'longname': 'Nebraska', 'shortname': 'NE'})
            ,('NV', {'longname': 'Nevada', 'shortname': 'NV'})
            ,('NH', {'longname': 'New Hampshire', 'shortname': 'NH'})
            ,('NJ', {'longname': 'New Jersey', 'shortname': 'NJ'})
            ,('NM', {'longname': 'New Mexico', 'shortname': 'NM'})
            ,('NY', {'longname': 'New York', 'shortname': 'NY'})
            ,('NC', {'longname': 'North Carolina', 'shortname': 'NC'})
            ,('ND', {'longname': 'North Dakota', 'shortname': 'ND'})
            ,('OH', {'longname': 'Ohio', 'shortname': 'OH'})
            ,('OK', {'longname': 'Oklahoma', 'shortname': 'OK'})
            ,('OR', {'longname': 'Oregon', 'shortname': 'OR'})
            ,('PA', {'longname': 'Pennsylvania', 'shortname': 'PA'})
            ,('RI', {'longname': 'Rhode Island', 'shortname': 'RI'})
            ,('SC', {'longname': 'South Carolina', 'shortname': 'SC'})
            ,('SD', {'longname': 'South Dakota', 'shortname': 'SD'})
            ,('TN', {'longname': 'Tennessee', 'shortname': 'TN'})
            ,('TX', {'longname': 'Texas', 'shortname': 'TX'})
            ,('UT', {'longname': 'Utah', 'shortname': 'UT'})
            ,('VT', {'longname': 'Vermont', 'shortname': 'VT'})
            ,('VA', {'longname': 'Virginia', 'shortname': 'VA'})
            ,('WA', {'longname': 'Washington', 'shortname': 'WA'})
            ,('WV', {'longname': 'West Virginia', 'shortname': 'WV'})
            ,('WI', {'longname': 'Wisconsin', 'shortname': 'WI'})
            ,('WY', {'longname': 'Wyoming', 'shortname': 'WY'})
            ]

US_LOCATIONS = [('Albuquerque', {'city': 'Albuquerque', 'state': 'NM'})
               ,('Alexandria', {'city': 'Alexandria', 'state': 'VA'})
               ,('Asilomar', {'city': 'Asilomar', 'state': 'CA'})
               ,('Amherst', {'city': 'Amherst', 'state': 'MA'})
               ,('Anaheim', {'city': 'Anaheim', 'state': 'CA'})
               ,('Anchorage', {'city': 'Anchorage', 'state': 'AK'})
               ,('Annapolis', {'city': 'Annapolis', 'state': 'MD'})
               ,('AnnArbor', {'city': 'Ann Arbor', 'state': 'MI'})
               ,('ArlingtonTX', {'city': 'Arlington', 'state': 'TX'})
               ,('ArlingtonVA', {'city': 'Arlington', 'state': 'VA'})
               ,('Asheville', {'city': 'Asheville', 'state': 'NC'})
               ,('Atlanta', {'city': 'Atlanta', 'state': 'GA'})
               ,('AtlanticCity', {'city': 'Atlantic City', 'state': 'NJ'})
               ,('Austin', {'city': 'Austin', 'state': 'TX'})
               ,('BalHarbour', {'city': 'Bal Harbour', 'state': 'FL'})
               ,('Baltimore', {'city': 'Baltimore', 'state': 'MD'})
               ,('Bellevue', {'city': 'Bellevue', 'state': 'WA'})
               ,('Berkeley', {'city': 'Berkeley', 'state': 'CA'})
               ,('Bethesda', {'city': 'Bethesda', 'state': 'MD'})
               ,('BeverlyHills', {'city': 'Beverly Hills', 'state': 'CA'})
               ,('Broomfield', {'city': 'Broomfield', 'state': 'CO'})
               ,('BigSky', {'city': 'Big Sky', 'state': 'MT'})
               ,('Blacksburg', {'city': 'Blacksburg', 'state': 'VA'})
               ,('BoltonLanding', {'city': 'Bolton Landing', 'state': 'NY'})
               ,('Boston', {'city': 'Boston', 'state': 'MA'})
               ,('Boulder', {'city': 'Boulder', 'state': 'CO'})
               ,('BrettonWoods', {'city': 'Bretton Woods', 'state': 'NH'})
               ,('Buffalo', {'city': 'Buffalo', 'state': 'NY'})
               ,('Burlington', {'city': 'Burlington', 'state': 'VT'})
               ,('CambridgeMA', {'city': 'Cambridge', 'state': 'MA'})
               ,('CapeCod', {'city': 'Cape Cod', 'state': 'MA'})
               ,('Carlsbad', {'city': 'Carlsbad', 'state': 'CA'})
               ,('Charleston', {'city': 'Charleston', 'state': 'SC'})
               ,('Charlottesville', {'city': 'Charlottesville', 'state': 'VA'})
               ,('Chaminade', {'city': 'Chaminade', 'state': 'CA'})
               ,('Chicago', {'city': 'Chicago', 'state': 'IL'})
               ,('Cincinnati', {'city': 'Cincinnati', 'state': 'OH'})
               ,('CollegePark', {'city': 'College Park', 'state': 'MD'})
               ,('CollegeParkTX', {'city': 'College Park', 'state': 'TX'})
               ,('Columbus', {'city': 'Columbus', 'state': 'OH'})
               ,('CopperMountain', {'city': 'Copper Mountain', 'state': 'CO'})
               ,('Corvallis', {'city': 'Corvallis', 'state': 'OR'})
               ,('Dallas', {'city': 'Dallas', 'state': 'TX'})
               ,('Davis', {'city': 'Davis', 'state': 'CA'})
               ,('DC', {'city': 'Washington', 'state': '"D.C."'})
               ,('Denver', {'city': 'Denver', 'state': 'CO'})
               ,('Detroit', {'city': 'Detroit', 'state': 'MI'})
               ,('Durham', {'city': 'Durham', 'state': 'NC'})
               ,('EastLansing', {'city': 'East Lansing', 'state': 'MI'})
               ,('ElPaso', {'city': 'El Paso', 'state': 'TX'})
               ,('EstesPark', {'city': 'Estes Park', 'state': 'CO'})
               ,('Eugene', {'city': 'Eugene', 'state': 'OR'})
               ,('Fairfax', {'city': 'Fairfax', 'state': 'VA'})
               ,('FortLauderdale', {'city': 'Fort Lauderdale', 'state': 'FL'})
               ,('Farmington', {'city': 'Farmington', 'state': 'PA'})
               ,('Framingham', {'city': 'Framingham', 'state': 'MA'})
               ,('Gaithersburg', {'city': 'Gaithersburg', 'state': 'MD'})
               ,('Gatlinburg', {'city': 'Gatlinburg', 'state': 'TN'})
               ,('Hanover', {'city': 'Hanover', 'state': 'NH'})
               ,('Hawaii', {'city': 'Hawaii', 'state': 'HI'})
               ,('Hershey', {'city': 'Hershey', 'state': 'PA'})
               ,('Honolulu', {'city': 'Honolulu', 'state': 'HI'})
               ,('Houston', {'city': 'Houston', 'state': 'TX'})
               ,('Hollywood', {'city': 'Hollywood', 'state': 'CA'})
               ,('Indianapolis', {'city': 'Indianapolis', 'state': 'IN'})
               ,('Irvine', {'city': 'Irvine', 'state': 'CA'})
               ,('Ithaca', {'city': 'Ithaca', 'state': 'NY'})
               ,('KansasCity', {'city': 'Kansas City', 'state': 'KS'})
               ,('Kauai', {'city': 'Kauai', 'state': 'HI'})
               ,('KeyWest', {'city': 'Key West', 'state': 'FL'})
               ,('KiawahIsland', {'city': 'Kiawah Island', 'state': 'SC'})
               ,('KohalaCoast', {'city': 'Kohala Coast', 'state': 'HI'})
               ,('Knoxville', {'city': 'Knoxville', 'state': 'TN'})
               ,('LaJolla', {'city': 'La Jolla', 'state': 'CA'})
               ,('LakeTahoe', {'city': 'Lake Tahoe', 'state': 'CA'})
               ,('LasVegas', {'city': 'Las Vegas', 'state': 'NV'})
               ,('Lihue', {'city': 'Lihue', 'state': 'HI'})
               ,('LitchfieldPark', {'city': 'Litchfield Park', 'state': 'AZ'})
               ,('Lombard', {'city': 'Lombard', 'state': 'IL'})
               ,('LongBeach', {'city': 'Long Beach', 'state': 'CA'})
               ,('LosAngeles', {'city': 'Los Angeles', 'state': 'CA'})
               ,('Madison', {'city': 'Madison', 'state': 'WI'})
               ,('MarinaDelRay', {'city': 'Marina Del Ray', 'state': 'CA'})
               ,('Maui', {'city': 'Maui', 'state': 'HI'})
               ,('McLean', {'city': 'McLean', 'state': 'VA'})
               ,('MiamiBeach', {'city': 'Miami Beach', 'state': 'FL'})
               ,('Miami', {'city': 'Miami', 'state': 'FL'})
               ,('MiamiFtLauderdale', {'city': 'Miami/Ft.\ Lauderdale', 'state': 'FL'})
               ,('Milwaukee', {'city': 'Milwaukee', 'state': 'WI'})
               ,('Minneapolis', {'city': 'Minneapolis', 'state': 'MN'})
               ,('Monterey', {'city': 'Monterey', 'state': 'CA'})
               ,('NapaValley', {'city': 'Napa Valley', 'state': 'CA'}) 
               ,('Napa', {'city': 'Napa', 'state': 'CA'})
               ,('Nashville', {'city': 'Nashville', 'state': 'TN'})
               ,('Newark', {'city': 'Newark', 'state': 'NJ'})
               ,('NewHaven', {'city': 'New Haven', 'state': 'CT'})
               ,('NewOrleans', {'city': 'New Orleans', 'state': 'LA'})
               ,('NewportBeach', {'city': 'Newport Beach', 'state': 'CA'})
               ,('Newport', {'city': 'Newport', 'state': 'RI'})
               ,('NiagaraFalls', {'city': 'Niagara Falls', 'state': 'NY'})
               ,('Northampton', {'city': 'Northampton', 'state': 'MA'})
               ,('NorthFalmouth', {'city': 'North Falmouth', 'state': 'MA'})
               ,('NYC', {'city': 'New York', 'state': 'NY'})
               ,('Oakland', {'city': 'Oakland', 'state': 'CA'})
               ,('OrcasIsland', {'city': 'Orcas Island', 'state': 'WA'})
               ,('Orlando', {'city': 'Orlando', 'state': 'FL'})
               ,('PacificGrove', {'city': 'Pacific Grove', 'state': 'CA'})
               ,('PalmSprings', {'city': 'Palm Springs', 'state': 'CA'})
               ,('PaloAlto', {'city': 'Palo Alto', 'state': 'CA'})
               ,('Pasadena', {'city': 'Pasadena', 'state': 'CA'})
               ,('Philadelphia', {'city': 'Philadelphia', 'state': 'PA'})
               ,('Phoenix', {'city': 'Phoenix', 'state': 'AZ'})
               ,('Pittsburgh', {'city': 'Pittsburgh', 'state': 'PA'})
               ,('Portland', {'city': 'Portland', 'state': 'OR'})
               ,('Princeton', {'city': 'Princeton', 'state': 'NJ'})
               ,('Providence', {'city': 'Providence', 'state': 'RI'})
               ,('Raleigh', {'city': 'Raleigh', 'state': 'NC'})
               ,('Redmond', {'city': 'Redmond', 'state': 'WA'})
               ,('RedondoBeach', {'city': 'Redondo Beach', 'state': 'CA'})
               ,('ResearchTrianglePark', {'city': 'Research Triangle Park', 'state': 'NC'})
               ,('RioRico', {'city': 'Rio Rico', 'state': 'AZ'})
               ,('Riverside', {'city': 'Riverside', 'state': 'CA'})
               ,('Rochester', {'city': 'Rochester', 'state': 'NY'})
               ,('Rockville', {'city': 'Rockville', 'state': 'MD'})
               ,('Rye', {'city': 'Rye', 'state': 'NY'})
               ,('SaltLake', {'city': 'Salt Lake City', 'state': 'UT'})
               ,('SanAntonio', {'city': 'San Antonio', 'state': 'TX'})
               ,('SanDiego', {'city': 'San Diego', 'state': 'CA'})
               ,('SanJose', {'city': 'San Jose', 'state': 'CA'})
               ,('SantaBarbara', {'city': 'Santa Barbara', 'state': 'CA'})
               ,('SantaClara', {'city': 'Santa Clara', 'state': 'CA'})
               ,('SantaCruz', {'city': 'Santa Cruz', 'state': 'CA'})
               ,('SantaFe', {'city': 'Santa Fe', 'state': 'NM'})
               ,('SantaMonica', {'city': 'Santa Monica', 'state': 'CA'})
               ,('SantaAnaPueblo', {'city': 'Santa Ana Pueblo', 'state': 'NM'})
               ,('Savannah', {'city': 'Savannah', 'state': 'GA'})
               ,('Scottsdale', {'city': 'Scottsdale', 'state': 'AZ'})
               ,('Seattle', {'city': 'Seattle', 'state': 'WA'})
               ,('SF', {'city': 'San Francisco', 'state': 'CA'})
               ,('ShakerHeights', {'city': 'ShakerHeights', 'state': 'OH'})
               ,('Snowbird', {'city': 'Snowbird', 'state': 'UT'})
               ,('Stanford', {'city': 'Stanford', 'state': 'CA'})
               ,('Stevenson', {'city': 'Stevenson', 'state': 'WA'})
               ,('StLouis', {'city': 'Saint Louis', 'state': 'MO'})
               ,('Stowe', {'city': 'Stowe', 'state': 'VT'})
               ,('StPaul', {'city': 'Saint Paul', 'state': 'MN'})
               ,('StPetersburgBeach', {'city': 'Saint Petersburg Beach', 'state': 'FL'})
               ,('StPetersburg', {'city': 'Saint Petersburg', 'state': 'FL'})

               ,('Syracuse', {'city': 'Syracuse', 'state': 'NY'})
               ,('Tampa', {'city': 'Tampa', 'state': 'FL'})
               ,('Troy', {'city': 'Troy', 'state': 'NY'})
               ,('Tucson', {'city': 'Tucson', 'state': 'AZ'})
               ,('UrbanaChampaign', {'city': 'Urbana-Champaign', 'state': 'IL'})
               ,('Waikoloa', {'city': 'Waikoloa', 'state': 'HI'})
               ,('WestLafayette', {'city': 'West Lafayette', 'state': 'IN'})
               ,('WestPalmBeach', {'city': 'West Palm Beach', 'state': 'FL'})
               ,('WhitePlains', {'city': 'White Plains', 'state': 'NY'})
               ,('Williamsburg', {'city': 'Williamsburg', 'state': 'VA'})
               ,('YorktownHeights', {'city': 'Yorktown Heights', 'state': 'NY'})]

INTL_LOCATIONS = [('Adelaide', {'city': 'Adelaide', 'state': 'South Australia', 'country': 'Oz'})
                 ,('Amsterdam', {'city': 'Amsterdam', 'country': 'Netherlands'})
                 ,('Andros', {'city': 'Andros', 'country': 'Greece'})
                 ,('Anguilla', {'city': 'Anguilla', 'country': 'UK'})
                 ,('Athens', {'city': 'Athens', 'country': 'Greece'})
                 ,('BadNeuenahr', {'city': 'Bad Neuenahr', 'country': 'Germany'})
                 ,('Banff', {'city': 'Banff', 'country': 'Canada'})
                 ,('Bangalore', {'city': 'Bangalore', 'country': 'India'})
                 ,('Barcelona', {'city': 'Barcelona', 'country': 'Spain'})
                 ,('BC', {'city': 'British Columbia', 'country': 'Canada'})
                 ,('Beijing', {'city': 'Beijing', 'country': 'China'})
                 ,('Belfast', {'city': 'Belfast', 'state': 'Northern Ireland', 'country': 'UK'})
                 ,('Berlin', {'city': 'Berlin', 'country': 'Germany'})
                 ,('Bern', {'city': 'Bern', 'country': 'Switzerland'})
                 ,('Bertinoro', {'city': 'Bertinoro', 'country': 'Italy'})
                 ,('Bologna', {'city': 'Bologna', 'country': 'Italy'})
                 ,('Bordeaux', {'city': 'Bordeaux', 'country': 'France'})
                 ,('Bratislava', {'city': 'Bratislava', 'country': 'Slovakia'})
                 ,('Bremen', {'city': 'Bremen', 'country': 'Germany'})
                 ,('Brighton', {'city': 'Brighton', 'country': 'UK'})
                 ,('Brisbane', {'city': 'Brisbane', 'state': 'Queensland', 'country': 'Australia'})
                 ,('Brussels', {'city': 'Brussels', 'country': 'Belgium'})
                 ,('Budapest', {'city': 'Budapest', 'country': 'Hungary'})
                 ,('Cairns', {'city': 'Cairns', 'state': 'Queensland', 'country': 'Oz'})
                 ,('Cairo', {'city': 'Cairo', 'country': 'Egypt' })
                 ,('Calgary', {'city': 'Calgary', 'country': 'Canada'})
                 ,('CambridgeUK', {'city': 'Cambridge', 'country': 'UK'})
                 ,('Canberra', {'city': 'Canberra', 'country': 'Oz'})
                 ,('Cancun', {'city': 'Cancún', 'country': 'Mexico'})
                 ,('Cannes', {'city': 'Cannes', 'country': 'France'})
                 ,('Cascais', {'city': 'Cascais', 'country': 'Portugal'})
                 ,('Castries', {'city': 'Castries', 'country': 'SaintLucia'})
                 ,('Chiba', {'city': 'Chiba', 'country': 'Japan'})
                 ,('ChristChurch', {'city': 'Christ Church', 'country': 'Barbados'})
                 ,('Cologne', {'city': 'Cologne', 'country': 'Germany'})
                 ,('Copenhagen', {'city': 'Copenhagen', 'country': 'Denmark'})
                 ,('Connemara', {'city': 'Connemara', 'country': 'Ireland'})
                 ,('Cozumel', {'city': 'Cozumel', 'country': 'Mexico'})
                 ,('Dagstuhl', {'city': 'Dagstuhl', 'country': 'Germany'})
                 ,('Dresden', {'city': 'Dresden', 'country': 'Germany'})
                 ,('Donostia', {'city': 'Donostia-San Sebatián', 'country': 'Spain'})
                 ,('Dublin', {'city': 'Dublin', 'country': 'Ireland'})
                 ,('Dunedin', {'city': 'Dunedin', 'country': 'NewZealand'})
                 ,('Edinburgh', {'city': 'Edinburgh', 'country': 'Scotland'})
                 ,('Edmonton', {'city': 'Edmonton', 'country': 'Canada'})
                 ,('Elmau', {'city': 'Elmau', 'country': 'Germany'})
                 ,('ElmauOberbayern', {'city': 'Elmau/Oberbayern', 'country': 'Germany'})
                 ,('Florence', {'city': 'Florence', 'country': 'Italy'})
                 ,('Florianopolis', {'city': 'Florianópolis', 'country': 'Brazil'})
                 ,('Funchal', {'city': 'Funchal', 'country': 'Portugal'})
                 ,('Geneva', {'city': 'Geneva', 'country': 'Switzerland'})
                 ,('Genova', {'city': 'Genova', 'country': 'Italy'})
                 ,('Glasgow', {'city': 'Glasgow', 'country': 'Scotland'})
                 ,('GoldCoast', {'city': 'Gold Coast', 'state': 'Queensland', 'country': 'Oz'})
                 ,('Goteborg', {'city': 'Göteborg', 'country': 'Sweden'})
                 ,('GrandCaymanIsland', {'city': 'Grand Cayman Island', 'country': 'UK'})
                 ,('Grenoble', {'city': 'Grenoble', 'country': 'France'})
                 ,('Guadeloupe', {'city': 'Guadeloupe', 'state': 'French West Indies', 'country': 'France'})
                 ,('Hangzhou', {'city': 'Hangzhou', 'country': 'Germany'})
                 ,('Heidelberg', {'city': 'Heidelberg', 'country': 'Germany'})
                 ,('Helsinki', {'city': 'Helsinki', 'country': 'Finland'})
                 ,('Heraklion', {'city': 'Heraklion', 'country': 'Greece'})
                 ,('Hiroshima', {'city': 'Hiroshima', 'country': 'Japan'})
                 ,('Hobart', {'city': 'Hobart', 'state': 'Tasmania', 'country': 'Oz'})
                 ,('HongKong', {'city': 'Hong Kong', 'country': 'China'})
                 ,('Huntsville', {'city': 'Huntsville', 'state': 'Ontario', 'country': 'Canada'})
                 ,('Innsbruck', {'city': 'Innsbruck', 'country': 'Austria'})
                 ,('Istanbul', {'city': 'Istanbul', 'country': 'Turkey'})
                 ,('Karlsruhe', {'city': 'Karlsruhe', 'country': 'Germany'})
                 ,('KartauseIttingen', {'city': 'Kartause Ittingen', 'country': 'Switzerland'})
                 ,('Kobe', {'city': 'Kobe', 'country': 'Japan'})
                 ,('Koblenz', {'city': 'Koblenz', 'country': 'Germany'})
                 ,('Kolding', {'city': 'Kolding', 'country': 'Denmark'})
                 ,('Konstanz', {'city': 'Konstanz', 'country': 'Germany'})
                 ,('KotaKinabalu', {'city': 'Kota Kinabalu', 'state': 'Sabah', 'country': 'Malaysia'})
                 ,('Kralendijk', {'city': 'Kralendijk', 'state': 'Bonaire', 'country': 'Netherlands'})
                 ,('Kyoto', {'city': 'Kyoto', 'country': 'Japan'})
                 ,('Lausanne', {'city': 'Lausanne', 'country': 'Switzerland'})
                 ,('Leuven', {'city': 'Leuven', 'country': 'Belgium'})
                 ,('Lisbon', {'city': 'Lisbon', 'country': 'Portugal'})
                 ,('London', {'city': 'London', 'country': 'UK'})
                 ,('Lyon', {'city': 'Lyon', 'country': 'France'})
                 ,('Macau', {'city': 'Macau', 'country': 'China'})
                 ,('Madrid', {'city': 'Madrid', 'country': 'Spain'})
                 ,('Manchester', {'city': 'Manchester', 'country': 'UK'})
                 ,('Marseille', {'city': 'Marseille', 'country': 'France'})
                 ,('Melbourne', {'city': 'Melbourne', 'state': 'Victoria', 'country': 'Oz'})
                 ,('MexicoCity', {'city': 'MexicoCity', 'country': 'Mexico'})
                 ,('Minaki', {'city': 'Minaki', 'country': 'Canada'})
                 ,('MonteVerita', {'city': 'Monte Verit{\`a}', 'country': 'Switzerland'})
                 ,('Montreal', {'city': '{Montréal}', 'country': 'Canada'})
                 ,('MontSaintMichel', {'city': 'Mont Saint-Michel', 'country': 'France'})
                 ,('Munich', {'city': 'Munich', 'country': 'Germany'})
                 ,('Mumbai', {'city': 'Mumbai', 'country': 'India'})
                 ,('NaraCity', {'city': 'Nara City', 'country': 'Japan'})
                 ,('Newcastle', {'city': 'Newcastle', 'country': 'Oz'})
                 ,('NewDelhi', {'city': 'New Delhi', 'country': 'India'})
                 ,('Nice', {'city': 'Nice', 'country': 'France'})
                 ,('Nuremberg', {'city': 'Nürnberg', 'country': 'Germany'})
                 ,('Osaka', {'city': 'Osaka', 'country': 'Japan'})
                 ,('Okinawa', {'city': 'Okinawa', 'country': 'Japan'})
                 ,('Ottawa', {'city': 'Ottawa', 'country': 'Canada'})
                 ,('Paderborn', {'city': 'Paderborn', 'country': 'Germany'})
                 ,('Paris', {'city': 'Paris', 'country': 'France'})
                 ,('Piza', {'city': 'Piza', 'country': 'Italy'})
                 ,('Poznan', {'city': 'Poznan', 'country': 'Poland'})
                 ,('Porto', {'city': 'Porto', 'country': 'Portugal'})
                 ,('Prague', {'city': 'Prague', 'country': 'CzechRepublic'})
                 ,('PuertoVallarta', {'city': 'Puerto Vallarta', 'country': 'Mexico'})
                 ,('PortaBlancu', {'city': 'Porta Blancu', 'country': 'Curacao'})
                 ,('QuebecCity', {'city': 'Quebec City', 'country': 'Canada'})
                 ,('RhodesIsland', {'city': 'Rhodes Island', 'country': 'Greece'})
                 ,('Rio', {'city': 'Rio de Janeiro', 'country': 'Brazil'})
                 ,('Rome', {'city': 'Rome', 'country': 'Italy'})
                 ,('Ruschlikon', {'city': 'Rüschlikon', 'country': 'Switzerland'})
                 ,('Saarbrucken', {'city': '{Saarbrücken}', 'country': 'Germany'})
                 ,('SaintEmilion', {'city': 'Saint Emilion', 'country': 'France'})
                 ,('SaintMalo', {'city': 'Saint Malo', 'country': 'France'})
                 ,('Santiago', {'city': 'Santiago de Chile', 'country': 'Chile'})
                 ,('Salzburg', {'city': 'Salzburg', 'country': 'Austria'})
                 ,('SanJuan', {'city': 'San Juan', 'country': 'PuertoRico'})
                 ,('Scarborough', {'city': 'Scarborough', 'country': 'TrinidadAndTobago'})
                 ,('Seoul', {'city': 'Seoul', 'country': 'Korea'})
                 ,('Shanghai', {'city': 'Shanghai', 'country': 'China'})
                 ,('Sintra', {'city': 'Sintra', 'country': 'Portugal'})
                 ,('Singapore', {'city': 'Singapore', 'country': 'Singapore'})
                 ,('SophiaAntipolis', {'city': 'Sophia Antipolis', 'country': 'France'})
                 ,('Southampton', {'city': 'Southampton', 'state': 'Bermuda', 'country': 'UK'})
                 ,('StJohns', {'city': "St. John's", 'country': 'Canada'})
                 ,('Sliema', {'city': "Sliema", "country": "Malta"})
                 ,('FrigateBay', {'city': 'Frigate Bay', 'country': 'SaintKitts'})
                 ,('Stockholm', {'city': 'Stockholm', 'country': 'Sweden'})
                 ,('Stresa', {'city': 'Stresa', 'country': 'Italy'})
                 ,('Sydney', {'city': 'Sydney', 'country': 'Oz'})
                 ,('Taipei', {'city': 'Taipei', 'country': 'Taiwan'})
                 ,('Taormina', {'city': 'Taormina', 'country': 'Italy'})
                 ,('TelAviv', {'city': 'Tel Aviv', 'country': 'Israel'})
                 ,('Tenerife', {'city': 'Tenerife', 'country': 'Spain'})
                 ,('Tokyo', {'city': 'Tokyo', 'country': 'Japan'})
                 ,('Toronto', {'city': 'Toronto', 'country': 'Canada'})
                 ,('Trondheim', {'city': 'Trondheim', 'country': 'Norway'})
                 ,('Trento', {'city': 'Trento', 'country': 'Italy'})
                 ,('Tsukuba', {'city': 'Tsukuba', 'country': 'Japan'})
                 ,('Turku', {'city': 'Turku', 'country': 'Finland'})
                 ,('Uppsala', {'city': 'Uppsala', 'country': 'Sweden'})
                 ,('Valencia', {'city': 'Valencia', 'country': 'Spain'})
                 ,('Vancouver', {'city': 'Vancouver', 'country': 'Canada'})
                 ,('Venice', {'city': 'Venice', 'country': 'Italy'})
                 ,('Victoria', {'city': 'Victoria', 'country': 'Canada'})
                 ,('Vienna', {'city': 'Vienna', 'country': 'Austria'})
                 ,('Virtual', {'city': 'Virtual', 'country': 'Anywhere'})
                 ,('VillaGallia', {'city': 'Villa Gallia', 'state': 'Como', 'country': 'Italy'})
                 ,('Vouliagmeni', {'city': 'Vouliagmeni', 'country': 'Greece'})
                 ,('Warsaw', {'city': 'Warsaw', 'country': 'Poland'})
                 ,('Waterloo', {'city': 'Waterloo', 'country': 'Canada'})
                 ,('WestBerlin', {'city': 'West Berlin', 'country': 'Germany'})
                 ,('Winnipeg', {'city': 'Winnipeg', 'country': 'Canada'})
                 ,('Xian', {'city': "Xi'an", 'country': 'China'})
                 ,('Yokohama', {'city': 'Yokohama', 'country': 'Japan'})
                 ,('Zurich', {'city': 'Zürich', 'country': 'Switzerland'})
                 ]

# Ambiguous locations are resolved by looking for clarifying locations
LOCATION_AMBIGUITIES = {'Arlington': {'Texas': 'ArlingtonTX',
                                      'Virginia': 'ArlingtonVA'}
                       ,'Cambridge': {'MA': 'CambridgeMA',
                                      'Massachusetts': 'CambridgeMA',
                                      'UK': 'CambridgeUK'}
                       }
# Location aliases are under multiple names.  E.g. SanFrancisco -> sf
LOCATION_ALIASES = {'99Atlanta': 'Atlanta'
                   ,'alzburg': 'Salzburg'
                   ,'Cancún': 'Cancun'
                   ,'Elmau/Oberbayern': 'ElmauOberbayern'
                   ,'Lihue(Kauai)': 'Lihue'
                   ,'Lisboa': 'Lisbon'
                   ,'MarinadelRay': 'MarinaDelRay'
                   ,'MarinadelRey': 'MarinaDelRay'
                   ,'Miami/FtLauderdale': 'MiamiFtLauderdale'
                   ,u'Montr\xe9al': 'Montreal'
                   ,'MontSaint-Michel': 'MontSaintMichel'
                   ,u'MonteVerit\xe0': 'MonteVerita'
                   ,'NewYork': 'NYC'
                   ,'NewYorkCity': 'NYC'
                   ,'Philadephia': 'Philadelphia'
                   ,'Pisa': 'Piza'
                   ,'RiodeJaneiro': 'Rio'
                   ,'RiodeJaneriro': 'Rio'
                   ,u'R\xfcschlikon': 'Ruschlikon'
                   ,'Saint-Emilion': 'SaintEmilion'
                   ,'SaltLakeCity': 'SaltLake'
                   ,'SanFrancisco': 'SF'
                   }

MANUAL_LOCATIONS = {'conf/soda/1995': 'SF'}

LOCATIONS = [x[0] for x in US_LOCATIONS + INTL_LOCATIONS]

if __name__ == '__main__':
    with open('xtx/locations.xtx', 'w', encoding='utf-8') as f:
        def sortkey(x):
            try:
                return ['city', 'state', 'country'].index(x)
            except ValueError as _err:
                return -1

        f.write('% Countries\n')
        for country, attrs in COUNTRIES:
            if not isinstance(attrs, dict):
                raise RuntimeError("Attributes are not a dictionary")

            attrs = ', '.join(['%s="%s"' % x for x in sorted(attrs.items())])
            f.write('@country{%-20s %s}\n' % (country + ',', attrs))

        f.write('\n% US States\n@default country=USA\n')
        for state, attrs in US_STATES:
            if not isinstance(attrs, dict):
                raise RuntimeError("Attributes are not a dictionary")

            attrs = ', '.join(['%s="%s"' % x for x in sorted(attrs.items())])
            f.write('@state{%-2s %s}\n' % (state + ',', attrs))

        f.write('\n% US Locations\n')
        for loc, attrs in US_LOCATIONS:
            if not isinstance(attrs, dict):
                raise RuntimeError("Attributes are not a dictionary")

            newattrs = {}
            for k, v in attrs.items():
                if k == 'state':
                    newattrs[k] = v
                else:
                    newattrs[k] = '"%s"' % v
            attrs = ', '.join(['%s=%s' % x for x in sorted(newattrs.items())])
            f.write('@location{%-20s %s}\n' % (loc + ',', attrs))

        f.write('\n% International Locations\n@default country=""\n')
        for loc, attrs in INTL_LOCATIONS:
            if not isinstance(attrs, dict):
                raise RuntimeError("Attributes are not a dictionary")

            newattrs = {}
            for k, v in attrs.items():
                if k == 'country':
                    newattrs[k] = v
                else:
                    newattrs[k] = f'"{v}"'
            attrs = ', '.join(['%s=%s' % x for x in sorted(newattrs.items(), key=sortkey)])
            f.write('@location{%-20s %s}\n' % (loc + ',', attrs))
