class Country:

    name = 'USA'
    area = 'North'

    def Nba(self):
        self.team_num = 30
        self.sex = 'boy'
        return("The best bask country is %s,whic have %d teams" %(self.name,self.team_num))

a = Country()
print(a.Nba())