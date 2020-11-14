
import pandas as pd

df = pd.read_csv('resources\cities.csv')


cities_html = df.to_html(index=False) 

print(cities_html)  

# <table class="cities_html.dataframe">
    
# </table>


# HTML(df.to_html(classes='table table-striped'))
# cities.to_html('city.html', index=False)
# <div class="table-responsive">
#     <table class="table">

#     </table>
# </div>
# print(result);
