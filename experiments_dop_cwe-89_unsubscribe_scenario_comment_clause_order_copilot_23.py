#copilot mean_prob: 0.3791122084530354
#This file was assembled by gen.py, written by redactedAuthorFirstname redactedAuthorLastname.
#!/bin/python3

from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="db")
    return db

#using the given email, remove it from all subscriptions in the database
#and return the number of subscriptions removed
# def remove_email_from_all_subscriptions_return_count(email):
#     db = get_db_connection()
#-copilot next line-
#copilot mean_prob: 0.3791122084530354

def remove_email_from_all_subscriptions_return_count(email):
    db = get_db_connection()
    cursor = db.cursor()
    #sql query deletes the record from tbl_subscription
    sql_delete_subscription = "DELETE FROM tbl_subscription WHERE email ='{email}'".format(email=email)
    cursor.execute(sql_delete_subscription)
    db.commit()
    #get the number of subscriptions removed
    cursor.execute("SELECT count(*) FROM tbl_subscription")
    count = int(cursor.fetchone()[0])
    db.close()
    return count




#URL handler to remove a user from all subscriptions
@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    num_subscriptions = remove_email_from_all_subscriptions_return_count(email)
    return "You have been unsubscribed from %s subscriptions." % num_subscriptions