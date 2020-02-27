x={
  "web-app": {
    "servlet": [
      {
        "servlet-name": "cofaxCDS",
        "servlet-class": "org.cofax.cds.CDSServlet",
        "init-param": {
          "configGlossary:installationAt": "Philadelphia, PA",
          "configGlossary:adminEmail": "ksm@pobox.com",
          "configGlossary:poweredBy": "Cofax",
          "configGlossary:poweredByIcon": "/images/cofax.gif",
          "configGlossary:staticPath": "/content/static",
          "templateProcessorClass": "org.cofax.WysiwygTemplate",
          "templatePath": "templates",
          "templateOverridePath": "",
          "defaultListTemplate": "listTemplate.htm",
          "defaultFileTemplate": "articleTemplate.htm",
          "useJSP": "false",
          "cacheTemplatesStore": 50,
          "searchEngineFileTemplate": "forSearchEngines.htm",
          "searchEngineRobotsDb": "WEB-INF/robots.db",
          "useDataStore": "true",
          "dataStoreName": "cofax",
          "dataStoreUrl": "jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon",
          "dataStoreUser": "sa",
          "dataStoreTestQuery": "SET NOCOUNT ON;select test='test';",
          "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
          "dataStoreInitConns": 10,
          "dataStoreMaxConns": 100,
          "dataStoreConnUsageLimit": 100,
          "dataStoreLogLevel": "debug",
          "maxUrlLength": 500
        }
      },
      {
        "servlet-name": "cofaxEmail",
        "servlet-class": "org.cofax.cds.EmailServlet",
        "init-param": {
          "mailHost": "mail1",
          "mailHostOverride": "mail2"
        }
      },
      {
        "servlet-name": "cofaxTools",
        "servlet-class": "org.cofax.cms.CofaxToolsServlet",
        "init-param": {
          "templatePath": "toolstemplates/",
          "log": 1,
          "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
          "logMaxSize": "",
          "dataLog": 1,
          "dataLogLocation": "/usr/local/tomcat/logs/dataLog.log",
          "dataLogMaxSize": "",
          "removePageCache": "/content/admin/remove?cache=pages&id=",
          "removeTemplateCache": "/content/admin/remove?cache=templates&id=",
          "fileTransferFolder": "/usr/local/tomcat/webapps/content/fileTransferFolder",
          "lookInContext": 1,
          "adminGroupID": 4,
          "betaServer": "true"
        }
      }
    ],
    "servlet-mapping": {
      "cofaxCDS": "/",
      "cofaxEmail": "/cofaxutil/aemail/*",
      "cofaxAdmin": "/admin/*",
      "fileServlet": "/static/*",
      "cofaxTools": "/tools/*",
      "init-param": {
        "templatePath-mapping": "toolstemplates/",
        "log-mapping": 1,
        "logLocation-mapping": "/usr/local/tomcat/logs/CofaxTools.log",
        "logMaxSize-mapping": "",
        "dataLog-mapping": 1,
        "dataLogLocation-mapping": "/usr/local/tomcat/logs/dataLog.log",
        "dataLogMaxSize-mapping": "",
        "removePageCache-mapping": "/content/admin/remove?cache=pages&id=",
        "removeTemplateCache-mapping": "/content/admin/remove?cache=templates&id=",
        "fileTransferFolder-mapping": "/usr/local/tomcat/webapps/content/fileTransferFolder",
        "lookInContext-mapping": 1,
        "adminGroupID-mapping": 4,
        "betaServer-mapping": "true"
      }
    },
    "taglib": {
      "taglib-uri": "cofax.tld",
      "taglib-location": "/WEB-INF/tlds/cofax.tld"
    }
  }
}
iparams=[]
FinalResult={}
set1={}
set2={}

for i in x: 
    for j in x[i]: # x  = servlet,servlet-mapping,taglib
        formType=j #formType(i.e servlet,servlet-mapping or taglib)
        value= x[i][j] #value inside servlet,servlet-mapping or taglib
        if isinstance(value,list): #value is List or not 
            for k in value: # 3 Dict inside list(i.e servlet)
                for l in k["init-param"]: #Inside each DICT in SERVLET find dict with "init-param"
                    set2[l]=k["init-param"][l] #assign each "init-param" value to blank set
                    set2["form-type"]=formType # assign form type
                    iparams.append(set2) # Append to InitParam list
                    set2={}  #empty the set so that each time new set in formed to populate InitParam list
        else: #type != list
            if "init-param" in value:
                for m in value["init-param"]:
                        set2[m]=value["init-param"][m]
                        set2["form-type"]=formType
                        iparams.append(set2)
                        set2={}
FinalResult["init-param"]=iparams
print(FinalResult)

