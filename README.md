# HHA_504_Final
                                                                                         
 
     EC2 Instance Assignment                                                
 
Public IP Address:  52.188.151.163

Private IP Address: 10.0.0.4



# Step 1: Create UBUNTU instance setup and deploy instance without deploying a pem key 

# Step 2: Open port 22 (SSH) and 3306 (MYSQL) in networking with new inbound rule for 3306

# Step 3: Connect to the UBUNTU instance using Replit terminal

# Step 4: Run command -> 
  Command: ssh sam@52.188.151.163

# Step 5: Run command after connecting to machine -> 
  Sudo apt-get update

# Step 6: Create User UBUNTU
#Username: dba
#Password: ahi2021
#Command Steps:
## Command-> 
  sudo adduser ‘dba’
## Command-> 
  sudo password ‘ahi2021’
##Edit configuration 
## Command -> 
  /etc/ssh/sshd_config
##Set Password Authentication and permit root login to yes
## Command -> 
  Restart ssh
## Command-> 
  sudo service ssh restart

# Step 7: Install MySQL
## Command-> 
  sudo apt install mysql-client mysql-server
##Select ‘OK’
##Update listings
## Command-> 
  sudo apt-get update

# Step 8: Check status 
## Command->
  sudo service mysql status
## Command->
  display actively running

# Step 9: Change bind address to 0.0.0.0 and save changes by Control O hit Control X to exit
## Command-> 
  sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
## Command-> 
  sudo service mysql restart

# Step 10: Start MySQL
## Command-> 
  Sudo MySQL

# Step 11: #Create MySQL user
## Command->
  Create user 'DBA'@'%' IDENTIFIED BY 'ahi2021';
## Grant all privileges to SQL user ->  
  GRANT ALL PRIVILEGES ON *.* TO 'DBA'@% WITH GRANT OPTION;
## Command->
  Show grants;

# Step 12 Create database
## Command->
  Create database tempdata;
## Command->
  Show databases;

# Step 13: Jupyter notebook to insert csv H1N1 data

##See attached notebook labeled AHI 504 final.py

# Step 14: # Create a dump (.sql) file
## Command-> 
  mysqldump -u dba -p tempdata > tempdata_dump.sql
## Command-> 
  sudo mysqldump-apt tempdata>tempdata_dump.sql

# 
