# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from gvm_sync_targets.models import GetTargetsResponse

data = """
<get_targets_response status="200" status_text="OK">
    <target id="26b1103a-acab-455b-8ae6-36d3d680a63f">
        <owner>
            <name>admin</name>
        </owner>
        <name>All Hosts</name>
        <comment></comment>
        <creation_time>2024-05-15T17:37:30Z</creation_time>
        <modification_time>2024-05-15T17:37:30Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <hosts>1.2.3.4, 1::1</hosts>
        <exclude_hosts></exclude_hosts>
        <max_hosts>44</max_hosts>
        <port_list id="4a4717fe-57d2-11e1-9a26-406186ea4fc5">
            <name>All IANA assigned TCP and UDP</name>
            <trash>0</trash>
        </port_list>
        <ssh_credential id="416d4541-8cb4-4745-ba27-7d509cec9455">
            <name>SSH auth</name>
            <port>22</port>
            <trash>0</trash>
        </ssh_credential>
        <smb_credential id="">
            <name></name>
            <trash>0</trash>
        </smb_credential>
        <esxi_credential id="">
            <name></name>
            <trash>0</trash>
        </esxi_credential>
        <snmp_credential id="">
            <name></name>
            <trash>0</trash>
        </snmp_credential>
        <ssh_elevate_credential id="">
            <name></name>
            <trash>0</trash>
        </ssh_elevate_credential>
        <reverse_lookup_only>0</reverse_lookup_only>
        <reverse_lookup_unify>0</reverse_lookup_unify>
        <alive_tests>Scan Config Default</alive_tests>
        <allow_simultaneous_ips>1</allow_simultaneous_ips>
    </target>
    <target id="7a7f3ae0-f95d-4e2a-a523-995f5f690f69">
        <owner>
            <name>admin</name>
        </owner>
        <name>New All Hosts</name>
        <comment></comment>
        <creation_time>2024-05-17T05:59:19Z</creation_time>
        <modification_time>2024-05-17T05:59:19Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <hosts>1.2.3.4, 1::1</hosts>
        <exclude_hosts></exclude_hosts>
        <max_hosts>41</max_hosts>
        <port_list id="4a4717fe-57d2-11e1-9a26-406186ea4fc5">
            <name>All IANA assigned TCP and UDP</name>
            <trash>0</trash>
        </port_list>
        <ssh_credential id="416d4541-8cb4-4745-ba27-7d509cec9455">
            <name>SSH auth</name>
            <port>22</port>
            <trash>0</trash>
        </ssh_credential>
        <smb_credential id="">
            <name></name>
            <trash>0</trash>
        </smb_credential>
        <esxi_credential id="">
            <name></name>
            <trash>0</trash>
        </esxi_credential>
        <snmp_credential id="">
            <name></name>
            <trash>0</trash>
        </snmp_credential>
        <ssh_elevate_credential id="">
            <name></name>
            <trash>0</trash>
        </ssh_elevate_credential>
        <reverse_lookup_only>0</reverse_lookup_only>
        <reverse_lookup_unify>0</reverse_lookup_unify>
        <alive_tests>Scan Config Default</alive_tests>
        <allow_simultaneous_ips>1</allow_simultaneous_ips>
    </target>
    <target id="1a11fc20-b767-4407-82ee-e87fbddbc74a">
        <owner><name>admin</name></owner><name>Unnamed</name>
        <comment></comment><creation_time>2024-05-15T20:41:23Z</creation_time>
        <modification_time>2024-05-15T20:41:23Z</modification_time>
        <writable>1</writable><in_use>1</in_use>
        <permissions>
            <permission><name>Everything</name></permission>
        </permissions>
        <hosts>1.2.3.4, 1::1</hosts>
        <exclude_hosts></exclude_hosts>
        <max_hosts>41</max_hosts>
        <port_list id="33d0cd82-57c6-11e1-8ed1-406186ea4fc5">
            <name>All IANA assigned TCP</name>
            <trash>0</trash>
        </port_list>
        <ssh_credential id="416d4541-8cb4-4745-ba27-7d509cec9455">
            <name>SSH auth</name>
            <port>22</port>
            <trash>0</trash>
        </ssh_credential>
        <smb_credential id="">
            <name></name>
            <trash>0</trash>
        </smb_credential>
        <esxi_credential id="">
            <name></name>
            <trash>0</trash>
        </esxi_credential>
        <snmp_credential id="">
            <name></name>
            <trash>0</trash>
        </snmp_credential>
        <ssh_elevate_credential id="">
            <name></name>
            <trash>0</trash>
        </ssh_elevate_credential>
        <reverse_lookup_only>0</reverse_lookup_only>
        <reverse_lookup_unify>0</reverse_lookup_unify>
        <alive_tests>Scan Config Default</alive_tests>
        <allow_simultaneous_ips>1</allow_simultaneous_ips>
    </target>
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
    <targets start="1" max="1000"/>
    <target_count>
        3
        <filtered>3</filtered>
        <page>3</page>
    </target_count>
</get_targets_response>
"""


