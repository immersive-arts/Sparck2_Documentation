## How to setup Visual Studio Code

This steps describe how to setup Visual Studio Code to use as a code completion editor for Quescript:

1. Go to Extensions and install the [XML Language Support by Red Hat](https://github.com/redhat-developer/vscode-xml/tree/main/docs) 
2. Go to Manage (the cog in the lower left corner) > Settings > search for 'xml.fileAssociations'
3. press 'edit in settings.json'
4. copy paste into: `"xml.fileAssociations": [`
       
```json
"xml.fileAssociations": [
        {
            "pattern": "**/*.que",
            "systemId": "${fileDirname}/quescript.xsd"
        }
]
```

5. Copy 'quescript.xsd' from this repository ~/misc/quescript.xsd to your folder with the quescripts.
6. Open the quescript inside Visual Studio Code.