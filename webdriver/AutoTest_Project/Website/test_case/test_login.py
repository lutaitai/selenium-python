#!/usr/bin/env Python
# coding=utf-8

import unittest
from model import myunit,function
from model.myunit import StartEnd
from page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login1_normal(self):
        '''username and password is normal'''
        print("test_login1_normal is start test...")
        po=LoginPage(self.driver)
        po.Login_action(u'鹿太太',123456)
        sleep(3)

        self.assertEqual(po.type_loginPass_hint(),u'我的空间')
        function.insert_img(self.driver,"51zxw_login1_nomal.jpg")
        print("test_login1_normal test end")

    def test_login2_PasswordError(self):
        '''username and password is error'''
        print("test_login2_passworderror is start test...")
        po=LoginPage(self.driver)
        po.Login_action('51zxw',44444444)
        sleep(3)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"test_login2_passworderror.jpg")

    def test_login3_empty(self):
        '''username and passwd is empty'''
        print("test_login3_empty is start test....")
        po=LoginPage(self.driver)
        po.Login_action('','')
        sleep(3)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,'test_login3_empty.jpg')
        print("test_login3_empty test end")


if __name__=="__main__":
    unittest.main()