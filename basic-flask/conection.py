import cx_Oracle

def con():
    dsn = cx_Oracle.makedsn(host='EXADB03PR-SCAN-ALSC.MERCK.COM', port=1521, service_name='PMCKCI')
    connection = cx_Oracle.connect(user='adroverd_4938', password='Nanita!20245', dsn=dsn)
    print("dns ===>>>> " + dsn)
    return connection

# SIMIL ORM
def conBull():
    connection = con()
    cursor = connection.cursor()
    
    query = "SELECT * FROM SB_TRACKER_INFO WHERE ROWNUM <= 20"
    cursor.execute(query)
    
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
 
    data_list = []

    for row in rows:
        data_list.append(dict(zip(columns, row)))

    cursor.close()
    connection.close()

    return data_list