import yelp_analysis_tools as yat 

dataset_business = "data/head_yads_business.json"
dataset_user = "data/head_yads_user.json"
dataset_review = "data/head_yads_review.json"

# dataset_business = "../yelp_academic_dataset_business.json"
# dataset_user     = "../yelp_academic_dataset_user.json"
# dataset_review   = "../yelp_academic_dataset_review.json"

# reviews, businesses, users = yat.importJSON(dataset) 
businesses  = yat.importBusinessesJSON(dataset_business)
users       = yat.importUsersJSON(dataset_user)
reviews     = yat.importReviewsJSON(dataset_review)

# print len(businesses)
# print len(users)
# print len(reviews)

#print users
# print reviews

prolificUsers = [u['user_id'] for u in users if u['review_count'] > 0] 
# print len(prolificUsers)
prolificUsersReviewDates = [r['date'] for r in reviews if r['user_id'] in prolificUsers]

'''for r in reviews:
    if r['user_id'] in prolificUsers
        print r['date']'''
# print prolificUsersReviewDates
prolificUsersReviewDays = yat.convertDatesToDays(prolificUsersReviewDates) 
# print prolificUsersReviewDays
prolificDays = yat.get_counts(prolificUsersReviewDays) 
print prolificDays
yat.buildBarDayPlot(prolificDays, title="Days Prolific Users Reviewed Businesses")
