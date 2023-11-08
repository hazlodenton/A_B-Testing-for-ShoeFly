import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count( ).reset_index()
clicks_pivot = clicks_by_source.pivot(
  index = 'utm_source',
  columns = 'is_click',
  values = 'user_id').reset_index()
clicks_pivot['Percent_clicked'] = \
   round(clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False]), 2)
# //////////
clicks_by_group = ad_clicks.groupby(['experimental_group','is_click']).user_id.count( ).reset_index()
# //////////
exp_pivot = clicks_by_group.pivot(
  index = 'experimental_group', 
  columns = 'is_click', 
  values = 'user_id').reset_index()
# //////////
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
clicks_day = ad_clicks.groupby(['day', 'is_click']).user_id.count( ).reset_index()
# /////////
day_pivot = clicks_day.pivot(
  index = 'day', 
  columns = 'is_click', 
  values = 'user_id').reset_index()
# /////////
# a_clicks['percent_clicked'] = clicks_day[True] / (clicks_day[True] + clicks_day[False])
# b_clicks['percent_clicked'] = clicks_day[True] / (clicks_day[True] + clicks_day[False])
aclicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
bclicks= b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
a_pivot = aclicks.pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id').reset_index()
b_pivot = bclicks.pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id').reset_index()
# ///////
a_pivot['percent_clicked'] = round(a_pivot[True] / a_pivot[True] + a_pivot[False], 2)
b_pivot['percent_clicked'] = round(b_pivot[True] / b_pivot[True] + b_pivot[False], 2)
# ///////
print(a_pivot)
print(b_pivot)