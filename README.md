# Project Name: <sub>  Cheap </sub>Eats
IST-303 - Class of Fall 2022 - Group Project

### Group Name: Syntax_Error 

### Group Members
Kasturi Gavali, Jasmin Dominguez, Stephen Adjei, Derek James 

### Project Concept 
Hello World! We are creating an application that will recommend grocery stores around you with cheapest price of a searched food item.
Since it is challenging to find the dataset of grocery store rates, we are intially creating an application which will let the customer to input
their grocery store name, shopping list and item prices while shopping.
This way we will collect and create our own dataset which we will use to create a dashboard of live rates across vatious stores in a city 

### How to Run the Code 
1. Git clone the code to the repository on your system: 
            $ git clone https://github.com/kasturigavali/Cheapeats.git 
2. Create a virtual environment in the downloaded directory 
     
     Get into the downloaded directory: 
     
             $ cd <directory_name> 
     Install Virtual environment: 
     
            $ pip install virtualenv      
            
     Create virtual environment name 'myenv':  
     
            $ python -m virtualenv myenv         
     Activate virtual environment:         
     
           $ source myenv/bin/activate OR myenv/Scripts/activate.bat 
3. Install the 'requirements.txt' file to download the required package:

           $ (myvenv)$ pip install -r requirements.txt 
        
4. Run the 'main.py'and click on the local host url to view the webpage
         
OR Copy paste the local host url in the browser to see the results
      
Type Cltr+C on the terminal to terminate the local host url in the browser 


### Stakeholders 
Grocery stores, Users(Public), Software developers 

### User Stories

1. Create an Account on CheapEats (Priority 10)
   
   User will open the website and see the welcome page

2. Create Shopping List  (Priority 20)
    
    User will create a shopping list of items
    
3. Dashboard of Prices  (Priority 40)
    
    User will be able to see Dashboard of pricelist across their city/town
    
    
 ### Decomposition of User Stories
 
1. As a user I will visit the website(6 days) Priority 10
   - Create welcome page  (Kasturi)
   - Create shopping cart tab routing to shopping cart page (Kasturi)
   - Create dashboard tab routing to dashboard page  (Kasturi)

2. As a user I will create a shopping list/ cart of items (6 days) Priority 20
   - Create a input tab for Store name in the users city (Jasmin)
   - Create a input tabs for Locatio of city  (Derek)
   - Create input tabs for price infront of the items in the cart (Stephen)
   - User will be able to submit the data with submit button

3. As a user goes to the store they can input the actual prices which is saved on cheapeats database(6 days) Priority 20
   - Create table for shopping list in the database (Kasturi)
   - User will input data for prices which will be saved in other table linked to shopping list table by foreign key (Kasturi)


4. As a user I can see the Dashboard of item prices acrooss the stores in my city (12 days) Priority 40
   - User can see the dashboard of live prices across various stores obtained by quering the input data to database

### Velocity

Considering the working hours, classes and other overhead our team working time will about 60% of our available time.
That is our teams velocity is 0.6


### Milestone 1.0

1. Iteration 1  (6 days)

- Users will create profile with login details and current location/address
  
    1. Create Welcome page
    2. Create input details for Name
    3. Create input details for location
    4. Save the input data
     
     
2. Iteration 2 (12 days)

- Users will create shopping list
    
     1. Create shopping list input tabs Store Name 
     2. Shopping list and Price columns
     3. Submit the data and save (backend)
    
     User will be able to save the list before going to store
     
     User will be able to submit the completed list with prices after visiting the store
     
     
While working on Milestone 1.0, we revised our user stories considering the project deadline and team velocity,
which was recorded to be 0.4
  
### Revised Milestone 1.0

1. Iteration 1  (6 days)

- Users will be able to view or welcome, shopping cart and dashboard page
  
    1. Create Welcome page
    2. Create the shopping cart tab to shopping cart html
    3. Create the dashboard cart tab to dashboard html
 
 User will be able to see the welcome page and know what our website does
     
2. Iteration 2 (12 days)

- Create user input tabs and database in shopping cart
    
     1. Create shopping list page with location input , store name input and default top 10 grocery items. 

### Milestone 2.0

1. Iteration 1  (10 days)

- Users will be able to submit the data he has entered

    1. Generate database with table for default shopping list
    1. User will be able to input data in the shopping list table (With current Price)
    2. User will input the location and store name.
    3. User will submit the data
    4. The cart entries table will be populated by values from input tabs, this table is linked to shoppinglist table.
    
    
   User submitted data will be save in cheapeats database
   
       
2. Iteration 2 (12 days)

- Users can see the dashboard which will display the item rates across various stores
    
     1. With help of collected data from the user ,create a query to display the store names and price of the item on dashboard.
    


### How to Test the Code and Test Coverage

The requirments.txt file will install pytest and pytest-flask in your virtual envirinment and hence you can directly run the following commands.

1. Open the test_models.py file from the tests folder of repo run following code in the terminal

             $ pytest
OR run the following code in the main repo folder

            $ pytest test_models.py
2. To see the test coverage report copy paste following in the terminal

            $ pytest --cov
            
            
### Things learned about software development from this project 

1. Choose a process that works for your team and your project. It necessary to understand what the team is capable of considering the skillsets
and their commitment towards the project, and then tailor the user stories to match what YOUR customer wants and needs

2. Version Control: Changes can be distributed across a team without risking file loss and overwrites. You can also tag and branch and keep up with multiple versions.

3. Evaluate and Access:  Even though we had great ideas from beginning regarding how the website should look, we evaluated and accesses what we can work on 
as per requirements, data available and time constraints and made changes accordingly throughout the process.

4. We can have great design ideas but what matters in the end is what kind of working software we can deliver in the limited time frame.

5. User stories and tasks are useful tools to keep track of the project.


  
    



        
        
       
