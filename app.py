from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_requests.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

class SupportRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    user = db.Column(db.String(80), nullable=False)
    topic = db.Column(db.String(120), nullable=False)
    request_title = db.Column(db.String(200), nullable=False)
    request_content = db.Column(db.Text, nullable=False)
    attachment = db.Column(db.String(120), nullable=True)
    response = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    response_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(10), nullable=False, default='open')
    messages = db.relationship('ChatMessage', backref='support_request', lazy=True)

class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    support_request_id = db.Column(db.Integer, db.ForeignKey('support_request.id'), nullable=False)
    sender = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/handle_support_request', methods=['POST'])
def handle_support_request():
    email = request.form['email']
    user = request.form['user']
    topic = request.form['topic']
    request_title = request.form['request-title']
    request_content = request.form['request-content']
    attachment = request.files['attachment']

    if attachment:
        attachment_filename = attachment.filename
        attachment.save(f'uploads/{attachment_filename}')
    else:
        attachment_filename = None

    support_request = SupportRequest(
        email=email,
        user=user,
        topic=topic,
        request_title=request_title,
        request_content=request_content,
        attachment=attachment_filename,
        created_at=datetime.utcnow(),
        status='open'
    )
    db.session.add(support_request)
    db.session.commit()

    flash('Yêu cầu hỗ trợ của bạn đã được gửi thành công!', 'success')
    return redirect(url_for('support'))

@app.route('/admin/support_requests')
def admin_support_requests():
    requests = SupportRequest.query.all()
    return render_template('admin_support_requests.html', requests=requests)

@app.route('/admin/respond/<int:request_id>', methods=['GET', 'POST'])
def respond(request_id):
    support_request = SupportRequest.query.get_or_404(request_id)
    if request.method == 'POST':
        response = request.form['response']
        support_request.response = response
        support_request.response_date = datetime.utcnow()
        support_request.status = 'closed'
        db.session.commit()

        msg = Message('Phản hồi yêu cầu hỗ trợ', sender='your_email@example.com', recipients=[support_request.email])
        msg.body = response
        mail.send(msg)

        flash('Phản hồi của bạn đã được gửi!', 'success')
        return redirect(url_for('admin_support_requests'))

    return render_template('respond.html', support_request=support_request)

@app.route('/support_request_detail/<int:request_id>', methods=['GET', 'POST'])
def support_request_detail(request_id):
    support_request = SupportRequest.query.get_or_404(request_id)
    if request.method == 'POST':
        sender = request.form['sender']
        message = request.form['message']
        chat_message = ChatMessage(
            support_request_id=request_id,
            sender=sender,
            message=message
        )
        db.session.add(chat_message)
        db.session.commit()
        return redirect(url_for('support_request_detail', request_id=request_id))

    return render_template('support_request_detail.html', support_request=support_request)

@app.route('/support')
def support():
    return render_template('supportuser.html')

if __name__ == '__main__':
    app.run(debug=True)