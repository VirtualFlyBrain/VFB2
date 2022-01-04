import sys
from os import listdir, chdir
from os.path import isfile, join
from vfb_connect.cross_server_tools import VfbConnect



note = """
{{% alert title="Note" color="primary" %}}This page displays the raw VFB json record for this term. Please use the link below to open the term inside the Virtual Fly Brain viewer{{% /alert %}}
"""
wrapper = """---
    title: "{0} [{1}]"
    linkTitle: "{0}"
    tags: [{4}]
    content: [term]
    date: {7}
    description: >
        {2} {3}
    weight: 1000
    sitemap_exclude: true
---

{8}

<span style="font-size:larger;">[Open **{0}** in **VFB**](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id={1})</span>

{6}

## VFB Term Json

```json
{5}
```

"""

def find_images(src, key, dest=set()):
    for k, v in zip(src.keys(), src.values()):
        if key == k:
            if not v in str(dest):
                dest.add('<img src="' + v + 'thumbnail.png" alt="{{< param linkTitle >}}" width="200"/>')
        elif isinstance(v, dict):
            if key in str(v):
                dest.union(find_images(v, key, dest))
        elif isinstance(v, list):
            if key in str(v):
                for i in v:
                    if key in str(i):
                        if isinstance(i, dict):
                            dest.union(find_images(i, key, dest))
    return dest

def find_values(src, key, dest=set()):
    for k, v in zip(src.keys(), src.values()):
        if key == k:
            if not v in str(dest):
                dest.add(v)
        elif isinstance(v, dict):
            if key in str(v):
                dest.union(find_values(v, key, dest))
        elif isinstance(v, list):
            if key in str(v):
                for i in v:
                    if key in str(i):
                        if isinstance(i, dict):
                            dest.union(find_values(i, key, dest))
    return dest

def save_terms(ids):
    run = 10000
    import os.path
    for id in ids:
        try:
            if run > 1:
                filename = id + ".md"
                if not os.path.isfile(filename):
                    print(id)
                    run -= 1
                    terms = vc.neo_query_wrapper.get_TermInfo([id])
                    for term in terms:
                        wrapStringInHTMLMac(term)
        except:
            print("ERROR:" + id)


def wrapStringInHTMLMac(term):
    import datetime
    import json
    import os.path
    import traceback
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = term["term"]["core"]["short_form"] + ".md"
    if not os.path.isfile(filename):
        f = open(filename, "w", encoding="utf-8")
        images = ""
        images = " ".join(find_images(term, "image_folder", set()))
        if "<img" in images:
            images = '## Available images\n<a href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id=' + term["term"]["core"]["short_form"] + '">' + images + '</a>'
        desc = ""
        com = ""
        try:
            desc = ' '.join(term["term"]["description"])
            com = ' '.join(term["term"]["comment"])
        except:
            print('missing desc')
        # If no description then combine all 'label' in the json to give a a crude description of term, xrefs, technique & examples.
        try:
            if desc == "":
                desc = " ".join(find_values(term, "label", set()))
        except Exception as e:
            print('error on label for desc')
            print(e)
            print(traceback.format_exc())
        whole = wrapper.format(term["term"]["core"]["label"].replace('\\','&bsol;'),term["term"]["core"]["short_form"],desc,com,','.join(term["term"]["core"]["types"]),json.dumps(term, indent=4),images,now,note)
        try:
            f.write(whole)
        except:
            print(whole)
        f.close()


vc=VfbConnect(neo_endpoint='http://pdb.v4.virtualflybrain.org', neo_credentials=('neo4j', 'vfb'), owlery_endpoint='http://owl.virtualflybrain.org/kbs/vfb/')


mypath = sys.argv[1]
print("Updating all files in " + mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

chdir(mypath + 'fbbt/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBbt' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbbi/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBbi' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbcv/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBcv' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbdv/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBdv' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'vfb/')
vfb = vc.nc.commit_list(["MATCH (n:Individual) WHERE n.short_form starts with 'VFB_' AND NOT n.short_form starts with 'VFB_internal' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0]
save_terms(vfb)
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'VFBexp_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
save_terms(vc.nc.commit_list(["MATCH (n:Dataset) with n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
save_terms(vc.nc.commit_list(["MATCH (n:pub) with n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
