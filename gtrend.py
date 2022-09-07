# NOTE : Import required 3rd party libs
from pytrends.request import TrendReq
import plotly.express as px
import pandas as pd


def get_google_trend(keyword):

    # NOTE: initialize pytrend
    pytrend = TrendReq() 

    # NOTE: build payload with keywords
    pytrend.build_payload(kw_list=[keyword])
    # NOTE: by default pytrend will output per weekly data.
    df = pytrend.interest_over_time()

    # NOTE : Print to console
    print(df)

    # NOTE: Save to csv file
    save_to_csv(df, "C:\\tmp\\result.csv")

    # NOTE: plot data
    plot(df, keyword)


def save_to_csv(data, file_path):

    result = pd.DataFrame(data)
    result.to_csv(file_path)


def plot(data, keyword):

    data = data.reset_index() 
    fig = px.line(data, x="date", y=[keyword], title='Keyword Web Search Interest Over Time')
    fig.show() 
    

# NOTE :main call
get_google_trend("bitcoin")   