import pandas as pd
import numpy as np

df = pd.read_csv("E:/Resume Projects/Python/youtube_channel_real_performance_analytics.csv")
print(df)

# Displaying the number of rows and columns
print(df.shape)

# Displaying column names
print(df.columns)

# Displaying data types
print(df.dtypes)

# Displaying statistical summary
print(df.describe())

# Check first 5 rows
print(df.head())

""" Analysis: The dataset was examined using df.shape, df.head(), df.columns, df.dtypes, and df.describe() to understand its structure, column names, data types, and statistical summary.
Observation: Dataset contains 364 rows and 70 columns.
First five records were examined.
Column names and data types were checked.
Statistical summary was generated. Conclusion: The dataset structure and its main characteristics were examined to understand the data before further analysis."""

"""Problem Statement 2: Identify Missing Values and Duplicate Records Objective: To identify missing values and duplicate records in the dataset."""
# Check missing values in each column
print(df.isnull().sum())

# Check total missing values
print(df.isnull().sum().sum())

# Check duplicate video IDs
print(df["ID"].duplicated().sum())

""""Analysis: Missing values were checked using df.isnull().sum() and df.isnull().sum().sum(). Duplicate records were identified using df.duplicated().sum(), and duplicate IDs were also checked.

Observation:

Total missing values: 0
Duplicate records: 0
Duplicate IDs: 0 Conclusion: No missing values or duplicate records were found in the dataset, so no removal or replacement was required for these checks."""

""""Problem Statement 3: Identify the Top 10 Records by Views Objective: To identify the 10 records with the highest number of views."""
# Identify the top 10 records by views
top_10_videos = df.sort_values(by="Views", ascending=False).head(10)
print(top_10_videos[["ID", "Views"]])

""""Observation The top 10 records have views ranging from 432,147 to 670,990. Record ID 228 has the highest number of views, with 670,990 views, followed by record ID 188 with 629,864 views. Conclusion Record ID 228 is the most-viewed record in the dataset, while record ID 197 ranks tenth among the top 10 records by views."""

"""""Problem Statement 4 Heading: Identify the Top 10 Records by Watch Time Objective: To identify the records with the highest total watch time and understand which records attract the most viewer attention."""
# Identify the top 10 records by watch time
top_10_watch_time = df.sort_values(by="Watch Time (hours)", ascending=False).head(10)
print(top_10_watch_time[["ID", "Watch Time (hours)"]])

"""Observation Record ID 196 has the highest watch time of 53,794.6587 hours, 
followed by record ID 228 with 50,228.5439 hours. The top 10 records have watch times 
ranging from 36,523.7522 to 53,794.6587 hours. Conclusion Record ID 196 has the highest total watch time in the dataset. 
Record ID 228 also performs strongly in both views and watch time, 
ranking second in watch time and second in views."""

#Problem Statement 5: Identify the Top 10 Records by Estimated Revenue Objective: To identify the records generating the highest estimated revenue.
# Identify the top 10 records by estimated revenue

top_10_revenue = df.sort_values(by="Estimated Revenue (USD)", ascending=False).head(10)
print(top_10_revenue[["ID", "Estimated Revenue (USD)"]])

"""Observation: Record ID 228 has the highest estimated revenue of $103.117, followed by Record ID 257 with $83.979.
The top 10 records have estimated revenue ranging from $44.228 to $103.117.
Conclusion: Record ID 228 generates the highest estimated revenue in the dataset, with an estimated revenue of $103.117. 
Record ID 257 ranks second among the top 10 records by estimated revenue."""


"""""Problem Statement 6: Identify the Top 10 Records by Subscribers Objective: To identify the 10 records with the highest number of subscribers."""
# Identify the top 10 records by subscribers

top_10_subscribers = df.sort_values(by="Subscribers", ascending=False).head(10)
print(top_10_subscribers[["ID", "Subscribers"]])

"""Observation: Record ID 188 has the highest number of subscribers, with 3,728, followed by Record ID 228 with 3,538.
The top 10 records have subscriber counts ranging from 1,456 to 3,728. 
Conclusion:Record ID 188 has the highest subscriber count in the dataset, with 3,728 subscribers. Record ID 228 ranks second with 3,538 subscribers."""

"""Problem Statement 7: Identify the Top 10 Records by Video Thumbnail CTR (%).
Objective: To identify the 10 records with the highest Video Thumbnail Click-Through Rate (CTR)."""
# Identify the top 10 records by video thumbnail CTR

top_10_ctr = df.sort_values(by="Video Thumbnail CTR (%)", ascending=False).head(10)
print(top_10_ctr[["ID", "Video Thumbnail CTR (%)"]])

