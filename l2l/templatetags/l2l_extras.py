from django import template
from datetime import datetime
from atexit import register

register = template.Library()

def render_date(date):
    if isinstance(date, str):
        return date.replace("T", " ")
    elif isinstance(date, datetime):
        return date.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return date
  

register.filter('l2l_dt', render_date)
