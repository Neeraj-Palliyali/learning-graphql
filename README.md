# UST

#TASK 1

##Steps

Step1: Go into the task1 directory<br>
Step2: Run<br>
  ```
  Python manage.py makemigrations countries
  Python manage.py migrate
  ```
Step3:Check db to see if the data is modeled and saved successfully<br>
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
