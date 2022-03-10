import pandas as pd
import pyodbc as pc

data = pd.read_csv('C:\\Users\\Fatima Ahmad\\Desktop\\SFLScientific Solution\\SFL-Scientific-Assesment\\DATA.csv')   
df = pd.DataFrame(data)

print(df) 

#Combine first and last name to full name
df['name'] = df['first_name'].str.cat(df['last_name'],sep=" ")
print(df)


# Connect to SQL Server
connection_string = "Driver=SQL Server;Server=DESKTOP-KGB2GN4;Database={0};Trusted_Connection=Yes;"                           
cnxn = pc.connect(connection_string.format("SFL"), autocommit=True)
cur=cnxn.cursor()
# Create Table
cur.execute('''
           CREATE TABLE  Data (
            id int,
            first_name varchar(50),
            last_name varchar(50),
            email varchar(100),
            gender varchar(50),
            ip_address varchar(100),
            name varchar(100))
               ''')
cnxn.close()

# Connect to SQL Server
connection_string = "Driver=SQL Server;Server=DESKTOP-KGB2GN4;Database={0};Trusted_Connection=Yes;"                           
cnxn = pc.connect(connection_string.format("SFL"), autocommit=True)
cur=cnxn.cursor()

for row in df.itertuples():
    cur.execute('''
                INSERT INTO data (id, first_name, last_name, email, gender, ip_address, name)
                VALUES (?,?,?,?,?,?,?)
                ''',
                row.id, 
                row.first_name,
                row.last_name,
                row.email, 
                row.gender,
                row.ip_address,
                row.name
                )
cnxn.close()