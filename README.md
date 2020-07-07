# office-access-control
Проект по лятна практика на учениците от ТУЕС 2020

Flask приложение, което визуализира данни за контрол на достъпа във фирмени офиси, теглещо самите данни от MS SQL Server.

How to run this app (Linux and Windows tutorial below)

Linux:

1. "sudo su" in Terminal - allows you not to type sudo everytime

2. Paste the following in Terminal:
	curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
	exit
	sudo apt-get update
	sudo ACCEPT_EULA=Y apt-get install msodbcsql17
	# optional: for bcp and sqlcmd
	sudo ACCEPT_EULA=Y apt-get install mssql-tools
	echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
	echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
	source ~/.bashrc
	# optional: for unixODBC development headers
	sudo apt-get install unixodbc-dev
	# optional: kerberos library for debian-slim distributions
	sudo apt-get install libgssapi-krb5-2

3. Run the database_connection file

Windows:

1. Go to https://www.microsoft.com/en-us/download/details.aspx?id=56567
2. Download whatever version suits you (32bit or 64bit)
3. Paste the following git bash:
	echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
	echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
	source ~/.bashrc

4. In the file config.example change the file name to config.ini
	Change host, username, password and DBName.
	For driver change:
	ODBC+Driver+17+for+SQL+Server for Linux
	and
	SQL+Server for Windows 
	
	
