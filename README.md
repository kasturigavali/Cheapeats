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

1. Git clone the code to the repository on your system 
` $ git clone https://github.com/kasturigavali/Cheapeats.git `
2. Create a virtual environment in the downloaded directory </li>
     Get into the downloaded directory
        ` $ cd <directory_name> `
     Install Virtual environment 
        ` $ pip install virtualenv `
     Create virtual environment name 'myenv' 
        ` $ python -m virtualenv myenv `
     Activate virtual environment 
        ```$ source myenv/bin/activate OR myenv/Scripts/activate.bat ``
3.Install the 'requirement.txt' file to download the required package </li>
         ``$ (myvenv)$ pip install -r requirements.txt ``
4. To run the hello.py 
      For Windows Type the following in the terminal:
        ```>set FLASK_APP=hello.py
           >flask run ```
      For MaC and Linux Type the following in the terminal:
        ``` >export FLASK_APP=hello.py 
            >flask run ```
      Copy paste the local host url in the browser to see the results
      Type Cltr+C on the terminal to terminat the local host url in the browser 


### Stakeholders 
Grocery stores, Users(Students and common public), Restaurant Owners, Event hosts, software developers 

<h3><strong> User Stories: Milestone 1.0<strong></h3>
<ul>
    <li>Users will create profile with login details and current location/address : 5 days</li>
    <ol>
        <li>Create Welcome page</li>
        <li>Create input details tab </li>
     </ol>
    <li>Users will create shopping list : 5 days</li>
    <ol>
        <li> Create shopping list input tabs (frontend): Store Name, shopping list and price columns </li>
        <li> Create database to store the input data (backend)
    (User will be able to save the list before going to store)
        <li> User will be able to submit the completed list with prices </li>
    </ol>
    <li>Users will be able to see the dashboard of current prices across stores: 5 days</li>
    <ol>
        <li>List submitted by users will reflect on dashboard for respective stores</li>
    </ol>
</ul>


        
        
        
