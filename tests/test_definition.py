#! /usr/bin/env python
#import testbase
import unittest
import samweb_client
import samweb_cli
import time,os

defname = 'test-project'

class TestDefinition(testbase.SamdevTest):

    def test_descDefinition_DefNotFound(self):
        fake_def_name = 'doesnotexist_%d' % time.time()
        self.assertRaises(samweb_client.exceptions.DefinitionNotFound, self.samweb.descDefinition, fake_def_name)
        self.assertRaises(samweb_client.exceptions.DefinitionNotFound, self.samweb.descDefinitionDict, fake_def_name)

    def test_descDefinition(self):
        output = self.samweb.descDefinition(defname)
        assert defname in output
        d = self.samweb.descDefinitionDict(defname)
        assert d['defname'] == defname

    def test_snapshot(self):
        output = self.samweb.takeSnapshot(defname)
        self.assertEquals(int(output),1)

    def test_create_rename_delete_definition(self):

        defname = 'samweb_client_test_def_%s_%d' % (os.getpid(), int(time.time()))
        self.samweb.createDefinition(defname, "file_name dummy", "illingwo", "samdev")

        d = self.samweb.descDefinition(defname)
        assert defname in d
        d = self.samweb.descDefinitionDict(defname)
        assert defname == d["defname"]

        defname2 = defname + '_2'

        self.samweb.modifyDefinition(defname,defname=defname2)

        d = self.samweb.descDefinitionDict(defname2)
        assert defname2 == d["defname"]

        self.samweb.deleteDefinition(defname2)

class TestDefinitionCommands(testbase.SAMWebCmdTest):

    def test_takeSnapshot(self):

        cmdline = '-e samdev take-snapshot %s' % defname
        self.check_cmd_return(cmdline.split())
        assert "1\n" == self.stdout


if __name__ == '__main__':
    unittest.main()
