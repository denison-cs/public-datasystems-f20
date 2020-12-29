import json
import sqlalchemy as sa
import pandas as pd
import re
import os
import os.path

def getmysql_creds(dirname=".",filename="creds.json"):
    """ Using directory and filename parameters, open a credentials file
        and obtain the five parts needed for a connection string to
        a remote provider using the "mysql" dictionary within
        an outer dictionary.  
        
        Return a scheme, server, user, password, and database
    """
    assert os.path.isfile(os.path.join(dirname, filename))
    with open(os.path.join(dirname, filename)) as f:
        D = json.load(f)
    mysql = D["mysql"]
    database = None
    if "database" in mysql:
        database = mysql["database"]
    return mysql["scheme"], mysql["server"], mysql["user"], mysql["pass"], database

def getsqlite_creds(dirname=".",filename="creds.json"):
    """ Using directory and filename parameters, open a credentials file
        and obtain the two parts needed for a connection string to
        a local provider using the "sqlite" dictionary within
        an outer dictionary.  
        
        Return a scheme and a dbfile
    """
    assert os.path.isfile(os.path.join(dirname, filename))
    with open(os.path.join(dirname, filename)) as f:
        D = json.load(f)
    sqlite = D["sqlite"]
    return sqlite["scheme"], sqlite["dbdir"], sqlite["database"]

def db_cstring(source, filename="creds.json", dirname=".", database=None):
    assert source in ["mysql", "sqlite"]
    if source == "mysql":
        scheme, server, user, password, filedatabase = getmysql_creds(dirname,filename)
        template = '{}://{}:{}@{}/{}'
        if database is None and filedatabase is None:
            db = ""
        elif database is not None:
            db = database
        else:
            db = filedatabase
        cstring = template.format(scheme, user, password, server, db)
    else:
        scheme, dbdir, filedatabase = getsqlite_creds(dirname, filename)
        if database is not None:
            db = database
        else:
            db = filedatabase
        if not os.path.isdir(dbdir):
            abs_dbdir = os.path.abspath(dbdir)
            base_dbdir = os.path.basename(abs_dbdir)
            dbdir = os.path.join("../../..", base_dbdir)
            assert os.path.isdir(dbdir)
        
        template = '{}:///{}/{}.db'
        cstring = template.format(scheme, dbdir, db)
    return cstring