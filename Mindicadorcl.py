class MiIndicadorcl:
    """
    
    Clase desarrollada por Sergio Reyes Gajardo, en base a la API de Mindicadorcl
    
    ## Parametros:
    
    indicador (str):    Indica el tipo de indicador a devolver (No válido para InfoActualAPI_df)
                        Posibles valores: uf, ivp, dolar, dolar_intercambio, euro, ipc, utm, imacec, tpm, libra_cobre, tasa_desempleo, bitcoin
    year:               Indica el año de rescatar valores (Válido para InfoActualAPI_df)
    date (str):         Indica la fecha a rescatar
    
    ## Methods

    InfoAPI_ultimo_mes:     Devuelve un Dataframe con una timeseries con la informacion del indicador pasado durante el ultimo mes
    InfoActualAPI_df:       Devuelve un DataFrame con la informacion actual de todos los indicadores
    Infoday_df:             Devuelve un DataFrame con la informacion de un dia en concreto para el indicador pasado 
    InfoApiYear_df:         Devuelve un DataFrame con la informacion del anio pasado en la instancia de clase
    """

    from datetime import date
    import pandas as pd
    import json
    import requests
    
    def __init__(self, indicador = 'uf', year  = date.today().year, date = date.today().strftime('%d-%m-%Y')):
        self.indicador = indicador
        self.year = year
        self.date = date
    
    def InfoApi_ultimo_mes(self):

        import datetime as dt
        import pandas as pd
        import json
        import requests

        url = f'https://mindicador.cl/api/{self.indicador}'
        response = requests.get(url)
        data = json.loads(response.text.encode('utf-8'))
        df = pd.DataFrame.from_dict(data['serie'])
        df['fecha'] = pd.to_datetime(df['fecha'])
        df['fecha'] = df['fecha'].dt.strftime('%d/%m/%Y')
        df['Tipo'] = self.indicador.upper()
        df = df[['Tipo', 'fecha', 'valor']]
        return df

    def InfoApi_year(self):


        import datetime as dt
        import pandas as pd
        import json
        import requests

        #En este caso hareos la solicitud para el caso de consulta de un indicador en un anio determinado
        url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
        response = requests.get(url)
        data = json.loads(response.text.encode('utf-8'))
        #Para que el json se vea ordenado, retoornar pretty_json
        pretty_json = json.dumps(data, indent = 2)
        return data

    def InfoApiYear_df(self):

        import datetime as dt
        import pandas as pd
        import json
        import requests

        url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
        response = requests.get(url)
        data = json.loads(response.text.encode('utf-8'))
        df = pd.DataFrame.from_dict(data['serie'])
        df['fecha'] = pd.to_datetime(df['fecha'])
        df['fecha'] = df['fecha'].dt.strftime("%d-%m-%Y")
        return df        
    
    def InfoActualAPI(self):

        import datetime as dt
        import pandas as pd
        import json
        import requests

        url = f'https://mindicador.cl/api'
        response = requests.get(url)
        data = json.loads(response.text.encode('utf-8'))
        pretty_json = json.dumps(data, indent = 2)
        return data
    
    def InfoActualAPI_df(self):

        import datetime as dt
        import pandas as pd
        import json
        import requests

        url = f'https://mindicador.cl/api'
        response = requests.get(url)
        df = pd.read_json(response.text)
        df_transpose = df.transpose()
        df_transpose.reset_index(inplace = True)
        df_transpose.rename({'index': 'Tipo'}, axis= 1, inplace = True)
        df_transpose = df_transpose[['Tipo', 'unidad_medida', 'fecha', 'valor']]
        df_transpose.drop([0,1], axis = 0, inplace= True)
        df_transpose['fecha'] = pd.to_datetime(df_transpose['fecha'])
        df_transpose['fecha'] = df_transpose['fecha'].dt.strftime('%d/%m/%Y')
        return df_transpose

    def InfoToday(self):

        import datetime as dt
        import pandas as pd
        import json
        import requests

        url = f'https://mindicador.cl/api/{self.indicador}/{self.date}'
        response = requests.get(url)
        data = json.loads(response.text.encode('utf-8'))
        pretty_json = json.dumps(data, indent = 2)
        return data

    def Infoday_df(self):
        
        import datetime as dt
        import pandas as pd
        import json
        import requests

        url = f'https://mindicador.cl/api/{self.indicador}/{self.date}'
        response = requests.get(url)
        data = json.loads(response.text.encode('utf-8'))
        df = pd.DataFrame.from_dict(data['serie'])
        df['fecha'] = pd.to_datetime(df['fecha'])
        df['fecha'] = df['fecha'].dt.strftime("%d-%m-%Y")
        return df