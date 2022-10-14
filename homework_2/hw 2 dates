# Justine Arzola 1804667
def find(in_date):

   new_month = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
              "August":8,"September":9,"October":10,"Novenber":11,"December":12}
   try:
      year = in_date.split(",")[-1].strip()
      month = in_date.split(",")[0].split()[0]
      day = in_date.split(",")[0].split()[-1]
      given_m = new_month[month]
      int(year)
      int(day)
      return str(given_m)+"/"+day+"/"+year
   except:
      return ""

with open("inputDates.txt") as f:
   for x in f.readlines():
      if x.strip() != "-1":
         res = find(x.strip())
         if res != "":
            with open("parsedDates.txt","a+") as w:
               w.write(res+"\n")
