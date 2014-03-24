import yelp_analysis_tools as yat, json, numpy as np, linecache, matplotlib.pyplot as plt
import itertools
from collections import Counter


# Dataset
businessIDjson = "data/extractedBusinessIDFromBusinessJSON.txt"
businessLats = "data/extractedBusinessLatitudeFromBusinessJSON.txt"
businessLongs = "data/extractedBusinessLongitudeFromBusinessJSON.txt"
businessIDs = "data/extractedBusinessIDFromReviews.txt"
userIDs = "data/extractedUserIDFromReviews.txt"
reviews = "data/extractedReviewsFromReviews.txt"
catgs = "data/extractedCategoriesFromBusinessJSON.txt"
bsnss = "data/extractedBusinessNameFromBusinessJSON.txt"

count = 1
line_index = 1
fakes = []
fakeindex = []

with open(reviews) as f:
    seen = set()
    for review in f:
        # line_lower = line.lower()
        if review in seen:
            # print 'line', line_index, line
            # print seen[-1]
            fakeindex.append(line_index)
            fakes.append(review)
            # print line_index
            count = count + 1
        else:
            # seen.add(line_lower)
            seen.add(review)
    	line_index=line_index+1



fr_businesses = []

for index in fakeindex:
	# fr_users.append(linecache.getline(userIDs, index).rstrip())
	fr_businesses.append(linecache.getline(businessIDs, index).rstrip())
	
# for f in fr_businesses:
# 	print f

fr_catgs = []
for index in fakeindex:
	# print linecache.getline(businessIDjson, index).rstrip()
	fr_catgs.append(linecache.getline(catgs, index).rstrip())

lookup = fr_businesses
# print lookup

bidj_index = []
# enumerate(open(businessIDjson))
with open(businessIDjson) as bidj:
	for num, line in enumerate(bidj, 1):
		for l in lookup:
			if l in line:
				bidj_index.append(num)
				# bidj_index.append(line)
# print bidj_index

lats = []
longs = []
# print len(fakeindex), len(bidj_index)
length = len(fakeindex)

# for l in fakeindex:
for i in xrange(length):
	lats.append(linecache.getline(businessLats, bidj_index[i]).rstrip())
	longs.append(linecache.getline(businessLongs, bidj_index[i]).rstrip())

fr_business = []
for index in bidj_index:
	# print linecache.getline(businessIDjson, index).rstrip()	
	line = linecache.getline(bsnss, index)
	line = line.replace("'", "").rstrip()
	fr_business.append(line)

inserts = []
for x, y, z in itertools.izip(fr_business, lats, longs):
	 inserts.append("%s%s%s%s%s%s%s" % ("['",x,"',",y,',',z,"],"))

d = Counter(fr_catgs)
freq, categ = d.keys(), d.values()
# print freq, categ

num_catgs = np.arange(len(freq))
# print num_catgs

labels = fr_catgs
plt.bar( num_catgs, categ , align='center' )
plt.xticks( num_catgs, labels )
plt.yticks( range(0,10) )
plt.show()