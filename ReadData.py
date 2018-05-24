from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# IEF

Ticker = ['VFINX', 'VINEX', 'VUSTX']

ts = TimeSeries(key='XAU63L4PGEZMXFRE', output_format='pandas')

for i in range(0, len(Ticker), 1):

    ts = TimeSeries(key='XAU63L4PGEZMXFRE', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=Ticker[i], outputsize='full')

    res = data.iloc[:,3]
    res = res.to_frame()
    res.columns = [Ticker[i]]

    if i==0:
        out = res
    else:
        out = out.join(res)

#data['close'].plot()
#plt.title('Intraday Times Series for the MSFT stock (1 min)')
#plt.show()

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/xudongsong/FinQuant/Indices.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
out.to_excel(writer, sheet_name='Indices')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
