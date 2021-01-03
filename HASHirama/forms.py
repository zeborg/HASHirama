from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import TextField, TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

hashlabel = {
    'blake2b': 'BLAKE2b',
    'blake2s': 'BLAKE2s',
    'md5': 'MD5',
    'sha1': 'SHA-1',
    'sha224': 'SHA-224',
    'sha3_224': 'SHA3-224',
    'sha256': 'SHA-256',
    'sha3_256': 'SHA3-256',
    'sha384': 'SHA-384',
    'sha512': 'SHA-512',
    'sha3_512': 'SHA3-512'
}

text_hashes = [('blake2b','BLAKE2b'), ('blake2s','BLAKE2s'), ('md5','MD5'),('sha1','SHA-1'), ('sha224', 'SHA-224'), ('sha3_224','SHA3-224'), ('sha256','SHA-256'), ('sha3_256','SHA3-256'), ('sha384','SHA-384'), ('sha512','SHA-512'), ('sha3_512','SHA3-512')]
file_hashes = text_hashes


class TextHash(FlaskForm):
    text = TextAreaField('TEXT INPUT', validators=[DataRequired()])
    algo = SelectField('ALGORITHM', choices=text_hashes)
    chain = IntegerField('CHAIN LENGTH', default=1)
    th_genr = SubmitField('GENERATE HASH')


class CheckTextHash(FlaskForm):
    inputhash = TextField('HASHED INPUT', validators=[DataRequired()])
    checktext = TextAreaField('VERIFY TEXT', validators=[DataRequired()])
    algo = SelectField('ALGORITHM', choices=text_hashes)
    chain = IntegerField('CHAIN LENGTH', default=1)
    ch_thash = SubmitField('VERIFY HASH')

class FileHash(FlaskForm):
    fileinput = FileField('UPLOAD FILE', validators=[FileRequired()])
    algo = SelectField('ALGORITHM', choices=file_hashes)
    chain = IntegerField('CHAIN LENGTH', default=1)
    fh_genr = SubmitField('GENERATE HASH')

class CheckFileHash(FlaskForm):
    input_hash = TextField('HASHED INPUT', validators=[DataRequired()])
    file_input = FileField('VERIFY FILE', validators=[FileRequired()])
    algo = SelectField('ALGORITHM', choices=file_hashes)
    chain = IntegerField('CHAIN LENGTH', default=1)
    ch_fhash = SubmitField('VERIFY HASH')
