# Project Name: <sub>  Cheap </sub>Eats
IST-303 - Class of Fall 2022 - Group Project

<h4> Group Name: Syntax_Error </h4>

<h4> Group Members: Kasturi Gavali, Jasmin Dominguez, Stephen Adjei, Derek James </h4>

<h3> <strong> Project Concept </strong> </h3>
<p>Hello World! We are creating an application that will recommend grocery stores around you with cheapest price of a searched food item.</br></br>
Since it is challenging to find the dataset of grocery store rates, we are intially creating an application which will let the customer to input
their grocery store name, shopping list and item prices while shopping.<br></br>
This way we will collect and create our own dataset which we will use to create a dashboard of live rates across vatious stores in a city </p>

<h3> How to Run the Code </h3>
<ol>
    <li> Git clone the code to the repository on your system </li>
       ``` $ git clone https://github.com/kasturigavali/Cheapeats.git ```
    <li> Create a virtual environment in the downloaded directory </li>
        Get into the downloaded directory
         ``` $ cd <directory_name> ```
        <p> Install Virtual environment <p>
        ``` $ pip install virtualenv ```
        <p> Create virtual environment name 'myenv' <p>
         ``` $ python -m virtualenv myenv ```
        <p> Activate virtual environment <p>
         ``` $ source myenv/bin/activate OR myenv/Scripts/activate.bat ```
    <li> Install the 'requirement.txt' file to download the required package </li>
        ``` $ (myvenv)$ pip install -r requirements.txt ```
    <li> To run the hello.py </li>
        <p>For Windows Type the following in the terminal:<br>
        >set FLASK_APP=hello.py <br>
        >flask run <br></p>
        <p> For MaC and Linux Type the following in the terminal: <br>
        >export FLASK_APP=hello.py <br>
        >flask run <br> </p>
        <p>Copy paste the local host url in the browser to see the results </p>
        <p>Type Cltr+C on the terminal to terminat the local host url in the browser </p>
</ol>

<h3><strong> Stakeholders </strong></h3>
<p> Grocery stores, Users(Students and common public), Restaurant Owners, Event hosts, software developers </p>

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


        
        
        
