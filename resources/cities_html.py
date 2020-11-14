
import pandas as pd

df = pd.read_csv('cities.csv')


cities_html = df.to_html("cities.html", index=False) 

print(cities_html)  

cities_html = df.to_html(classes='table table-responsive'))
# print
# <table class="cities_html.dataframe">
    
# </table>


# HTML(df.to_html(classes='table table-striped')) - this would work
# cities.to_html('city.html', index=False)
# <div class="table-responsive">
#     <table class="table">

#     </table>
# </div>
# print(result);
