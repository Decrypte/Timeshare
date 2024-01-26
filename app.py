from flask import Flask, request, render_template, redirect, url_for, session
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from flask_migrate import Migrate
from datetime import datetime
from flask import jsonify
import openai


# Import models at the top
from models.user import User
from models.resort import Resort
from models.booking import Booking


from flask import request
from qa_system import get_answer


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timeshare.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for session management

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/init_db')
def init_db():
    with app.app_context():
        db.create_all()
    return "Database initialized!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        # Ensure you're in the app context when accessing the database
        with app.app_context():
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)  # Log in the user
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'

    return render_template('login.html')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/add_resort', methods=['GET', 'POST'])
@login_required
def add_resort():
    print("Current User:", current_user.username)  # Debug: Print username
    print("Is Admin:", current_user.is_admin)

    if not current_user.is_admin:
        return "Unauthorized Access", 403

    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        # Ensure these match the fields in your Resort model
        description = request.form.get('description')
        access_level = request.form.get('access_level')
        amenities = request.form.get('amenities')
        special_services = request.form.get('special_services')

        new_resort = Resort(name=name, location=location, description=description, access_level=access_level, amenities=amenities, special_services=special_services)
        db.session.add(new_resort)
        db.session.commit()

        return redirect(url_for('list_resorts'))
    return render_template('add_resort.html')

@app.route('/resorts')
def resorts():
    all_resorts = Resort.query.all()
    return render_template('resorts.html', resorts=all_resorts)

@app.route('/resorts/<int:resort_id>')
def resort_detail(resort_id):
    resort = Resort.query.get_or_404(resort_id)
    return render_template('resort_detail.html', resort=resort)

@app.route('/book_resort/<int:resort_id>', methods=['GET', 'POST'])
@login_required
def book_resort(resort_id):
    resort = Resort.query.get_or_404(resort_id)
    if request.method == 'POST':
        check_in_date_str = request.form.get('check_in_date')
        check_out_date_str = request.form.get('check_out_date')

        # Convert string dates to date objects
        check_in_date = datetime.strptime(check_in_date_str, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out_date_str, '%Y-%m-%d').date()

        new_booking = Booking(user_id=current_user.id, resort_id=resort.id,
                              check_in_date=check_in_date, check_out_date=check_out_date)
        db.session.add(new_booking)
        db.session.commit()

        return redirect(url_for('my_bookings'))
    return render_template('book_resort.html', resort=resort)



@app.route('/my_bookings')
@login_required
def my_bookings():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('my_bookings.html', bookings=bookings)


@app.route('/modify_booking/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def modify_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    # Check if the current user owns the booking
    if booking.user_id != current_user.id:
        return "Unauthorized", 403

    if request.method == 'POST':
        booking.check_in_date = request.form.get('check_in_date')
        booking.check_out_date = request.form.get('check_out_date')
        db.session.commit()
        return redirect(url_for('my_bookings'))

    return render_template('modify_booking.html', booking=booking)

@app.route('/cancel_booking/<int:booking_id>', methods=['POST'])
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    # Check if the current user owns the booking
    if booking.user_id != current_user.id:
        return "Unauthorized", 403

    db.session.delete(booking)
    db.session.commit()
    return redirect(url_for('my_bookings'))


@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        question = request.form.get('question')
        user_id = current_user.id if current_user.is_authenticated else None
        stage = session.get('chat_stage', 'suggestion')
        context = session.get('chat_context', {})

        answer, next_stage, next_context = get_answer(question, user_id, stage, context)

        session['chat_stage'] = next_stage
        session['chat_context'] = next_context

        # Return JSON response for AJAX request
        return jsonify({"answer": answer})
    else:
        # Render the chat template for GET request
        return render_template('qa_page.html')




if __name__ == '__main__':
    app.run(debug=True)
