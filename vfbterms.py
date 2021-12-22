import sys

def wrapStringInHTMLMac(term):
    import datetime
    import json
    from webbrowser import open_new_tab
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = term['term']['core']['short_form'] + '.html'
    f = open(filename,'w',encoding='utf-8')
    amp = """<style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>"""
    wrapper = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta name="description" content="{0} [{1}] {2} {3}">
    <link rel="preload" as="script" href="https://cdn.ampproject.org/v0.js">
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <script type="application/ld+json">
	{4}
    </script>
    <script async src="https://virtualflybrain.org/data/VFB/json/redirect.js"></script>
    {6}

    <link rel="canonical" href="https://virtualflybrain.org/reports/{1}">
    <title>{0} [{1}]</title>
  </head>
  <body>
    <h1><a id="vfblink" href=\"https://v2.virtualflybrain.org/reports/{1}\">{0}</a></h1>
    	<div id="link"><a id="vfblink" href=\"https://v2.virtualflybrain.org/reports/{1}\">Click here if not redirected</a></div>
	<div id="json">{5}</div>
  </body>
</html>"""
    dictionary={} 
    for header in term.keys(): 
            if header == "term": 
                dictionary["@context"] = "https://schema.org" 
                dictionary["@type"] = "Dataset" 
                dictionary["license"] = "http://creativecommons.org/licenses/by-sa/4.0/"
                dictionary["name"] = term["term"]["core"]["label"]
                dictionary["termCode"] = term["term"]["core"]["short_form"] 
                dictionary["sameAs"] = term["term"]["core"]["iri"] 
                dictionary["url"] = "https://virtualflybrain.org/reports/" + term["term"]["core"]["short_form"] 
                dictionary["description"] = term["term"]["core"]["label"] + " [" +  term["term"]["core"]["short_form"] + "] " + " ".join(term["term"]["description"]) + " (" + " ".join(term["term"]["comment"]) + ")" 
                if len(dictionary["description"]) < 50:
                    dictionary["description"] = dictionary["description"].ljust(50,".")
                dictionary["creator"] = json.loads('{"@type": "Organization","url": "https://virtualflybrain.org","logo": "https://v2.virtualflybrain.org/images/vfbbrain_icon.png","brand":"Virtual Fly Brain","name":"Virtual Fly Brain","legalName":"Virtual Fly Brain","description":"VFB integrates data curated from the literature with image data from many bulk sources. The search system allows you to search for neurons and neuroanatomical structures using almost any name found in the literature. The query system can identify neurons innervating any specified neuropil or fasciculating with any specified tract. It also allows queries for genes, transgenes and phenotypes expressed in any brain region or neuron. Search and query results combine referenced textual descriptions with 3D images and links to originating data sources. VFB features tens of thousands of 3D images of neurons, clones and expression patterns, registered to standard template brains. Any combination of these images can be viewed together. A BLAST-type query system (NBLAST) allows you to find similar neurons and drivers starting from a registered neuron.","headline":"A hub for fruit fly (Drosophila melanogaster) neuronal anatomy, connectivity & imaging data","affiliation":[{"@type": "Organization","name":"Institute for Adaptive and Neural Computation, School of Informatics, University of Edinburgh","logo":"https://v2.virtualflybrain.org/images/vfb/project/logos/InformaticsLogo.gif","url":"https://web.inf.ed.ac.uk/anc"},{"@type": "Organization","name":"Department of Genetics, University of Cambridge","logo":"https://v2.virtualflybrain.org/images/vfb/project/logos/CUnibig.png","url":"http://www.gen.cam.ac.uk/"},{"@type": "Organization","name":"Department of Physiology, Development and Neuroscience, University of Cambridge", "url":"https://www.pdn.cam.ac.uk/","logo":"https://www.pdn.cam.ac.uk/images/157071101713274785.png/image_logo"},{"@type": "Organization","name":"FlyBase","url":"https://flybase.org","logo":"http://flybase.org/images/fly_logo.png"},{"@type": "Organization","name":"MRC Laboratory of Molecular Biology, Cambridge","logo":"https://v2.virtualflybrain.org/images/vfb/project/logos/MRC-LMB_logo.png","url":"http://www2.mrc-lmb.cam.ac.uk/"},{"@type": "Organization","name":"European Bioinformatics Institute (EMBL-EBI), Cambridge","logo":"https://v2.virtualflybrain.org/images/vfb/project/logos/EMBL_EBI_logo_180pixels_RGB.png","url":"http://www.ebi.ac.uk/"}],"funder":{"@type": "Organization","name":"Wellcome Trust","logo":"https://v2.virtualflybrain.org/images/vfb/project/logos/wtvm050446.png","url":"https://wellcome.org/"},"sameAs":["https://en.wikipedia.org/wiki/Virtual_Fly_Brain","https://www.youtube.com/channel/UC1g10aJo13fXpO9VwRJPdHg","https://www.facebook.com/Virtual-Fly-Brain-131151036987118","https://twitter.com/virtualflybrain","https://virtualflybrain.tumblr.com/"],"alternateName":"VFB","subjectOf":[{"@type": "ScholarlyArticle","citation":"http://dx.doi.org/10.1093/bioinformatics/btr677","sameAs":"http://dx.doi.org/10.1093/bioinformatics/btr677","headline":"The Virtual Fly Brain browser and query interface","name":"The Virtual Fly Brain browser and query interface","datePublished":"2012","author":[{"@type":"person","name":"Milyaev, N."},{"@type":"person","name":"Osumi-Sutherland, D."},{"@type":"person","name":"Reeve, S."},{"@type":"person","name":"Burton, N."},{"@type":"person","name":"Baldock, R. A."},{"@type":"person","name":"Armstrong, J. D."}],"publisher":"Bioinformatics"},{"@type": "ScholarlyArticle","citation":"http://dx.doi.org/10.1098/rstb.2017.0380","sameAs":"http://dx.doi.org/10.1098/rstb.2017.0380","headline":"Geppetto: a reusable modular open platform for exploring neuroscience data and models","name":"Geppetto: a reusable modular open platform for exploring neuroscience data and models","author":"Cantarelli, Matteo and Marin, Boris and Quintana, Adrian and Earnshaw, Matt and Court, Robert and Gleeson, Padraig and Dura-Bernal, Salvador and Silver, R. Angus and Idili, Giovanni","publisher": "Philosophical Transactions of the Royal Society B: Biological Sciences","datePublished": "2018"}]}')
            if header == "dataset_license": 
                    for dl in term["dataset_license"][0].keys(): 
                        if dl == "dataset" and not term["dataset_license"][0]["dataset"]["core"]["short_form"] is None:
                            dictionary["subjectOf"] = {} 
                            dictionary["subjectOf"]["@type"] = "Dataset" 
                            dictionary["subjectOf"]["name"] = term["dataset_license"][0]["dataset"]["core"]["label"] 
                            dictionary["subjectOf"]["termCode"] = term["dataset_license"][0]["dataset"]["core"]["short_form"]
                            dictionary["subjectOf"]["description"] = dictionary["subjectOf"]["name"] + " [" + dictionary["subjectOf"]["termCode"] + " ]"
                            if "description" in term["dataset_license"][0]["dataset"]:
                               dictionary["subjectOf"]["description"] = " ".join(term["dataset_license"][0]["dataset"]["description"]) + " (" + " ".join(term["dataset_license"][0]["dataset"]["comment"]) + ")"
                            if len(dictionary["subjectOf"]["description"]) < 50:
                               dictionary["subjectOf"]["description"] = dictionary["subjectOf"]["description"].ljust(50,".")
                            dictionary["subjectOf"]["url"] = term["dataset_license"][0]["dataset"]["core"]["iri"] 
                            dictionary["subjectOf"]["citation"] = term["dataset_license"][0]["dataset"]["link"]
                            dictionary["subjectOf"]["creator"] = dictionary["creator"]
                            dictionary["subjectOf"]["license"] = "http://creativecommons.org/licenses/by-sa/4.0/"
                            if "license" in term["dataset_license"][0]:
                                dictionary["subjectOf"]["license"] = term["dataset_license"][0]["license"]["core"]["iri"] 
                        if dl == "license": 
                            dictionary["license"] = " ".join(term["dataset_license"][0]["license"]["core"]["homepage"]) 
            if header == "channel_image": 
                    dictionary["image"] = [] 
                    for ci in term["channel_image"]: 
                        dictionary["image"].append({"@type":"imageObject","caption":term["term"]["core"]["label"] + " [" + ci["image"]["template_anatomy"]["label"] + "]", "thumbnail":ci["image"]["image_folder"] + "thumbnail.png"}) 
    result = json.dumps(dictionary, indent = 4)
    whole = wrapper.format(term['term']['core']['label'], term['term']['core']['short_form'], term['term']['description'], term['term']['comment'], result ,json.dumps(term, indent = 4).replace("\n","<br>\n "), amp )
    try:
        f.write(whole)
    except:    
        print(whole)
    f.close()

from vfb_connect.cross_server_tools import VfbConnect
vc=VfbConnect()

from os import listdir, chdir
from os.path import isfile, join
mypath=sys.argv[1]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

chdir(mypath)

all = sorted([w.replace('.md', '') for w in onlyfiles if w.startswith('FBbt') ])
for id in all:
	try: 
		terms = vc.neo_query_wrapper.get_TermInfo([id])
		for term in terms:
			wrapStringInHTMLMac(term) 
	except:
  		print(id)


