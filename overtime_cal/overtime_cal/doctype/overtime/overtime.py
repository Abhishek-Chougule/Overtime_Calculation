# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# Copyright (c) 2023, by Abhishek Chougule developer.mrabhi@gmail.com
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime as dt,timedelta

class Overtime(Document):
    
    @frappe.whitelist()
    def getemplist(self):
        doc = frappe.db.get_list("Employee", fields=["name","employee_name"])
        for d in doc:
            self.append("emp",
            {
                "empid": d.name,
                "empname": d.employee_name,
            },
                        )
                  
    @frappe.whitelist()
    def getempot(self): 
        doc = frappe.db.get_list("Employee Checkinout", fields=["time","employee","employee_name","overtime"])
        company=frappe.db.get_list("Overtime Settings", fields=["minreqot","workinghours"])
        
        if str(self.fromdate)!='None':
            for d in doc:
                for row in self.get("emp"):
                        if row.empcheckbox and row.empid==d.employee and (dt.strptime(str(self.fromdate), "%Y-%m-%d") <= dt.strptime(str(d.time)[:10], "%Y-%m-%d")) and (dt.strptime(str(self.todate), "%Y-%m-%d") >= dt.strptime(str(d.time)[:10], "%Y-%m-%d")):
                            count=0
                            if str(d.overtime)!='None' and str(d.overtime)[0]!='-' and str(d.overtime)!='0':
                                for s in company:
                                    self.minreqot=str(s.minreqot)
                                    
                                if (dt.strptime(d.overtime, "%H:%M:%S") >= dt.strptime(str(self.minreqot), "%H:%M:%S")):
                                                                                                
                                        for m in self.get('ot'):
                                            temp2=str(m.otdate)[:10]
                                            temp3=str(d.time)[:10]
                                            if dt.strptime(str(temp2), "%Y-%m-%d") == dt.strptime(str(temp3), "%Y-%m-%d")  and m.otid==d.employee:
                                                m.otovertime='0:00:00'        
                                               
                                        self.append("ot",{"otdate":d.time,"otid": d.employee,"otname": d.employee_name,"otovertime":d.overtime},)
                
                                
        else:
            frappe.msgprint('Please Select From Date to proceed !')
        
        time_by_name = {}
        for row in self.ot:
            if row.otid in time_by_name:
                total_time=dt.strptime(time_by_name[row.otid], '%H:%M:%S')+timedelta(hours=dt.strptime(row.otovertime, '%H:%M:%S').hour,minutes=dt.strptime(row.otovertime, '%H:%M:%S').minute,seconds=dt.strptime(row.otovertime, '%H:%M:%S').second)
                time_by_name[row.otid] = total_time.strftime('%H:%M:%S')
              
                
            else:
                time_by_name[row.otid] = dt.strptime(row.otovertime, '%H:%M:%S').strftime('%H:%M:%S')
               

        self.tot = []

        for otid, otovertime in time_by_name.items():
            for nm in self.get('ot'):
                if otid==nm.otid:
                    otname=nm.otname
            row = self.append('tot', {})
            row.totid = otid
            row.totname=otname
            row.tottot = otovertime

        
        
            
            
            
            
    @frappe.whitelist()
    def selectall(self):
        children = self.get("emp")
        if not children:
            return
        for child in children:
            all_selected = all([child.empcheckbox for child in children])
            if not all_selected:
                value = 1   
            else:
                value = 0
            for child in children:
                child.empcheckbox = value
            
                  	