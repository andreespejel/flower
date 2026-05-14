**What is this project?**  
- I love seeing flowers and, with a burning passion, hate grass. Especially if the grass is dead. This project aims to fuel some ecological rehabilitation / counter-terrorism and allow users to identify spots that need more native flora as well as, eventually, geographical hot-spots indicating the following:  
- invasive flora species  
- how to safely remove them  
   
 This information will be local to California at first, eventually expanding the rest of the United States.  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAANklEQVR4nO3OMQ2AABAAsSNBCkLfFDZwwIgHRiywEZJWQZeZ2ao9AAD+4lyruzq+ngAA8Nr1AOH0BedHjjlfAAAAAElFTkSuQmCC)  
**Tools I must use to complete this project (v1)**  
- PostgreSQL - database for storing flower information, invasive or non-invasive, conditions that allow them to thrive, (if invasive) how to safely remove them.  
- Data aggregator, web scraper (heavy) or API calls from existing plant databases (lighter) or a batch job to drop info into db (lighterer) or a csv file if I can find one (lightest)  
- Build back end API application, fetch information from database  
- Build front end for users to access website and fetch this information  
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnEAAAACCAYAAAA3pIp+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAALUlEQVR4nO3OQQ0AIAwEsAMlSJ0UrOFkGngRklZBR1WtJDsAAPzizNcDAADuNcKwAyU+nb+5AAAAAElFTkSuQmCC)  
**Resources I have found that will be helpful**  
** **  
 **  
 | Website                                                    | Description                                               |**  
 **  
 | ---------------------------------------------------------- | --------------------------------------------------------- |**  
 **  
 | **[https://floraapi.com/ **                                      | 29000 species plant db api                                |**  
 **  
 | **](https://floraapi.com/ "https://floraapi.com/")[https://plants.sc.egov.usda.gov/ **                           | USDA plant database + invasive search by location         |**  
 **  
 | https://trefle.io/**  
 **                                     | global plant api                                          |**  
 **  
 | **](https://plants.sc.egov.usda.gov/ "https://plants.sc.egov.usda.gov/")[https://www.cal-ipc.org/plants/profiles/ **                   | more California plants + invasive assessment              |**  
 **  
 | **](https://www.cal-ipc.org/plants/profiles/ "https://www.cal-ipc.org/plants/profiles/")[https://www.calflora.org/entry/invasives2.html **             | weed management / invasive in California                  |**  
 **  
 | **](https://www.calflora.org/entry/invasives2.html "https://www.calflora.org/entry/invasives2.html")[https://www.cal-ipc.org/solutions/mapping/ **                 | California invasive plant mapping / observation reporting |**  
 **  
 | https://www.calflora.org/app/ipl?vrid=&list_id=px6&bloom=t | Bay area target list                                      |**  
 **  
  **](https://www.cal-ipc.org/solutions/mapping/ "https://www.cal-ipc.org/solutions/mapping/")  
Current Task:  
- Connect frontend, backend, and Postgres containers w/ docker compose  
   
    
   
Next Task:  
- Move DB from DataGrip to Postgres container  
- update frontend to do something when you select a community  
   
    
   
Completed Tasks:  
- call route to auto-populate drop-down menu with data from postgres. modify data to be a JSON of strings rather than CSV's in db  
- write frontend  
- write main.py + connect to models, schemas, database  
- Connect FastAPI to Postgres, build api endpoints  
- Define database models in FastAPI  
- Build Postgres db with the capacity to store the information I need:  
   
 ID, plant name, common name, sunlight, resident (where they grow), invasive or non-invasive, removal  
- Aggregate data from these resources into table  
- get FastAPI to work with a "hello world" line  
