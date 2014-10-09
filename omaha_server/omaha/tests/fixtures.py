# coding: utf8

request_update_check = """<?xml version="1.0" encoding="UTF-8"?>
<request protocol="3.0"
         version="1.3.23.0"
         ismachine="0"
         sessionid="{5FAD27D4-6BFA-4daa-A1B3-5A1F821FEE0F}"
         userid="{D0BBD725-742D-44ae-8D46-0231E881D58E}"
         installsource="scheduler"
         testsource="ossdev"
         requestid="{C8F6EDF3-B623-4ee6-B2DA-1D08A0B4C665}">
    <os platform="win" version="6.1" sp="" arch="x64"/>
    <app appid="{430FD4D0-B729-4F61-AA34-91526481799D}" version="1.2.23.0" nextversion="" lang="en" brand="GGLS"
         client="someclientid" installage="39">
        <updatecheck/>
        <ping r="1"/>
    </app>
    <app appid="{D0AB2EBC-931B-4013-9FEB-C9C4C2225C8C}" version="2.2.2.0" nextversion="" lang="en" brand="GGLS"
         client="" installage="6">
        <updatecheck/>
        <ping r="1"/>
    </app>
</request>"""

request_event = """<?xml version="1.0" encoding="UTF-8"?>
<request protocol="3.0" version="1.3.23.0" ismachine="1" sessionid="{2882CF9B-D9C2-4edb-9AAF-8ED5FCF366F7}" userid="{F25EC606-5FC2-449b-91FF-FA21CADB46E4}" installsource="otherinstallcmd" testsource="ossdev" requestid="{164FC0EC-8EF7-42cb-A49D-474E20E8D352}">
  <os platform="win" version="6.1" sp="" arch="x64"/>
  <app appid="{8A69D345-D564-463C-AFF1-A69D9E530F96}" version="" nextversion="13.0.782.112" lang="en" brand="" client="" installage="6">
    <event eventtype="9" eventresult="1" errorcode="0" extracode1="0"/>
    <event eventtype="5" eventresult="1" errorcode="0" extracode1="0"/>
    <event eventtype="2" eventresult="4" errorcode="-2147219440" extracode1="268435463"/>
  </app>
</request>
"""

request_data = """<?xml version="1.0" encoding="UTF-8"?>
<request protocol="3.0" version="1.3.23.0" ismachine="0" sessionid="{5FAD27D4-6BFA-4daa-A1B3-5A1F821FEE0F}" userid="{D0BBD725-742D-44ae-8D46-0231E881D58E}" installsource="scheduler" testsource="ossdev" requestid="{C8F6EDF3-B623-4ee6-B2DA-1D08A0B4C665}">
  <os platform="win" version="6.1" sp="" arch="x64"/>
  <app appid="{430FD4D0-B729-4F61-AA34-91526481799D}" version="1.3.23.0" nextversion="" lang="en" brand="GGLS" client="someclientid" installage="39">
    <updatecheck/>
    <data name="install" index="verboselogging"/>
    <data name="untrusted">Some untrusted data</data>
    <ping r="1"/>
  </app>
</request>"""

response_update_check_negative = """<?xml version="1.0" encoding="UTF-8"?>
<response protocol="3.0" server="prod">
  <daystart elapsed_seconds="56508"/>
  <app appid="{430FD4D0-B729-4F61-AA34-91526481799D}" status="ok">
    <updatecheck status="noupdate"/>
    <ping status="ok"/>
  </app>
  <app appid="{D0AB2EBC-931B-4013-9FEB-C9C4C2225C8C}" status="ok">
    <updatecheck status="noupdate"/>
    <ping status="ok"/>
  </app>
</response>"""

response_update_check_positive = """<?xml version="1.0" encoding="UTF-8"?>
<response protocol="3.0" server="prod">
  <daystart elapsed_seconds="56508"/>
  <app appid="{430FD4D0-B729-4F61-AA34-91526481799D}" status="ok">
    <updatecheck status="noupdate"/>
    <ping status="ok"/>
  </app>
  <app appid="{D0AB2EBC-931B-4013-9FEB-C9C4C2225C8C}" status="ok">
    <updatecheck status="ok">
      <urls>
        <url codebase="http://cache.pack.google.com/edgedl/chrome/install/782.112/"/>
      </urls>
      <manifest version="13.0.782.112">
        <packages>
          <package hash="VXriGUVI0TNqfLlU02vBel4Q3Zo=" name="chrome_installer.exe" required="true" size="23963192"/>
        </packages>
        <actions>
          <action arguments="--do-not-launch-chrome" event="install" run="chrome_installer.exe"/>
          <action version="13.0.782.112" event="postinstall" onsuccess="exitsilentlyonlaunchcmd"/>
        </actions>
      </manifest>
    </updatecheck>
    <ping status="ok"/>
  </app>
</response>"""

response_event = """<?xml version="1.0" encoding="UTF-8"?>
<response protocol="3.0" server="prod">
  <daystart elapsed_seconds="56754"/>
  <app appid="{8A69D345-D564-463C-AFF1-A69D9E530F96}" status="ok">
    <event status="ok"/>
    <event status="ok"/>
    <event status="ok"/>
  </app>
</response>"""

response_data = """<?xml version="1.0" encoding="UTF-8"?>
<response protocol="3.0" server="prod">
  <daystart elapsed_seconds="56754"/>
  <app appid="{8A69D345-D564-463C-AFF1-A69D9E530F96}" status="ok">
    <data index="verboselogging" name="install" status="ok">
      app-specific values here
    </data>
    <data name="untrusted" status="ok"/>
  </app>
</response>"""