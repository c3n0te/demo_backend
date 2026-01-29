import os
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI
from supabase import create_client, Client
import numpy as np

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

class Datum(BaseModel):
    date: str
    mobile: float
    desktop: float

app = FastAPI()
supabase: Client = create_client(url, key)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/average_monthly_visitors")
def read_average_monthly_visitors():
    resp = (supabase.table("visitor_data").select("*").execute())
    data = [Datum(**data_point) for data_point in resp.data]
    data.sort(key=lambda x: x.date)
    month = 1
    days = 0
    monthly_avg = 0.
    averages = []

    for datum in data:
        date = datetime.strptime(datum.date, "%Y-%m-%d")

        if date.month > month:
            monthly_avg = monthly_avg / days
            averages.append(monthly_avg)
            monthly_avg = 0.
            days = 0
            month = date.month  

        monthly_avg = monthly_avg + datum.mobile + datum.desktop 
        days = days + 1
    
    avg_avg = int(np.round(np.mean(averages)))
    return {"average_monthly_visitors": avg_avg}


@app.get("/peak_day")
def read_peak_day():
    resp = (supabase.table("visitor_data").select("*").execute())
    data = [Datum(**data_point) for data_point in resp.data]
    data.sort(key=lambda x: x.date)

    peak_day = "2025-01-01"
    max = 0.

    for datum in data:
        tot = datum.mobile + datum.desktop
        if tot > max:
            peak_day = datum.date
            max = tot

    return {"peak_day": peak_day}


@app.get("/total_visitors")
def read_total_visitors():
    resp = (supabase.table("visitor_data").select("*").execute())
    data = [Datum(**data_point) for data_point in resp.data]
    data.sort(key=lambda x: x.date)
    sum = 0 

    for datum in data:
        tot = datum.mobile + datum.desktop
        sum = sum + tot
    
    total = int(np.round(sum))
    return {"total_visitors": total}
