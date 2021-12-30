class Country:
    def __init__(self, name, iso2):
        self.name = name
        self.iso2 = iso2


saudi_arabia = Country("Saudi Arabia", "SA")
egypt = Country("Egypt", "EG")
morocco = Country("Morocco", "MA")
jordan = Country("Jordan", "JO")
algeria = Country("Algeria", "DZ")
kuwait = Country("Kuwait", "KW")

arabic_countries = [saudi_arabia, egypt, morocco, jordan, algeria, kuwait]