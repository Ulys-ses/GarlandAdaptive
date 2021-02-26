import sqlite3

SQLiteConnect = sqlite3.connect("Data/GarlandAdaptive.db")
cursGarlandAdaptive = SQLiteConnect.cursor()
 
# Создание таблиц
# Сетки
cursGarlandAdaptive.execute("""CREATE TABLE Grids  -- Сетки
                   (
                   Name       text,    -- Имя сетки
                   Dimensions text,    -- Размерность сетки (1-3)
                   Groups     text     -- Группы светодиодов (json)
                   )""")

# Программы
# В программе с именем __parameters__ хранятся параметры
cursGarlandAdaptive.execute("""CREATE TABLE Programms  -- Программы
                   (
                   Name       text,    -- Имя Программы
                   Programm   text     -- Программа (json)
                   )""")

