from MySQL_config import MySQL_config
import plotly.express as px
import pandas as pd

def population_rf(df):
    fig = px.bar(df, x='год', y='население',
                 labels={'население': 'Население РФ', 'год': 'Год'}, text_auto=True, color="население")
    fig.update_yaxes(range=[141000000, 147000000])
    fig.show()


def population_growth(df):
    fig = px.bar(df, x='год', y='общий прирост', labels={'общий прирост': 'Общий прирост население РФ', 'год': 'Год'},
                 text_auto=True, color="общий прирост")
    fig.show()


def family(df):
    fig = px.bar(df, x="год", y=['браки', "разводы"],
                       labels={'variable': ' ', 'год': 'Год', 'value': 'Количество'},
                       barmode='group', height=600)
    fig.show()


def animation():
    dataframe = pd.DataFrame.from_dict(MySQL_config().output("ok"))
    fig = px.bar(dataframe, x="Демографическая характеристика", y="Коэффициент на 1000 населения", color="Демографическая характеристика",
                 animation_frame="Год", range_y=[0, 20])
    fig.show()


def main():
    df = pd.DataFrame.from_dict(MySQL_config().output("demographics"))

    population_rf(df)
    population_growth(df)
    family(df)
    animation()


if __name__ == "__main__":
    main()