data_with_tasks = """
<get_targets_response status="200" status_text="OK">
    <target id="26b1103a-acab-455b-8ae6-36d3d680a63f">
        <owner>
            <name>admin</name>
        </owner>
        <name>All Hosts</name>
        <comment></comment>
        <creation_time>2024-05-15T17:37:30Z</creation_time>
        <modification_time>2024-05-15T17:37:30Z</modification_time>
        <writable>1</writable>
        <in_use>1</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <hosts>1.2.3.4, 1::1</hosts>
        <exclude_hosts></exclude_hosts>
        <max_hosts>44</max_hosts>
        <port_list id="4a4717fe-57d2-11e1-9a26-406186ea4fc5">
            <name>All IANA assigned TCP and UDP</name>
            <trash>0</trash>
        </port_list>
        <ssh_credential id="416d4541-8cb4-4745-ba27-7d509cec9455">
            <name>SSH auth</name>
            <port>22</port>
            <trash>0</trash>
        </ssh_credential>
        <smb_credential id="">
            <name></name>
            <trash>0</trash>
        </smb_credential>
        <esxi_credential id="">
            <name></name>
            <trash>0</trash>
        </esxi_credential>
        <snmp_credential id="">
            <name></name>
            <trash>0</trash>
        </snmp_credential>
        <ssh_elevate_credential id="">
            <name></name>
            <trash>0</trash>
        </ssh_elevate_credential>
        <reverse_lookup_only>0</reverse_lookup_only>
        <reverse_lookup_unify>0</reverse_lookup_unify>
        <alive_tests>Scan Config Default</alive_tests>
        <allow_simultaneous_ips>1</allow_simultaneous_ips>
        <tasks><task id="111"><name>foo</name></task></tasks>
    </target>
    <target id="7a7f3ae0-f95d-4e2a-a523-995f5f690f69">
        <owner>
            <name>admin</name>
        </owner>
        <name>New All Hosts</name>
        <comment></comment>
        <creation_time>2024-05-17T05:59:19Z</creation_time>
        <modification_time>2024-05-17T05:59:19Z</modification_time>
        <writable>1</writable>
        <in_use>0</in_use>
        <permissions>
            <permission>
                <name>Everything</name>
            </permission>
        </permissions>
        <hosts>1.2.3.4, 1::1</hosts>
        <exclude_hosts></exclude_hosts>
        <max_hosts>41</max_hosts>
        <port_list id="4a4717fe-57d2-11e1-9a26-406186ea4fc5">
            <name>All IANA assigned TCP and UDP</name>
            <trash>0</trash>
        </port_list>
        <ssh_credential id="416d4541-8cb4-4745-ba27-7d509cec9455">
            <name>SSH auth</name>
            <port>22</port>
            <trash>0</trash>
        </ssh_credential>
        <smb_credential id="">
            <name></name>
            <trash>0</trash>
        </smb_credential>
        <esxi_credential id=""><name></name><trash>0</trash></esxi_credential>
        <snmp_credential id=""><name></name><trash>0</trash></snmp_credential>
        <ssh_elevate_credential id="">
            <name></name><trash>0</trash>
        </ssh_elevate_credential>
        <reverse_lookup_only>0</reverse_lookup_only>
        <reverse_lookup_unify>0</reverse_lookup_unify>
        <alive_tests>Scan Config Default</alive_tests>
        <allow_simultaneous_ips>1</allow_simultaneous_ips>
    </target>
    <target id="1a11fc20-b767-4407-82ee-e87fbddbc74a">
        <owner><name>admin</name></owner><name>Unnamed</name>
        <comment></comment><creation_time>2024-05-15T20:41:23Z</creation_time>
        <modification_time>2024-05-15T20:41:23Z</modification_time>
        <writable>1</writable><in_use>1</in_use>
        <permissions>
            <permission><name>Everything</name></permission>
        </permissions>
        <hosts>1.2.3.4, 1::1</hosts>
        <exclude_hosts></exclude_hosts><max_hosts>41</max_hosts>
        <port_list id="33d0cd82-57c6-11e1-8ed1-406186ea4fc5">
            <name>All IANA assigned TCP</name><trash>0</trash>
        </port_list>
        <ssh_credential id="416d4541-8cb4-4745-ba27-7d509cec9455">
            <name>SSH auth</name><port>22</port><trash>0</trash>
        </ssh_credential>
        <smb_credential id="">
            <name></name><trash>0</trash>
        </smb_credential>
        <esxi_credential id="">
            <name></name><trash>0</trash>
        </esxi_credential>
        <snmp_credential id="">
            <name></name><trash>0</trash>
        </snmp_credential>
        <ssh_elevate_credential id="">
            <name></name><trash>0</trash>
        </ssh_elevate_credential>
        <reverse_lookup_only>0</reverse_lookup_only>
        <reverse_lookup_unify>0</reverse_lookup_unify>
        <alive_tests>Scan Config Default</alive_tests>
        <allow_simultaneous_ips>1</allow_simultaneous_ips>
    </target>
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
    <targets start="1" max="1000"/>
    <target_count>
        3
        <filtered>3</filtered>
        <page>3</page>
    </target_count>
</get_targets_response>
"""


def test_parse_model() -> None:
    model = GetTargetsResponse.from_xml(data)
    assert not model.model_extra


def test_parse_model_with_tasks() -> None:
    model = GetTargetsResponse.from_xml(data_with_tasks)
    assert not model.model_extra
