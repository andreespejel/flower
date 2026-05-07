##### **What is this project?**  
- I love seeing flowers and, with a burning passion, hate grass. Especially if the grass is dead. This project aims to fuel some ecological rehabilitation / counter-terrorism and allow users to identify spots that need more native flora as well as, eventually, geographical hot-spots indicating the following:   
- invasive flora species  
- how to safely remove them  
  This information will be local to California at first, eventually expanding the rest of the United States.  
##### **Tools I must use to complete this project (v1)**  
- PostgreSQL - database for storing flower information, invasive or non-invasive, conditions that allow them to thrive, (if invasive) how to safely remove them.  
- Data aggregator, web scraper (heavy) or API calls from existing plant databases (lighter) or a batch job to drop info into db (lighterer) or a csv file if I can find one (lightest)  
- Build back end API application, fetch information from database  
- Build front end for users to access website and fetch this information  
##### **Resources I have found that will be helpful**  
| | |  
|-|-|  
| **Website** | **Description** |   
| [https://floraapi.com/](https://floraapi.com/ "https://floraapi.com/") | 29000 species plant db api |   
| [https://plants.sc.egov.usda.gov/](https://plants.sc.egov.usda.gov/ "https://plants.sc.egov.usda.gov/") | USDA plant database + invasive search by location |   
| [https://trefle.io/](https://trefle.io/ "https://trefle.io/") | global plant api |   
| [https://www.cal-ipc.org/plants/profiles/](https://www.cal-ipc.org/plants/profiles/ "https://www.cal-ipc.org/plants/profiles/") | more California plants + invasive assessment |   
| [https://www.calflora.org/entry/invasives2.html](https://www.calflora.org/entry/invasives2.html "https://www.calflora.org/entry/invasives2.html") | weed management / invasive in California |   
| [https://www.cal-ipc.org/solutions/mapping/](https://www.cal-ipc.org/solutions/mapping/ "https://www.cal-ipc.org/solutions/mapping/") | California invasive plant mapping / observation reporting |   
| [https://www.calflora.org/app/ipl?vrid=&list_id=px6&bloom=t](https://www.calflora.org/app/ipl?vrid=&list_id=px6&bloom=t "https://www.calflora.org/app/ipl?vrid=&list_id=px6&bloom=t") | Bay area target list |   
Current Task:  
- Define database models in FastAPI  
   
Next Task:  
- Connect FastAPI to Postgres, build api endpoints  
- Connect FastAPI and Postgres containers w/ docker compose  
- Move DB from DataGrip to Postgres container  
- Build frontend web interface (call API, take input, etc.)  
   
Completed Tasks:   
- Build Postgres db with the capacity to store the information I need:  
  ID, plant name, common name, sunlight, resident (where they grow), invasive or non-invasive, removal  
- Aggregate data from these resources into table  
- get FastAPI to work with a "hello world" line  
