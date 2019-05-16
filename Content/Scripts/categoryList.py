import json,os
import requests

githubUrl = "https://github.com/datacenter/cloudcentersuite/raw/master/Content"

def service_category():
    """
    Function is used to get the services zip file in category vice and stored
    required directory

    :return:
    """
    try:
        path = os.getcwd()
        json_path = path +"/ServiceList.json"
        service_data = json.load(open(json_path, 'r'))
        print(service_data)
        category = []
        for data in service_data:
            category.append(data["serviceCategory"])
        if len(category) > 0:
            print "--------------------------------"
            print "ID Name of the Category"
            print "--------------------------------"
            print "0   exit"
            i = 1
            for item in category:
                print str(i) + "   " + item
                i = i + 1
            print ""
            print "Select the Category ID  from the list (press 0 to exit): "
        else:
            print "No Repository"
            exit()
        input = int(raw_input())
        if input == 0:
            exit()
        count = input-1
        category_input = category[count]
        serviceList = []

        for data in service_data:
            if data["serviceCategory"] == category_input:
                serviceList.append(data["name"])

        if len(serviceList) > 0:
            print "--------------------------------"
            print "ID Name of the ServiceList"
            print "--------------------------------"
            print "0   exit"
            i = 1
            for item in serviceList:
                print str(i) + "   " + item
                i = i + 1
            print ""
            print "Select the Category ID  from the list (press 0 to exit): "
        else:
            print "No Repository"
            exit()
        service_input = int(raw_input())
        if input == 0:
            exit()
        service_input = serviceList[service_input-1]
        serviceList = []
        url_list = []
        for data in service_data:
            if data["serviceCategory"] == category_input and data["name"] == service_input:
                url_list.append(data["urls"])
        downloadFiles(url_list)
    except Exception as e:
        print("Error while Iterating service list json ",e)


def downloadFiles(url_list):
    """
    Function used to download ServiceImport,iu & dockerfile file from github

    :return:
    """
    try:
        for list in url_list:
            serviceImportUrl = list["serviceImport"]
            dockerFile = list["dockerFile"]
            serviceLibraryBundle = list["serviceLibraryBundle"]

        print(serviceImportUrl,dockerFile,serviceLibraryBundle)

        serviceImportUrl = githubUrl+"/"+serviceImportUrl

        ### Integration unit bundle
        try:
            iubundleUrl = githubUrl+'/'+serviceLibraryBundle
            name = iubundleUrl.split("/")[-1]
            r = requests.get(url=iubundleUrl)
            with open(name,'wb') as file:
                file.write(r.content)
                #zip = ZipFile(os.getcwd()+"/"+name,'r')
                #zip.extractall(os.getcwd()+"/"+name.replace(".zip",""))
        except Exception as er:
            print("Error while downloading IU bundle from github",er)
            exit()


    except Exception as Er:
        print("Error while Getting url and downloading file from github",Er)

service_category()