"""Observation: Record ID 0 has the highest Video Thumbnail CTR of 27.66%, 
followed by Record ID 72 with 13.22%. The top 10 records have Video Thumbnail CTR values ranging from 11.61% to 27.66%. 
Conclusion: Record ID 0 has the highest Video Thumbnail CTR in the dataset, at 27.66%. 
Its CTR is substantially higher than that of the second-ranked record, ID 72, at 13.22%."""

#Problem Statement 8: Identify the Top 10 Records by Impressions. Objective: To identify the 10 records with the highest number of impressions."""
# Identify the top 10 records by impressions

top_10_impressions = df.sort_values(by="Impressions", ascending=False).head(10)
print(top_10_impressions[["ID", "Impressions"]])

"""Observation: Record ID 228 has the highest number of impressions, with 12,702,263, followed by Record ID 197 with 5,679,808. The top 10 records have impressions ranging from 3,598,719 to 12,702,263. Conclusion: Record ID 228 has the highest number of impressions in the dataset, with 12,702,263 impressions. Its impression count is substantially higher than that of the second-ranked record, ID 197."""

#Problem Statement 9: Identify the Top 10 Records by Likes. Objective: To identify the 10 records with the highest number of likes.
# Identify the top 10 records by likes
top_10_likes = df.sort_values(by="Likes", ascending=False).head(10)


print(top_10_likes[["ID", "Likes"]])

"""Observation:Record ID 228 has the highest number of likes, with 27,222, followed by Record ID 142 with 20,908. The top 10 records have likes ranging from 14,894 to 27,222. Conclusion:Record ID 228 has the highest number of likes in the dataset, with 27,222 likes. Record ID 142 ranks second with 20,908 likes."""

#Problem Statement 10: Identify the Top 10 Records by New Comments. Objective: To identify the 10 records with the highest number of New Comments
# Calculate like rate for each record
df["Calculated Like Rate (%)"] = (df["Likes"] / df["Views"]) * 100

print(df[["ID", "Views", "Likes", "Calculated Like Rate (%)"]].head(10))

"""Observation:Record ID 108 has the highest number of new comments, with 2,510, followed by Record ID 145 with 1,414. The top 10 records have new comment counts ranging from 1,113 to 2,510. Conclusion:Record ID 108 has the highest number of new comments in the dataset, with 2,510 new comments. Record ID 145 ranks second with 1,414 new comments."""

#Problem Statement 11: Identify the Top 10 Records by Shares. Objective: To identify the 10 records with the highest number of shares.
# Identify the top 10 records by shares
top_10_shares = df.sort_values(by="Shares", ascending=False).head(10)
print(top_10_shares[["ID", "Shares"]])

"""Observation:Record ID 228 has the highest number of shares, with 4,190, followed by Record ID 175 with 1,789. The top 10 records have share counts ranging from 1,369 to 4,190. Conclusion:Record ID 228 has the highest number of shares in the dataset, with 4,190 shares. Its share count is substantially higher than that of the second-ranked record, ID 175, which has 1,789 shares."""

#Problem Statement 12: Analyze Like Rate Across Records Objective: To calculate the like rate for each record and identify the top 10 records with the highest like rate.
# Calculate like rate for each record
df["Like Rate (%)"] = (df["Likes"] / df["Views"]) * 100

print(df[["ID", "Views", "Likes", "Like Rate (%)"]].head(10))


# Identify the top 10 records by like rate
top_10_like_rate = df.sort_values(by="Like Rate (%)", ascending=False).head(10)

print(top_10_like_rate[["ID", "Views", "Likes", "Like Rate (%)"]])

"""Observation:

Record ID 271 has the highest like rate at approximately 11.90%.

Record ID 320 ranks second with a like rate of approximately 11.72%.

Record ID 274 ranks third with a like rate of approximately 10.82%.

Record ID 249 has the highest number of likes among these 10 records, with 19,610 likes, and a like rate of approximately 9.44%.

All 10 records have a like rate above 9%.

Conclusion: The analysis shows that record ID 271 has the highest like rate, followed by IDs 320 and 274. These records receive more likes relative to their views than the other records in the dataset. However, a higher like rate does not necessarily mean a higher total number of likes, as demonstrated by record ID 249, which has the most likes among the top 10 but ranks tenth in like rate. This metric measures likes relative to views and does not include other forms of engagement, such as comments and shares."""

#Problem Statement 13:Analyze Average View Duration Objective: To examine the average view duration across records and identify the records with the highest average view duration.
# Display average view duration for the first 10 records
print(df[["ID", "Average View Duration"]].head(10))

# Identify the top 10 records by average view duration
top_10_duration = df.sort_values(
    by="Average View Duration", ascending=False
).head(10)

print(top_10_duration[["ID", "Average View Duration"]])

