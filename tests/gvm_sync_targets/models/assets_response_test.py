# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from gvm_sync_targets.models.assets_response import GetAssetsResponse

data = """
<get_assets_response status="200" status_text="OK">
    <asset id="a8bee9e4-65cf-4e78-9c98-13b1356ca32e">
        <owner>
            <name>admin</name>
        </owner>
        <name>3.4.2.55</name>
        <comment></comment>
        <creation_time>2024-05-03T22:31:44Z</creation_time>
        <modification_time>2024-05-04T21:58:39Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <identifiers>
            <identifier id="cd89be4a-4aa1-4cdb-ba18-8f9928a8ef86">
                <name>ssh-key</name>
                <value>22 ssh-ed25519</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="db880c02-3081-4db7-be2b-e51e8d034dc9">
                <name>OS</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.105586</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
                <os id="8fc2ef19-3f31-435a-aa87-16709ce6a946">
                    <title>(null)</title>
                </os>
            </identifier>
            <identifier id="e909e870-2c64-4f6b-b09c-8c1ba0b13667">
                <name>hostname</name>
                <value>server.example.com</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="437f104a-60d2-4066-9e27-099b187fc7ab">
                <name>ssh-key</name>
                <value>22 ecdsa-sha2-nistp256</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="16dc3353-1e6e-4360-be9f-f0d315e620c6">
                <name>ip</name>
                <value>5.7.8.9</value>
                <creation_time>2024-05-04T14:27:57Z</creation_time>
                <modification_time>2024-05-04T14:27:57Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host</type>
                    <data></data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="5ae2847e-6846-46c8-bb70-0fb60d8bb1fe">
                <name>ssh-key</name>
                <value>22 ssh-ed25519</value>
                <creation_time>2024-05-03T22:56:00Z</creation_time>
                <modification_time>2024-05-03T22:56:00Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="b585bd3c-d0ca-4f78-95c5-f91e63372b08">
                <name>OS</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <creation_time>2024-05-03T22:56:00Z</creation_time>
                <modification_time>2024-05-03T22:56:00Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.105586</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
                <os id="8fc2ef19-3f31-435a-aa87-16709ce6a946">
                    <title>(null)</title>
                </os>
            </identifier>
            <identifier id="191a5a73-e505-4c33-9cbd-aa69d09db442">
                <name>ssh-key</name>
                <value>22 ecdsa-sha2-nistp256</value>
                <creation_time>2024-05-03T22:56:00Z</creation_time>
                <modification_time>2024-05-03T22:56:00Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="a6fea9d7-3b84-46c3-9cbb-8d61d1274460">
                <name>hostname</name>
                <value>fooa.example.com</value>
                <creation_time>2024-05-03T22:56:00Z</creation_time>
                <modification_time>2024-05-03T22:56:00Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="fdbd2df0-f7c0-494f-90b4-d9244be8fd2d">
                <name>hostname</name>
                <value>foobar.example.com</value>
                <creation_time>2024-05-03T22:56:00Z</creation_time>
                <modification_time>2024-05-03T22:56:00Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="4e546ada-e467-41c6-90ee-806a4ba0c6f0">
                <name>ip</name>
                <value>5.5.4.3</value>
                <creation_time>2024-05-03T22:31:44Z</creation_time>
                <modification_time>2024-05-03T22:31:44Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host</type>
                    <data></data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
        </identifiers>
        <type>host</type>
        <host>
            <severity>
                <value>2.6</value>
            </severity>
            <detail>
                <name>best_os_cpe</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>best_os_txt</name>
                <value>Ubuntu 22.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>traceroute</name>
                <value>172.19.0.6,6.5.8.3</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
        </host>
    </asset>
    <asset id="0124dca7-e258-4831-b30a-968a90bdf28b">
        <owner>
            <name>admin</name>
        </owner>
        <name>4.5.6.7</name>
        <comment></comment>
        <creation_time>2024-05-04T15:47:34Z</creation_time>
        <modification_time>2024-05-04T21:58:39Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <identifiers>
            <identifier id="081497c9-b458-43bc-838c-28df7b6930c3">
                <name>OS</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.105586</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
                <os id="8fc2ef19-3f31-435a-aa87-16709ce6a946">
                    <title>(null)</title>
                </os>
            </identifier>
            <identifier id="19f978d6-9059-493a-9907-48b9443e4a1b">
                <name>ssh-key</name>
                <value>22 ecdsa-sha2-nistp256</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="c533150d-9906-4a35-a37a-a9ae5feed015">
                <name>hostname</name>
                <value>www.example.com</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="0896da14-9fbb-46e9-8d1a-4e7a6134e6ee">
                <name>hostname</name>
                <value>testserver.example.com</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="2f5bc506-0ec6-4fa2-843e-eedb916edd00">
                <name>ssh-key</name>
                <value>22 ssh-ed25519</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="25e35420-06f7-4fcc-952e-06327d5ee0cc">
                <name>ip</name>
                <value>192.168.2.1</value>
                <creation_time>2024-05-04T15:47:34Z</creation_time>
                <modification_time>2024-05-04T15:47:34Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host</type>
                    <data></data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
        </identifiers>
        <type>host</type>
        <host>
            <severity>
                <value>2.6</value>
            </severity>
            <detail>
                <name>best_os_cpe</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>best_os_txt</name>
                <value>Ubuntu 22.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>traceroute</name>
                <value>172.19.0.6,5.4.1.8</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
        </host>
    </asset>
    <asset id="5fe6da16-4d9d-4d01-87df-3f55462a7e03">
        <owner>
            <name>admin</name>
        </owner>
        <name>192.168.2.34</name>
        <comment></comment>
        <creation_time>2024-05-04T14:51:20Z</creation_time>
        <modification_time>2024-05-04T21:58:39Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <identifiers>
            <identifier id="532d3a3d-f9aa-4fb6-bf54-d53f9b39c7c2">
                <name>ssh-key</name>
                <value>22 ecdsa-sha2-nistp256</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="6b0d970f-3426-4424-94af-ab21e0131c0e">
                <name>hostname</name>
                <value>a.example.com</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="e8c342e0-56c6-464b-a343-7790aeb10886">
                <name>ssh-key</name>
                <value>22 ssh-ed25519</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="7ea0bac0-8fc3-41a1-8a68-712e97307e34">
                <name>OS</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.105586</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
                <os id="8fc2ef19-3f31-435a-aa87-16709ce6a946">
                    <title>(null)</title>
                </os>
            </identifier>
            <identifier id="bb378c05-7f51-4817-b56c-fa87b3f4e55e">
                <name>hostname</name>
                <value>foov</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="1ab2de57-f05b-49bf-baf5-e1b2c52bb679">
                <name>hostname</name>
                <value>foo.example.com</value>
                <creation_time>2024-05-04T21:58:39Z</creation_time>
                <modification_time>2024-05-04T21:58:39Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="9987fe14-dd22-4c8a-953b-b39f436325ff">
                <name>ip</name>
                <value>192.168.2.3</value>
                <creation_time>2024-05-04T14:51:20Z</creation_time>
                <modification_time>2024-05-04T14:51:20Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host</type>
                    <data></data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
        </identifiers>
        <type>host</type>
        <host>
            <severity>
                <value>4.3</value>
            </severity>
            <detail>
                <name>best_os_cpe</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>best_os_txt</name>
                <value>Ubuntu 22.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>traceroute</name>
                <value>172.19.0.6,5.3.7.2</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
        </host>
    </asset>
    <asset id="31a6834f-dd4e-456f-9757-4249bb9fb049">
        <owner>
            <name>admin</name>
        </owner>
        <name>192.168.2.15</name>
        <comment></comment>
        <creation_time>2024-05-04T17:04:01Z</creation_time>
        <modification_time>2024-05-04T21:58:40Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <identifiers>
            <identifier id="1fa8e555-850d-49ca-bbe1-9167cacd46c8">
                <name>ssh-key</name>
                <value>22 ssh-ed25519</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="98590596-1508-4e67-9280-bd29ae6bdc2b">
                <name>hostname</name>
                <value>test.example.com</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="b61ef3c1-1f23-4dc7-8ce9-1cdc9daaa1ae">
                <name>hostname</name>
                <value>myserver.example.com</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="236b1ce5-8f9a-4050-9141-caf290a1f93a">
                <name>OS</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.105586</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
                <os id="8fc2ef19-3f31-435a-aa87-16709ce6a946">
                    <title>(null)</title>
                </os>
            </identifier>
            <identifier id="04bf9500-e3ef-439b-b19d-06aa0bf2b27d">
                <name>ssh-key</name>
                <value>22 ecdsa-sha2-nistp256</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="ee15ab6e-0979-4735-88b4-bf7f08f29f90">
                <name>hostname</name>
                <value>example.com</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="debe775f-acf8-4d04-8547-254d0863c459">
                <name>ip</name>
                <value>14.3.2.5</value>
                <creation_time>2024-05-04T17:04:01Z</creation_time>
                <modification_time>2024-05-04T17:04:01Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host</type>
                    <data></data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
        </identifiers>
        <type>host</type>
        <host>
            <severity>
                <value>2.6</value>
            </severity>
            <detail>
                <name>best_os_cpe</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>best_os_txt</name>
                <value>Ubuntu 22.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>traceroute</name>
                <value>172.19.0.6,4.5.6.7</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
        </host>
    </asset>
    <asset id="2e10a5c9-6f28-474d-8437-f9231d432da1">
        <owner>
            <name>admin</name>
        </owner>
        <name>143.45.4.3</name>
        <comment></comment>
        <creation_time>2024-05-04T21:58:36Z</creation_time>
        <modification_time>2024-05-04T21:58:40Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <identifiers>
            <identifier id="4b2a7370-dd8c-4f9b-8a8f-1371cd998272">
                <name>ssh-key</name>
                <value>22 ssh-rsa</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="3fc0d980-5471-41db-9958-4374796683b7">
                <name>hostname</name>
                <value>foo.bar</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="1ca70678-6061-4a30-ba85-fd823b05b8ef">
                <name>OS</name>
                <value>cpe:/o:canonical:ubuntu_linux:20.04</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.105586</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
                <os id="49e22c91-36c9-4c0f-8d5b-db886697cf98">
                    <title>Canonical Ubuntu Linux 20.04</title>
                </os>
            </identifier>
            <identifier id="43980c66-4384-4273-a570-e95e080da788">
                <name>ssh-key</name>
                <value>22 ssh-ed25519</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="1571eaf4-1c84-43eb-8450-d6563d454683">
                <name>hostname</name>
                <value>servera.example.com</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="626d4d84-9d25-45de-b9a4-62bce4971954">
                <name>ssh-key</name>
                <value>22 ecdsa-sha2-nistp256</value>
                <creation_time>2024-05-04T21:58:40Z</creation_time>
                <modification_time>2024-05-04T21:58:40Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="ca389e4c-9dd6-4ad7-bbe4-455acb330de7">
                <name>ip</name>
                <value>7.8.8.7</value>
                <creation_time>2024-05-04T21:58:36Z</creation_time>
                <modification_time>2024-05-04T21:58:36Z</modification_time>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report Host</type>
                    <data></data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
        </identifiers>
        <type>host</type>
        <host>
            <severity>
                <value>5.0</value>
            </severity>
            <detail>
                <name>best_os_cpe</name>
                <value>cpe:/o:canonical:ubuntu_linux:20.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>best_os_txt</name>
                <value>Ubuntu 20.04</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>traceroute</name>
                <value>172.19.0.6,5.4.3.2</value>
                <source id="6514506e-56ae-4386-a2b0-8bb1206120cd">
                    <type>Report</type>
                </source>
            </detail>
        </host>
    </asset>
    <asset id="2a0db5c6-8540-4352-91df-505435797f85">
        <owner>
            <name>admin</name>
        </owner>
        <name>56.54.32.3</name>
        <comment></comment>
        <creation_time>2024-05-03T22:37:02Z</creation_time>
        <modification_time>2024-05-03T22:56:01Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <identifiers>
            <identifier id="cf46e3c4-5a6e-486c-90c1-3c98c0901848">
                <name>hostname</name>
                <value>serverb.example.com</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="087c3cb8-bc50-4611-8be2-b7490b8b9124">
                <name>OS</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.105586</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
                <os id="8fc2ef19-3f31-435a-aa87-16709ce6a946">
                    <title>(null)</title>
                </os>
            </identifier>
            <identifier id="74e3e8dc-3588-477d-ae9a-55b233ace20e">
                <name>ssh-key</name>
                <value>22 ssh-ed25519</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="587cf512-e9d5-4af1-9747-15f5f7de9159">
                <name>hostname</name>
                <value>some.host</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="988f6695-932d-41c2-b57f-a754935af66e">
                <name>ssh-key</name>
                <value>22 ecdsa-sha2-nistp256</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="cdaf0716-0212-49a0-9ca5-e97e986d0056">
                <name>ip</name>
                <value>5.4.6.7</value>
                <creation_time>2024-05-03T22:37:02Z</creation_time>
                <modification_time>2024-05-03T22:37:02Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host</type>
                    <data></data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
        </identifiers>
        <type>host</type>
        <host>
            <severity>
                <value>9.8</value>
            </severity>
            <detail>
                <name>best_os_cpe</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>best_os_txt</name>
                <value>Ubuntu 22.04</value>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>traceroute</name>
                <value>1.5.3.2,3.2.1.45</value>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report</type>
                </source>
            </detail>
        </host>
    </asset>
    <asset id="c00298a4-3d39-4df3-b91e-0d61e5702ee6">
        <owner>
            <name>admin</name>
        </owner>
        <name>4.3.2.1</name>
        <comment></comment>
        <creation_time>2024-05-03T22:55:58Z</creation_time>
        <modification_time>2024-05-03T22:56:01Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <identifiers>
            <identifier id="38d065ba-cd85-45be-a751-14c207eab518">
                <name>ssh-key</name>
                <value>22 ssh-ed25519</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="8ae95928-d9af-4809-bc83-0ff0ffcdb75f">
                <name>hostname</name>
                <value>another.host.name</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="460e1e46-2f86-4563-8b9c-8bd284d70b70">
                <name>ssh-key</name>
                <value>22 ecdsa-sha2-nistp256</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.100259</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="ab119464-95fd-4874-82d3-6c3d626101b9">
                <name>hostname</name>
                <value>my.host.name</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.103997</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
            <identifier id="d259ccb4-db29-4557-bbdd-8f1f09d0719e">
                <name>OS</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <creation_time>2024-05-03T22:56:01Z</creation_time>
                <modification_time>2024-05-03T22:56:01Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host Detail</type>
                    <data>1.3.6.1.4.1.25623.1.0.105586</data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
                <os id="8fc2ef19-3f31-435a-aa87-16709ce6a946">
                    <title>(null)</title>
                </os>
            </identifier>
            <identifier id="a44de44d-558f-4202-8f27-b5ee40f665a2">
                <name>ip</name>
                <value>1.3.4.2</value>
                <creation_time>2024-05-03T22:55:58Z</creation_time>
                <modification_time>2024-05-03T22:55:58Z</modification_time>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report Host</type>
                    <data></data>
                    <deleted>0</deleted>
                    <name></name>
                </source>
            </identifier>
        </identifiers>
        <type>host</type>
        <host>
            <severity>
                <value>9.8</value>
            </severity>
            <detail>
                <name>best_os_cpe</name>
                <value>cpe:/o:canonical:ubuntu_linux:22.04</value>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>best_os_txt</name>
                <value>Ubuntu 22.04</value>
                <source id="b1d5fd6d-9124-40da-b994-7f89768d21fd">
                    <type>Report</type>
                </source>
            </detail>
            <detail>
                <name>traceroute</name>
                <value>1.2.3.4,2.3.4.5,6.7.8.9</value>
                <source id="affdeecc-1234-5678-abcd-abcdefabcdef">
                    <type>Report</type>
                </source>
            </detail>
        </host>
    </asset>
    <filters id="">
        <term>first=1 rows=10 sort=name</term>
        <keywords>
            <keyword>
                <column>first</column>
                <relation>=</relation>
                <value>1</value>
            </keyword>
            <keyword>
                <column>rows</column>
                <relation>=</relation>
                <value>10</value>
            </keyword>
            <keyword>
                <column>sort</column>
                <relation>=</relation>
                <value>name</value>
            </keyword>
        </keywords>
    </filters>
    <sort>
        <field>
            name
            <order>ascending</order>
        </field>
    </sort>
    <assets start="1" max="1000"/>
    <asset_count>
        7
        <filtered>7</filtered>
        <page>7</page>
    </asset_count>
</get_assets_response>
"""


def test_parse_model() -> None:
    model = GetAssetsResponse.from_xml(data)
    assert not model.model_extra
    assert model.assets[0].identifiers.identifiers[0].source is not None
    assert model.count.total == 7
