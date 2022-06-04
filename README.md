# UST

#TASK 1
<br>
##Steps

Step1: Go into the task1 directory
Step2: Run
  ```
  Python manage.py makemigrations countries
  Python manage.py migrate
  ```
Step3:Check db to see if the data is modeled and saved successfully<br>
<br>
<br>
#TASK 2
<br>
##Steps
<br>
Step4:Go into task2 directory<br>
Step5:Run
  ```
  Python manage.py runserver
  ```
<br>
Step6:Go into the server link
<br>

Step7:run the required queries(Paginated all countries :answer 2.1)
  ```
  query{
    allCountries(first:10){
    pageInfo {
        startCursor
        endCursor
        hasNextPage
        hasPreviousPage
        }
    edges {
        cursor
        node {
            name,
            capital
        }
    }
}
}
```


Step8:run the required queries(Country by id :answer 2.2)
  ```
  query{
    countriesId(id:4){
        name,
        capital,
        status,
        independent,
        region,
        subregion,
        capital,
        lat,
        long
}
}
```

Step9:run the required queries(Finding nearby countries from latitiude and longitude answer 2.3)
  ```
  query{
  closestCoordinate(lat:18.5, long:-63.41666666){
    name,
          capital,
          status,
          independent,
          region,
          subregion,
          capital,
          lat,
          long
  }
}
 ```
 
Step10:run the required queries(Finding coutries with languages answer 2.4)
  
 ```
  query{
  countryLanguages(language:"English"){
        name,
          capital,
          status,
          independent,
          region,
          subregion,
          capital,
          lat,
          long
    }
  }
  ```
