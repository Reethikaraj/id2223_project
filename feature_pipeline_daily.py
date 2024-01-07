#feature_pipeline_daily.py


import yfinance as yf
import pandas as pd
import os
from datetime import date

sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(period="max")

sp500.index = pd.to_datetime(sp500.index)
today = str(date.today())


import os
import modal

BACKFILL = False
LOCAL = False

if LOCAL == False:
    stub = modal.Stub()
    image = modal.Image.debian_slim().pip_install(["dataframe-image", "hopsworks", "joblib", "seaborn", "scikit-learn", "yfinance"])

    @stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("HOPSWORKS_API_KEY"))
    def f():
        g()

def get_latest():
    """
    Returns the latest value in a DataFrame
    """
    import pandas as pd
    import yfinance as yf
    
    sp500 = yf.Ticker("^GSPC")
    sp500 = sp500.history(period="max")
    sp500.index = pd.to_datetime(sp500.index)
    
    # Deleting unnecessary columns
    del sp500["Dividends"]
    del sp500["Stock Splits"]
    
    from datetime import date
    today = str(date.today())
    
    if today > sp500.index.max().strftime('%Y-%m-%d'):
        df = sp500.tail(1)
        print("df", df)
        return df

def g():
    import hopsworks
    import pandas as pd

    project = hopsworks.login()
    fs = project.get_feature_store()

    if BACKFILL == True:
        sp500 = pd.read_csv("sp500.csv")
    else:
        sp500 = get_latest()

    sp500_fg = fs.get_or_create_feature_group(
        name="sp500_modal",
        version=1,
        primary_key=["Open", "High", "Low", "Close", "Volume"],
        description="sp500 dataset")
    
    sp500_fg.insert(sp500, write_options={"wait_for_job": False})

if __name__ == "__main__":
    if LOCAL == True:
        g.local()
    else:
        with stub.run():
            f.remote()