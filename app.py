import os
from datetime import datetime
import re
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import stripe
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
# STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
# STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')

EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_APP_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')
CONTACT_RECIPIENT = os.getenv('CONTACT_RECIPIENT') or EMAIL_SENDER

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'change-me')

# stripe.api_key = STRIPE_SECRET_KEY

supabase = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

COMPANY = {
    'name': 'Prime Vertix Group',
    'members': [
        {'name': 'Aziza Mosavi', 'role': 'Owner'},
        {'name': 'Sayed Dawood Mosavi', 'role': 'CEO'},
        {'name': 'Sayed Mujtaba Mosavi', 'role': 'Director & IT / Teacher'},
    ]
}

LESSON_INFO = {
    'title': 'Introduction to AI Vision with Python',
    'topics': ['Face tracking', 'Hand tracking', 'Body tracking', 'Object tracking'],
    'price_usd': 80,
    'age_min': None,
    'age_max': None,
    'requirements': ['Computer with webcam', 'Python 3.8+', 'Google Chrome or Firefox', 'Basic Python knowledge'],
    'schedule': [
        '21 Jun 2025, 10:00 - 11:00 (Botany Library focus room 21)',
        '28 Jun 2025, 10:00 - 11:00',
        '05 Jul 2025, 10:00 - 11:00',
        '12 Jul 2025, 10:00 - 11:00',
        '19 Jul 2025, 10:00 - 11:00',
        '26 Jul 2025, 10:00 - 11:00',
        '02 Aug 2025, 10:00 - 11:00',
        '09 Aug 2025, 10:00 - 11:00',
    ]
}

