# import webapp2
# import cgi
# import re
#
# USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
# PASSWORD_RE = re.compile(r"^.{3,20}$")
# EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
#
# def valid_username(username):
#     return USER_RE.match(username)
#
# def valid_password(password):
#     return PASSWORD_RE.match(password)
#
# def valid_email(email):
#     return EMAIL_RE.match(email)
#
# header = "<!DOCTYPE html><html><head></head><body><h2>User signup</h2>"
# form = """<form method="post">
#         <table>
#             <tr>
#                 <td>
#                     <label for="user">Username</label>
#                         <input type="text" name="user" value="%(user)s" required>
#
#                 </td>
#             </tr>
#             <tr>
#                 <td>
#                     <label for="password">Password</label>
#                         <input type="password" name="password" required>
#
#                 </td>
#             </tr>
#             <tr>
#                 <td>
#                     <label for="verify">Verify Password</label>
#                         <input type="password" name="verify" required>
#
#                 </td>
#             </tr>
#             <tr>
#                 <td>
#                     <label for="email">Email Address (Optional)</label>
#                         <input type="email" name="email" value="%(email)s">
#
#                 </td>
#             <tr>
#         </table>
#         <br>
#         <input type="submit"/>
# </form>
# </body>
# </html>
# """
#
# content = header + form
#
# class MainHandler(webapp2.RequestHandler):
#         def write_form(self, user="", email=""):
#             self.response.write(content % {"user": user, "email":email})
#
#         def get(self):
#             self.write_form()
#
#         def post(self):
#             username = self.request.get("user")
#             password = self.request.get("password")
#             verify = self.request.get("verify")
#             email = self.request.get("email")
#
#             user_error = ""
#             password_error = ""
#             verify_error = ""
#             email_error = ""
#
#             if not valid_username(username):
#                 user_error = "You entered an invalid username"
#
#             if not valid_password(password):
#                 password_error = "You entered an invalid password"
#
#             if  verify != password:
#                 verify_error = "Please re-enter and verify your password"
#
#             if email and not valid_email(email):
#                 email_error = "Please enter a valid email"
#
#             content = header + form.format(user_error, password_error, verify_error, email_error, username, email)
#             self.response.write(content)
#
# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)

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
                        <input type="text" name="user" value="{4}" required>
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
                    <label for="verify">Verify Password</label>
                        <input type="password" name="verify" required>
                        <span class="error">{2}</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="email">Email Address (Optional)</label>
                        <input type="email" name="email" value="{5}">
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
            content = header + form.format("","","","","","")
            self.response.write(content)



        def post(self):
            error = False
            username = self.request.get("user")
            password = self.request.get("password")
            verify = self.request.get("verify")
            email = self.request.get("email")

            user_error = ""
            password_error = ""
            verify_error = ""
            email_error = ""

            if not valid_username(username):
                user_error = "You entered an invalid username"
                error = True

            if not valid_password(password):
                password_error = "You entered an invalid password"
                error = True

            if  verify != password:
                verify_error = "Please re-enter and verify your password"
                error = True

            if email and not valid_email(email):
                email_error = "Please enter a valid email"
                error = True

            content = header + form.format(user_error, password_error, verify_error, email_error, username, email)
            if error == True:
                self.response.write(content)
            else:
                self.redirect('/welcome?username=' + username)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write("Welcome! " + username)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
