# utility file for functions!! 


# this funtion takes the mean of both visitor columns for a given day of the week
from sqlite3 import Date


def get_series(df, day):
    grouped = df.get_group(day)
    new = grouped['New Visitor'].mean()
    old = grouped['Returning Visitor'].mean()
    return (new, old)

# this function will determine what month a date is in
def get_month(df):
    df2 = df.copy()
    ser = df2['Date']
    for i in range(len(ser)):
        ser.iloc[i] = ser.iloc[i].replace("/", " ")
        if ser.iloc[i].startswith("1", 0, 2):
            ser.iloc[i] = "january"
        elif ser.iloc[i].startswith("2", 0, 2):
            ser.iloc[i] = 'february'
        elif ser.iloc[i].startswith("3", 0, 2):
            ser.iloc[i] = 'march'
        elif ser.iloc[i].startswith("4", 0, 2):
            ser.iloc[i] = 'april'
        elif ser.iloc[i].startswith("5", 0, 2):
            ser.iloc[i] = 'may'
        elif ser.iloc[i].startswith("6", 0, 2):
            ser.iloc[i] = 'june'
        elif ser.iloc[i].startswith("7", 0, 2):
            ser.iloc[i] = 'july'
        elif ser.iloc[i].startswith("8", 0, 2):
            ser.iloc[i] = 'august'
        elif ser.iloc[i].startswith("9", 0, 2):
            ser.iloc[i] = 'september'
        elif ser.iloc[i].startswith("10", 0, 2):
            ser.iloc[i] = 'october'
        elif ser.iloc[i].startswith("11", 0, 2):
            ser.iloc[i] = 'november'
        elif ser.iloc[i].startswith("12", 0, 2):
            ser.iloc[i] = 'december'
    return df2

# def eval_months(df, month):
#     grouped = df.groupby