navLinks = [
  { "label": 'About', "href": '#about' },
  { "label": 'Services', "href": '#services' },
  { "label": 'Team', "href": '#team' },
  { "label": 'Course', "href": '#course' },
  { "label": 'Future', "href": '#future' },
  { "label": 'Contact', "href": '#contact' },
]
values = [
  {
    "icon": "Target",
    "title": 'Mission',
    "desc": 'To make high-quality technology education accessible and transformative for the next generation of digital leaders.',
    "color": 'brand',
  },
  {
    "icon": "Eye",
    "title": 'Vision',
    "desc": 'A world where every student can harness the power of AI and programming to solve real problems and create meaningful impact.',
    "color": 'sky',
  },
  {
    "icon": "Lightbulb",
    "title": 'Innovation',
    "desc": 'We continuously evolve our curriculum and products to stay ahead of the technology curve and industry demands.',
    "color": 'amber',
  },
  {
    "icon": "Award",
    "title": 'Excellence',
    "desc": 'Every course, product, and service we deliver reflects our commitment to the highest standards of quality and results.',
    "color": 'emerald',
  },
]
services = [
  {
    "icon": "Brain",
    "title": 'AI & Machine Learning Education',
    "desc": 'Hands-on courses teaching practical applications of artificial intelligence including computer vision, face detection, hand tracking, and object recognition using Python and modern libraries.',
    "tags": ['Python', 'OpenCV', 'MediaPipe', 'AI Vision'],
    "badge": 'Active',
    "badgeColor": 'emerald',
    "featured": "true",
  },
  {
    "icon": "Code2",
    "title": 'Programming Foundations',
    "desc": 'Structured programming courses tailored for beginners and intermediate learners covering Python, algorithmic thinking, and real-world project development.',
    "tags": ['Python', 'Algorithms', 'Projects'],
    "badge": 'Active',
    "badgeColor": 'emerald',
    "featured": "false",
  },
  {
    "icon": "BookOpen",
    "title": 'Educational Resources',
    "desc": 'Curated study materials, guides, and upcoming educational books to supplement learning and serve as long-term reference resources for students.',
    "tags": ['Guides', 'Books', 'Resources'],
    "badge": 'Coming Soon',
    "badgeColor": 'amber',
    "featured": "false",
  },
  {
    "icon": "Layers",
    "title": 'Digital Products & Solutions',
    "desc": 'Future technology products and digital services designed to support learners, educators, and businesses in the evolving digital landscape.',
    "tags": ['Digital Tools', 'Platforms', 'Services'],
    "badge": 'Coming Soon',
    "badgeColor": 'amber',
    "featured": "false",
  },
]
sessions = [
  { "num": 1, "date": 'Sun, 21 Jun 2026' },
  { "num": 2, "date": 'Sun, 28 Jun 2026' },
  { "num": 3, "date": 'Sun, 05 Jul 2026' },
  { "num": 4, "date": 'Sun, 12 Jul 2026' },
  { "num": 5, "date": 'Sun, 19 Jul 2026' },
  { "num": 6, "date": 'Sun, 26 Jul 2026' },
  { "num": 7, "date": 'Sun, 02 Aug 2026' },
  { "num": 8, "date": 'Sun, 09 Aug 2026' },
]
topics = [
  'Introduction to Python for AI applications',
  'Computer Vision fundamentals with OpenCV',
  'Face detection and recognition algorithms',
  'Real-time hand tracking with MediaPipe',
  'Full-body pose estimation techniques',
  'Multi-object detection and classification',
  'Combining tracking systems in a project',
  'Final project presentation and showcase',
]
plans = [
  {
    "icon": "BookOpen",
    "title": 'Educational Books',
    "desc": 'Comprehensive textbooks and reference guides covering programming, AI, and digital technology — designed specifically for young learners and self-study.',
    "timeline": 'Coming Soon',
    "color": 'amber',
    "items": ['Python for Beginners', 'AI Fundamentals', 'Digital Literacy Series'],
  },
  {
    "icon": "Code2",
    "title": 'Advanced Tech Courses',
    "desc": 'Expanding our curriculum with advanced courses in web development, data science, cybersecurity, and emerging technologies for teens and young adults.',
    "timeline": 'In Planning',
    "color": 'sky',
    "items": ['Web Development', 'Data Science', 'Cybersecurity Basics'],
  },
  {
    "icon": "Layers",
    "title": 'Digital Products & Platforms',
    "desc": 'Innovative digital tools, learning platforms, and productivity applications designed to support students, educators, and the wider tech community.',
    "timeline": 'Future Vision',
    "color": 'emerald',
    "items": ['Learning Management System', 'AI-Powered Study Tools', 'Educator Toolkit'],
  },
]
links = {
  "Company": [
    { "label": 'About Us', "href": '#about' },
    { "label": 'Our Team', "href": '#team' },
    { "label": 'Services', "href": '#services' },
    { "label": 'Contact', "href": '#contact' },
  ],
  "Programs": [
    { "label": 'AI Vision with Python', "href": '#course' },
    { "label": 'Programming Foundations', "href": '#services' },
    { "label": 'Future Courses', "href": '#future' },
    { "label": 'Educational Books', "href": '#future' },
  ],
}
@app.route('/')
def index():
  # normalize icon names to lucide kebab-case (e.g., BookOpen -> book-open, Code2 -> code-2)
  def normalize_icon(name):
    if not isinstance(name, str):
      return name
    # insert hyphen between lower-uppercase boundaries
    s = re.sub(r'([a-z0-9])([A-Z])', r"\1-\2", name)
    # insert hyphen between letters and digits
    s = re.sub(r'([A-Za-z])([0-9])', r"\1-\2", s)
    return s.replace('_', '-').lower()

  # create shallow copies with normalized icon names to avoid mutating module-level data
  norm_values = [dict(v, icon=normalize_icon(v.get('icon'))) for v in values]
  norm_services = [dict(s, icon=normalize_icon(s.get('icon'))) for s in services]
  norm_plans = [dict(p, icon=normalize_icon(p.get('icon'))) for p in plans]

  return render_template(
    'index.html',
    company=COMPANY,
    lesson=LESSON_INFO,
    navLinks=navLinks,
    values=norm_values,
    services=norm_services,
    sessions=sessions,
    topics=topics,
    plans=norm_plans,
    links=links,
    current_year=datetime.now().year,
  )

def _build_logo_url():
  try:
    return url_for('static', filename='logo.jpeg', _external=True)
  except RuntimeError:
    return ''