"""Observation:

Record ID 358 has the highest average view duration at 776.

Record ID 363 ranks second with an average view duration of 755.

Record ID 361 ranks third with an average view duration of 703.

The average view duration among the top 10 records ranges from 544 to 776.

Conclusion: Record ID 358 has the highest average view duration among all records in the dataset. These results identify the records with the longest average view duration, which can help highlight videos that hold viewers' attention for longer."""

"""Problem Statement 14: Identify the Top 10 Records by Unsubscribes Objective: 
To identify the 10 records with the highest number of unsubscribes and understand which records experienced the greatest loss of subscribers."""

# Identify the top 10 records by unsubscribes
top_10_unsubscribes = df.sort_values(
    by="Unsubscribes", ascending=False
).head(10)

print(top_10_unsubscribes[["ID", "Unsubscribes"]])

"""Observation:

Record ID 274 has the highest number of unsubscribes, with 713.

Record ID 57 ranks second, with 359 unsubscribes.

Record ID 188 ranks third, with 197 unsubscribes.

The number of unsubscribes among the top 10 records ranges from 91 to 713.

Conclusion: Record ID 274 has the highest number of unsubscribes in the dataset. This record experienced substantially more unsubscribes than the other records in the top 10. Further investigation may help identify possible reasons for this result."""

#Problem Statement 15: Analyze Summary Statistics of Views and Watch Time Objective: To calculate and analyze the average, minimum, maximum, and other summary statistics of views and watch time across all records.
# Calculate summary statistics for views and watch time
print(df[["Views", "Watch Time (hours)"]].describe())

"""Observation:- The dataset contains 364 records for both Views and Watch Time (hours).
The average number of views is 128,800.10, while the average watch time is 10,058.97 hours.
The median views are 101,950.50, which is lower than the mean of 128,800.10.
Views range from 2,461 to 670,990, while watch time ranges from 12.6979 to 53,794.6587 hours.
Both metrics show substantial variation across records, as indicated by their standard deviations. 
Conclusion:The summary statistics show considerable variation in views and watch time across the 364 records. The average views exceed the median views, indicating that some records with higher view counts influence the overall average."""

#Problem Statement 16: Analyze Video Performance by Day of the Week Objective: To compare the average views across different days of the week and identify which days have higher average views.
# Calculate average views for each day of the week
average_views_by_day = df.groupby("Day of Week")["Views"].mean()


print(average_views_by_day)


"""Observation:- Friday has the highest average views, at approximately 142,267.04.
Sunday ranks second, with approximately 140,092.06 average views.
Thursday has the lowest average views, at approximately 110,206.80.
Average views vary across the days of the week, ranging from approximately 110,206.80 to 142,267.04. 
Conclusion:The analysis shows that Friday has the highest average views, while Thursday has the lowest. 
This indicates differences in average views across days of the week, but it does not establish that the day itself causes higher or lower views."""

#Problem Statement 17: Analyze Video Performance by Month. Objective: To compare the average views across different months and identify monthly differences in video performance.
#Calculate average views for each month
average_views_by_month = df.groupby("Month")["Views"].mean()


print(average_views_by_month)

"""Observation:October has the highest average views, at 181,558.75.

July ranks second, with 161,448.41 average views, followed by September with 153,248.33.

May has the lowest average views, at 91,280.24.

Average views vary across months, ranging from 91,280.24 to 181,558.75.

Conclusion:October has the highest average views, while May has the lowest average views among the months in the dataset. This analysis highlights monthly differences in average views but does not establish the reason for those differences."""


#Problem Statement 18: Analyze the Relationship Between Views and Estimated Revenue Objective: To compare views and estimated revenue across records and examine whether records with higher views also tend to have higher estimated revenue.
# Calculate the correlation between views and estimated revenue
views_revenue_correlation = df["Views"].corr(df["Estimated Revenue (USD)"])


print(views_revenue_correlation)

"""Observation:The correlation coefficient between Views and Estimated Revenue (USD) is approximately 0.358.

The positive value indicates that higher views tend to be associated with higher estimated revenue.

The correlation is not particularly strong, suggesting that views alone do not fully explain differences in estimated revenue.

Conclusion:Views and estimated revenue have a positive but relatively weak-to-moderate correlation in the dataset. Although records with higher views may tend to generate higher revenue, other factors may also contribute to revenue differences."""

#Problem Statement 19: Analyze Revenue per 1,000 Views. Objective: To examine the distribution of revenue per 1,000 views using summary statistics.
# Calculate summary statistics for revenue per 1,000 views
print(df["Revenue per 1000 Views (USD)"].describe())

