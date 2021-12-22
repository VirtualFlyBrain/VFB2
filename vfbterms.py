import sys
from os import listdir, chdir
from os.path import isfile, join
from vfb_connect.cross_server_tools import VfbConnect


def gen_dict_extract(key, var):
    if hasattr(var, "iteritems"):
        for k, v in var.iteritems():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def wrapStringInHTMLMac(term):
    import datetime
    import json
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = term["term"]["core"]["short_form"] + ".md"
    f = open(filename, "w", encoding="utf-8")
    note = """
    {{% alert title="Note" color="primary" %}}
    This page displays the raw VFB json record for this term.
    Please use the button below to open the term inside the Virtual Fly Brain viewer:
    {{% /alert %}}
    """
    wrapper = """---
    title: "{0} [{1}]"
    tags: [{4}]
    content: [term]
    date: {7}
    description: >
        {2} {3}
---

    {8}

    {{< button class="btn btn-lg btn-secondary mr-3 mb-4" href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id={1}" >}}View term in VFB <i class="fas fa-desktop ml-2 "></i>{{< /button >}}

        ## VFB Term Json

        ```json
        {5}
        ```
        ## Available images
        <a href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id={1}">
        {6}
        </a>

    """
    folders = gen_dict_extract("image_folder", term)
    images = ""
    for folder in folders:
        images += '<img src="' + folder + 'thumbnail.png" alt="drawing" width="200"/>'
    print(images)
    whole = wrapper.format(term["term"]["core"]["label"],term["term"]["core"]["short_form"],' '.join(term["term"]["description"]),' '.join(term["term"]["comment"]),','.join(term["term"]["core"]["types"]),json.dumps(term, indent=4),images,now,note)
    try:
        f.write(whole)
    except:
        print(whole)
    f.close()


vc = VfbConnect()

mypath = sys.argv[1]
print("Updating all files in " + mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

chdir(mypath)

all = sorted([w.replace(".md", "") for w in onlyfiles if w.startswith("FBbt")])
for id in all:
    print(id)
    terms = vc.neo_query_wrapper.get_TermInfo([id])
    for term in terms:
        wrapStringInHTMLMac(term)