def send_email(subject: str, html_body: str, plain_body: str = '', to_address: str = None):
  """Send an email using SMTP_SSL. Requires EMAIL_SENDER and EMAIL_APP_PASSWORD set in env.
  """
  if not EMAIL_SENDER or not EMAIL_APP_PASSWORD:
    raise RuntimeError('EMAIL_SENDER and EMAIL_APP_PASSWORD must be configured in environment')
  if not to_address:
    to_address = CONTACT_RECIPIENT

  msg = MIMEMultipart('alternative')
  msg['Subject'] = subject
  msg['From'] = EMAIL_SENDER
  msg['To'] = to_address

  if plain_body:
    part1 = MIMEText(plain_body, 'plain')
    msg.attach(part1)

  part2 = MIMEText(html_body, 'html')
  msg.attach(part2)

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(EMAIL_SENDER, EMAIL_APP_PASSWORD)
    server.sendmail(EMAIL_SENDER, to_address, msg.as_string())

@app.route('/contact', methods=['POST'])
def handle_contact():
  # expected form fields: name, email, subject, message
  name = request.form.get('name') or 'Website visitor'
  email = request.form.get('email') or 'noreply'
  subject_field = request.form.get('subject') or 'New contact'
  message = request.form.get('message') or ''

  subject = f"Contact: {subject_field} — {name}"
  logo_url = _build_logo_url()
  html_body = f"""
  <div style="font-family:Arial,Helvetica,sans-serif;color:#111;background:#fff;padding:18px;">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
      {f'<img src="{logo_url}" alt="logo" style="width:80px;border-radius:8px;">' if logo_url else ''}
      <div>
        <strong>Prime Vertix Group</strong><br/>
        <small>New contact submission</small>
      </div>
    </div>
    <h3 style="margin:6px 0 12px 0;color:#0f172a;">{subject_field}</h3>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Message:</strong><br/>{message.replace('\n','<br/>')}</p>
    <hr/>
    <p style="font-size:12px;color:#6b7280;">Sent from the website on {datetime.utcnow().isoformat()} UTC</p>
  </div>
  """
  plain = f"{subject}\nFrom: {name} <{email}>\n\n{message}"
  try:
    send_email(subject, html_body, plain)
    flash('Message sent — we will get back to you shortly.', 'success')
  except Exception as e:
    print('Error sending contact email:', e)
    flash('There was an error sending your message. Please try again later.', 'error')
  return redirect(url_for('index') + '#contact')

@app.route('/enrol', methods=['POST'])
def handle_enrol():
  # Extract from student/parent form fields
  student_first = request.form.get('student_first_name') or ''
  student_last = request.form.get('student_last_name') or ''
  full_name = f"{student_first} {student_last}".strip() or request.form.get('name') or 'Applicant'
  
  email = request.form.get('student_email') or request.form.get('email') or ''
  phone = request.form.get('student_cellphone') or request.form.get('phone') or ''
  selected_session = request.form.get('session') or request.form.get('selected_session') or ''
  extra = '\n'.join([f"{k}: {v}" for k, v in request.form.items() if k not in ('full_name','name','email','phone','session','selected_session','student_first_name','student_last_name','student_email','student_cellphone')])

  subject = f"New enrolment — {full_name}"
  logo_url = _build_logo_url()
  html_body = f"""
  <div style="font-family:Arial,Helvetica,sans-serif;color:#111;background:#fff;padding:18px;">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
      {f'<img src="{logo_url}" alt="logo" style="width:80px;border-radius:8px;">' if logo_url else ''}
      <div>
        <strong>Prime Vertix Group</strong><br/>
        <small>New enrolment submission</small>
      </div>
    </div>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Phone:</strong> {phone}</p>
    <p><strong>Selected session:</strong> {selected_session}</p>
    <p><strong>Additional info:</strong><br/>{extra.replace('\n','<br/>')}</p>
    <hr/>
    <p style="font-size:12px;color:#6b7280;">Sent from the website on {datetime.utcnow().isoformat()} UTC</p>
  </div>
  """
  plain = f"{subject}\nName: {full_name}\nEmail: {email}\nPhone: {phone}\nSession: {selected_session}\n\n{extra}"
  try:
    send_email(subject, html_body, plain)
    flash('Enrolment submitted — we will contact you with next steps.', 'success')
  except Exception as e:
    print('Error sending enrolment email:', e)
    flash('There was an error submitting your enrolment. Please try again later.', 'error')
  return redirect(url_for('index') + '#course')
