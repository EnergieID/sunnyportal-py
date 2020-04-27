import datetime as dt
import pandas as pd

from .client import Plant


class PandasPlant(Plant):
    def month_overview(self, date: dt.date) -> pd.DataFrame:
        req = super(PandasPlant, self).month_overview(date=date)
        df = pd.DataFrame(req.days)
        if df.empty:
            return df
        df.set_index('timestamp', inplace=True)
        return df