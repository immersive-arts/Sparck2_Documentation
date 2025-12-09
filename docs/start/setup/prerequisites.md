# Preparation

Before you install SPARCK, you need the following Software and Libraries installed:

=== "Step 1: Installing Max"

    [INSTALL MaxMSP ![](https://assets.cycling74.com/web/logos/C74-dark.svg)](https://cycling74.com/downloads){ .md-button }

=== "Step 2: Installing Java"

    === "MacOS"

        === "Easy Way"
            1. direct download: [jdk-19.0.2 for ARM 64](https://download.oracle.com/java/19/archive/jdk-19.0.2_macos-aarch64_bin.dmg)
                1. or if you are on an older machine: download [jdk-19.0.2 for x64](https://download.oracle.com/java/19/archive/jdk-19.0.2_macos-x64_bin.dmg)
            2. Install the JDK
        === "Custom Way"
            1. Alternatively go to [Java Archive](https://www.oracle.com/java/technologies/downloads/archive/)
                1. If you encounter an error message, click on the url and press enter. This will reload that page correctly.
                2. Select "Java SE 19" (Newer versions do not work anymore with Max)
                3. scroll down to "macOS Arm 64 DMG Installer" or "macOS x64 DMG Installer" depending on your machine
                4. download the installer
            2. Install the JDK

    === "Windows"

        === "Easy Way"
            3. direct download: [jdk-19.0.2](https://download.oracle.com/java/19/archive/jdk-19.0.2_windows-x64_bin.zip)
            4. Install the JDK by running the installer
            5. right-click "save-link-as" this [link](https://raw.githubusercontent.com/immersive-arts/Sparck2/refs/heads/master/scripts/java19.reg)
            6. double click the downloaded java19.reg file to add the needed paths to your registry
            7. done. Max should now be able to find Java.
   
        === "Custom Way"
            1.  Alternatively go to [Java Archive](https://www.oracle.com/java/technologies/downloads/archive/)
                1. If you encounter an error message, click on the url and press enter. This will reload that page correctly.
                2. Select "Java SE 19" (Newer versions do not work anymore with Max)
                3. scroll down to "Windows x64 Installer"
                4. download the installer
            2.  Install the JDK
            3.  Set the Registry paths for Max
                1. you need to adjust the paths in this .reg script accordingly:
                    ```
                    Windows Registry Editor Version 5.00

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft]

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\JDK]
                    "CurrentVersion"="1.19"

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\JDK\1.19]
                    "JavaHome"="C:\\Program Files\\Java\\jdk-19"

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Development Kit]
                    "CurrentVersion"="1.19"

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Development Kit\1.19]
                    "JavaHome"="C:\\Program Files\\Java\\jdk-19"

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\JRE]
                    "CurrentVersion"="1.19"

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\JRE\1.19]
                    "RuntimeLib"="C:\\Program Files\\Java\\jdk-19\\bin\\server\\jvm.dll"
                    "JavaHome"="C:\\Program Files\\Java\\jdk-19"

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Runtime Environment]
                    "CurrentVersion"="1.19"

                    [HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Runtime Environment\1.19]
                    "RuntimeLib"="C:\\Program Files\\Java\\jdk-19\\bin\\server\\jvm.dll"
                    "JavaHome"="C:\\Program Files\\Java\\jdk-19"
                    ```
                2.  replace all `1.19` with the version you have installed
                3.  replace all `C:\\Program Files\\Java\\jdk-19` with the path where you have installed Java
                4.  Save the script as a .reg file and double click it to add the paths to your registry.

=== "Step 3: (optional) Installing GIT"

    === "MacOS"
        1. Install Brew -> https://brew.sh/
            
            Open Terminal (press cmd-space and enter 'terminal' in the spotlight search bar)

            > https://brew.sh/ and follow the instructions

        2. Install Git via Brew

            Open Terminal (or the same as above

            > https://git-scm.com/install/mac and follow instructions under Homebrew

    === "Windows"

        3. Open Power Shell (search for 'power shell' in the windows search bar
        4. select the one with the admin rights
        5. follow link and the instructions under Using winget tool -> https://git-scm.com/install/windows


