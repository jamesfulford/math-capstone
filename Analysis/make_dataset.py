# make_dataset.py
# by James Fulford

import analytics as a
import commons
import utils
from copy import deepcopy as dc

scheme = {
    "section": {
        "stat_type": "nominal",
        "data_type": "str"
    },
    "year_round": {
        "stat_type": "nominal",
        "data_type": "bool",
    },
    "name": {
        "stat_type": "nominal",
        "id": True,
        "data_type": "str"
    },
    "volunteering": [
        {
            "date": {
                "stat_type": "interval",
                "data_type": "str"
            },
            "event": {
                "stat_type": "nominal",
                "data_type": "str"
            }
        }
    ],
    "attendance": {
        "stat_type": "nominal",
        "data_type": "bool"
    },
    "absences": [
        {
            "stat_type": "ordinal",
            "data_type": "int"
        }
    ]
}

ds = {
    "name": "Confirmation Program",
    "schema": scheme,
    "attributes": {
    },
    "data": commons.dataset(),
    "attribute_schema": {},
    "save_path": "/Users/jamesfulford/Desktop",
    "error_path": "/Users/jamesfulford/Desktop"
}


# There are 6 people who did not have absence/attendance and confirmation records
# They dropped out before our scope begins (Conf II or start of Summer program)
# So, we can filter these volunteering records out.
for entry in ds["data"]:
    if "attendance" not in map(str, entry.keys()):
        entry["attendance"] = None
ds["data"] = filter(lambda x: type(x["attendance"]) is not type(None), ds["data"])


clean_volunteers = False
i = 0
if clean_volunteers:
    for entry in ds["data"]:
        keys = map(str, entry.keys())
        if "volunteering" not in keys:
            entry["volunteering"] = None
            i += 1
    # Take out non-vol records if clean_out is true
    ds["data"] = filter(lambda x: type(x["volunteering"]) is not type(None), ds["data"])
    print i, "volunteer records scrubbed."
else:
    for entry in ds["data"]:
        if "volunteering" not in map(str, entry.keys()):
            entry["volunteering"] = []
            if not entry["attendance"]:
                i += 1
            else:
                i += 1
    print i, "shell volunteers created. (0 volunteering events each)"




ds = a.dataset.Dataset(ds)

# Map event titles to the categories defined in remap_events.json
# mapping = utils.load("remap_events.json")
# ds.write("event", mapping)

ds.save()
