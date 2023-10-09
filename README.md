# CyberSecurity-Dashboard
ETSU Class Project - DSS
This is a project for CSCI-5050-901 Decision Support System for a imaginary company Scorpius II that has 3 locations:
Nashville, Rio de Janerio, and Shanghai. Primary limitation was the short development time frame of 3 weeks. This generates a 
very basic Dashboard to support an upper level IT-Security manager. There are 4 input files containing fictional 
datasets that are placeholders for actual corporate data: User accounts, System Inventory, list of security violations, 
and estimated repair time and cost to return failed components to service.

The Dashboard was developed using Python with Streamlit and other relevant libraries. This a multipage structure with
4 scripts: 
  CyberSec.py the main page 
  1-Scorpius-Dashboard.py containing tables: component failures, estimated repair time 
    and cost, user security violations, and count of incidents for each violation. 
  2-Scorpius-Information.py generating user account and inventory information and a few KPIs
  3-Live-Threat-Map.py contains links to realtime threat mapping websites. 

The Scorpius scripts present data according to Location. 
The Scorpius Dashboard script simulates realtime input using a timed (3 seconds) loop with data randomly selected for each 
loop from all datasets. Each time thru the loop all of the tables are automatically updated. 

Three weeks is not enough time for a deep dive into Streamlit. Initial impression is very positive. Being touted as easy
to learn which is true for the basics. There are tons of websites that cover the basics but not many that go into the more
complex uses. Support from the user community is disappointing. Q&A blog type sites are poorly organized with few 
definitive answers to questions. They could learn a lot from the stackoverflow.com users.
