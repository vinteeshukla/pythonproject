from django.test import TestCase
import sqlite3



# Create your tests here.

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

cursor.execute("CREATE TABLE auth_group(id integer NOT NULL PRIMARY KEY AUTOINCREMENT,name varchar(150)NOT NULL UNIQUE")
cursor.execute("CREATE TABLE auth_group_permisssions(id integer NOT NULL PRIMARY KEY AUTOINCREMENT,group_id integer NOT NULL REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED,permission_id integer NOT NULL REFERENCES auth_permission(id) DEFERRABLE INTIALLY DEFERRED")
cursor.execute("CREATE TABLE auth_permission(id integer NOT NULL PRIMARY KEY AUTOINCREMENT,content_type_id integer NOT NULL REFRENCES django_content_type(id) DEFERRABLE INITIALY DEFERRED,codename varchar(100)NOT NULL,name varchar(255)NOT NULL")
cursor.execute("CREATE TABLE auth_user(id integer NOT NULL PRIMARY KEY AUTO INCREMENT,password varchar(128) NOT NULL,last_login datetime NULL ,is_superuser bool NOT NULL,username varchar(150) NOT NULL UNIQUE,last_name varchar(150)NOT NULL,emal varchar(254)NOT NULL,is_staff bool NOT NULL, is_active bool NOT NULL,date_joined datetime NOT NULL,first_name varchar(150) NOT NULL")
cursor.execute("CREATE TABLE auth_user_groups(id integer NOT NULL PRIMARY KEY AUTOINCREMENT,user_id integer NOT NULL REFRENCES,auth_user(id)DEFERRABLE INITIALY DEFERRED,group_id integer NOT NULL REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED")
cursor.execute("CREATE TABLE auth_user_user_permissions(id integer NOT NULL PRIMARY KEY AUTOINCREMENT,user_id integer NOT NULL REFERENCES auth_user (id) DEFERRABLE INITIALY DEFERRED,permission_id integer NOT NULL REFERENCES auth_permission(id)DERERRABLE INITILLAY DEFERRED")
cursor.execute("CREATE TABLE chatbot_syllabus(id integer,subject varchar(50)")
cursor.execute("CREATE TABLE chatbot_user(id integer,name varchar(100),age varchar(10)")
cursor.execute("CREATE TABLE dhango_admin_log(id integer NOT NULL PRIMARY KEY AUTOINCREMENT,action_time datetime NOT NULL,object_id text NULL,object_repr varchar(200)NOT NULL,change_message text NOT NULL,content_type_id integer NULL REFERENCES django_content_type(id)DEFERRABLE INITIALLY DEFERRED,user_id integer NOT NULL REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED,action_flag smallint unsigned NOT NULL CHECK(action_flag>+=0)")
cursor.execute("CREATE TABLE django_content_type(id integer NOT NULL PRIMARY KEY AUTOINCREMENT,app_label varchar(100)NOT NULL,model varchar(100)NOT NULL")
cursor.execute("CREATE TABLE django_migrations(id integer NOT NULL PRIMARY KEY AUTOINCREMENT,app varchar(255)NOT NULL,name vrachar(255)NOT NULL,applied datetime NOT NULL")
cursor.execute("CREATE TABLE django_session(session_key varchar(40)NOT NULL PRIMARY KEY,session_data text NOT NULL,expire_date datetime NOT NULL")
cursor.execute("CREATE TABLE sqlite_sequence(name,seq)")
cursor.execute("CREATE TABLE chatbot_detailform (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, title varchar(2.50) NOT NULL, description varchar(150) NOT NULL)")
cursor.execute("CREATE TABLE chatbot_text(id integer NOT NULL PRIMARY KEY AUTOINCREMENT, message varchar(250) NOT NULL, time REAL NOT NULL)")