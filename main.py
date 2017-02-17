#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

header = "<!DOCTYPE html><html><head></head><body><h2>User signup</h2>"
form = """<form method="post">
        <table>
            <tr>
                <td>
                    <label for="user">Username</label>
                        <input type="text" name="user" value="" required>
                        <span class="error">{0}</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="password">Password</label>
                        <input type="password" name="password" required>
                        <span class="error">{1}</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="verify">Verify Password</lable>
                        <input type="password" name="verify" required>
                        <span class="error">{2}</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="email">Email Address (Optional)</label>
                        <input type="email" name="email" value="">
                        <span class="error">{3}</span>
                </td>
            <tr>
        </table>
        <br>
        <input type="submit"/>
</form>
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
        def get(self):
            content = header + form.format("","","","")
            self.response.write(content)



        def post(self):
            username = self.request.get("user")
            password = self.request.get("password")
            verify = self.request.get("verify")
            email = self.request.get("email")

            user_error = ""
            password_error = ""
            verify_error = ""
            email_error = ""

            if not username or valid_username(username):
                user_error = "You entered an invalid username"

            if not password or valid_password(password):
                password_error = "You entered an invalid password"

            if not verify or verify != password:
                verify_error = "Please re-enter and verify your password"

            if email and valid_email(email):
                email_error = "Please enter a valid email"

            content = header + form.format(user_error, password_error, verify_error, email_error)
            self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
