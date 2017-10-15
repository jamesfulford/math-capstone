# analysis.py
# by James Fulford

from analytics.dataset import Dataset as DS
import analytics as a

ds = DS.load("Confirmation Program.json")



# Creating Subsets:

subset = {
    "BASE": ds.data,
    "2013": filter(lambda x: x["section"].__contains__("2013"), ds.data),
    "2014": filter(lambda x: x["section"].__contains__("2014"), ds.data),
    "2015": filter(lambda x: x["section"].__contains__("2015"), ds.data),
    "2016": filter(lambda x: x["section"].__contains__("2016"), ds.data),
    # "summer": filter(lambda x: x["section"].__contains__("Summer") and not x["section"].__contains__("Year"), ds.data),
    # "year": filter(lambda x: x["section"].__contains__("Year") and not x["section"].__contains__("Summer"), ds.data),
    "summer": filter(lambda x: "Summer" in x["section"] and "Year" not in x["section"], ds.data),
    "year": filter(lambda x: "Year" in x["section"] and "Summer" not in x["section"], ds.data),
    "low_vol": filter(lambda x: len(x["volunteering"]) < 5, ds.data),
    "high_vol": filter(lambda x: len(x["volunteering"]) > 8, ds.data),
    "confirmed": filter(lambda x: x["attendance"] is True, ds.data),
    "not_confirmed": filter(lambda x: x["attendance"] is False, ds.data),  # not represented
    "no_vol": filter(lambda x: len(x["volunteering"]) is 0, ds.data)
}

# import json
# print json.dumps(map(lambda x: x["attendance"], subset["no_vol"]), indent=4)
# print len(filter(lambda x: x["attendance"] is False, subset["no_vol"]))

print a.mean(map(lambda x: len(x["volunteering"]), subset["summer"]))

for sub in subset.keys():
    print sub, len(subset[sub])


iden = lambda x: x
binary = lambda x: 1 if x is True else 0

variables = [("volunteering", len), ("attendance", binary), ("absences", sum)]

conf = .95  # s presumed to be max-min/4 by Empirical Rule
for var in variables:
    subs = {}
    for key in subset.keys():
        subs[key] = map(lambda x: var[1](x[var[0]]), subset[key])
        subs[key] = filter(lambda x: x is not None, subs[key])

    print var[0]
    mean = a.mean(subs["BASE"])
    print "BASE mean " + str(mean)
    print "BASE mean interval " + str(a.confidence_interval(subs["BASE"], conf=conf, pop_stdev=a.datarange(subs["BASE"]) / 4.))
    # s presumed to be max-min/4 by the Empirical Rule

    st_dev = a.p_standard_deviation(subs["BASE"])
    for key in subs.keys():
        confi = a.confidence_interval(subs[key], conf=conf, pop_stdev=st_dev)
        if mean < confi[0]:
            print "\t" + key + " mean above population at " + str(conf) + " assurance:"
            print "\t" * 2 + str(confi)
        elif mean > confi[1]:
            print "\t" + key + " mean below population at " + str(conf) + " assurance:"
            print "\t" * 2 + str(confi)
        else:
            pass

    if var[1] is binary:
        print
        phat = a.mean(subs["BASE"])
        print "BASE proportion " + str(phat)
        print "BASE proportion interval " + str(a.proportion_confidence_interval(subs["BASE"]))
        for key in subs.keys():
            prop = a.proportion_confidence_interval(subs[key])
            if phat < prop[0]:
                print "\t" + key + " proportion above population at " + str(conf) + " assurance:"
                print "\t" * 2 + str(prop)
            elif phat > prop[1]:
                print "\t" + key + " proportion below population at " + str(conf) + " assurance:"
                print "\t" * 2 + str(prop)
            else:
                pass

    print "-" * 80

print "*" * 90
print "Correlation Analysis"
print "*" * 90


for var1 in variables:
    index = variables.index(var1)
    for var2 in variables[index + 1:]:
        # this will go through all pairings once.
        print var1[0] + " and " + var2[0] + ":"
        subs1 = {}
        subs2 = {}
        for key in subset.keys():
            subs1[key] = map(lambda x: var1[1](x[var1[0]]), subset[key])
            subs1[key] = filter(lambda x: x is not None, subs1[key])
            subs2[key] = map(lambda x: var2[1](x[var2[0]]), subset[key])
            subs2[key] = filter(lambda x: type(x) is not type(None), subs2[key])
            print "\t" + key + ": " + str(a.pearson_r(subs1[key], subs2[key]))

ds.save(path="Sandbox")
