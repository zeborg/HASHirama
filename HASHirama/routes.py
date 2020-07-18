from HASHirama import app, forms, os, hashfx, MAX_FILE_SIZE_MB
from flask import render_template, url_for, flash
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET','POST'])
def home():
    h_genr = (False,None)
    h_veri = (False,None,None,None)
    th_form = forms.TextHash()
    fh_form = forms.FileHash()
    ch_th_form = forms.CheckTextHash()
    ch_fh_form = forms.CheckFileHash()

    if th_form.validate_on_submit():
        thash = hashfx.thash()
        hashgen = th_form.text.data
        msg = thash.algo(hashgen, th_form.algo.data)
        h_genr = (True,forms.hashlabel[th_form.algo.data])
        flash('success', msg)

    elif ch_th_form.validate_on_submit():
        ch_thash = hashfx.thash()
        hashgen = ch_th_form.checktext.data
        genhash = ch_thash.algo(hashgen, ch_th_form.algo.data)
        h_veri = (True,forms.hashlabel[th_form.algo.data],genhash,False)
        flash('success', 'matched!') if ch_th_form.inputhash.data == genhash else flash('warning', 'did not match!')

    elif fh_form.validate_on_submit():
        f = fh_form.fileinput.data
        fhash = hashfx.fhash()
        filename = secure_filename(f.filename)
        filename_str = os.path.join(app.config['UPLOADS_FOLDER'], f'{filename}')
        if not os.path.exists(app.config['UPLOADS_FOLDER']):
            os.makedirs(app.config['UPLOADS_FOLDER'])
        f.save(filename_str)
        msg = fhash.algo(filename_str, 4096, fh_form.algo.data)
        os.remove(filename_str)
        h_genr = (True,forms.hashlabel[fh_form.algo.data])
        flash('success', msg)

    elif ch_fh_form.validate_on_submit():
        f = ch_fh_form.file_input.data
        fhash = hashfx.fhash()
        filename = secure_filename(f.filename)
        filename_str = os.path.join(app.config['UPLOADS_FOLDER'], f'{filename}')
        if not os.path.exists(app.config['UPLOADS_FOLDER']):
            os.makedirs(app.config['UPLOADS_FOLDER'])
        f.save(filename_str)
        genhash = fhash.algo(filename_str, 4096, ch_fh_form.algo.data)
        os.remove(filename_str)
        h_veri = (True,forms.hashlabel[ch_fh_form.algo.data],genhash,True)
        flash('success', 'matched!') if ch_fh_form.input_hash.data == genhash else flash('warning', 'did not match!')

    return render_template('home.html', th_form=th_form, ch_th_form=ch_th_form, fh_form=fh_form, ch_fh_form=ch_fh_form, generated=h_genr, verified=h_veri)

@app.errorhandler(413)
def handle_413(err):
    return f'File size exceeded. Maximum allowed file size: {MAX_FILE_SIZE_MB} MB. <a href="{url_for("home")}">Return to Home</a>', 413
