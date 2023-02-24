<h1>Overtime Calculation</h1>

   <h2>Steps:</h2> <br>
   <li>Install Required Modules/apps on bench and site : 1. erpnext 2. hrms <br>
   <li>After successfull installation of erpnext and hrms on your bench and site <br>
   <li>Run below commands in your [bench-name] dir : <br>
     <br>    
      
     $ bench get-app "https://github.com/Abhishek-Chougule/overtime_cal" --branch Mr-Abhi
     $ bench --site [site-name] install-app overtime_cal
         
      
   <li>After successfull installation of overtime_cal run below commands : <br>
      <br>
         
     $ bench use [site-name]
     $ bench start
     $ bench --site [site-name] migrate
         
   <li>You have successfully installed overtime_cal Module/app. <br>
<li>Now check mark the <b>"Is Overtime allowed"</b> checkbox from Employee Module, employees for which you want to allow overtime <br>
   <li>Note: Make sure you have already created the salary structure and asigned to the employees.
<li>Goto <b>"Overtime Settings"</b> Module - set settings according to companies requirement.
<li>Attendance will be marked in Module <b>"Employee Checkinout"</b>
<li>Goto <b>"Overtime"</b> Module select the employees select the date range click on get overtime button
   <li>You will get overtime details and overtime salary for your employees.<br>
   
   <b>Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors <br>
   Copyright (c) 2023, by Abhishek Chougule chouguleabhis@gmail.com <br>
   For license information, please see license.txt <br>
      <br>
      <h2>Thank You ! </h2>  
      </b>
