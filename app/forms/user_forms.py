"""Users - Forms"""
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
)


# Register user form
class RegisterUserForm(FlaskForm):
    """Register user form"""

    firstname= StringField('First Name*', validators=[DataRequired()])
    lastname = StringField('Last Name*', validators=[DataRequired()])
    email = StringField('Email*', validators=[DataRequired(), Email()])
    phone = StringField('Phone*', validators=[DataRequired()])
    password = PasswordField('Password*', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords must match.')])
    pass_confirm = PasswordField(
        'Confirm Password*', validators=[DataRequired()])
    submit = SubmitField('Register')


# Form - Short Code
class ShortCodeForm(FlaskForm):
    """Short Code Form"""

    short_code = StringField(
        label="Short Code*", validators=[DataRequired(), Length(min=6, max=6)]
    )
    submit = SubmitField(label="Submit")


# Form - Login
class LoginForm(FlaskForm):
    '''Form to login a user'''

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


# Form - Change Password
class ChangePasswordForm(FlaskForm):
    """Change Password Form"""

    password = PasswordField(
        label="Password*", validators=[DataRequired(), Length(min=6, max=50)]
    )
    confirm_password = PasswordField(
        label="Confirm Password*", validators=[DataRequired(),
                                               EqualTo("password")]
    )
    submit = SubmitField(label="Change Password")


# Form - Edit Profile
class EditProfileForm(FlaskForm):
    """Edit Profile Form"""

    firstname = StringField(label="First Name*", validators=[DataRequired()])
    lastname = StringField(label="Last Name*", validators=[DataRequired()])
    email = StringField(label="Email*", validators=[DataRequired(), Email()])
    phone = StringField(label="Phone*", validators=[DataRequired()])
    submit = SubmitField(label="Save Changes")


# Form - Request Password Reset
class RequestPasswordResetForm(FlaskForm):
    """Request Password Reset Form"""

    email = StringField(label="Email*", validators=[DataRequired(), Email()])
    submit = SubmitField(label="Request Password Reset")
