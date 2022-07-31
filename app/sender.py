import psycopg2
from bottle import route, run, request

DSN = 'dbname=email_sender user=postgres host=db password=123456789'
QUERY = 'INSERT INTO emails (subject_d,message_d) VALUES (%s, %s)'

def register_message(subject,message):
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute(QUERY, (subject,message))
    conn.commit()
    cur.close()
    conn.close()
    print('message registered!')

@route('/', method = 'POST')
def send():
    subject = request.forms.get('subject')
    message = request.forms.get('message')
    register_message(subject,message)
    return 'enqueue message #[subject: {} message: {}]'.format(subject,message)

if __name__ == '__main__':
    run(host='0.0.0.0',port=8080,debug=True)