"""Observation:The dataset contains 364 records for Revenue per 1,000 Views (USD).

The average value is approximately $0.1123, while the median is $0.05.

The minimum value is $0.00, and the maximum is $1.60.

The standard deviation is approximately $0.1797, indicating considerable variation in the values.

Since the mean is higher than the median, some higher values may be influencing the average.
    
Conclusion:Revenue per 1,000 views varies considerably across records. The mean of approximately $0.1123 is higher than the median of $0.05, suggesting that the distribution may be influenced by records with higher values."""


#Problem Statement 20: Compare Likes and Dislikes. Objective: To compare the average number of likes and dislikes across all records.
# Calculate average likes and dislikes
print("Average Likes:", df["Likes"].mean())
print("Average Dislikes:", df["Dislikes"].mean())

"""Observation:The average number of likes across all records is approximately 5,526.73.

The average number of dislikes is approximately 123.96.

On average, records have substantially more likes than dislikes.

Conclusion:The dataset shows that the average number of likes is considerably higher than the average number of dislikes. This indicates that likes are more frequent than dislikes on average across the records."""

#Problem Statement 21: Analyze the Relationship Between Video Duration and Views. Objective: To examine whether video duration is associated with the number of views.
#Calculate the correlation between video duration and views
duration_views_correlation = df["Video Duration"].corr(df["Views"])
print(duration_views_correlation)

"""Observation:The correlation coefficient between Video Duration and Views is approximately −0.052.

The negative value indicates a very slight negative linear relationship between video duration and views.

Since the coefficient is close to zero, there is almost no linear relationship between these two variables in the dataset.

Conclusion:The analysis shows a negligible negative linear relationship between video duration and views. Therefore, video duration alone does not show a meaningful linear association with views in this dataset."""

#Problem Statement 22: Identify Records with Views Above the Average. Objective: To identify the number of records with views greater than the overall average views.
# Calculate the average views
average_views = df["Views"].mean()

# Count records with views above the average
above_average_views = df[df["Views"] > average_views]

# Display the results
print("Average Views:", average_views)
print("Records above average views:", len(above_average_views))

"""Observation:The average number of views across all records is approximately 128,800.10.

Out of 364 records, 148 records have views greater than the average.

The remaining 216 records have views equal to or below the average.

Conclusion:Out of 364 records, 148 have views above the overall average of 128,800.10. This means approximately 40.66% of the records exceed the average views."""

#Problem Statement 23: Analyze Video Thumbnail CTR and Impressions. Objective: To examine the relationship between video thumbnail click-through rate (CTR) and impressions.
# Calculate the correlation between thumbnail CTR and impressions
ctr_impressions_correlation = df["Video Thumbnail CTR (%)"].corr(df["Impressions"])

# Display the result
print(ctr_impressions_correlation)

"""Observation:The correlation coefficient between Video Thumbnail CTR (%) and Impressions is approximately 0.155.

The positive value indicates a weak positive linear relationship between thumbnail CTR and impressions.

Since the coefficient is close to zero, the linear relationship between these variables is weak. Conclusion:The analysis indicates a weak positive linear relationship between Video Thumbnail CTR and Impressions in this dataset. Therefore, the two variables have only a limited linear association, and this result does not establish a causal relationship."""

#Problem Statement 24: Analyze Subscribers and Views. Objective: To examine the relationship between subscriber count and views across records.
# Calculate the correlation between subscribers and views
subscribers_views_correlation = df["Subscribers"].corr(df["Views"])

# Display the result
print(subscribers_views_correlation)

"""Observation:The correlation coefficient between Subscribers and Views is approximately 0.802.

The positive value indicates that records with higher subscriber counts tend to have higher view counts.

The correlation is relatively strong, indicating a strong positive linear association between these two variables.

Conclusion:The analysis shows a strong positive linear relationship between subscriber count and views in the dataset. Records with higher subscriber counts tend to be associated with higher views, although correlation alone does not establish causation."""

#Problem Statement 25: Summarize Key Channel Performance Metrics Objective: To calculate summary statistics for views, watch time, subscribers, likes, and estimated revenue to understand overall channel performance.
# Calculate summary statistics for key performance metrics
print(df[["Views", "Watch Time (hours)", "Subscribers", "Likes", "Estimated Revenue (USD)"]].describe())

"""Observation:The dataset contains 364 records for all five performance metrics.

The average views are approximately 128,800.10, and the average watch time is 10,058.97 hours.

The average subscriber value is 321.02, while the median is 180.

The average number of likes is 5,526.73, with a maximum of 27,222.

Estimated revenue averages 
0.00 and a maximum of $103.117.

The minimum subscriber value is -3, which may require further investigation.

Conclusion:The summary statistics show considerable variation in views, watch time, subscribers, likes, and estimated revenue across the 364 records. The mean values of views, subscribers, and estimated revenue are higher than their respective medians, suggesting that some records with higher values influence the averages. 
The negative minimum subscriber value should be investigated before drawing further conclusions about subscriber performance."""